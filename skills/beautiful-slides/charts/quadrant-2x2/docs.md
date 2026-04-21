# quadrant-2x2 chart

Native python-pptx 2x2 quadrant matrix. The iconic consulting strategy slide: four-quadrant grid with labeled axes and quadrant labels. Items placed as dots with labels.

## When to use

- Effort vs. impact prioritization (quick wins, big bets, fill-ins, money pits).
- BCG-style growth-share matrices (stars, cash cows, question marks, dogs).
- Any two-axis categorization where you want four named zones.
- Strategic positioning of products, teams, or initiatives.

## When not to use

- Continuous numeric axes with precise tick marks -> use a scatter chart.
- More than ~12 items -> labels crowd.
- When you need a third dimension (size) -> use a bubble chart.

## Data shape

```python
data = {
    "title": "Effort vs. impact prioritization",       # optional
    "x_label": "Effort",                                # optional axis label
    "y_label": "Impact",                                # optional axis label
    "x_low_label": "Low",                               # optional endpoint
    "x_high_label": "High",                             # optional endpoint
    "y_low_label": "Low",                               # optional endpoint
    "y_high_label": "High",                             # optional endpoint
    "quadrant_labels": [                                # [TL, TR, BR, BL]
        "Rethink",          # top-left
        "Big bets",         # top-right
        "Fill-ins",         # bottom-right
        "Quick wins",       # bottom-left
    ],
    "point_radius_pt": 5,                               # optional; default 5
    "items": [
        {"x": 0.2, "y": 0.8, "label": "Project A"},    # x,y in 0..1
        {"x": 0.7, "y": 0.9, "label": "Project B"},
        {"x": 0.8, "y": 0.3, "label": "Project C"},
        {"x": 0.15, "y": 0.25, "label": "Project D"},
    ],
}
```

- `x` and `y` are fractions 0..1 (0 = left/bottom, 1 = right/top).
- `quadrant_labels` order: top-left, top-right, bottom-right, bottom-left.
- Items may include optional `color` hex string to override `tokens["primary"]`.

## Example

```python
from pptx import Presentation
from pptx.util import Inches
from charts.quadrant_2x2.render import render

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
data = {
    "title": "Effort vs. impact",
    "x_label": "Effort", "y_label": "Impact",
    "x_low_label": "Low", "x_high_label": "High",
    "y_low_label": "Low", "y_high_label": "High",
    "quadrant_labels": ["Rethink", "Big bets", "Fill-ins", "Quick wins"],
    "items": [
        {"x": 0.2, "y": 0.8, "label": "Project A"},
        {"x": 0.7, "y": 0.9, "label": "Project B"},
        {"x": 0.8, "y": 0.3, "label": "Project C"},
        {"x": 0.15, "y": 0.25, "label": "Project D"},
    ],
}
m = Inches(0.5)
bounds = (m, m, prs.slide_width - 2 * m, prs.slide_height - 2 * m)
render(slide, data, tokens, bounds)
prs.save("quadrant_example.pptx")
```
