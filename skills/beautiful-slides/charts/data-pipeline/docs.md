# data-pipeline

Directed left-to-right pipeline diagram showing data flow through stages. Each stage is a column with a header and vertically stacked node boxes. Arrows connect stages.

## `render(slide, data, tokens, bounds)`

### `data`

```python
{
    "title": "Real-time analytics pipeline",     # optional
    "stages": [
        {
            "label": "Sources",
            "nodes": ["Clickstream", "App events", "Server logs"],
        },
        {
            "label": "Ingestion",
            "nodes": ["Kafka", "Kinesis"],
        },
        {
            "label": "Transform",
            "nodes": ["Flink", "dbt", "Spark"],
        },
        {
            "label": "Storage",
            "nodes": ["Snowflake", "S3", "Redis"],
        },
        {
            "label": "Serve",
            "nodes": ["API", "Dashboard", "Alerts"],
        },
    ],
}
```

Each stage has a `label` string and a `nodes` list of component names.

### Style

- Stages are arranged as columns left-to-right, evenly distributed.
- Each stage has a colored header bar and a tinted background column.
  Header fill color interpolates from `tokens["primary"]` (leftmost) to
  `tokens["accent"]` (rightmost). Header text uses `tokens["bg"]` for
  contrast.
- Nodes render as stacked boxes within each column: `font_body`,
  ~0.8x base size, `tokens["text"]` text, `tokens["bg"]` fill, thin
  `tokens["muted"]` outline.
- Directional arrows (freeform shaft + triangle head) connect consecutive
  stages horizontally. Arrow color is a blend of `tokens["muted"]` and
  `tokens["primary"]`.
- Title (optional): top-left, `font_display`, 1.5x base, bold.
- No hardcoded colors or fonts.

### Bounds

The chart fills `(x, y, w, h)` exactly: title at top, then the pipeline
columns with arrows in the gaps between them.

## Proof

`python example.py` writes `example-<mode>.pptx` at the chart root, one per mode.
