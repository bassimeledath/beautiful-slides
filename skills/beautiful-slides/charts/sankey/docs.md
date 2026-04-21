# sankey

Weighted flow bands between stages where band width is proportional to volume. Bezier curves are approximated with freeform line segments. Supports 2-4 stages, up to 12 flows.

## `render(slide, data, tokens, bounds)`

### `data`

```python
{
    "title": "Website traffic flow",               # optional
    "stages": [
        # Stage 0 (sources)
        [
            {"label": "Organic",  "value": 5000},
            {"label": "Paid",     "value": 3000},
            {"label": "Referral", "value": 2000},
        ],
        # Stage 1 (pages)
        [
            {"label": "Homepage",  "value": 6000},
            {"label": "Pricing",   "value": 2500},
            {"label": "Blog",      "value": 1500},
        ],
        # Stage 2 (outcomes)
        [
            {"label": "Signup",    "value": 3000},
            {"label": "Bounce",    "value": 7000},
        ],
    ],
    "flows": [
        {"from": [0, 0], "to": [1, 0], "value": 3000},
        {"from": [0, 0], "to": [1, 1], "value": 1500},
        {"from": [0, 0], "to": [1, 2], "value":  500},
        # ... more flows
    ],
}
```

`stages` is a list of lists. Each inner list defines the nodes at that
stage. Each node has a `label` and `value` (total volume). `flows`
connect nodes across stages with `[stage_idx, node_idx]` references
and a `value` that determines band width.

### Style

- Node bars are filled rectangles (rounded if `radius_px > 0`).
  Height is proportional to value. Fill interpolates from
  `tokens["primary"]` to `tokens["accent"]` across nodes within
  each stage.
- Flow bands are freeform closed polygons with cubic bezier top/bottom
  edges approximated as 16-segment polylines. Fill is a blend of the
  source node color toward `tokens["bg"]` (35% blend for translucency
  effect).
- Node labels include the value in parentheses: `font_body`, bold,
  ~0.7x base, `tokens["text"]`. First-stage labels are right-aligned
  to the left of the node; last-stage labels are left-aligned to the
  right; middle-stage labels are centered above.
- Flows are stacked within nodes so band edges don't overlap.
- Title (optional): top-left, `font_display`, 1.5x base, bold.
- No hardcoded colors or fonts.

### Bounds

The chart fills `(x, y, w, h)` exactly: title at top, then stages
spaced evenly across the available width.

## Proof

`python example.py` writes `example-<mode>.pptx` at the chart root, one per mode.
