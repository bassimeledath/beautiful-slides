# lollipop chart

Native python-pptx lollipop chart. A dot on a thin stem per item -- a high data-ink-ratio alternative to a bar chart. Horizontal by default. Best for ranking 5-15 items.

## When to use

- Ranking items by a single metric (e.g. top customers by revenue).
- When you want a cleaner, less ink-heavy look than solid bars.
- Horizontal orientation makes long category labels easy to read.

## When not to use

- Comparing two or more series per item -- use a grouped bar or dumbbell.
- Fewer than 5 items -- a bar chart is simpler and equally effective.
- Part-to-whole relationships -- use a stacked bar or donut.

## Data shape

```python
data = {
    "orientation": "horizontal",  # "horizontal" (default) or "vertical"
    "title": "Top 10 accounts by ARR",  # optional
    "items": [
        {"label": "Acme Corp",   "value": 2.4},
        {"label": "Globex",      "value": 1.9},
        {"label": "Initech",     "value": 1.7},
        {"label": "Umbrella",    "value": 1.3},
        {"label": "Wonka Inc",   "value": 0.9},
    ],
    "value_suffix": "M",    # optional
    "show_values": True,     # optional; default True
}
```

- Up to 15 items. Dot uses `tokens["primary"]`, stem uses `tokens["muted"]`.
- Items are rendered in the order given (pre-sort descending for a ranked list).

## Example

```python
from pptx import Presentation
from pptx.util import Inches
from charts.lollipop.render import render

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
    "orientation": "horizontal",
    "title": "Top 10 accounts by ARR",
    "items": [
        {"label": "Acme Corp",   "value": 2.4},
        {"label": "Globex",      "value": 1.9},
        {"label": "Initech",     "value": 1.7},
        {"label": "Umbrella",    "value": 1.3},
        {"label": "Wonka Inc",   "value": 0.9},
    ],
    "value_suffix": "M", "show_values": True,
}
m = Inches(0.5)
bounds = (m, m, prs.slide_width - 2 * m, prs.slide_height - 2 * m)
render(slide, data, tokens, bounds)
prs.save("example.pptx")
```
