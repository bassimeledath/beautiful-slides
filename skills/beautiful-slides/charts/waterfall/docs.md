# waterfall chart

Native python-pptx waterfall chart. Shows how an initial value is affected by sequential positive/negative changes to reach a final value. Start and end columns are anchored to the baseline; intermediates float. Positive deltas use `tokens["primary"]`, negative deltas use `tokens["accent"]`, and totals use `tokens["muted"]`. Dotted connector lines bridge successive columns.

## When to use

- Explaining how a starting value transforms into an ending value through a series of gains and losses.
- Bridge charts: revenue breakdown, cost buildup, P&L walk.
- Budget variance analysis: showing where budget was gained or lost.

## When not to use

- Simple category comparisons with no cumulative story -- use a bar chart.
- Time series trends -- use a line chart.
- More than ~10 steps -- labels crowd and the narrative loses clarity.

## Data shape

```python
data = {
    "title": "Revenue bridge, Q4 to Q1",    # optional; may be None
    "steps": [
        {"label": "Q4 Revenue", "value": 100},     # starting total
        {"label": "New logos",   "value": 18},      # positive delta
        {"label": "Expansion",   "value": 12},      # positive delta
        {"label": "Churn",       "value": -8},      # negative delta
        {"label": "Contraction", "value": -5},      # negative delta
        {"label": "Q1 Revenue", "value": 117},      # ending total
    ],
    "value_suffix": "M",     # optional; appended to value labels
    "show_values": True,     # optional; default True
}
```

- 4-10 steps. First step is the starting total, last step is the ending total.
- Intermediate steps are deltas (positive or negative).
- The ending total should equal the starting total plus all intermediate deltas.

## Example

```python
from pptx import Presentation
from pptx.util import Inches
from charts.waterfall.render import render

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
    "title": "Revenue bridge, Q4 to Q1",
    "steps": [
        {"label": "Q4 Revenue", "value": 100},
        {"label": "New logos",   "value": 18},
        {"label": "Expansion",   "value": 12},
        {"label": "Churn",       "value": -8},
        {"label": "Contraction", "value": -5},
        {"label": "Q1 Revenue", "value": 117},
    ],
    "value_suffix": "M",
    "show_values": True,
}
m = Inches(0.5)
bounds = (m, m, prs.slide_width - 2 * m, prs.slide_height - 2 * m)
render(slide, data, tokens, bounds)
prs.save("example.pptx")
```
