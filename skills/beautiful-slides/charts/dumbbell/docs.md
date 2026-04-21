# dumbbell chart

Native python-pptx dumbbell chart. Two dots connected by a line per category, showing the gap between two values (before/after, plan/actual, male/female, etc.). Always horizontal.

## When to use

- Comparing two values per category to highlight the gap (e.g. 2023 vs. 2024 revenue).
- Before/after or plan/actual comparisons.
- When the magnitude of change matters as much as the individual values.

## When not to use

- Only one value per category -- use a lollipop or bar chart.
- Many categories (>15) -- the chart becomes too dense.
- Time-series data with many points -- use a line chart.

## Data shape

```python
data = {
    "title": "Satisfaction score, 2023 vs 2024",  # optional
    "series_names": ["2023", "2024"],              # labels for the two dots
    "items": [
        {"label": "Onboarding", "value_a": 72, "value_b": 88},
        {"label": "Support",    "value_a": 65, "value_b": 79},
        {"label": "Billing",    "value_a": 58, "value_b": 61},
        {"label": "Product",    "value_a": 80, "value_b": 85},
    ],
    "value_suffix": "%",    # optional
    "show_values": True,     # optional; default True
}
```

- Up to 15 items. First dot (`value_a`) uses `tokens["primary"]`, second dot (`value_b`) uses `tokens["accent"]`.
- A legend is drawn using `series_names`.
- Items are rendered in the order given.

## Example

```python
from pptx import Presentation
from pptx.util import Inches
from charts.dumbbell.render import render

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
    "title": "Satisfaction score, 2023 vs 2024",
    "series_names": ["2023", "2024"],
    "items": [
        {"label": "Onboarding", "value_a": 72, "value_b": 88},
        {"label": "Support",    "value_a": 65, "value_b": 79},
        {"label": "Billing",    "value_a": 58, "value_b": 61},
        {"label": "Product",    "value_a": 80, "value_b": 85},
    ],
    "value_suffix": "%", "show_values": True,
}
m = Inches(0.5)
bounds = (m, m, prs.slide_width - 2 * m, prs.slide_height - 2 * m)
render(slide, data, tokens, bounds)
prs.save("example.pptx")
```
