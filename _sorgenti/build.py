#!/usr/bin/env python3
"""Genera tutte le pagine della bozza GRAIA.

Uso:  python3 _sorgenti/build.py

Moduli:
  layout.py       header, footer, lingua
  it_main.py      home, portfolio
  it_dynamic.py   attività, news, team, BLU, contatti, documenti, privacy, ricerca (dai dati in data/)
  it_proposta.py  pagina "La proposta"
  en_main.py      versione inglese delle pagine principali (cartella en/)
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
ROOT = HERE.parent

import it_main, it_dynamic, it_proposta, en_main  # noqa: E402

allp = {}
for mod in (it_main, it_dynamic, it_proposta, en_main):
    for name, html in mod.pages.items():
        assert name not in allp, f"pagina duplicata: {name}"
        allp[name] = html

(ROOT / "en").mkdir(exist_ok=True)
for name, html in allp.items():
    (ROOT / name).write_text(html, encoding="utf-8")

# indice per la ricerca (client-side)
idx = [dict(t=d["t"], k=d["k"], u=d["u"], x=d["x"][:2500]) for d in it_dynamic.search_index]
(ROOT / "cerca-indice.js").write_text(
    "var INDICE=" + json.dumps(idx, ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8"
)
print(f"{len(allp)} pagine, {len(idx)} voci di ricerca")
