# heatmap

Grid of colored cells filling `bounds`. Each cell's fill is linearly interpolated between `tokens["bg"]` and `tokens["primary"]` by the normalized value — so every mode produces its own gradient family (black→cyan, cream→wine, peach→orange, white→navy, off-white→sage).

## API

```python
render(slide, data, tokens, bounds)
```

## Data shape

```python
data = {
    "title": "Usage intensity by hour and weekday",   # optional
    "row_labels": ["Mon", "Tue", ...],
    "col_labels": ["00", "02", ...],
    "values": [[0.1, 0.1, ...], ...],                 # row-major
    "value_min": 0.0,                                  # optional, auto from values
    "value_max": 1.0,                                  # optional, auto from values
    "show_values": False,                              # print formatted value in each cell
    "value_format": "{:.0%}",                          # python format string
}
```

## Layout

- Title at top (if provided), `font_display`, `text`.
- Column labels across the top row, `font_body`, `muted`, ~0.75× base size.
- Row labels on the left, right-aligned, `font_body`, `muted`.
- Cell grid fills remaining area; hairline gap + hairline `muted` outline at 0.25pt.
- Cell fill: `lerp(bg, primary, normalized_value)`. Normalized value clamped to [0, 1].
- `radius_px` honored via `MSO_SHAPE.ROUNDED_RECTANGLE`.
- If `show_values`: formatted value centered in each cell, `font_mono`, auto-chosen color (light vs dark) based on cell luminance relative to `bg`.
- Legend strip bottom-right: 24-step gradient + min/max labels in `font_mono`/`muted`.

## Tokens used

`primary`, `text`, `muted`, `bg`, `font_display`, `font_body`, `font_mono`, `font_size_base_pt`, `radius_px`.

## Proof

`python example.py` writes `example-<mode>.pptx` at the chart root, one per mode. Passed.
