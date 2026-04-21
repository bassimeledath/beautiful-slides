# slopegraph

Two vertical axes (before/after) with lines connecting each item's position, showing rank or value changes. Direct-labeled on both sides, no legend needed.

## Usage

```python
from charts.slopegraph.render import render

render(slide, data, tokens, bounds)
```

## Data shape

```python
data = {
    "title": "Market share shift, 2024 vs 2025",        # optional
    "left_label": "2024",                                 # axis header, default "Before"
    "right_label": "2025",                                # axis header, default "After"
    "items": [
        {"name": "Alpha Corp",  "left": 32, "right": 28},
        {"name": "Beta Inc",    "left": 25, "right": 30},
        {"name": "Gamma Ltd",   "left": 18, "right": 19},
        {"name": "Delta Co",    "left": 15, "right": 14},
        {"name": "Epsilon AG",  "left": 10, "right": 9},
    ],
    "highlight": ["Beta Inc"],       # optional; items to emphasize (primary color)
    "value_suffix": "%",              # optional; appended to displayed values
}
```

- `items`: 5-12 entries recommended. Each must have `name`, `left`, and `right` numeric values.
- `highlight`: when provided, highlighted items use `tokens["primary"]` with bold labels; others use `tokens["muted"]`. When omitted, lines are colored by direction: increases use `tokens["accent"]`, decreases use `tokens["primary"]`, flat uses `tokens["muted"]`.

## Styling

- Background fills with `tokens["bg"]`.
- Title uses `tokens["font_display"]`, bold, ~1.55x base size.
- Axis headers use `tokens["font_body"]`, bold, in `tokens["muted"]`.
- Item labels use `tokens["font_body"]` at ~0.9x base size.
- Endpoint dots are small filled circles matching the line color.
- Lines are ~1.75-2pt weight depending on highlight state.

## Proof

Ran `python example.py` -- emits 5 `.pptx` files, one per mode. OK.
