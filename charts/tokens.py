"""Canonical per-mode token dicts.

Single source of truth for the 5 chart modes. Every `example.py` imports
`MODES` from here instead of redefining the block. Keep in sync with
`MODE_TOKENS.md`.
"""

MODES = {
    "sv-keynote": {
        "primary": "#21D4FD",
        "accent":  "#17B26A",
        "text":    "#F5F7FA",
        "muted":   "#9AA4B2",
        "bg":      "#05070A",
        "font_display": "Manrope",
        "font_body":    "Manrope",
        "font_mono":    "JetBrains Mono",
        "font_size_base_pt": 18,
        "radius_px": 6,
    },
    "editorial-magazine": {
        "primary": "#8C2F39",
        "accent":  "#9C5B00",
        "text":    "#181514",
        "muted":   "#6F675F",
        "bg":      "#F6F1E8",
        "font_display": "Fraunces",
        "font_body":    "Newsreader",
        "font_mono":    "IBM Plex Mono",
        "font_size_base_pt": 16,
        "radius_px": 0,
    },
    "playful-marketing": {
        "primary": "#FF7A00",
        "accent":  "#0AB39C",
        "text":    "#1B1B1F",
        "muted":   "#6E6A73",
        "bg":      "#FFF4EB",
        "font_display": "Bricolage Grotesque",
        "font_body":    "Plus Jakarta Sans",
        "font_mono":    "Recursive Mono",
        "font_size_base_pt": 18,
        "radius_px": 12,
    },
    "consulting-boardroom": {
        "primary": "#0F4C81",
        "accent":  "#05603A",
        "text":    "#101828",
        "muted":   "#475467",
        "bg":      "#FFFFFF",
        "font_display": "Public Sans",
        "font_body":    "Public Sans",
        "font_mono":    "Public Sans",
        "font_size_base_pt": 14,
        "radius_px": 0,
    },
    "craft-minimal": {
        "primary": "#7C8571",
        "accent":  "#9A6B39",
        "text":    "#22201C",
        "muted":   "#7B776F",
        "bg":      "#FCFBF8",
        "font_display": "Instrument Serif",
        "font_body":    "Instrument Sans",
        "font_mono":    "Instrument Sans",
        "font_size_base_pt": 16,
        "radius_px": 2,
    },
}
