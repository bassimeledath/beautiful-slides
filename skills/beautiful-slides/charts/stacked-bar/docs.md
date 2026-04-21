# stacked-bar chart

Native python-pptx stacked-bar chart. Bars are split into additive colored segments showing part-to-whole within each category. Supports vertical and horizontal orientations, plus a percentage-stacked variant.

## When to use

- Part-to-whole comparisons across a small number of categories (3-10).
- Showing composition of a total (e.g. revenue by product within each region).
- Comparing how segment mix varies across categories.

## When not to use

- Too many segments (>5) -- colors become hard to distinguish.
- When individual segment values matter more than the total -- use a grouped bar.
- Only one segment -- use a regular bar chart instead.

## Data shape

```python
data = {
    "orientation": "vertical",   # "vertical" or "horizontal"
    "title": "Revenue by product, per region",  # optional; may be None
    "categories": ["AMER", "EMEA", "APAC", "LATAM"],
    "series": [
        {"name": "Product A", "values": [8.2, 5.1, 3.4, 1.2]},
        {"name": "Product B", "values": [4.1, 3.9, 2.8, 0.9]},
        {"name": "Product C", "values": [2.0, 1.5, 1.1, 0.6]},
    ],
    "value_suffix": "M",    # optional; appended to each value label
    "show_values": True,     # optional; default True
    "percent": False,        # optional; if True, normalize each bar to 100%
}
```

- Up to 5 series (segments). Colors cycle through `primary`, `accent`, `muted`, `text`.
- When `percent` is True, each bar is normalized to 100% and segment labels show percentages.
- A legend is drawn when there are 2+ series.

## Example

```python
from pptx import Presentation
from pptx.util import Inches
from charts.stacked_bar.render import render

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
slide = prs.slides.add_slide(prs.slide_layouts[6])

tokens = {
    "primary": "#21D4FD", "accent": "#17B26A", "text": "#F5F7FA",
    "muted": "#9AA4B2", "bg": "#05070A",
    "font_display": "Manrope", "font_body": "Manrope",
    "font_mono": "JetBrains Mono", "font_size_base_pt": 18, "radius_px": 6,
}
data = {
    "orientation": "vertical",
    "title": "Revenue by product, per region",
    "categories": ["AMER", "EMEA", "APAC", "LATAM"],
    "series": [
        {"name": "Product A", "values": [8.2, 5.1, 3.4, 1.2]},
        {"name": "Product B", "values": [4.1, 3.9, 2.8, 0.9]},
        {"name": "Product C", "values": [2.0, 1.5, 1.1, 0.6]},
    ],
    "value_suffix": "M", "show_values": True,
}
m = Inches(0.5)
bounds = (m, m, prs.slide_width - 2 * m, prs.slide_height - 2 * m)
render(slide, data, tokens, bounds)
prs.save("example.pptx")
```
