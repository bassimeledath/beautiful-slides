# org-chart

Top-down tree hierarchy of people or teams connected by L-shaped connector lines.

## `render(slide, data, tokens, bounds)`

### `data`

```python
{
    "title": "Engineering Organization",      # optional
    "root": {
        "name": "Alice Chen",
        "role": "CEO",                        # optional
        "children": [
            {
                "name": "Bob Park",
                "role": "VP Engineering",
                "children": [
                    {"name": "Carol Wu", "role": "Tech Lead"},
                    {"name": "Dan Lee", "role": "Tech Lead"},
                ],
            },
            {
                "name": "Eve Rao",
                "role": "VP Product",
                "children": [
                    {"name": "Frank Li", "role": "PM"},
                ],
            },
        ],
    },
}
```

The tree is recursive: each node has `name`, optional `role`, and optional
`children` (a list of the same shape). Supports 5-20 nodes total.

### Style

- Nodes are rounded rectangles (if `radius_px > 0`) or plain rectangles,
  filled with a color that interpolates from `tokens["primary"]` (root)
  to `tokens["accent"]` (deepest leaves).
- Node text: `name` in `font_body`, bold, white (`tokens["bg"]`);
  `role` below in smaller font, slightly blended toward the fill color.
- L-shaped connectors (parent-bottom to child-top via a horizontal bar)
  use a blend of `tokens["muted"]` and `tokens["primary"]`.
- Node widths auto-scale based on the number of leaves so the tree fits
  within bounds.
- Title (optional): top-left, `font_display`, 1.5x base, bold.
- No hardcoded colors or fonts.

### Bounds

The chart fills `(x, y, w, h)` exactly: title at top, then the tree
centered horizontally in the remaining space.

## Proof

`python example.py` writes `example-<mode>.pptx` at the chart root, one per mode.
