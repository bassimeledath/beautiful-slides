# sparkline strip

Row of tiny inline line charts (sparklines) paired with KPI labels and current values. Each metric shows a label, hero value, optional delta, and a small trendline.

## Usage

```python
from charts.sparkline_strip.render import render

render(slide, data, tokens, bounds)
```

## Data shape

```python
data = {
    "title": "Key metrics dashboard",              # optional
    "metrics": [
        {
            "name": "Revenue",
            "value": 2.4,
            "prefix": "$",
            "suffix": "M",
            "delta": 0.3,
            "delta_label": "vs prev quarter",
            "sparkline": [1.8, 1.9, 2.0, 2.1, 2.0, 2.2, 2.3, 2.4],
        },
        {
            "name": "Active Users",
            "value": 14200,
            "suffix": "",
            "delta": 1200,
            "delta_label": "MoM",
            "sparkline": [11000, 11500, 12000, 12800, 13200, 13500, 14000, 14200],
        },
        {
            "name": "Churn Rate",
            "value": 3.2,
            "suffix": "%",
            "delta": -0.5,
            "delta_label": "vs last month",
            "sparkline": [4.1, 3.9, 3.8, 3.7, 3.5, 3.4, 3.3, 3.2],
        },
        {
            "name": "NPS",
            "value": 72,
            "delta": 4,
            "sparkline": [60, 62, 65, 67, 68, 70, 71, 72],
        },
    ],
}
```

- `metrics`: 4-8 entries recommended.
- Each metric has `name`, `value`, optional `prefix`/`suffix` for formatting, optional `delta` (numeric change), optional `delta_label`, and `sparkline` (list of numeric values, minimum 2 points).
- `sparkline` values of `None` are treated as gaps.

## Styling

- Background fills with `tokens["bg"]`.
- Title uses `tokens["font_display"]`, bold, ~1.55x base size.
- Metric labels use `tokens["font_body"]` in `tokens["muted"]`.
- Hero values use `tokens["font_display"]`, bold, in `tokens["text"]`.
- Positive deltas use `tokens["accent"]`; negative deltas use `tokens["primary"]`.
- Sparklines are drawn in `tokens["primary"]` with ~1.5pt weight.
- End point of each sparkline is marked with a small `tokens["accent"]` dot.
- Layout auto-grids: 1 row for 4 or fewer, 2 rows for 5-8 metrics.

## Proof

Ran `python example.py` -- emits 5 `.pptx` files, one per mode. OK.
