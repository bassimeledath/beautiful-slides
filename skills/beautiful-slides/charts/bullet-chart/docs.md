# bullet chart

Native python-pptx bullet chart (Stephen Few's gauge replacement). A thin horizontal performance bar plotted against a target marker and qualitative range bands (poor / satisfactory / good). Stacks 3-6 metrics vertically for a compact dashboard view.

## When to use

- Showing actual vs. target for KPIs where qualitative context (poor/ok/good ranges) matters.
- Compact dashboard: 3-6 metrics at a glance without wasting space on pie/gauge charts.
- Performance scorecards, SLA dashboards, quarterly goal tracking.

## When not to use

- Single hero number with no reference ranges -- use a KPI tile.
- Trend over time -- use a line chart.
- Category comparison across many items -- use a bar chart.

## Data shape

```python
data = {
    "title": "Q1 performance scorecard",   # optional; may be None
    "metrics": [
        {
            "label": "Revenue",
            "actual": 82,
            "target": 90,
            "ranges": [100, 75, 50],   # [good, satisfactory, poor] thresholds
            "suffix": "M",             # optional
        },
        {
            "label": "Profit margin",
            "actual": 22,
            "target": 25,
            "ranges": [30, 20, 10],
            "suffix": "%",
        },
        {
            "label": "NPS",
            "actual": 65,
            "target": 70,
            "ranges": [80, 60, 40],
            "suffix": "",
        },
    ],
    "show_values": True,   # optional; default True
}
```

- 3-6 metrics. Each has `label`, `actual`, `target`, and `ranges`.
- `ranges` is a list of 3 numeric thresholds defining the qualitative bands. The largest value determines the scale.
- Performance bar uses `tokens["primary"]`; target marker uses `tokens["accent"]`.
- Qualitative bands are progressively shaded from `tokens["bg"]` toward `tokens["muted"]`.

## Example

```python
from pptx import Presentation
from pptx.util import Inches
from charts.bullet_chart.render import render

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
slide = prs.slides.add_slide(prs.slide_layouts[6])

tokens = {
    "primary": "#0F4C81", "accent": "#05603A", "text": "#101828",
    "muted": "#475467", "bg": "#FFFFFF",
    "font_display": "Public Sans", "font_body": "Public Sans",
    "font_mono": "Public Sans", "font_size_base_pt": 14, "radius_px": 0,
}
data = {
    "title": "Q1 performance scorecard",
    "metrics": [
        {"label": "Revenue",       "actual": 82,  "target": 90, "ranges": [100, 75, 50], "suffix": "M"},
        {"label": "Profit margin", "actual": 22,  "target": 25, "ranges": [30, 20, 10],  "suffix": "%"},
        {"label": "NPS",           "actual": 65,  "target": 70, "ranges": [80, 60, 40],  "suffix": ""},
    ],
    "show_values": True,
}
m = Inches(0.5)
bounds = (m, m, prs.slide_width - 2 * m, prs.slide_height - 2 * m)
render(slide, data, tokens, bounds)
prs.save("example.pptx")
```
