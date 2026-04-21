# decision-tree

Branching path of choices and outcomes. Each node has a question or label.
Branches have option labels. Tree expands left-to-right or top-to-bottom
from a single root question.

## `render(slide, data, tokens, bounds)`

### `data`

```python
{
    "title": "Pricing strategy",                        # optional
    "direction": "LR",                                  # "LR" (default) or "TB"
    "root": {
        "id": "q1",
        "label": "Enterprise customer?",
        "children": [
            {
                "label": "Yes",
                "node": {
                    "id": "q2",
                    "label": "Annual contract?",
                    "children": [
                        {"label": "Yes", "node": {"id": "a1", "label": "Enterprise Annual"}},
                        {"label": "No",  "node": {"id": "a2", "label": "Enterprise Monthly"}},
                    ],
                },
            },
            {
                "label": "No",
                "node": {
                    "id": "q3",
                    "label": "Team size > 10?",
                    "children": [
                        {"label": "Yes", "node": {"id": "a3", "label": "Business plan"}},
                        {"label": "No",  "node": {"id": "a4", "label": "Starter plan"}},
                    ],
                },
            },
        ],
    },
}
```

### Tree structure

The tree is nested: each node has an `id`, a `label`, and an optional
`children` list. Each child entry has a `label` (the branch/edge label)
and a `node` (the child node, same structure).

### Node styles

| position   | shape             | fill                            |
|------------|-------------------|---------------------------------|
| root       | rounded rectangle | solid `primary`, text in `bg`   |
| interior   | rectangle         | subtle tint of `bg`, text color |
| leaf       | rounded rectangle | `accent`-tinted, text in `bg`   |

### Layout

Nodes are laid out recursively. Leaf count determines how much vertical
(LR mode) or horizontal (TB mode) space each subtree occupies.

- `"LR"` — depth flows left to right; subtrees spread vertically.
- `"TB"` — depth flows top to bottom; subtrees spread horizontally.

### Style

- Arrow color: blend of `tokens["muted"]` and `tokens["primary"]`.
- Branch labels appear near the midpoint of each arrow.
- All text uses `tokens["font_body"]` at `tokens["font_size_base_pt"]`.
- Title (optional): top-left, `font_display`, 1.5x base, bold.
- No hardcoded colors or fonts.

### Bounds

The chart fills `(x, y, w, h)` exactly: title at top, then the tree
in the remaining space.

## Proof

`python example.py` writes `example-<mode>.pptx` at the chart root, one per mode.
