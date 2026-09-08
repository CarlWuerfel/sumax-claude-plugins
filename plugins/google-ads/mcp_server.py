#!/usr/bin/env python3
"""SUMAX Google Ads — MCP-Server (stdio, reine Standardbibliothek).

Duenner Bruecken-Server: stellt Claude Code Lese-Werkzeuge fuer die SUMAX-MCC
bereit. Dahinter steckt der SUMAX-Gateway (`/api/google-ads/*`) — inklusive
Caching, damit dieselbe Abfrage nicht doppelt Google-Ads-API-Kontingent kostet.

STRIKT READ-ONLY. Es gibt hier bewusst kein Werkzeug, das Budgets, Gebote,
Keywords, Anzeigen oder Status aendert. Mutationen laufen ueber den
`google-ads-agent` mit Freigabe-Queue — nicht aus einer freien Chat-Session.

Bewusst OHNE externe Abhaengigkeiten (kein `mcp`-Paket, kein httpx) — laeuft mit
jedem python3 auf jeder Mitarbeiter-Maschine ohne Installation. Kommuniziert per
newline-delimited JSON-RPC 2.0 ueber stdin/stdout (MCP-stdio-Transport).

Konfiguration ueber Umgebungsvariablen:
  SUMAX_ADS_TOKEN          Schmaler Zugangs-Token (NUR Google-Ads-Lesedaten) — Pflicht
  SUMAX_ADS_TOKEN_FILE     Alternative: Datei mit dem Token (Default ~/.sumax/ads-token)
  SUMAX_ADS_GATEWAY_URL    Default https://ads-mcp.sumax.dev
  SUMAX_ADS_CALLER         Name dieses Nutzers (Default: user@host) — landet im Logging
  SUMAX_ADS_MAX_CHARS      Kappungsgrenze pro Antwort (Default 60000 Zeichen)
  CF_ACCESS_CLIENT_ID      Master-CF-Service-Token (NUR intern, nicht an MA geben)
  CF_ACCESS_CLIENT_SECRET
"""
# Muss mit dem System-Python von macOS (3.9) laufen: Claude Desktop startet
# /usr/bin/python3. Deshalb Annotationen lazy auswerten (str | None ist erst 3.10).
from __future__ import annotations

import getpass
import json
import os
import socket
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request

PROTOCOL_VERSION = "2024-11-05"
GATEWAY = os.environ.get("SUMAX_ADS_GATEWAY_URL", "https://ads-mcp.sumax.dev").rstrip("/")
TIMEOUT = 90  # Google-Ads-Reports koennen bei kalten Caches dauern


def _caller() -> str:
    c = os.environ.get("SUMAX_ADS_CALLER", "").strip()
    if c:
        return c.lower()
    try:
        return f"{getpass.getuser()}@{socket.gethostname()}".lower()
    except Exception:
        return "claude-code"


def _token() -> str:
    """Zugangs-Token. Reihenfolge: Umgebungsvariable, dann Token-Datei.

    Die Datei-Variante ist fuer alle Faelle gedacht, in denen keine Shell im Spiel ist
    (Claude Desktop, Desktop-App, GUI-Start) — dort greift ein `export` in ~/.zshrc nicht.
    Standardpfad ~/.sumax/ads-token, ueberschreibbar per SUMAX_ADS_TOKEN_FILE.
    """
    tok = os.environ.get("SUMAX_ADS_TOKEN", "").strip()
    if tok:
        return tok
    path = os.environ.get("SUMAX_ADS_TOKEN_FILE", "").strip() or os.path.join(
        os.path.expanduser("~"), ".sumax", "ads-token")
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read().strip()
    except OSError:
        return ""


def _max_chars() -> int:
    try:
        return max(4000, int(os.environ.get("SUMAX_ADS_MAX_CHARS", "60000")))
    except ValueError:
        return 60000


def _headers() -> dict:
    # Eigener User-Agent: Cloudflare blockt die Standard-Signatur von python-urllib
    # (error 1010). Ein benannter UA kommt sauber durch.
    h = {
        "Content-Type": "application/json",
        "User-Agent": "sumax-google-ads-mcp/1.0",
        "X-Caller": f"mcp-google-ads:{_caller()}",
    }
    tok = _token()
    if tok:
        h["X-Ads-Token"] = tok
    # Optionaler Master-CF-Service-Token (nur intern/Server-zu-Server, NICHT an MA geben).
    cid = os.environ.get("CF_ACCESS_CLIENT_ID", "")
    if cid:
        h["CF-Access-Client-Id"] = cid
        h["CF-Access-Client-Secret"] = os.environ.get("CF_ACCESS_CLIENT_SECRET", "")
    return h


def _ssl_ctx() -> ssl.SSLContext:
    ctx = ssl.create_default_context()
    # Interne Tailscale-URLs laufen mit selbst-signierten Certs.
    if "tail61b1.ts.net" in GATEWAY or "localhost" in GATEWAY or "127.0.0.1" in GATEWAY:
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
    return ctx


def _request(method: str, path: str, params: dict | None = None, body: dict | None = None):
    url = f"{GATEWAY}{path}"
    if params:
        clean = {k: v for k, v in params.items() if v is not None and v != ""}
        if clean:
            url += "?" + urllib.parse.urlencode(clean)
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, headers=_headers(), method=method)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT, context=_ssl_ctx()) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")[:600]
        if e.code == 401:
            raise RuntimeError(
                "Zugang abgelehnt (401). Token fehlt oder ist falsch — entweder "
                "SUMAX_ADS_TOKEN in der Shell setzen oder in die Datei ~/.sumax/ads-token "
                "schreiben. Token bei c.wuerfel@sumax.de anfragen."
            )
        if e.code == 503:
            raise RuntimeError("Gateway meldet: kein Ads-MCP-Token konfiguriert (Server-seitig).")
        raise RuntimeError(f"Gateway-Fehler {e.code}: {detail}")


# ──────────────────────────────────────────────────────────────────────────
# Endpoint-Landkarte — jeder Eintrag wird 1:1 zu einem MCP-Werkzeug
# ──────────────────────────────────────────────────────────────────────────
CID = {"customer_id": ("string", "Konto-ID aus ads_accounts, z.B. '123-456-7890' oder '1234567890'.", True)}
DR30 = {"date_range": ("string", "Zeitraum, z.B. LAST_30_DAYS, LAST_7_DAYS, LAST_90_DAYS, THIS_MONTH. Default LAST_30_DAYS.", False)}
DR90 = {"date_range": ("string", "Zeitraum, z.B. LAST_90_DAYS, LAST_30_DAYS, THIS_MONTH. Default LAST_90_DAYS.", False)}
FREE = {
    "start_date": ("string", "Freier Zeitraum-Start YYYY-MM-DD (nur zusammen mit end_date; uebersteuert date_range).", False),
    "end_date": ("string", "Freier Zeitraum-Ende YYYY-MM-DD (nur zusammen mit start_date).", False),
}
LIMIT = {"limit": ("integer", "Maximale Zeilen (Default 100). Bei grossen Konten klein halten.", False)}

SPECS: dict[str, dict] = {
    "ads_accounts": {
        "path": "/accounts",
        "desc": "Alle Kunden-Konten der SUMAX-MCC (Name + Konto-ID + Waehrung). Immer der erste Schritt: hier die customer_id des Kunden holen. Optional 'search' filtert nach Kontoname.",
        "params": {"search": ("string", "Optionaler Namensfilter, z.B. ein Teil des Kundennamens — filtert lokal ueber die Kontoliste.", False)},
    },
    "ads_account_overview": {
        "path": "/account-overview",
        "desc": "Konto-KPIs auf einen Blick: Kosten, Klicks, Impressionen, CTR, CPC, Conversions, Conv.-Wert, ROAS. Der Einstieg in jede Analyse.",
        "params": {**CID, **DR30},
    },
    "ads_campaigns": {
        "path": "/campaigns",
        "desc": "Performance je Kampagne (Kosten, Klicks, Conversions, CPA, ROAS, Status). Basis fuer Budget- und Struktur-Analysen.",
        "params": {**CID, **DR90, **FREE},
    },
    "ads_campaign_dates": {
        "path": "/campaign-dates",
        "desc": "Echte Startdaten der Kampagnen (Go-Live), ohne Zeitraum-Filter — zum Einordnen, seit wann etwas laeuft.",
        "params": {**CID},
    },
    "ads_kpi_timeseries": {
        "path": "/kpi-timeseries",
        "desc": "Monatliche KPI-Zeitreihe des Kontos (Impressionen, Klicks, Kosten, Conversions, Conv.-Wert). Fuer Verlaeufe, Knicke und Vorjahresvergleiche.",
        "params": {**CID, "lookback_days": ("integer", "Rueckblick in Tagen (Default 545 = ca. 18 Monate).", False)},
    },
    "ads_adgroups": {
        "path": "/adgroup-performance",
        "desc": "Performance je Anzeigengruppe, optional auf eine Kampagne gefiltert.",
        "params": {**CID, **DR30, "campaign_id": ("string", "Optional: nur diese Kampagnen-ID.", False), **FREE},
    },
    "ads_ads": {
        "path": "/ad-performance",
        "desc": "Einzelne Anzeigen: Typ, Status, CTR, Conversions. Fuer Creative-/RSA-Bewertung und Ablehnungen.",
        "params": {**CID, **DR30},
    },
    "ads_keywords": {
        "path": "/keywords",
        "desc": "Keyword-Performance inklusive Quality Score. Fuer Kosten-Treiber, Nullbringer und Match-Type-Analysen.",
        "params": {**CID, **DR90, **LIMIT},
    },
    "ads_search_terms": {
        "path": "/search-terms",
        "desc": "Search-Terms-Report — die echten Suchanfragen. Wichtigste Quelle fuer Streuverluste und Negativ-Keywords.",
        "params": {**CID, **DR90, **LIMIT},
    },
    "ads_negative_keywords": {
        "path": "/negative-keywords",
        "desc": "Alle aktiven Negativ-Keywords (Kampagnen- und Anzeigengruppen-Ebene). Immer VOR einer Negativ-Empfehlung pruefen, damit nichts doppelt vorgeschlagen wird.",
        "params": {**CID},
    },
    "ads_conversions": {
        "path": "/conversions",
        "desc": "Conversion-Aktionen mit Einstellungen (primaer/sekundaer, Zaehlweise, Status). Der Tracking-Gesundheitscheck.",
        "params": {**CID},
    },
    "ads_conversions_by_action": {
        "path": "/conversions-by-action",
        "desc": "Echte Conversion-Zahlen je Zielvorhaben inkl. conversions_value und all_conversions. Achtung: 'conversions' zaehlt nur primaere Aktionen, 'all_conversions' auch sekundaere — das ist keine Doppelzaehlung.",
        "params": {**CID, **DR30, **FREE},
    },
    "ads_conversions_by_campaign_action": {
        "path": "/conversions-by-campaign-action",
        "desc": "Conversions je Kampagne, aufgeschluesselt nach Conversion-Aktion. start_date und end_date sind Pflicht.",
        "params": {**CID,
                   "start_date": ("string", "Start YYYY-MM-DD (Pflicht).", True),
                   "end_date": ("string", "Ende YYYY-MM-DD (Pflicht).", True)},
    },
    "ads_budget_analysis": {
        "path": "/budget-analysis",
        "desc": "Budget-Auslastung je Kampagne (heute) — wo Budget limitiert und wo es liegen bleibt.",
        "params": {**CID},
    },
    "ads_bidding_strategies": {
        "path": "/bidding-strategies",
        "desc": "Gebotsstrategie je Kampagne inkl. Ziel-CPA / Ziel-ROAS. Fuer die Frage, ob die Strategie zum Ziel passt.",
        "params": {**CID},
    },
    "ads_quality_scores": {
        "path": "/quality-scores",
        "desc": "Quality Scores der Keywords mit den Komponenten (Anzeigenrelevanz, erwartete CTR, Landingpage — ABOVE/AVERAGE/BELOW).",
        "params": {**CID, **DR30},
    },
    "ads_impression_share": {
        "path": "/impression-share",
        "desc": "Search Impression Share plus verlorener Anteil durch Budget bzw. Anzeigenrang. Zeigt Wachstums-Spielraum.",
        "params": {**CID, **DR30},
    },
    "ads_auction_insights": {
        "path": "/auction-insights",
        "desc": "Auction Insights: Wettbewerber in denselben Auktionen, Overlap Rate, Position above Rate.",
        "params": {**CID, **DR90},
    },
    "ads_account_structure": {
        "path": "/account-structure",
        "desc": "Hierarchie Kampagne → Anzeigengruppe → Keyword-Anzahl. Fuer Struktur- und Aufraeum-Analysen.",
        "params": {**CID},
    },
    "ads_ad_groups": {
        "path": "/ad-groups",
        "desc": "Reine Liste der aktiven Anzeigengruppen (ohne Performance), optional nach Kampagne gefiltert.",
        "params": {**CID, "campaign_id": ("string", "Optional: nur diese Kampagnen-ID.", False)},
    },
    "ads_audience_performance": {
        "path": "/audience-performance",
        "desc": "Zielgruppen-Segmente mit Performance-Metriken (Beobachtung/Targeting).",
        "params": {**CID, **DR30},
    },
    "ads_device_split": {
        "path": "/device-split",
        "desc": "Aufteilung nach Geraet (Mobile/Desktop/Tablet) mit Klicks, Kosten, Conversions und Anteilen.",
        "params": {**CID, **DR30, **FREE},
    },
    "ads_shopping_campaigns": {
        "path": "/shopping-campaigns",
        "desc": "Shopping-Kampagnen mit Performance (nur bei E-Commerce-Konten relevant).",
        "params": {**CID, **DR30},
    },
    "ads_shopping_search_terms": {
        "path": "/shopping-search-terms",
        "desc": "Search Terms aus Shopping-Kampagnen (shopping_performance_view).",
        "params": {**CID, **DR30},
    },
    "ads_change_history": {
        "path": "/change-history",
        "desc": "Aenderungshistorie des Kontos (Gebote, Budgets, Status, Anzeigen) — wer hat wann was geaendert. Unverzichtbar, wenn Zahlen ploetzlich kippen.",
        "params": {**CID, "date_range": ("string", "Zeitraum, Default LAST_14_DAYS.", False)},
    },
    "ads_benchmarks": {
        "path": "/benchmarks",
        "desc": "Branchen-Benchmarks aus der gesamten SUMAX-MCC (CTR, CPC, Conv.-Rate, CPA) — zum Einordnen eines Konto-Werts.",
        "params": {**DR90, "industry": ("string", "Optional: Branche eingrenzen.", False)},
    },
    "ads_keyword_ideas": {
        "path": "/keyword-ideas",
        "method": "POST",
        "desc": "Keyword Planner: Ideen inkl. Suchvolumen und Wettbewerb — aus Seed-Keywords oder einer URL. Funktioniert ohne Kunden-Konto.",
        "params": {
            "seed_keywords": ("array", "Liste von Start-Keywords, z.B. ['beispiel keyword'].", False),
            "url": ("string", "Alternativ: URL, aus der Google Ideen ableitet.", False),
            "language": ("string", "Sprache, Default 'de'.", False),
            "location": ("string", "Land, Default 'DE'.", False),
        },
    },
}


def _schema(params: dict) -> dict:
    props, required = {}, []
    for name, (typ, desc, req) in params.items():
        entry: dict = {"type": typ, "description": desc}
        if typ == "array":
            entry["items"] = {"type": "string"}
        props[name] = entry
        if req:
            required.append(name)
    return {"type": "object", "properties": props, "required": required}


TOOLS = [
    {
        "name": name,
        "description": spec["desc"] + " (Lesezugriff auf die SUMAX Google-Ads-MCC ueber den Gateway.)",
        "inputSchema": _schema(spec["params"]),
    }
    for name, spec in SPECS.items()
]


def _shorten(payload) -> str:
    text = json.dumps(payload, ensure_ascii=False, indent=1)
    cap = _max_chars()
    if len(text) <= cap:
        return text
    return (
        text[:cap]
        + f"\n\n… gekuerzt bei {cap:,} Zeichen. Enger eingrenzen: kleineres 'limit', kuerzerer "
          "'date_range' oder Filter auf eine campaign_id."
    )


def _call_tool(name: str, args: dict) -> str:
    spec = SPECS.get(name)
    if not spec:
        return f"Unbekanntes Werkzeug: {name}"

    # Sonderfall: Kontoliste lokal nach Namen filtern
    if name == "ads_accounts":
        data = _request("GET", "/api/google-ads/accounts")
        rows = data.get("accounts", data) if isinstance(data, dict) else data
        needle = (args.get("search") or "").strip().lower()
        if needle and isinstance(rows, list):
            rows = [r for r in rows
                    if needle in json.dumps(r, ensure_ascii=False).lower()]
            if not rows:
                return f"Kein Konto gefunden, dessen Name '{needle}' enthaelt. Ohne 'search' aufrufen, um alle zu sehen."
        return _shorten(rows)

    if spec.get("method") == "POST":
        body = {k: v for k, v in args.items() if v is not None}
        return _shorten(_request("POST", f"/api/google-ads{spec['path']}", body=body))

    params = {k: v for k, v in args.items() if k in spec["params"]}
    return _shorten(_request("GET", f"/api/google-ads{spec['path']}", params=params))


# ──────────────────────────────────────────────────────────────────────────
# JSON-RPC / MCP-stdio-Schleife
# ──────────────────────────────────────────────────────────────────────────
def _send(msg: dict) -> None:
    sys.stdout.write(json.dumps(msg) + "\n")
    sys.stdout.flush()


def _result(req_id, result) -> None:
    _send({"jsonrpc": "2.0", "id": req_id, "result": result})


def _error(req_id, code, message) -> None:
    _send({"jsonrpc": "2.0", "id": req_id, "error": {"code": code, "message": message}})


def main() -> None:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            continue

        method = msg.get("method")
        req_id = msg.get("id")

        if method == "initialize":
            _result(req_id, {
                "protocolVersion": PROTOCOL_VERSION,
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "sumax-google-ads", "version": "1.0.1"},
            })
        elif method == "notifications/initialized":
            continue
        elif method == "tools/list":
            _result(req_id, {"tools": TOOLS})
        elif method == "tools/call":
            params = msg.get("params", {})
            tool = params.get("name", "")
            args = params.get("arguments", {}) or {}
            try:
                text = _call_tool(tool, args)
                _result(req_id, {"content": [{"type": "text", "text": text}]})
            except urllib.error.URLError as e:
                _result(req_id, {"content": [{"type": "text", "text": f"Gateway nicht erreichbar: {e}"}], "isError": True})
            except Exception as e:
                _result(req_id, {"content": [{"type": "text", "text": f"Fehler: {e}"}], "isError": True})
        elif method == "ping":
            _result(req_id, {})
        elif req_id is not None:
            _error(req_id, -32601, f"Methode nicht unterstuetzt: {method}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
