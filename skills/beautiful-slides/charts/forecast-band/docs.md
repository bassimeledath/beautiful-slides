# forecast-band

Central trend line with upper/lower confidence or scenario bands drawn using native python-pptx shapes.

## When to use

- Showing actuals alongside a forecast with uncertainty ranges.
- Scenario planning (base/optimistic/pessimistic).
- Displaying confidence intervals for projections.

## When not to use

- No uncertainty or range to show -> use a plain line chart.
- Comparing many independent series -> use a multi-line chart.
- Categorical data -> use a bar chart.

## Data shape

```python
data = {
    "x_labels": ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6"],
    "actuals": [100, 110, 108, 115],             # observed values (solid line)
    "forecast": [100, 110, 108, 115, 122, 130],   # full forecast (dashed from forecast_start)
    "upper": [100, 115, 116, 125, 140, 155],       # upper confidence bound
    "lower": [100, 105, 100, 105, 104, 105],       # lower confidence bound
    "title": "Revenue forecast with 90% CI",       # optional
    "x_label": "Quarter",                          # optional
    "y_label": "Revenue ($M)",                     # optional subtitle
    "forecast_start": 4,                           # index where forecast begins (default: len(actuals))
    "band_label": "90% CI",                        # optional legend label for band
}
```

- `actuals` is drawn as a solid line; stops where observed data ends.
- `forecast` covers the full x-axis; segments from `forecast_start` onward are dashed.
- `upper`/`lower` define the shaded band (semi-transparent fill using `tokens["primary"]`).
- The junction point (last actual) is highlighted with `tokens["accent"]`.

## Example

```python
from pptx import Presentation
from pptx.util import Inches
from charts.forecast_band.render import render

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
    "x_labels": ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6"],
    "actuals": [100, 110, 108, 115],
    "forecast": [100, 110, 108, 115, 122, 130],
    "upper": [100, 115, 116, 125, 140, 155],
    "lower": [100, 105, 100, 105, 104, 105],
    "title": "Revenue forecast with 90% CI",
    "band_label": "90% CI",
}
m = Inches(0.5)
bounds = (m, m, prs.slide_width - 2 * m, prs.slide_height - 2 * m)
render(slide, data, tokens, bounds)
prs.save("example.pptx")
```
