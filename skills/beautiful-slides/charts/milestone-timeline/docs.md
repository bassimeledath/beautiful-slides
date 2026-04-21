# milestone-timeline

Horizontal sequence of dated milestones connected by a track line, with alternating above/below placement.

## `render(slide, data, tokens, bounds)`

### `data`

```python
{
    "title": "Product launch roadmap",       # optional
    "milestones": [
        {"date": "Jan 2025", "label": "Kickoff"},
        {"date": "Mar 2025", "label": "Alpha release"},
        {"date": "Jun 2025", "label": "Beta launch"},
        {"date": "Sep 2025", "label": "GA release"},
        {"date": "Dec 2025", "label": "V2 planning"},
    ],
}
```

Supports 3-7 milestones. Each milestone has a `date` string and a `label` string.

### Style

- A horizontal track line spans the chart width, drawn as a thin rectangle
  using `tokens["muted"]`.
- Circular nodes sit on the track at evenly spaced intervals. Fill color
  interpolates from `tokens["primary"]` to `tokens["accent"]` across
  the sequence.
- Thin vertical connectors extend from each node up or down (alternating)
  to the label area.
- Date labels: `font_body`, `tokens["muted"]`, smaller size (~0.78x base).
- Event labels: `font_body`, `tokens["text"]`, bold, base size.
- Title (optional): top-left, `font_display`, 1.5x base, bold.
- No outlines on shapes. No hardcoded colors or fonts.

### Bounds

The chart fills `(x, y, w, h)` exactly: title at top, then the track
line centred vertically with labels alternating above and below.

## Proof

`python example.py` writes `example-<mode>.pptx` at the chart root, one per mode.
