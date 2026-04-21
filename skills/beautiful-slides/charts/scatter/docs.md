# scatter chart

Native python-pptx scatter plot. Points on x/y axes showing the relationship between two continuous variables. Supports optional trend line, optional divider lines, and optional direct labels per point.

## When to use

- Showing correlation or relationship between two numeric variables (e.g., spend vs. revenue).
- Identifying outliers or clusters in data.
- Overlaying a trend line (OLS) to show directionality.
- Adding divider lines to split the field into quadrants for simple segmentation.

## When not to use

- Categorical x-axis with discrete buckets → use a bar chart.
- Encoding a third variable by size → use a bubble chart.
- More than ~25 points → labels crowd; consider dropping `show_labels`.

## Data shape

```python
data = {
    "title": "Ad spend vs. revenue",               # optional
    "x_label": "Ad spend ($K)",                     # optional axis label
    "y_label": "Revenue ($K)",                      # optional axis label
    "show_labels": True,                            # default True; label each point
    "show_trend_line": True,                        # default False; OLS best-fit
    "x_divider": 50,                                # optional vertical divider at x=50
    "y_divider": 200,                               # optional horizontal divider at y=200
    "point_radius_pt": 5,                           # optional; default 5
    "points": [
        {"x": 12, "y":  95, "label": "Acme"},
        {"x": 34, "y": 180, "label": "Beta"},
        {"x": 55, "y": 240, "label": "Gamma"},
        {"x": 78, "y": 310, "label": "Delta"},
    ],
}
```

- Each point has `x` (float), `y` (float), and optional `label` (str).
- Points may include an optional `color` hex string to override `tokens["primary"]`.
- First series uses `tokens["primary"]` for dots; trend line uses `tokens["accent"]`.

## Example

```python
from pptx import Presentation
from pptx.util import Inches
from charts.scatter.render import render

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
    "title": "Ad spend vs. revenue",
    "x_label": "Ad spend ($K)",
    "y_label": "Revenue ($K)",
    "show_trend_line": True,
    "points": [
        {"x": 12, "y":  95, "label": "Acme"},
        {"x": 34, "y": 180, "label": "Beta"},
        {"x": 55, "y": 240, "label": "Gamma"},
        {"x": 78, "y": 310, "label": "Delta"},
    ],
}
m = Inches(0.5)
bounds = (m, m, prs.slide_width - 2 * m, prs.slide_height - 2 * m)
render(slide, data, tokens, bounds)
prs.save("scatter_example.pptx")
```
