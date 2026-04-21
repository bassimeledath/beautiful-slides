# venn chart

Native python-pptx Venn diagram. 2-3 overlapping circles with semi-transparent fills showing set relationships. Labels in each region (A-only, B-only, intersections, etc).

## When to use

- Showing overlap between 2-3 categories, teams, skill sets, or market segments.
- Visualizing shared vs. unique attributes between groups.
- Concept slides showing where ideas, strategies, or capabilities converge.

## When not to use

- More than 3 sets -> Venn diagrams become unreadable.
- Precise proportional area encoding -> Venn circles are schematic, not proportional.
- Hierarchical containment -> use nested rectangles or a treemap instead.

## Data shape

```python
data = {
    "title": "Engineering skill overlap",                  # optional
    "transparency": 65,                                    # 0-100; default 65
    "sets": [
        {
            "label": "Frontend",
            "color": "#21D4FD",                            # optional; overrides primary
            "items": ["React", "CSS", "A11y"],             # optional; shown in exclusive zone
        },
        {
            "label": "Backend",
            "color": "#17B26A",                            # optional; overrides accent
            "items": ["Go", "SQL", "K8s"],
        },
        {                                                  # optional 3rd set
            "label": "Data",
            "items": ["Python", "Spark"],
        },
    ],
    "intersections": {                                     # optional
        "ab": "REST APIs",                                 # Frontend & Backend
        "ac": "Dashboards",                                # Frontend & Data
        "bc": "Pipelines",                                 # Backend & Data
        "abc": "Full stack",                               # all three
    },
}
```

- Maximum 3 sets.
- `items` in each set are displayed in the exclusive (non-overlapping) region; max ~3-4 items.
- `intersections` keys: `ab`, `ac`, `bc`, `abc` (case-insensitive).
- Each set may include an optional `color` hex string.

## Example

```python
from pptx import Presentation
from pptx.util import Inches
from charts.venn.render import render

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
    "title": "Engineering skill overlap",
    "sets": [
        {"label": "Frontend", "items": ["React", "CSS"]},
        {"label": "Backend", "items": ["Go", "SQL"]},
    ],
    "intersections": {"ab": "REST APIs"},
}
m = Inches(0.5)
bounds = (m, m, prs.slide_width - 2 * m, prs.slide_height - 2 * m)
render(slide, data, tokens, bounds)
prs.save("venn_example.pptx")
```
