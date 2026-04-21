# cohort-retention

Triangular heatmap showing user retention by cohort. Rows represent cohorts (earliest at top), columns represent periods since start. Later cohorts naturally have fewer data points, producing the characteristic triangular shape. Cell fill intensity maps retention percentage using a gradient from `tokens["bg"]` to `tokens["accent"]`.

## API

```python
render(slide, data, tokens, bounds)
```

## Data shape

```python
data = {
    "title": "Weekly cohort retention",                # optional
    "cohorts": ["Jan W1", "Jan W2", "Jan W3", ...],    # row labels
    "periods": ["Week 0", "Week 1", "Week 2", ...],    # column labels
    "values": [                                         # row-major, ragged OK
        [1.0, 0.82, 0.71, 0.65, 0.58],                 # oldest cohort — most periods
        [1.0, 0.79, 0.68, 0.60],                        # next cohort — one fewer
        [1.0, 0.75, 0.63],                               # etc.
        [1.0, 0.80],
        [1.0],                                           # newest cohort — only period 0
    ],
    "value_min": 0.0,                                   # optional, auto from values
    "value_max": 1.0,                                   # optional, auto from values
    "value_format": "{:.0%}",                           # python format string
}
```

Use `None` in a row to indicate a missing data point that should render as an empty cell.

## Layout

- Title at top (if provided), `font_display`, `text`.
- Column labels across the top row, `font_body`, `muted`, ~0.75x base size.
- Row labels on the left, right-aligned, `font_body`, `muted`.
- Cell grid fills remaining area; hairline gap + hairline `muted` outline at 0.25pt.
- Filled cells: `lerp(bg, accent, normalized_value)`. Empty cells (beyond the cohort's available data) show `bg` fill with `muted` outline.
- Values always displayed in cells using `font_mono`, auto-chosen color (light vs dark) based on cell luminance.
- `radius_px` honored via `MSO_SHAPE.ROUNDED_RECTANGLE`.
- Legend strip bottom-right: 24-step gradient from bg to accent + min/max labels in `font_mono`/`muted`.

## Tokens used

`primary`, `accent`, `text`, `muted`, `bg`, `font_display`, `font_body`, `font_mono`, `font_size_base_pt`, `radius_px`.

## Proof

`python example.py` writes `example-<mode>.pptx` at the chart root, one per mode.
