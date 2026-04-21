# league-table

Ranked table with inline visual elements drawn using native python-pptx shapes. Supports inline bars for magnitude, directional arrows, and badge labels. Top/bottom row highlighting.

## When to use

- Ranked lists with supporting metrics (leaderboards, scorecards).
- Comparing entities across multiple dimensions with visual cues.
- When you want table clarity plus chart-like visual encoding.

## When not to use

- Pure data tables with no visual encoding -> use a plain table.
- Time-series trends -> use a line chart.
- Part-to-whole relationships -> use a donut or stacked bar.

## Data shape

```python
data = {
    "title": "Sales leaderboard, Q1",
    "columns": [
        {"name": "Rep",      "key": "rep",    "type": "text",   "width_pct": 2.0},
        {"name": "Revenue",  "key": "rev",    "type": "bar",    "suffix": "K"},
        {"name": "Deals",    "key": "deals",  "type": "number"},
        {"name": "Trend",    "key": "trend",  "type": "arrow"},
        {"name": "Tier",     "key": "tier",   "type": "badge"},
    ],
    "rows": [
        {"rep": "Alice",  "rev": 420, "deals": 18, "trend": "up",   "tier": "Gold"},
        {"rep": "Bob",    "rev": 380, "deals": 15, "trend": "up",   "tier": "Gold"},
        {"rep": "Carlos", "rev": 310, "deals": 12, "trend": "flat", "tier": "Silver"},
        {"rep": "Dana",   "rev": 280, "deals": 10, "trend": "down", "tier": "Silver"},
        {"rep": "Eve",    "rev": 190, "deals": 7,  "trend": "down", "tier": "Bronze"},
    ],
    "highlight_top": 2,
    "highlight_bottom": 1,
    "show_rank": True,
}
```

### Column types

| type     | Renders as                                                       |
|----------|------------------------------------------------------------------|
| `text`   | Plain left-aligned text.                                         |
| `number` | Right-aligned mono-font number with optional suffix.             |
| `bar`    | Number label + inline horizontal bar scaled to max value.        |
| `arrow`  | Directional triangle: "up" (accent), "down" (primary), "flat".  |
| `badge`  | Small pill/rectangle label in muted color.                       |

### Highlight

- `highlight_top: N` adds a semi-transparent primary background to the top N rows.
- `highlight_bottom: N` adds a semi-transparent accent background to the bottom N rows.

## Example

```python
from pptx import Presentation
from pptx.util import Inches
from charts.league_table.render import render

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
slide = prs.slides.add_slide(prs.slide_layouts[6])

tokens = {
    "primary": "#0F4C81", "accent": "#05603A", "text": "#101828",
    "muted": "#475467", "bg": "#FFFFFF",
    "font_display": "Public Sans", "font_body": "Public Sans",
    "font_mono": "Public Sans", "font_size_base_pt": 14, "radius_px": 0,
}
data = { ... }  # see above
m = Inches(0.5)
bounds = (m, m, prs.slide_width - 2 * m, prs.slide_height - 2 * m)
render(slide, data, tokens, bounds)
prs.save("example.pptx")
```
