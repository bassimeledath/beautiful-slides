# capability-map

Tiled/grouped view of business capabilities organized by domain.

## `render(slide, data, tokens, bounds)`

### `data`

```python
{
    "title": "Platform Capability Map",          # optional
    "domains": [
        {
            "name": "Customer",
            "capabilities": [
                "Onboarding",
                "Support",
                "Feedback",
                "Loyalty",
            ],
        },
        {
            "name": "Product",
            "capabilities": [
                "Catalog",
                "Search",
                "Recommendations",
            ],
        },
        # ...
    ],
}
```

Each domain becomes a column. Domain headers sit across the top; capability
tiles are stacked below in each column.

### Style

- Domain headers are filled rectangles (rounded if `radius_px > 0`),
  colored on a gradient from `tokens["primary"]` to `tokens["accent"]`
  across the columns. Header text: `font_display`, bold, `tokens["bg"]`.
- Capability tiles have a subtle background tint (12% blend of the
  domain color into `tokens["bg"]`) and a thin border (35% blend).
  Tile text: `font_body`, `tokens["text"]`, centered.
- Columns are equal width with proportional gaps.
- Tile height auto-scales to fit the domain with the most capabilities.
- Title (optional): top-left, `font_display`, 1.5x base, bold.
- No hardcoded colors or fonts.

### Bounds

The chart fills `(x, y, w, h)` exactly: title at top, then the column
grid in the remaining space.

## Proof

`python example.py` writes `example-<mode>.pptx` at the chart root, one per mode.
