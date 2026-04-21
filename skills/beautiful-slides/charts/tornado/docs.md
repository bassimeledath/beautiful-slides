# tornado chart

Native python-pptx tornado (butterfly) chart. Two horizontal bar series extend left and right from a shared central category axis. Used for sensitivity analysis, population pyramids, and bilateral comparisons.

## When to use

- Sensitivity / tornado analysis: showing how each input variable pushes a result up or down.
- Population pyramids: age-band breakdowns by gender.
- Any bilateral comparison where two metrics share the same categories and you want to compare magnitudes side-by-side.

## When not to use

- More than 2 series -- use a grouped bar chart.
- Time series / trend -- use a line chart.
- Unrelated categories with no natural pairing -- use separate bar charts.

## Data shape

```python
data = {
    "title": "Sensitivity analysis: NPV drivers",   # optional; may be None
    "categories": ["Discount rate", "Revenue growth", "COGS %", "CapEx", "Terminal value"],
    "left": {
        "name": "Downside",
        "values": [38, 25, 22, 18, 15],
    },
    "right": {
        "name": "Upside",
        "values": [42, 30, 19, 14, 12],
    },
    "value_suffix": "M",     # optional
    "show_values": True,     # optional; default True
}
```

- `categories` labels sit on the shared center axis.
- `left` extends bars to the left using `tokens["primary"]`.
- `right` extends bars to the right using `tokens["accent"]`.
- Both series share the same scale (largest absolute value determines the axis range).

## Example

```python
from pptx import Presentation
from pptx.util import Inches
from charts.tornado.render import render

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
    "title": "Sensitivity analysis: NPV drivers",
    "categories": ["Discount rate", "Revenue growth", "COGS %", "CapEx", "Terminal value"],
    "left":  {"name": "Downside", "values": [38, 25, 22, 18, 15]},
    "right": {"name": "Upside",   "values": [42, 30, 19, 14, 12]},
    "value_suffix": "M",
    "show_values": True,
}
m = Inches(0.5)
bounds = (m, m, prs.slide_width - 2 * m, prs.slide_height - 2 * m)
render(slide, data, tokens, bounds)
prs.save("example.pptx")
```
