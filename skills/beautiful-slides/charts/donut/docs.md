# Donut chart

Ring chart with proportional arc segments and a hero number/label in the center. Best for showing composition of a whole (1-3 segments). Each segment is drawn as a freeform arc wedge using native python-pptx shapes.

## `render(slide, data, tokens, bounds)`

### `data`

```python
{
    "title": "Revenue Mix",                    # optional
    "segments": [
        {"label": "Subscription", "value": 72},
        {"label": "Services", "value": 18},
        {"label": "Other", "value": 10},
    ],
    "center_value": "72%",                     # hero number in the ring center
    "center_label": "Subscription",            # subtitle below the hero number
}
```

### Behavior

- Up to 3 segments. Additional segments are silently dropped.
- Segments are drawn as freeform arc wedges (outer arc, inner arc, closed). No rasterization.
- Segment colors cycle through `primary`, `accent`, `muted`.
- A small angular gap separates segments for visual clarity.
- The center of the ring displays `center_value` (large, bold, `font_display`) and `center_label` (smaller, `font_body`, `muted`).
- Legend below the donut shows colored swatches, labels, and computed percentages.
- Optional `title` renders above the chart in `font_display`, bold.

### Constraints

- Draws entirely inside `bounds`.
- All colors/fonts come from `tokens`. No hardcoded hex or font names.
- Native python-pptx shapes only.

## Proof

`python example.py` generates five `example-<mode>.pptx` files without errors.
