#!/usr/bin/env python3
"""SUMAX Büro-Status: meldet Start, Lebenszeichen und Ende einer Claude-Code-Sitzung.

Aufruf durch die Plugin-Hooks (hooks/hooks.json):
  python3 melden.py start      bei SessionStart
  python3 melden.py heartbeat  bei Stop (nach jeder Antwort, gedrosselt auf 5 Minuten)
  python3 melden.py end        bei SessionEnd

Gesendet wird nur: Sitzungs-ID, Zustand und der Name des Git-Repos (Ordnername
des Git-Toplevels, sonst leer). Keine Prompts, keine Antworten, keine Dateinamen,
keine Pfade.

Grundsatz: Das Plugin darf Claude Code nie stören. Ohne Token, bei abgeschaltetem
Plugin und bei JEDEM Fehler endet das Skript still mit Exit-Code 0 und gibt nichts
auf stdout aus (stdout eines SessionStart-Hooks landet sonst im Kontext).

Nur Python-Standardbibliothek.

Umgebungsvariablen:
  CLAUDE_PLUGIN_OPTION_TOKEN  Plugin-Token aus der Plugin-Konfiguration (userConfig)
  SUMAX_BUERO_TOKEN           Ersatz, falls kein Plugin-Token gesetzt ist
  SUMAX_BUERO_URL             Ziel, Standard https://context-store.sumax.dev/api/buero/claude
                              (http nur für 127.0.0.1/localhost, für Tests)
  SUMAX_BUERO_AUS=1           schaltet alle Meldungen ab
"""
import json
import os
import re
import ssl
import subprocess
import sys
import tempfile
import time
import urllib.parse
import urllib.request

STANDARD_URL = "https://context-store.sumax.dev/api/buero/claude"
USER_AGENT = "sumax-buero-status/1.0"  # Cloudflare blockt die Standardsignatur von python-urllib
ZUSTAENDE = ("start", "heartbeat", "end")
TIMEOUT = 3
HEARTBEAT_ABSTAND = 300  # Sekunden: höchstens ein Lebenszeichen alle 5 Minuten
MAX_STDIN = 1_000_000
LOKALE_HOSTS = ("127.0.0.1", "localhost", "::1")


SUMAX_REMOTES = ("github.com:carlwuerfel/", "github.com/carlwuerfel/", "github-buero:")


def _token() -> str:
    return (os.environ.get("CLAUDE_PLUGIN_OPTION_TOKEN", "").strip()
            or os.environ.get("SUMAX_BUERO_TOKEN", "").strip())


def _ziel() -> str:
    """Ziel-URL; leer, wenn sie nicht erlaubt ist (nur https, http nur lokal)."""
    url = os.environ.get("SUMAX_BUERO_URL", "").strip() or STANDARD_URL
    teile = urllib.parse.urlsplit(url)
    if teile.scheme == "https" and teile.hostname:
        return url
    if teile.scheme == "http" and teile.hostname in LOKALE_HOSTS:
        return url
    return ""


def _sitzung(roh) -> str:
    """Sitzungs-ID auf sichere Zeichen begrenzen (dient auch als Dateiname)."""
    if not isinstance(roh, str):
        return ""
    return re.sub(r"[^A-Za-z0-9_-]", "", roh)[:128]


def _repo(cwd) -> str:
    """Ordnername des Git-Toplevels von cwd, sonst leer."""
    if not isinstance(cwd, str) or not cwd or not os.path.isdir(cwd):
        return ""
    try:
        erg = subprocess.run(
            ["git", "-C", cwd, "rev-parse", "--show-toplevel"],
            stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
            timeout=2, check=False, text=True,
        )
    except Exception:
        return ""
    if erg.returncode != 0:
        return ""
    name = os.path.basename(erg.stdout.strip().rstrip("/\\"))
    return re.sub(r"[^A-Za-z0-9._-]", "", name)[:120]


def _sumax_repo(cwd) -> bool:
    """Nur SUMAX-Repos melden: origin zeigt auf das SUMAX-GitHub-Konto. Private und fremde Projekte verlassen den
    Rechner nie (Carl, 19.10.2026: „darf nicht gezeigt werden, wenn ich an privaten Projekten arbeite“)."""
    if not isinstance(cwd, str) or not cwd or not os.path.isdir(cwd):
        return False
    try:
        erg = subprocess.run(
            ["git", "-C", cwd, "remote", "get-url", "origin"],
            stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
            timeout=2, check=False, text=True,
        )
    except Exception:
        return False
    url = erg.stdout.strip().lower() if erg.returncode == 0 else ""
    return any(z in url for z in SUMAX_REMOTES)


def _marken_ordner() -> str:
    ordner = os.path.join(tempfile.gettempdir(), "sumax-buero-status")
    os.makedirs(ordner, mode=0o700, exist_ok=True)
    return ordner


def _aufraeumen(ordner: str) -> None:
    """Marken älter als einen Tag löschen (Sitzungen, deren Ende nie gemeldet wurde)."""
    grenze = time.time() - 86400
    for name in os.listdir(ordner):
        pfad = os.path.join(ordner, name)
        try:
            if os.path.getmtime(pfad) < grenze:
                os.remove(pfad)
        except OSError:
            pass


def _drosseln(zustand: str, sitzung: str) -> bool:
    """True, wenn jetzt nichts gesendet werden soll. Merkt sich den letzten Versuch."""
    ordner = _marken_ordner()
    marke = os.path.join(ordner, sitzung)
    jetzt = time.time()
    if zustand == "end":
        try:
            os.remove(marke)
        except OSError:
            pass
        return False
    if zustand == "start":
        _aufraeumen(ordner)
    elif zustand == "heartbeat":
        try:
            with open(marke, encoding="utf-8") as f:
                letzter = float(f.read().strip() or 0)
            if 0 <= jetzt - letzter < HEARTBEAT_ABSTAND:
                return True
        except (OSError, ValueError):
            pass
    # Versuch merken, auch wenn das Senden gleich scheitert: ein nicht erreichbarer
    # Server soll nicht nach jeder Antwort erneut drei Sekunden kosten.
    with open(marke, "w", encoding="utf-8") as f:
        f.write(str(jetzt))
    return False


def _senden(url: str, token: str, rumpf: dict) -> None:
    req = urllib.request.Request(
        url,
        data=json.dumps(rumpf).encode("utf-8"),
        method="POST",
        headers={
            "Content-Type": "application/json",
            "User-Agent": USER_AGENT,
            "X-Buero-Token": token,
        },
    )
    ctx = ssl.create_default_context() if url.startswith("https:") else None
    with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as resp:
        resp.read(4096)


def main() -> None:
    if len(sys.argv) < 2 or sys.argv[1] not in ZUSTAENDE:
        return
    zustand = sys.argv[1]
    if os.environ.get("SUMAX_BUERO_AUS", "").strip() == "1":
        return
    token = _token()
    url = _ziel()
    if not token or not url:
        return
    daten = json.loads(sys.stdin.read(MAX_STDIN) or "null")
    if not isinstance(daten, dict):
        return
    sitzung = _sitzung(daten.get("session_id"))
    if not sitzung or not _sumax_repo(daten.get("cwd")):
        return
    if _drosseln(zustand, sitzung):
        return
    _senden(url, token, {"session_id": sitzung, "state": zustand, "repo": _repo(daten.get("cwd"))})


if __name__ == "__main__":
    try:
        main()
    except BaseException:
        pass
    sys.exit(0)
