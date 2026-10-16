#!/usr/bin/env python3
"""HTML im SUMAX-Stil in ein PDF umwandeln.

Aufruf:  python3 pdf_erzeugen.py dokument.html [ausgabe.pdf]

Nimmt WeasyPrint, wenn es installiert ist, sonst Google Chrome (headless).
Die HTML-Datei muss neben sumax-pdf.css liegen (oder den Pfad dorthin richtig
verlinken), damit Schriften und Logo gefunden werden.
"""
import os
import shutil
import subprocess
import sys
from pathlib import Path

CHROME_PFADE = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "google-chrome",
    "google-chrome-stable",
    "chromium",
    "chromium-browser",
]


def mit_weasyprint(html: Path, pdf: Path) -> bool:
    try:
        import weasyprint
    except OSError:
        # macOS mit Homebrew: Pango liegt in /opt/homebrew/lib und wird ohne
        # diesen Pfad nicht gefunden. Einmal mit gesetzter Variable neu starten.
        if sys.platform == "darwin" and not os.environ.get("SUMAX_PDF_NEUSTART"):
            env = dict(os.environ, DYLD_FALLBACK_LIBRARY_PATH="/opt/homebrew/lib:/usr/local/lib",
                       SUMAX_PDF_NEUSTART="1")
            r = subprocess.run([sys.executable, *sys.argv], env=env)
            sys.exit(r.returncode)
        return False
    except ImportError:
        return False
    weasyprint.HTML(filename=str(html)).write_pdf(str(pdf))
    print(f"PDF erstellt mit WeasyPrint {weasyprint.__version__}: {pdf}")
    return True


def mit_chrome(html: Path, pdf: Path) -> bool:
    for kandidat in CHROME_PFADE:
        pfad = kandidat if os.path.isabs(kandidat) else shutil.which(kandidat)
        if pfad and os.path.exists(pfad):
            subprocess.run(
                [pfad, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                 "--allow-file-access-from-files", f"--print-to-pdf={pdf}", html.as_uri()],
                check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120,
            )
            print(f"PDF erstellt mit Chrome: {pdf}")
            return True
    return False


def main() -> None:
    # macOS mit Homebrew: Pango vor dem ersten Import auffindbar machen
    if (sys.platform == "darwin" and "DYLD_FALLBACK_LIBRARY_PATH" not in os.environ
            and os.path.exists("/opt/homebrew/lib/libgobject-2.0.0.dylib")):
        env = dict(os.environ, DYLD_FALLBACK_LIBRARY_PATH="/opt/homebrew/lib", SUMAX_PDF_NEUSTART="1")
        sys.exit(subprocess.run([sys.executable, *sys.argv], env=env).returncode)
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    html = Path(sys.argv[1]).resolve()
    pdf = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else html.with_suffix(".pdf")
    if not html.exists():
        sys.exit(f"HTML-Datei nicht gefunden: {html}")
    if os.environ.get("SUMAX_PDF_CHROME") == "1":
        ok = mit_chrome(html, pdf)
    else:
        ok = mit_weasyprint(html, pdf) or mit_chrome(html, pdf)
    if not ok:
        sys.exit("Weder WeasyPrint noch Chrome gefunden. Installieren: "
                 "pip install weasyprint (macOS zusätzlich: brew install pango).")
    try:
        from pypdf import PdfReader
        print(f"Seiten: {len(PdfReader(str(pdf)).pages)}")
    except Exception:
        pass


if __name__ == "__main__":
    main()
