# value-chain

Porter-style value chain with chevron arrows flowing left-to-right for
primary activities, horizontal support bars below, and a vertical margin
bar on the far right.

## `render(slide, data, tokens, bounds)`

### `data`

```python
{
    "title": "Retail Value Chain",              # optional
    "primary": [                                # list of str
        "Inbound\nLogistics",
        "Operations",
        "Outbound\nLogistics",
        "Marketing\n& Sales",
        "Service",
    ],
    "support": [                                # optional list of str
        "Firm Infrastructure",
        "Human Resource Management",
        "Technology Development",
        "Procurement",
    ],
    "margin_label": "Margin",                   # optional, default "Margin"
}
```

Also accepts legacy format where `primary_activities` / `support_activities`
are lists of `{"label": str}`.

### Style

- Primary activities are freeform chevron shapes (pentagon with arrow
  point on the right). The first chevron has a flat left edge; subsequent
  ones have a V-notch. Fill color interpolates from `tokens["primary"]` to
  `tokens["accent"]`, desaturated 25% toward `tokens["bg"]`. Labels use
  luminance-based contrast color, `font_body`, bold.
- A "Margin" bar on the right spans the full height of both sections,
  filled with `tokens["accent"]` blended 40% toward `tokens["bg"]`.
  Text: `font_body`, bold.
- Support activities are full-width horizontal bars below the chevrons
  with subtle fill (`tokens["primary"]` blended 85% toward `tokens["bg"]`).
  Labels: `font_body`, `tokens["text"]`, left-aligned.
- Section labels ("Primary Activities" / "Support Activities"): `font_body`,
  `tokens["muted"]`, bold, small.
- Title (optional): top-left, `font_display`, 1.5x base, bold.
- No hardcoded colors or fonts.

### Bounds

The chart fills `(x, y, w, h)` exactly: title at top, then the chevron
chain (~45% height), gap, and support bars (~40% height) plus the margin
column on the right (6% width, with 1% right padding).

## Proof

`python example.py` writes `example-<mode>.pptx` at the chart root, one per mode.
