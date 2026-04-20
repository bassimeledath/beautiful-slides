# line chart

Single- or multi-series line chart drawn with native python-pptx connectors.

## Usage

```python
from charts.line.render import render

render(slide, data, tokens, bounds)
```

## Data shape

```python
data = {
    "title": "Revenue retention by cohort, first 12 months",  # optional
    "x_labels": ["M0", "M1", ..., "M12"],
    "series": [
        {"name": "Q1 '25", "values": [100, 98, ..., 106]},
        {"name": "Q2 '25", "values": [100, 99, ..., 110]},
        {"name": "Q3 '25", "values": [100, 102, ..., 113]},   # shorter ok
        {"name": "Q4 '25", "values": [100, 104, 111, 118]},    # shorter ok
    ],
    "x_label": "Months from cohort start",   # optional
    "y_label": "Revenue retention (%)",       # optional
    "emphasize_last_series": True,            # primary style goes to last series
    "end_labels": True,                       # direct end-of-line labels vs legend
}
```

- `values` may be shorter than `x_labels` (partial / in-flight series).
- A value of `None` is treated as missing and breaks the line.

## Styling

- Background fills with `tokens["bg"]`.
- Emphasized series: `tokens["primary"]`, ~2.25pt. Other series: `tokens["muted"]`, ~1.25pt, dashed variants for separation.
- Single series always uses `tokens["primary"]`.
- Last point of the primary series is marked with a small `tokens["accent"]` circle.
- Gridlines and axes are hairlines in `tokens["muted"]`.
- Y tick labels use `tokens["font_mono"]`; X tick labels use `tokens["font_body"]`.
- Title uses `tokens["font_display"]`, bold, ~1.55× base size.
- When `end_labels=False`, a compact legend sits above the top-right of the plot area.

## Proof

Ran `python example.py` — emits 5 `.pptx` files, one per mode. OK.
