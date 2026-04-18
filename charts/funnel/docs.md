# funnel

Vertical conversion funnel drawn with native freeform trapezoids.

## `render(slide, data, tokens, bounds)`

### `data`

```python
{
    "title": "Enterprise pipeline, Q1",    # optional
    "stages": [
        {"label": "Leads",      "value": 10000},
        {"label": "Qualified",  "value":  4200},
        # ...
    ],
    "show_conversion": True,    # show % between stages
    "value_format": "{:,}",     # format string for values
}
```

Stages render top-down, widest to narrowest. Widths are proportional to
each stage's value, normalized so the widest stage = ~98% of the inner
funnel column and the narrowest last stage >= ~18% of that.

### Style

- Each trapezoid is a 4-point freeform (TL, TR, BR, BL) so the bottom
  width of stage *i* matches the top width of stage *i+1* — the funnel
  is continuous.
- Fill color interpolates linearly in sRGB from `tokens["primary"]` at
  the top to `tokens["muted"]` at the bottom.
- Stage labels: left column, `font_body`, `tokens["text"]`, right-aligned.
- Stage values: right column, `font_mono`, `tokens["text"]`, bold,
  left-aligned, formatted via `value_format`.
- Conversion %: between trapezoids, `font_mono`, `tokens["muted"]`,
  small (~0.75× base).
- Title (optional): top-left, `font_display`, 1.5× base, bold.
- No outlines on trapezoids. No hardcoded colors or fonts.

### Bounds

The chart fills `(x, y, w, h)` exactly: title at top, then the funnel
with its left/right label gutters.

## Proof

`python example.py` renders one pptx per mode into `renders/`.
