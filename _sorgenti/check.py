#!/usr/bin/env python3
"""Controlla link e immagini relativi e le ancore in tutte le pagine."""
import re, sys
from pathlib import Path
from urllib.parse import urlparse, unquote
ROOT = Path(__file__).resolve().parent.parent
files = list(ROOT.glob("*.html")) + list(ROOT.glob("en/*.html"))
ids = {f: set(re.findall(r'\sid="([^"]+)"', f.read_text(encoding="utf-8"))) for f in files}
bad = []
for f in files:
    h = f.read_text(encoding="utf-8")
    for attr, u in re.findall(r'(href|src)="([^"]+)"', h):
        if re.match(r"(https?:|mailto:|tel:|#$|data:)", u) or u.startswith("javascript") or "+" in u or "'" in u:
            continue
        p = urlparse(u)
        target = (f.parent / unquote(p.path)).resolve() if p.path else f
        if not target.exists():
            bad.append((f.name, u)); continue
        if p.fragment and target.suffix == ".html" and p.fragment not in ids.get(target, set()):
            bad.append((f.name, u + " (ancora mancante)"))
print(len(files), "pagine controllate;", len(bad), "problemi")
for b in bad[:60]: print(b)
sys.exit(1 if bad else 0)
