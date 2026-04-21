# rag-status-matrix

Red/Amber/Green status grid for tracking workstream health across criteria or milestones. Rows represent workstreams or items, columns represent criteria or milestones. Each cell contains a colored circle indicator showing RAG status. Colors are derived from the theme tokens: R uses `primary`, G uses `accent`, and A uses a blend of both.

## API

```python
render(slide, data, tokens, bounds)
```

## Data shape

```python
data = {
    "title": "Q2 program status",                       # optional
    "rows": ["Auth service", "Payment", "Analytics"],    # workstream names
    "columns": ["Schedule", "Budget", "Quality", "Risk"],# criteria/milestones
    "statuses": [                                        # row-major, values: "R", "A", "G", or None
        ["G", "G", "A", "G"],
        ["A", "R", "G", "A"],
        ["G", "G", "G", "R"],
    ],
    "show_labels": True,                                 # show R/A/G letter below indicator (default True)
}
```

Status values are case-insensitive. Unrecognized values (None, "", "N/A", "-") render as empty cells. Any other string is shown as-is in muted text.

## Layout

- Title at top (if provided), `font_display`, `text`.
- Column headers across the top, `font_body`, `muted`, bold.
- Row labels on the left, right-aligned, `font_body`, `text`.
- Cell grid fills remaining area; each cell has a `bg` background with `muted` hairline border.
- RAG indicator: colored circle (`MSO_SHAPE.OVAL`) centered in cell. Color mapping:
  - R = `primary` (the bold theme color)
  - A = `lerp(primary, accent, 0.5)` (blended midpoint)
  - G = `accent` (the positive/secondary theme color)
- Optional letter label ("R", "A", "G") below the circle in `font_mono`, `muted`.
- Legend strip at bottom with colored dots + labels.
- `radius_px` honored on cell background rectangles.

## Tokens used

`primary`, `accent`, `text`, `muted`, `bg`, `font_display`, `font_body`, `font_mono`, `font_size_base_pt`, `radius_px`.

## Proof

`python example.py` writes `example-<mode>.pptx` at the chart root, one per mode.
