# comparison-matrix

Classic "us vs them" competitive grid. Rows represent items (products, competitors), columns represent criteria (features, capabilities). Cells show checkmarks, crosses, or partial indicators as native Unicode glyphs.

## API

```python
render(slide, data, tokens, bounds)
```

## Data shape

```python
data = {
    "title": "Feature Comparison",                  # optional
    "row_labels": ["Our Product", "Competitor A", "Competitor B"],
    "col_labels": ["SSO", "API Access", "Mobile App", "Analytics"],
    "values": [                                      # row-major
        ["check", "check", "check", "partial"],
        ["check", "cross", "check", "cross"],
        ["cross", "cross", "partial", "cross"],
    ],
    "highlight_row": 0,                              # optional: index of "our" row
}
```

### Cell values

Accepted values per cell:
- Check: `"check"`, `"yes"`, `true`, `True`, `1`
- Cross: `"cross"`, `"no"`, `false`, `False`, `0`, `"x"`
- Partial: `"partial"`, `0.5`, or any other value

## Layout

- Title at top (if provided), `font_display`, `text`, bold, ~1.15x base.
- Column headers across the top, `font_body`, `muted`, bold, centered, ~0.80x base.
- Row labels on the left, `font_body`, `text`, ~0.88x base.
- Highlight row (if set): subtle `primary` tint background, label in `primary`, bold.
- Alternating row striping with subtle `muted` tint.
- Cell glyphs:
  - Check: `accent` colored checkmark (U+2713)
  - Cross: `muted` colored multiplication X (U+2715)
  - Partial: `primary` colored half circle (U+25D0)
- Bottom border: hairline `muted`.

## Tokens used

`primary`, `accent`, `text`, `muted`, `bg`, `font_display`, `font_body`, `font_size_base_pt`, `radius_px`.

## Proof

`python example.py` writes `example-<mode>.pptx` at the chart root, one per mode.
