# layered-architecture

Horizontal layers stacked top-to-bottom representing an architecture (client, services, data, infra). Each layer is a full-width rounded rectangle with a label and optional inline component boxes.

## `render(slide, data, tokens, bounds)`

### `data`

```python
{
    "title": "Platform architecture",           # optional
    "layers": [
        {
            "label": "Client",
            "items": ["Web app", "Mobile app", "CLI"],
        },
        {
            "label": "API gateway",
            "items": ["Auth", "Rate limiting", "Routing"],
        },
        {
            "label": "Services",
            "items": ["Users", "Orders", "Payments", "Notifications"],
        },
        {
            "label": "Data",
            "items": ["PostgreSQL", "Redis", "S3"],
        },
        {
            "label": "Infrastructure",
            "items": ["Kubernetes", "Terraform", "Monitoring"],
        },
    ],
}
```

Each layer has a `label` string and an optional `items` list of component names displayed as inline boxes within that layer.

### Style

- Layers stack vertically, first layer at the top, last at the bottom.
- Each layer is a full-width rectangle (rounded if `radius_px > 0`) with a
  subtle tinted background derived from that layer's color.
- Layer colors interpolate from `tokens["primary"]` (top) to
  `tokens["accent"]` (bottom).
- A thin colored stripe on the left edge of each layer reinforces the color.
- Layer labels: left-aligned, `font_display`, bold, base size, `tokens["text"]`.
- Items render as inline component boxes to the right of the label: `font_body`,
  ~0.75x base size, `tokens["text"]` text, `tokens["bg"]` fill, thin
  `tokens["muted"]` outline.
- Title (optional): top-left, `font_display`, 1.5x base, bold.
- No hardcoded colors or fonts.

### Bounds

The chart fills `(x, y, w, h)` exactly: title at top, then the layers
with even vertical distribution in the remaining space.

## Proof

`python example.py` writes `example-<mode>.pptx` at the chart root, one per mode.
