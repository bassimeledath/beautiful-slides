# risk-heat-matrix

Impact vs likelihood risk matrix. Rows represent impact levels (highest at top), columns represent likelihood levels (lowest at left). Cell background color indicates severity via a gradient derived from `tokens["accent"]` (low risk) through a blend to `tokens["primary"]` (high risk), all tinted toward `tokens["bg"]`. Named risks are placed as text labels in their respective cells.

## API

```python
render(slide, data, tokens, bounds)
```

## Data shape

```python
data = {
    "title": "Project risk assessment",                     # optional
    "grid_size": 5,                                         # 3 or 5 (default 5)
    "impact_labels": ["Critical", "High", "Medium",         # top to bottom
                      "Low", "Negligible"],
    "likelihood_labels": ["Rare", "Unlikely", "Possible",   # left to right
                          "Likely", "Almost Certain"],
    "x_axis_label": "Likelihood",                           # optional, default "Likelihood"
    "y_axis_label": "Impact",                               # optional, default "Impact"
    "risks": [
        {"name": "Data breach", "impact": 0, "likelihood": 2},    # row 0 = highest impact
        {"name": "Key person leaves", "impact": 1, "likelihood": 3},
        {"name": "Budget overrun", "impact": 2, "likelihood": 4},
    ],
}
```

`impact` and `likelihood` are 0-based indices into the label arrays. Row 0 is the highest impact (top of grid).

## Layout

- Title at top (if provided), `font_display`, `text`.
- Y-axis label on the far left, `font_body`, `muted`, bold.
- X-axis label at the bottom, `font_body`, `muted`, bold.
- Impact labels (rows) right-aligned on left side, `font_body`, `muted`.
- Likelihood labels (columns) centered across top, `font_body`, `muted`.
- Cell grid fills remaining area; hairline gap + hairline `muted` outline.
- Cell fill: severity gradient from `accent` (low) to blended mid to `primary` (high), tinted toward `bg`.
- Risk labels centered in cells, `font_body`, auto-chosen text color based on luminance.
- `radius_px` honored via `MSO_SHAPE.ROUNDED_RECTANGLE`.

## Tokens used

`primary`, `accent`, `text`, `muted`, `bg`, `font_display`, `font_body`, `font_mono`, `font_size_base_pt`, `radius_px`.

## Proof

`python example.py` writes `example-<mode>.pptx` at the chart root, one per mode.
