# issue-tree

MECE branching decomposition in consulting style. Root question on the left,
branches fan out to the right with sub-branches. Each level decomposes the
parent into mutually exclusive, collectively exhaustive components.

## `render(slide, data, tokens, bounds)`

### `data`

```python
{
    "title": "Why is revenue declining?",              # optional
    "root": {
        "label": "Revenue decline",
        "children": [
            {
                "label": "Volume down",
                "children": [
                    {"label": "Fewer new customers"},
                    {"label": "Higher churn rate"},
                ],
            },
            {
                "label": "Price down",
                "children": [
                    {"label": "Discount pressure"},
                    {"label": "Mix shift to low-tier"},
                ],
            },
            {
                "label": "Product issues",
                "children": [
                    {"label": "Feature gaps"},
                    {"label": "Quality/bugs"},
                ],
            },
        ],
    },
}
```

### Tree structure

The tree is nested: each node has a `label` and an optional `children`
list (same structure). Typically 2-4 levels deep with 2-4 children per
node. No `id` field required (unlike decision-tree).

### Node styles

| position   | shape             | fill                                |
|------------|-------------------|-------------------------------------|
| root       | rounded rectangle | solid `primary`, text in `bg`       |
| interior   | rectangle         | subtle tint of `bg`, bordered       |
| leaf       | rectangle         | subtle tint of `bg`, thin border    |

Borders use depth-interpolated colors from `primary` to `accent`.

### Layout

Left-to-right only. Each column represents a depth level. Columns are
connected by bracket-style vertical bars with horizontal connector lines.
The root column is slightly wider; children columns share remaining space
equally.

### Style

- Connector lines and brackets: blend of `tokens["muted"]` and `tokens["primary"]`.
- Node fill colors become subtler at deeper levels.
- Root node text uses `bg` color on `primary` fill, bold.
- Interior/leaf text uses `text` color, `font_body`.
- Title (optional): top-left, `font_display`, 1.5x base, bold.
- No hardcoded colors or fonts.

### Bounds

The chart fills `(x, y, w, h)` exactly: title at top, then the tree
in the remaining space, expanding left-to-right.

## Proof

`python example.py` writes `example-<mode>.pptx` at the chart root, one per mode.
