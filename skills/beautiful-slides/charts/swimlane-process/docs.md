# swimlane-process

Flowchart split into horizontal lanes by team, system, or owner. Steps flow left-to-right within lanes, arrows cross lanes for handoffs. Lane labels on the left.

## `render(slide, data, tokens, bounds)`

### `data`

```python
{
    "title": "Order fulfilment flow",              # optional
    "lanes": [
        {
            "label": "Customer",
            "steps": [
                {"label": "Place order"},
                {"label": "Receive confirmation"},
            ],
        },
        {
            "label": "Sales",
            "steps": [
                {"label": "Validate order"},
                {"label": "Process payment"},
            ],
        },
        {
            "label": "Warehouse",
            "steps": [
                {"label": "Pick & pack"},
                {"label": "Ship"},
            ],
        },
    ],
    "connections": [
        {"from": [0, 0], "to": [1, 0]},   # Customer -> Sales
        {"from": [1, 0], "to": [1, 1]},   # within Sales
        {"from": [1, 1], "to": [0, 1]},   # Sales -> Customer
        {"from": [1, 1], "to": [2, 0]},   # Sales -> Warehouse
        {"from": [2, 0], "to": [2, 1]},   # within Warehouse
    ],
}
```

Each lane has a `label` and a list of `steps`. Each step has a `label`. Connections reference `[lane_index, step_index]` for source and target.

### Style

- Lanes are horizontal rows with alternating subtle background tints
  (blends of `tokens["bg"]` and `tokens["muted"]`).
- Lane labels appear on the left column, `font_display`, bold,
  ~0.9x base size, `tokens["text"]`.
- Steps are filled rectangles (rounded if `radius_px > 0`).
  Fill color interpolates from `tokens["primary"]` to `tokens["accent"]`
  across lanes. Step labels: `font_body`, bold, ~0.75x base,
  `tokens["bg"]` (inverted for contrast).
- Connections are freeform arrows (shaft + triangle head) in a blend
  of `tokens["muted"]` and `tokens["text"]`.
- Horizontal connections go right-edge to left-edge. Cross-lane
  connections go bottom/top edge to top/bottom edge.
- Lane divider lines: subtle blend toward `tokens["muted"]`.
- Title (optional): top-left, `font_display`, 1.5x base, bold.
- No hardcoded colors or fonts.

### Bounds

The chart fills `(x, y, w, h)` exactly: title at top, then lanes
stacked vertically with a label column on the left.

## Proof

`python example.py` writes `example-<mode>.pptx` at the chart root, one per mode.
