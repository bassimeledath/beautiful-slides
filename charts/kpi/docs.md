# KPI tile

Big-number tile with label, value, delta, and optional footnote. One call = one tile; callers compose rows/grids themselves.

## `render(slide, data, tokens, bounds)`

### `data`

```python
{
    "label": "ARR",
    "value": "$47.2M",                       # pre-formatted hero string
    "delta": "+12.4% vs plan",               # optional
    "delta_direction": "up",                 # "up" | "down" | None
    "footnote": "Source: NetSuite, Apr 10",  # optional
}
```

### Behavior

- Tile is a rounded rect (or sharp if `radius_px == 0`) filled with `bg`, hairline border in `muted`.
- Label: `font_body`, uppercased, `muted`, ~0.78 × base.
- Value: `font_display`, `text`, sized from `bounds` height (capped at 96pt, shrunk to fit width).
- Dark modes (`sv-keynote`) get a short neon underline in `primary` under the value.
- Delta: `font_mono`. `up` → `accent` with ▲; `down` → `muted` (or `primary` where it reads as attention without clashing) with ▼.
- Footnote: `font_body`, `muted`, ~0.7 × base, anchored near the bottom of the tile.

### Constraints

- Draws entirely inside `bounds`.
- All colors/fonts come from `tokens`. No hardcoded hex or font names.
- Native python-pptx shapes only.

## Proof

`python example.py` → five `example-<mode>.pptx` files render without errors.
