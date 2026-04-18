# Chart Interface Contract — load-bearing

Every chart file MUST expose EXACTLY one public function:

```python
def render(slide, data, tokens, bounds):
    """
    Render this chart type into the given slide using native python-pptx shapes.

    Parameters
    ----------
    slide : pptx.slide.Slide
        The target slide. Shapes are added to slide.shapes.
    data : dict or list
        Chart-type-specific data payload. See the chart's docs.md for shape.
    tokens : dict
        Theme tokens. Keys (all required): primary, accent, text, muted, bg,
        font_display, font_body, font_mono, font_size_base_pt.
        Optional: radius_px.
        All colors are hex strings "#RRGGBB". Fonts are family-name strings.
    bounds : tuple
        (x_emu, y_emu, w_emu, h_emu). The chart must fit inside this rectangle.
    """
```

## Rules

- Native python-pptx shapes ONLY. No pptxgenjs, no SVG, no embedded pptx chart types, no matplotlib-to-image.
- Acceptable imports: `pptx.util`, `pptx.shapes.*`, `pptx.dml.color`, `pptx.enum.shapes`, `pptx.enum.text`. Stdlib fine.
- `tokens` is the ONLY styling source. Never hardcode a color or font anywhere.
- Read colors as hex strings; convert with `pptx.dml.color.RGBColor.from_string(hex[1:])` (skip the `#`).
- Use `pptx.util.Emu(n)` / `pptx.util.Pt(n)` for coordinate math.
- The chart fills `bounds`. Anything outside `bounds` is a bug.
- No network calls. No file I/O inside `render()`.
- The function mutates `slide` and returns None (or the root shape group, optional).

## Example color/font pattern

```python
from pptx.dml.color import RGBColor
from pptx.util import Emu, Pt

def _rgb(hex_):
    return RGBColor.from_string(hex_.lstrip("#"))

def render(slide, data, tokens, bounds):
    x, y, w, h = bounds
    bg = _rgb(tokens["bg"])
    primary = _rgb(tokens["primary"])
    font_body = tokens["font_body"]
    size = Pt(tokens["font_size_base_pt"])
    # ... build shapes ...
```

## Forbidden

- Hardcoded hex literals (except inside the `_rgb` helper above, which only reads from `tokens`).
- Hardcoded font names.
- `matplotlib`, `PIL`, any rasterizer.
- `pptx.chart.*` (the built-in chart API) — we want native drawn shapes, not embedded Excel charts.
- Drawing outside `bounds`.
