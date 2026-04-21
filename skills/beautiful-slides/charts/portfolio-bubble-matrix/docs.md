# portfolio-bubble-matrix chart

Native python-pptx GE/McKinsey portfolio bubble matrix. Combines a segmented grid (2x2 or 3x3) with area-scaled bubbles positioned by (x, y) coordinates. Each bubble's radius encodes a third variable. Ideal for portfolio analysis, strategic planning, and investment prioritization.

## When to use

- GE/McKinsey nine-box portfolio analysis (market attractiveness vs. competitive strength, sized by revenue).
- Investment or product portfolio views where position in grid conveys strategic zone and bubble size conveys magnitude.
- Any strategic matrix where you want named grid cells plus a third size-encoded variable per entity.

## When not to use

- Only two variables without size encoding -> use a quadrant-2x2 chart.
- Continuous numeric axes with tick marks -> use a bubble chart.
- More than ~20 items -> bubbles overlap badly.
- No grid segmentation needed -> use a plain bubble chart.

## Data shape

```python
data = {
    "title": "GE/McKinsey portfolio matrix",              # optional
    "x_label": "Competitive strength",                     # optional axis label
    "y_label": "Market attractiveness",                    # optional axis label
    "x_segments": ["Low", "Medium", "High"],               # column headers (L-to-R)
    "y_segments": ["High", "Medium", "Low"],               # row headers (top-to-bottom)
    "quadrant_labels": [                                    # optional; row-major order
        "Selective growth", "Invest/grow", "Invest/grow",
        "Harvest", "Selective", "Selective growth",
        "Divest", "Harvest", "Selective",
    ],
    "size_label": "Revenue ($M)",                          # optional; legend title
    "show_labels": True,                                   # default True
    "show_size_legend": True,                              # default True
    "min_radius_pt": 6,                                    # optional; default 6
    "max_radius_pt": 28,                                   # optional; default 28
    "bubbles": [
        {"x": 0.85, "y": 0.9, "size": 200, "label": "Product A"},
        {"x": 0.5,  "y": 0.5, "size": 120, "label": "Product B"},
        {"x": 0.15, "y": 0.2, "size": 50,  "label": "Product C"},
    ],
}
```

- `x` and `y` are fractions 0..1 (0 = left/bottom, 1 = right/top).
- `x_segments` and `y_segments` define the grid columns and rows (default 3x3).
- `quadrant_labels` is an optional flat list in row-major order for cell labels.
- Each bubble has `x`, `y`, `size` (area-proportional), and optional `label` and `color`.
- Maximum 20 bubbles (extras are silently dropped).

## Example

```python
from pptx import Presentation
from pptx.util import Inches
from charts.portfolio_bubble_matrix.render import render

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
    "title": "GE/McKinsey portfolio matrix",
    "x_label": "Competitive strength",
    "y_label": "Market attractiveness",
    "x_segments": ["Low", "Medium", "High"],
    "y_segments": ["High", "Medium", "Low"],
    "size_label": "Revenue ($M)",
    "bubbles": [
        {"x": 0.85, "y": 0.9, "size": 200, "label": "Cloud"},
        {"x": 0.5,  "y": 0.5, "size": 120, "label": "Mobile"},
        {"x": 0.15, "y": 0.2, "size": 50,  "label": "Legacy"},
    ],
}
m = Inches(0.5)
bounds = (m, m, prs.slide_width - 2 * m, prs.slide_height - 2 * m)
render(slide, data, tokens, bounds)
prs.save("portfolio_bubble_matrix_example.pptx")
```
