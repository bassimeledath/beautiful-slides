# Mode Tokens — synthesized from `/Users/bassime/Downloads/joy.md`

Every chart in this experiment accepts a `tokens` dict with exactly these keys:

- `primary` (str) — hex color "#RRGGBB" (main chart color / primary data series)
- `accent` (str) — hex color "#RRGGBB" (secondary data color / highlights)
- `text` (str) — hex color "#RRGGBB" (foreground / labels)
- `muted` (str) — hex color "#RRGGBB" (axes, gridlines, secondary labels)
- `bg` (str) — hex color "#RRGGBB" (slide background / chart fill)
- `font_display` (str) — font family name for large titles/numbers
- `font_body` (str) — font family name for labels
- `font_mono` (str) — font family name for numeric columns (may equal font_body in modes without a mono)
- `font_size_base_pt` (int) — body text size in points
- `radius_px` (int) — corner radius in pixels (optional, 0 for sharp corners)

Use ONLY these keys. Use `pptx.util.Emu` and `pptx.util.Pt` for conversions. No hardcoded colors or fonts anywhere.

## The 5 modes

### sv-keynote (Silicon Valley Keynote)

```python
SV_KEYNOTE = {
    "primary": "#21D4FD",       # neon cyan accent
    "accent":  "#17B26A",       # success green for secondary
    "text":    "#F5F7FA",       # near-white foreground
    "muted":   "#9AA4B2",       # cool grey
    "bg":      "#05070A",       # black-glass
    "font_display": "Manrope",
    "font_body":    "Manrope",
    "font_mono":    "JetBrains Mono",
    "font_size_base_pt": 18,
    "radius_px": 6,
}
```

Vibe: cinematic, black-glass stagecraft, huge type, one electric accent.

### editorial-magazine (Editorial Magazine)

```python
EDITORIAL_MAGAZINE = {
    "primary": "#8C2F39",       # literary red-wine accent
    "accent":  "#9C5B00",       # warm amber
    "text":    "#181514",       # ink black
    "muted":   "#6F675F",       # warm grey
    "bg":      "#F6F1E8",       # warm paper
    "font_display": "Fraunces",
    "font_body":    "Newsreader",
    "font_mono":    "IBM Plex Mono",
    "font_size_base_pt": 16,
    "radius_px": 0,
}
```

Vibe: literate, warm, sharply edited. Hairlines > boxes. Serif display.

### playful-marketing (Playful Marketing)

```python
PLAYFUL_MARKETING = {
    "primary": "#FF7A00",       # saturated orange
    "accent":  "#0AB39C",       # teal counterweight
    "text":    "#1B1B1F",       # near-black
    "muted":   "#6E6A73",       # warm grey
    "bg":      "#FFF4EB",       # peach cream
    "font_display": "Bricolage Grotesque",
    "font_body":    "Plus Jakarta Sans",
    "font_mono":    "Recursive Mono",
    "font_size_base_pt": 18,
    "radius_px": 12,
}
```

Vibe: confident, warm, kinetic, internet-native, slightly mischievous.

### consulting-boardroom (Consulting Boardroom)

```python
CONSULTING_BOARDROOM = {
    "primary": "#0F4C81",       # navy
    "accent":  "#05603A",       # dark green for favorable deltas
    "text":    "#101828",       # near-black
    "muted":   "#475467",       # steel grey
    "bg":      "#FFFFFF",       # pure white
    "font_display": "Public Sans",
    "font_body":    "Public Sans",
    "font_mono":    "Public Sans",
    "font_size_base_pt": 14,
    "radius_px": 0,
}
```

Vibe: sober, structured, expensive paper, no nonsense. Takeaway titles; hairline rules; tabular figures.

### craft-minimal (Craft Minimal)

```python
CRAFT_MINIMAL = {
    "primary": "#7C8571",       # muted sage
    "accent":  "#9A6B39",       # oxidized copper
    "text":    "#22201C",       # warm ink
    "muted":   "#7B776F",       # stone grey
    "bg":      "#FCFBF8",       # off-white paper
    "font_display": "Instrument Serif",
    "font_body":    "Instrument Sans",
    "font_mono":    "Instrument Sans",
    "font_size_base_pt": 16,
    "radius_px": 2,
}
```

Vibe: quiet, tactile, restrained, museum-bookstore expensive. Enormous margins. Almost no color.

## Key distinctions charts MUST honor

- `bg` color: sv-keynote is dark; the other four are light. Chart fills, axis lines, and text must adapt. NEVER hardcode `white` or `black`.
- `primary` varies wildly: cyan neon, wine red, orange, navy, sage. Charts should feel materially different.
- `font_display` vs `font_body`: use `font_display` on big numbers (KPI values) and optional chart headings; use `font_body` on labels/axis ticks. Use `font_mono` where numeric alignment matters (axis values, KPI deltas).
- `radius_px`: convert to EMUs and use on bar corners / cell corners where the chart supports rounding. 0 = sharp.

## EMU primer

python-pptx works in English Metric Units. 914400 EMU per inch. 12700 EMU per point. Use `pptx.util.Emu(n)`, `pptx.util.Inches(n)`, `pptx.util.Pt(n)` helpers.
