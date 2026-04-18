"""Render the bar chart in all 5 modes as separate 16:9 slides."""

from pathlib import Path

from pptx import Presentation
from pptx.util import Inches

from render import render


MODES = {
    "sv-keynote": {
        "primary": "#21D4FD", "accent": "#17B26A", "text": "#F5F7FA",
        "muted": "#9AA4B2", "bg": "#05070A",
        "font_display": "Manrope", "font_body": "Manrope",
        "font_mono": "JetBrains Mono",
        "font_size_base_pt": 18, "radius_px": 6,
    },
    "editorial-magazine": {
        "primary": "#8C2F39", "accent": "#9C5B00", "text": "#181514",
        "muted": "#6F675F", "bg": "#F6F1E8",
        "font_display": "Fraunces", "font_body": "Newsreader",
        "font_mono": "IBM Plex Mono",
        "font_size_base_pt": 16, "radius_px": 0,
    },
    "playful-marketing": {
        "primary": "#FF7A00", "accent": "#0AB39C", "text": "#1B1B1F",
        "muted": "#6E6A73", "bg": "#FFF4EB",
        "font_display": "Bricolage Grotesque", "font_body": "Plus Jakarta Sans",
        "font_mono": "Recursive Mono",
        "font_size_base_pt": 18, "radius_px": 12,
    },
    "consulting-boardroom": {
        "primary": "#0F4C81", "accent": "#05603A", "text": "#101828",
        "muted": "#475467", "bg": "#FFFFFF",
        "font_display": "Public Sans", "font_body": "Public Sans",
        "font_mono": "Public Sans",
        "font_size_base_pt": 14, "radius_px": 0,
    },
    "craft-minimal": {
        "primary": "#7C8571", "accent": "#9A6B39", "text": "#22201C",
        "muted": "#7B776F", "bg": "#FCFBF8",
        "font_display": "Instrument Serif", "font_body": "Instrument Sans",
        "font_mono": "Instrument Sans",
        "font_size_base_pt": 16, "radius_px": 2,
    },
}


DATA_SINGLE = {
    "orientation": "vertical",
    "title": "Revenue by segment, Q1",
    "categories": ["Enterprise", "Mid-market", "SMB", "Startup"],
    "series": [
        {"name": "Q1 Actual", "values": [12.4, 8.1, 4.3, 1.8]},
    ],
    "value_suffix": "M",
    "show_values": True,
}

DATA_GROUPED = {
    "orientation": "vertical",
    "title": "Q1 actual vs. plan, by segment",
    "categories": ["Enterprise", "Mid-market", "SMB", "Startup"],
    "series": [
        {"name": "Actual", "values": [12.4, 8.1, 4.3, 1.8]},
        {"name": "Plan",   "values": [11.0, 8.5, 5.0, 2.0]},
    ],
    "value_suffix": "M",
    "show_values": True,
}

DATA_HORIZONTAL = {
    "orientation": "horizontal",
    "title": "Revenue by segment, Q1",
    "categories": ["Enterprise", "Mid-market", "SMB", "Startup"],
    "series": [
        {"name": "Q1 Actual", "values": [12.4, 8.1, 4.3, 1.8]},
    ],
    "value_suffix": "M",
    "show_values": True,
}


# Pair each mode with a data variant so we exercise grouped + horizontal forms.
MODE_DATA = {
    "sv-keynote": DATA_SINGLE,
    "editorial-magazine": DATA_HORIZONTAL,
    "playful-marketing": DATA_GROUPED,
    "consulting-boardroom": DATA_GROUPED,
    "craft-minimal": DATA_SINGLE,
}


def main():
    out_dir = Path(__file__).parent
    for mode, tokens in MODES.items():
        prs = Presentation()
        prs.slide_width = Inches(13.333)
        prs.slide_height = Inches(7.5)
        slide = prs.slides.add_slide(prs.slide_layouts[6])

        margin = Inches(0.5)
        bounds = (
            margin,
            margin,
            prs.slide_width - 2 * margin,
            prs.slide_height - 2 * margin,
        )

        data = MODE_DATA[mode]
        render(slide, data, tokens, bounds)

        out = out_dir / f"example-{mode}.pptx"
        prs.save(str(out))
        print(f"wrote {out.name}")


if __name__ == "__main__":
    main()
