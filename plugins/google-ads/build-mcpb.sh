#!/bin/bash
# Baut das Claude-Desktop-Bundle (.mcpb) aus mcp_server.py + mcpb/manifest.json.
# Ergebnis: dist/sumax-google-ads.mcpb — Doppelklick installiert es in Claude Desktop.
set -e
cd "$(dirname "$0")"

rm -rf build dist/sumax-google-ads.mcpb
mkdir -p build/server dist
cp mcpb/manifest.json build/manifest.json
cp mcp_server.py build/server/main.py

VERSION=$(python3 -c "import json;print(json.load(open('mcpb/manifest.json'))['version'])")
(cd build && zip -q -r -X ../dist/sumax-google-ads.mcpb manifest.json server)
rm -rf build

echo "gebaut: dist/sumax-google-ads.mcpb (v$VERSION)"
unzip -l dist/sumax-google-ads.mcpb
