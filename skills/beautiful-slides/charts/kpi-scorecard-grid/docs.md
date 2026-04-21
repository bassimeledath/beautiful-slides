# kpi-scorecard-grid

Structured grid of 4-8 KPI tiles arranged in a 2x2, 2x3, 2x4, or 1x4 layout. Each tile shows a label, hero value, delta indicator, and optional footnote. Delegates individual tile rendering to the `kpi` chart module, so all tile styling (neon underlines, delta arrows, etc.) is inherited.

## API

```python
render(slide, data, tokens, bounds)
```

## Data shape

```python
data = {
    "title": "Q1 2025 Scorecard",               # optional
    "layout": "auto",                             # "auto" | "1x4" | "2x2" | "2x3" | "2x4"
    "tiles": [
        {
            "label": "ARR",
            "value": "$47.2M",
            "delta": "+12.4% vs plan",
            "delta_direction": "up",              # "up" | "down" | None
            "footnote": "Source: NetSuite",       # optional
        },
        # ... 4-8 tiles
    ],
}
```

## Layout

- Title at top (if provided), `font_display`, `text`, bold, ~1.25x base size.
- Grid fills remaining `bounds` area below title.
- `layout` controls tile arrangement:
  - `"auto"`: picks best fit for tile count (4->2x2, 5-6->2x3, 7-8->2x4, 3->1x3, etc.)
  - `"RxC"`: explicit rows x cols (e.g. `"2x3"`).
- Gutter between tiles: 2.5% width horizontal, 4% height vertical.
- Each tile is rendered by the `kpi` chart (rounded rect, label, hero value, delta, footnote).

## Tokens used

`primary`, `accent`, `text`, `muted`, `bg`, `font_display`, `font_body`, `font_mono`, `font_size_base_pt`, `radius_px`.

## Proof

`python example.py` writes `example-<mode>.pptx` at the chart root, one per mode.
