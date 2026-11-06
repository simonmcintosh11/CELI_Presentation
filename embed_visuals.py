"""Embed every visuals/*.html into balcony-solar-slides.html so the deck stays one file.

Run from this folder:  python3 embed_visuals.py
A slot uses a visual with data-vis="<file name without .html>".
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
DECK = HERE / "balcony-solar-slides.html"

docs = {p.stem: p.read_text(encoding="utf-8") for p in sorted((HERE / "visuals").glob("*.html"))}
payload = json.dumps(docs, ensure_ascii=False).replace("</", "<\\/")

html = DECK.read_text(encoding="utf-8")
new, n = re.subn(
    r"/\*DOCS-START\*/.*?/\*DOCS-END\*/",
    lambda _: "/*DOCS-START*/var DOCS=" + payload + ";/*DOCS-END*/",
    html,
    flags=re.S,
)
if n != 1:
    raise SystemExit("DOCS markers not found in the deck")
DECK.write_text(new, encoding="utf-8")
print("Embedded:", ", ".join(docs))
