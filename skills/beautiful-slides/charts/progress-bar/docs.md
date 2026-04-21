# Progress bar

Horizontal completion meters stacked vertically, forming a goal dashboard. Each bar shows a label, current value, target, and a vertical target marker line.

## `render(slide, data, tokens, bounds)`

### `data`

```python
{
    "title": "Q2 Goal Progress",             # optional
    "bars": [
        {"label": "Revenue", "value": 8.4, "target": 10.0, "format": "${:,.1f}M"},
        {"label": "New Logos", "value": 34, "target": 40},
        {"label": "NPS", "value": 68, "target": 70},
        {"label": "Retention", "value": 94, "target": 95, "format": "{:.0f}%"},
    ],
}
```

### Behavior

- Up to 6 bars rendered. Additional bars are silently dropped.
- Each bar block: label + value/target text on top, track + fill + target marker below.
- Track is a full-width bar in a subtle tint of `bg`.
- Fill portion uses `primary` / `accent` alternating.
- Target marker is a vertical line in `text` color that overshoots the bar slightly.
- Label row: label (`font_body`, bold, left-aligned), value/target (`font_mono`, muted, right-aligned).
- Bars auto-scale to fit available height; spacing adjusts if needed.
- Bar shapes use `radius_px` for rounding.
- Optional `title` renders above bars in `font_display`, bold.

### Constraints

- Draws entirely inside `bounds`.
- All colors/fonts come from `tokens`. No hardcoded hex or font names.
- Native python-pptx shapes only.

## Proof

`python example.py` generates five `example-<mode>.pptx` files without errors.
