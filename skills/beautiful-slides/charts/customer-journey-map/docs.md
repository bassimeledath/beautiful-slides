# customer-journey-map

Stage-by-stage customer journey with touchpoints, actions, feelings, pain points, and opportunities. Horizontal stages across the top, aspect rows below, and a sentiment curve connecting dots.

## `render(slide, data, tokens, bounds)`

### `data`

```python
{
    "title": "SaaS onboarding journey",          # optional
    "stages": [
        {
            "label": "Awareness",
            "actions": "Sees ad, reads blog post",
            "touchpoints": "Social media, blog",
            "feelings": "Curious but skeptical",
            "sentiment": 3,                        # 1-5 scale
            "pain_points": "Too many options",
            "opportunities": "Targeted content",
        },
        # ... more stages
    ],
    "rows": ["Actions", "Touchpoints", "Feelings",
             "Pain points", "Opportunities"],      # optional override
}
```

Each stage has a `label` and content strings for each aspect row.
`sentiment` is an integer 1-5 (1 = very negative, 5 = very positive).

### Style

- Stage headers are colored pills/rectangles spanning the top.
  Fill color interpolates from `tokens["primary"]` to `tokens["accent"]`.
  Labels: `font_display`, bold, ~0.85x base, `tokens["bg"]`.
- Sentiment row sits between header and body. A horizontal track line
  connects dots that are vertically positioned by sentiment value.
  Positive dots use `tokens["accent"]`, negative use `tokens["primary"]`,
  neutral use `tokens["muted"]`. Connecting lines are thin freeform quads.
- Body grid: row labels on the left column in `font_body`, bold, muted.
  Cell content in `font_body`, ~0.65x base, `tokens["text"]`.
- Vertical gridlines separate stage columns: subtle blend toward
  `tokens["muted"]`.
- Title (optional): top-left, `font_display`, 1.5x base, bold.
- No hardcoded colors or fonts.

### Bounds

The chart fills `(x, y, w, h)` exactly: title at top, then the header
row, sentiment row, and body grid.

## Proof

`python example.py` writes `example-<mode>.pptx` at the chart root, one per mode.
