# bubble chart

Native python-pptx bubble chart. Scatter plot where point size (area-scaled circles) encodes a third variable. Supports optional size legend and direct labels.

## When to use

- Three-variable comparison: two continuous axes plus a magnitude dimension (e.g., revenue vs. growth, sized by headcount).
- Portfolio or market-map views where each bubble is an entity.
- When you want to show clusters and outliers with an extra size encoding.

## When not to use

- Only two variables → use a scatter chart (no size encoding needed).
- More than ~20 items → bubbles overlap badly.
- Categorical x-axis → use a bar chart instead.

## Data shape

```python
data = {
    "title": "Market opportunity map",                  # optional
    "x_label": "Market growth (%)",                     # optional axis label
    "y_label": "Market share (%)",                      # optional axis label
    "size_label": "Revenue ($M)",                       # optional; legend title
    "show_labels": True,                                # default True
    "show_size_legend": True,                           # default True
    "min_radius_pt": 4,                                 # optional; default 4
    "max_radius_pt": 28,                                # optional; default 28
    "bubbles": [
        {"x": 12, "y": 35, "size": 50,  "label": "Product A"},
        {"x": 28, "y": 60, "size": 120, "label": "Product B"},
        {"x": 45, "y": 22, "size": 30,  "label": "Product C"},
        {"x": 60, "y": 75, "size": 200, "label": "Product D"},
    ],
}
```

- Each bubble has `x` (float), `y` (float), `size` (float, area-proportional), and optional `label` (str).
- Bubbles may include optional `color` hex string to override `tokens["primary"]`.
- Maximum 20 bubbles (extras are silently dropped).
- Labels render inside the bubble if they fit; otherwise they appear to the right (or left near the edge).

## Example

```python
from pptx import Presentation
from pptx.util import Inches
from charts.bubble.render import render

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
    "title": "Market opportunity map",
    "x_label": "Market growth (%)",
    "y_label": "Market share (%)",
    "size_label": "Revenue ($M)",
    "bubbles": [
        {"x": 12, "y": 35, "size": 50,  "label": "Product A"},
        {"x": 28, "y": 60, "size": 120, "label": "Product B"},
        {"x": 45, "y": 22, "size": 30,  "label": "Product C"},
        {"x": 60, "y": 75, "size": 200, "label": "Product D"},
    ],
}
m = Inches(0.5)
bounds = (m, m, prs.slide_width - 2 * m, prs.slide_height - 2 * m)
render(slide, data, tokens, bounds)
prs.save("bubble_example.pptx")
```
