# Balcony Solar Capstone (CELI presentation)

A single-file HTML slide deck on plug-in balcony solar for PG&E residential customers.

## Files

- `balcony-solar-slides.html`: the deck. Open it in a browser. It is self-contained apart from Google Fonts.
- `visuals/`: the interactive visuals shown inside the deck, each a standalone page:
  - `sunny-day.html`: one household on a sunny July day, hour by hour
  - `grid-cost-spread.html`: how fixed grid costs spread over fewer customers
  - `balcony-solar-model.html`: system-wide effect across PG&E's four residential schedules
- `embed_visuals.py`: copies every `visuals/*.html` into the deck so it stays one file.

## Editing a visual

1. Edit the file in `visuals/`.
2. From this folder, run `python3 embed_visuals.py`.
3. A slide uses a visual with `data-vis="<file name without .html>"`.
