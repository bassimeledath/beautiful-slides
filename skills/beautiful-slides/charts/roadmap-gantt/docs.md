# roadmap-gantt

Time-scaled horizontal bars showing workstreams with optional milestone diamonds and a "today" marker.

## `render(slide, data, tokens, bounds)`

### `data`

```python
{
    "title": "2025 Engineering roadmap",         # optional
    "time_units": ["Q1", "Q2", "Q3", "Q4"],     # column headers
    "rows": [
        {"label": "Platform",   "start": 0, "end": 3, "milestones": [1.5]},
        {"label": "Mobile app", "start": 1, "end": 4},
        {"label": "API v2",     "start": 0, "end": 2, "milestones": [2]},
        {"label": "Analytics",  "start": 2, "end": 4},
    ],
    "today": 1.3,    # optional, fractional index into time_units
}
```

- `time_units`: list of strings labeling the time columns.
- `rows`: 4-12 rows. `start`/`end` are 0-based indices into `time_units`
  (fractional values OK). `milestones` is an optional list of indices
  where diamond markers are placed.
- `today`: optional fractional index for a vertical marker line.

### Style

- Header row shows time unit labels: `font_body`, `tokens["muted"]`, bold.
- Light vertical gridlines between columns using `tokens["muted"]`.
- Alternating row stripes (subtle tint of `tokens["bg"]` toward `tokens["muted"]`).
- Bars: fill color interpolates from `tokens["primary"]` to `tokens["accent"]`
  top-to-bottom across rows. Rounded rectangles when `radius_px > 0`.
- Row labels: left column, `font_body`, `tokens["text"]`, right-aligned.
- Milestone diamonds: `tokens["text"]` fill, no outline.
- Today marker: vertical line in `tokens["accent"]` with "Today" label above.
- Title (optional): top-left, `font_display`, 1.5x base, bold.
- No hardcoded colors or fonts.

### Bounds

The chart fills `(x, y, w, h)` exactly: title at top, time axis header,
then the bar rows filling the remaining height.

## Proof

`python example.py` writes `example-<mode>.pptx` at the chart root, one per mode.
