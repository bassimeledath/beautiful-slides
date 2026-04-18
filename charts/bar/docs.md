# bar chart

Native python-pptx bar chart. Supports vertical and horizontal orientations, single-series and grouped (2-series) forms.

## When to use

- Discrete comparisons across a small number of categories (3–12).
- Showing actuals vs. plan, or two related series side-by-side (grouped).
- When the emphasis is on ranking/magnitude rather than trend over time.

## When not to use

- Time series with many points → use a line chart.
- Part-to-whole where categories sum to a meaningful total → use a stacked bar or donut.
- More than ~12 categories → the labels crowd.

## Data shape

```python
data = {
    "orientation": "vertical",   # "vertical" or "horizontal"
    "title": "Revenue by segment, Q1",   # optional; may be None
    "categories": ["Enterprise", "Mid-market", "SMB", "Startup"],
    "series": [
        {"name": "Q1 Actual", "values": [12.4, 8.1, 4.3, 1.8]},
        {"name": "Q1 Plan",   "values": [11.0, 8.5, 5.0, 2.0]},   # optional
    ],
    "value_suffix": "M",    # optional; appended to each value label
    "show_values": True,    # optional; default True
}
```

- Up to 2 series. First series uses `tokens["primary"]`, second uses `tokens["accent"]`.
- When 2 series are provided, a small legend is drawn at the top-right.

## Example

```python
from pptx import Presentation
from pptx.util import Inches, Emu
from charts.bar.render import render

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
    "orientation": "vertical",
    "title": "Revenue by segment, Q1",
    "categories": ["Enterprise", "Mid-market", "SMB", "Startup"],
    "series": [{"name": "Q1 Actual", "values": [12.4, 8.1, 4.3, 1.8]}],
    "value_suffix": "M", "show_values": True,
}
m = Inches(0.5)
bounds = (m, m, prs.slide_width - 2 * m, prs.slide_height - 2 * m)
render(slide, data, tokens, bounds)
prs.save("example.pptx")
```
