# histogram

Native python-pptx histogram chart. Adjacent bars (no gaps) showing frequency distribution of continuous data across equal-width bins.

## When to use

- Showing the distribution / frequency of a continuous variable.
- Understanding spread, skewness, and outliers in a dataset.
- Comparing actual distribution against expectations.

## When not to use

- Categorical comparisons -> use a bar chart.
- Time-series data -> use a line chart.
- Fewer than ~15 data points -> raw values or a dot plot may be clearer.

## Data shape

```python
data = {
    "values": [23.1, 45.0, 12.8, ...],  # raw numeric observations
    "bins": 10,                           # number of equal-width bins (default 10)
    "title": "Response time distribution", # optional
    "x_label": "Latency (ms)",            # optional x-axis label
    "y_label": "Frequency",               # optional y-axis label / subtitle
    "value_suffix": "ms",                 # optional suffix on x-axis tick labels
    "show_counts": False,                 # show count above each bar (default False)
}
```

- `values` is binned automatically into `bins` equal-width buckets.
- Bars use `tokens["primary"]`; no gaps between adjacent bars.

## Example

```python
from pptx import Presentation
from pptx.util import Inches
from charts.histogram.render import render

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
    "values": [12, 15, 14, 10, 18, 22, 25, 30, 28, 35, 40, 42, 38, 50, 55],
    "bins": 8,
    "title": "Response time distribution",
    "x_label": "Latency (ms)",
}
m = Inches(0.5)
bounds = (m, m, prs.slide_width - 2 * m, prs.slide_height - 2 * m)
render(slide, data, tokens, bounds)
prs.save("example.pptx")
```
