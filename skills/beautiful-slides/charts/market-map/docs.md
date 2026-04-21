# market-map chart

Native python-pptx market map. Labeled boxes arranged by segment/category in a column grid layout. Ideal for vendor landscapes, partner ecosystems, competitive analysis, and whitespace identification.

## When to use

- Vendor landscape or competitive overview (group players by segment).
- Partner ecosystem mapping (categorize by type, tier, or capability).
- Whitespace analysis showing coverage across market categories.
- Technology stack visualization (categories = layers, items = tools/platforms).

## When not to use

- Precise quantitative comparison -> use a bar or bubble chart.
- Hierarchical relationships -> use a treemap or org chart.
- Only 1-2 items -> overkill; use a simple text slide.

## Data shape

```python
data = {
    "title": "Competitive landscape",                      # optional
    "subtitle": "Enterprise SaaS market Q4 2024",          # optional
    "categories": [
        {
            "name": "CRM",                                 # column header
            "color": "#0F4C81",                            # optional; overrides theme
            "items": [
                "Salesforce",                              # simple string
                "HubSpot",
                {"label": "Zoho", "color": "#FF7A00"},     # or dict with optional color
            ],
        },
        {
            "name": "Analytics",
            "items": ["Tableau", "Looker", "Power BI"],
        },
        {
            "name": "DevOps",
            "items": ["GitHub", "GitLab", "Jira"],
        },
    ],
}
```

- Each category becomes a labeled column with stacked item boxes.
- Items can be plain strings or dicts with `label` and optional `color`.
- Categories auto-size to fill the available width evenly.
- Items that would overflow the slide bounds are silently truncated.

## Example

```python
from pptx import Presentation
from pptx.util import Inches
from charts.market_map.render import render

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
    "title": "Competitive landscape",
    "categories": [
        {"name": "CRM", "items": ["Salesforce", "HubSpot", "Zoho"]},
        {"name": "Analytics", "items": ["Tableau", "Looker", "Power BI"]},
        {"name": "DevOps", "items": ["GitHub", "GitLab", "Jira"]},
    ],
}
m = Inches(0.5)
bounds = (m, m, prs.slide_width - 2 * m, prs.slide_height - 2 * m)
render(slide, data, tokens, bounds)
prs.save("market_map_example.pptx")
```
