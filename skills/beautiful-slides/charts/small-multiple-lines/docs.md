# Small-multiple lines

Grid of repeated mini line charts sharing a common y-scale. Each panel has its own title and draws a single trend line. Best for comparing the same metric across many segments (regions, cohorts, products).

## `render(slide, data, tokens, bounds)`

### `data`

```python
{
    "title": "Monthly Active Users by Region",       # optional
    "y_label": "MAU (thousands)",                    # optional
    "x_labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "panels": [
        {"title": "North America", "values": [120, 125, 130, 128, 135, 142]},
        {"title": "Europe",        "values": [80, 82, 85, 88, 90, 94]},
        {"title": "APAC",          "values": [45, 50, 55, 62, 70, 78]},
        {"title": "LATAM",         "values": [30, 32, 31, 35, 38, 40]},
        {"title": "MEA",           "values": [15, 16, 18, 20, 22, 25]},
        {"title": "ANZ",           "values": [12, 13, 14, 15, 16, 18]},
    ],
}
```

### Behavior

- Up to 12 panels. Grid layout auto-selects: 1x2, 2x2, 2x3, 3x3, or 3x4 based on panel count.
- All panels share the same y-axis scale (min/max computed globally).
- Each panel shows: title (bold, `font_body`), top/bottom y-tick labels (`font_mono`, `muted`), top/bottom gridlines.
- Lines drawn in `primary`; last data point gets an `accent` dot.
- First and last x-axis labels shown per panel when `x_labels` provided.
- Optional overall `title` (`font_display`, bold) and `y_label` (`font_body`, `muted`) above the grid.

### Constraints

- Draws entirely inside `bounds`.
- All colors/fonts come from `tokens`. No hardcoded hex or font names.
- Native python-pptx shapes only.

## Proof

`python example.py` generates five `example-<mode>.pptx` files without errors.
