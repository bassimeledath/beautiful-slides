# area chart

Line chart with filled region between line and x-axis. Supports single-series and stacked (max 4 series) with semi-transparent fills.

## Usage

```python
from charts.area.render import render

render(slide, data, tokens, bounds)
```

## Data shape

```python
data = {
    "title": "Monthly active users by platform",           # optional
    "x_labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "series": [
        {"name": "Mobile",  "values": [120, 135, 148, 162, 175, 190]},
        {"name": "Desktop", "values": [80, 78, 75, 72, 70, 68]},
        {"name": "Tablet",  "values": [30, 32, 35, 38, 40, 42]},
    ],
    "x_label": "Month",                  # optional
    "y_label": "Users (thousands)",       # optional
    "stacked": True,                      # optional; default False
}
```

- `series`: 1-4 series supported. Each has `name` and `values`.
- `values` may be shorter than `x_labels`. `None` values are treated as missing.
- `stacked`: when True, series values are cumulated so areas stack on top of each other. When False, areas overlap with transparency.

## Styling

- Background fills with `tokens["bg"]`.
- Title uses `tokens["font_display"]`, bold, ~1.55x base size.
- Series 1 uses `tokens["primary"]`, series 2 uses `tokens["accent"]`, additional series use blended variants.
- Fill areas are semi-transparent (~35-50% opacity).
- Lines on top of fills are ~2pt weight.
- Gridlines and axes are hairlines in `tokens["muted"]`.
- Y tick labels use `tokens["font_mono"]`; X tick labels use `tokens["font_body"]`.
- When multiple series, a compact legend sits above the top-right of the plot area.

## Proof

Ran `python example.py` -- emits 5 `.pptx` files, one per mode. OK.
