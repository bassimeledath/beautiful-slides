# flywheel

Circular arrangement of 3-6 steps with directional arrows forming a reinforcing loop.

## `render(slide, data, tokens, bounds)`

### `data`

```python
{
    "title": "Growth flywheel",                 # optional
    "center": "Growth",                         # optional center label
    "steps": [
        {"label": "Acquire users"},
        {"label": "Deliver value"},
        {"label": "Retain & engage"},
        {"label": "Generate referrals"},
        {"label": "Lower CAC"},
    ],
}
```

Supports 3-6 steps. Each step has a `label` string.

### Style

- Steps are arranged in a circle, starting at the top and going clockwise.
- Each step is a filled circle (node) with a step number inside.
  Fill color interpolates from `tokens["primary"]` to `tokens["accent"]`.
- Directional arrows (freeform shaft + triangle head) connect consecutive
  nodes, forming a closed loop. Arrow color is a blend of `tokens["muted"]`
  and `tokens["primary"]`.
- Step labels sit radially outside their nodes: `font_body`, `tokens["text"]`,
  bold, base size.
- A decorative center ring uses a subtle tint of `tokens["bg"]` toward
  `tokens["primary"]`, with a thin `tokens["muted"]` outline.
- Optional center text: `font_display`, bold, ~0.85x base size.
- Title (optional): top-left, `font_display`, 1.5x base, bold.
- No hardcoded colors or fonts.

### Bounds

The chart fills `(x, y, w, h)` exactly: title at top, then the flywheel
circle centred in the remaining space.

## Proof

`python example.py` writes `example-<mode>.pptx` at the chart root, one per mode.
