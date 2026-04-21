# flowchart

Boxes and arrows for linear or branching process logic. Supports process
(rectangle), decision (diamond), and terminal/start-end (rounded rectangle)
node types. Auto-layout top-to-bottom or left-to-right.

## `render(slide, data, tokens, bounds)`

### `data`

```python
{
    "title": "User signup flow",                    # optional
    "direction": "TB",                              # "TB" (default) or "LR"
    "nodes": [
        {"id": "start", "label": "Start",           "type": "terminal"},
        {"id": "input", "label": "Enter details",   "type": "process"},
        {"id": "valid", "label": "Valid?",           "type": "decision"},
        {"id": "save",  "label": "Save to DB",      "type": "process"},
        {"id": "error", "label": "Show error",       "type": "process"},
        {"id": "end",   "label": "Done",             "type": "terminal"},
    ],
    "edges": [
        {"from": "start", "to": "input"},
        {"from": "input", "to": "valid"},
        {"from": "valid", "to": "save",  "label": "Yes"},
        {"from": "valid", "to": "error", "label": "No"},
        {"from": "save",  "to": "end"},
    ],
}
```

### Node types

| type       | shape             | fill                                          |
|------------|-------------------|-----------------------------------------------|
| `terminal` | rounded rectangle | solid primary-to-accent gradient, text in bg  |
| `process`  | rectangle         | subtle tint of bg toward primary, text color  |
| `decision` | diamond           | accent-to-primary gradient, text in bg        |

### Edges

Edges are directional arrows drawn from the source node edge to the
destination node edge. Optional `label` strings appear near the midpoint
of each arrow.

### Layout

Nodes are placed on a grid. Linear chains stay in one column. When a
decision node has multiple outgoing edges, children fan out into adjacent
columns.

- `"TB"` — rows flow top to bottom; branching spreads left/right.
- `"LR"` — rows flow left to right; branching spreads up/down.

### Style

- Arrow color: blend of `tokens["muted"]` and `tokens["primary"]`.
- Node fill colors interpolate from `tokens["primary"]` to `tokens["accent"]`.
- Process node borders use a blend of `tokens["primary"]` and `tokens["muted"]`.
- All text uses `tokens["font_body"]` at `tokens["font_size_base_pt"]`.
- Title (optional): top-left, `font_display`, 1.5x base, bold.
- No hardcoded colors or fonts.

### Bounds

The chart fills `(x, y, w, h)` exactly: title at top, then the flowchart
grid centred in the remaining space.

## Proof

`python example.py` writes `example-<mode>.pptx` at the chart root, one per mode.
