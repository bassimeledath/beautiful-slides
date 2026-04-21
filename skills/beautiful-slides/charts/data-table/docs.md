# data-table

Clean styled table with header row, aligned columns, optional row striping, and optional cell highlights. Applies mode tokens for colors/fonts, uses tabular figures for numeric columns, and provides controlled padding.

## API

```python
render(slide, data, tokens, bounds)
```

## Data shape

```python
data = {
    "title": "Q1 Revenue by Region",            # optional
    "columns": [
        {"label": "Region", "align": "left"},
        {"label": "Revenue", "align": "right"},
        {"label": "Growth", "align": "right"},
        {"label": "Margin", "align": "right"},
    ],
    "rows": [
        ["North America", "$12.4M", "+18%", "72%"],
        ["EMEA",          "$8.1M",  "+12%", "68%"],
        ["APAC",          "$5.6M",  "+34%", "65%"],
    ],
    "highlight_cells": [[0, 1], [2, 2]],         # optional (row, col) pairs
    "row_striping": true,                         # optional, default true
}
```

## Layout

- Title at top (if provided), `font_display`, `text`, bold, ~1.15x base.
- Header row: uppercased labels in `font_body`, `muted`, bold, ~0.85x base.
- Header bottom border: 1.5pt line in `primary`.
- Body rows: `font_body` for left/center-aligned, `font_mono` for right-aligned (numeric) columns.
- Row striping: alternating rows get a subtle tint (light mix of `bg` toward `muted`).
- Highlighted cells: subtle `primary` tint background, `primary`-colored bold text.
- Row separators: hairline `muted` lines between body rows.
- Columns are evenly distributed across width.

## Tokens used

`primary`, `accent`, `text`, `muted`, `bg`, `font_display`, `font_body`, `font_mono`, `font_size_base_pt`, `radius_px`.

## Proof

`python example.py` writes `example-<mode>.pptx` at the chart root, one per mode.
