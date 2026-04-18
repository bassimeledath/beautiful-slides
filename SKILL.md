---
name: beautiful-slides
description: Produce editable, visually disciplined PowerPoint decks (.pptx) from a brief. Use whenever a task mentions a deck, slides, a presentation, a .pptx file, or asks you to build/edit/inspect a slide deck. Uses python-pptx for fine control, LibreOffice for round-trip rendering, and enforces explicit mood→mode selection, a canvas-bounds check, and a must-include self-audit before declaring the deck done.
---

# Beautiful Slides

A disciplined authoring skill for producing editable PowerPoint decks that pass a human "this looks intentional" bar. The target is not pretty-by-accident — it is a deck where every slide's register (palette, type, spacing) is predictable from the brief, every shape lives inside the canvas, and every must-include from the brief is actually present.

This skill is designed for an LLM that will write Python, execute it, inspect the rendered output, and iterate. It does not assume a GUI. It assumes Python 3, `python-pptx`, and a headless LibreOffice (`soffice`) are available.

## Thesis

**Say one thing, show one thing, prove one thing.** One decision-relevant idea per narrative slide; evidence may be dense, but it must still point at one conclusion. A deck is not a mood board and not a memo — it is a memory machine. Story first, evidence second, appendix always.

Bullet points are not banned; they are on probation. They are defensible only when the audience needs a checklist, taxonomy, agenda, or parallel comparison — and only when the list is short enough to be scanned in one breath. In every other case, the bullet list is a failure of compression.

Live narrative decks and send-ahead read decks are different artifacts. A presenter-driven deck is a stage instrument; a read deck is a document with page logic, denser prose, and appendix-grade evidence. Trying to make one artifact do both produces the worst of both. If you need both, build two layers — a narrative deck in front, a reference appendix behind it.

## When to use this skill

Trigger on any of:
- a `.pptx` file mentioned as input or output
- the words "deck", "slides", "presentation", "pitch", "keynote", "read-ahead", "board", "launch"
- a request to build, edit, split, merge, summarise, or extract content from slides
- a request to produce a visual for a talk, a board meeting, a launch, or a dinner

Do not trigger for plain-document work (essays, reports, blog posts, emails) unless the user is explicitly asking for a slide rendering of that content.

## Core workflow

A small, boring cycle. Do not deviate — the discipline is the feature.

1. **Parse the brief.** Extract: audience, length (exact slide count if given), mood cues, must-include items, do-not-do items. If any of these are missing, pick a reasonable default and note what you defaulted.
2. **Pick one mode.** Use the Mood → Mode table below. One mode, one palette, one type stance. Commit to it for every slide.
3. **Write the outline.** One line per slide: `N. [pattern name] — [single message]`. Do not proceed until the outline covers every must-include. A pitch-deck default cadence is listed under "Deck structure".
4. **Author in Python.** Use `python-pptx`. Create a new `Presentation`, set `slide_width = Inches(13.333)` and `slide_height = Inches(7.5)` for widescreen 16:9. Emit one slide at a time. Save.
5. **Render to PNG.** Use `soffice --headless --convert-to pdf` then `pdftoppm -r 100` to turn the pptx into per-slide PNGs. Open slides 1, 2, and the final slide at minimum — do not skip this step.
6. **Run the bounds check.** `python scripts/check_bounds.py out.pptx` must exit 0. Fix any violation and re-save.
7. **Run the must-include self-audit.** Extract the brief's must-includes into a checklist, extract text from the pptx, and mark every item COVERED / MENTIONED / MISSING. Patch until all are COVERED.
8. **Ship.**

If any step fails, go back — do not paper over a violation by shrinking type to the point of unreadability or by dropping a must-include.

## Mood → Mode Mapping

The generator's first job is to classify the deck's mood from the brief — scan for cues like "keynote", "board", "launch", "review", "docs", "conference", and adjectives such as "cinematic", "sober", "playful", "craft", or "technical". The second job is to pick exactly ONE mode from the table below that matches the dominant signal. The third job is to stay in that mode for every slide in the deck — palette, type stance, and layout stance all come from the same row.

| Mood cues in brief | Mode name | Palette / type stance | Layout stance |
|---|---|---|---|
| "Apple keynote", "cinematic", "OLED", "stage" | `keynote-dark` | near-black bg, off-white type, single electric accent, display serif OR grotesque at 84–120pt | full-bleed, asymmetric, one hero element |
| "board", "read-ahead", "Bain", "Economist" | `boardroom` | white bg, charcoal text, single muted accent, tabular figures | dense-but-aligned, takeaway titles, small type (14–18pt) |
| "Linear", "Vercel", "Stripe Docs", "changelog" | `tech-docs` | flat bg, single accent, mono for code/metrics, geist-like sans | thin rules, direct labels, no ornament |
| "Kenya Hara", "Muji", "Kinfolk", "craft" | `craft-minimal` | warm off-white bg, near-black, optional muted olive/stone used once | huge margins, 1 image per slide, serif display as punctuation |
| "Figma Config", "Notion launch", "Linear launch", "playful" | `playful-marketing` | warm off-white + one orange-ish accent, custom grotesque display | oversize headlines, asymmetric but disciplined |
| (default) | `default-light` | warm off-white bg, near-black text, one accent, system sans | safe 12-col grid |

### Authoring examples

- Brief says "Series B pitch on a big OLED, cinematic, confident, quiet, expensive" → pick `keynote-dark`. Do NOT use gradients. Do NOT use 3 colors. Use ONE accent, black bg, single 120pt hero number on slide 2.
- Brief says "internal board read-ahead for Q3 portfolio review, Economist-style, dense" → pick `boardroom`. Do NOT use oversized display type. Do NOT use a dark bg. Use takeaway titles, 14–18pt body, one muted accent for the single KPI that matters.

### Mode discipline (explicit ban)

Once a mode is picked, do not mix in elements from another mode. If the brief signals two modes, pick the dominant one from the LAST stated style sentence. A deck that is 70% `keynote-dark` and 30% `tech-docs` reads as inconsistent; a deck that is 100% `keynote-dark` reads as intentional, even if the mode choice is debatable. Consistency beats optimality.

### Mode tokens

Recommended tokens per mode. Use these verbatim or tighten them — do not invent a fourth hue.

| Mode | bg | fg | muted | accent | display face | body face |
|---|---|---|---|---|---|---|
| `keynote-dark` | `#05070A` | `#F5F7FA` | `#9AA4B2` | `#21D4FD` | Manrope ExtraBold | Manrope Medium |
| `boardroom` | `#FFFFFF` | `#101828` | `#475467` | `#0F4C81` | Public Sans Semibold | Public Sans Regular |
| `tech-docs` | `#F5F7FB` | `#111827` | `#667085` | `#174CD3` | Geist Sans Semibold | Geist Sans Regular |
| `craft-minimal` | `#FCFBF8` | `#22201C` | `#7B776F` | `#7C8571` | Instrument Serif | Instrument Sans |
| `playful-marketing` | `#FFF4EB` | `#1B1B1F` | `#6E6A73` | `#FF7A00` | Bricolage Grotesque Bold | Plus Jakarta Sans Medium |
| `default-light` | `#F8F7F4` | `#111111` | `#4B5563` | `#1E40AF` | Inter Semibold | Inter Regular |

If a font is not installed, LibreOffice will silently substitute. Either install the font or switch the mode's face to something you know resolves — do not ship without verifying the rendered output.

## Canvas, grid, and rhythm

The canvas is 16:9 widescreen: **13.333 in × 7.5 in** (EMU: `12,192,000 × 6,858,000`; 1 in = 914,400 EMU). The 1920 × 1080 px preview maps cleanly onto it. Every shape you place must fit inside this rectangle; the bounds check enforces that.

```
canvas-px:              1920 × 1080
canvas-in:              13.333 × 7.5
canvas-emu:             12192000 × 6858000

title-safe-margin-in:   0.667 left/right, 0.375 top/bottom
safe-area-in:           12.0 × 6.75

master-grid:            12 columns
gutter-in:              0.167
alias-grid-6:           compare, paired charts, before/after
alias-grid-4:           section dividers, three-up, hero slides

baseline-grid:          8 px / 4 pt / 50800 EMU
```

The 12-column grid is the operating system. Collapse to 6 for bilateral slides (before/after, counterweight). Collapse to 4 for hero slides, section breaks, or strict three-ups. Always land vertical breaks on a baseline — 8 px / 4 pt is fine enough for type, coarse enough for layout.

Spacing is a scale, not a vibe:

```
spacing-px:    4 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128
```

Outer margins: **96 px** on narrative slides, **64 px** on dense reference slides. Gaps between related elements: **24–32 px**. Gaps between unrelated groups: **48–64 px**. Around the focal element, preserve at least **64 px** of breathing room on every exposed side. If you cannot afford that, the slide has too many things on it.

Target ink ratios:

```
narrative-slides:     65/35 whitespace-to-ink
mixed-proof-slides:   55/45
chart-slides:         45/55
appendix-slides:      35/65
```

## Typography

We use exact steps, not formulas.

```
type-scale-pt:   112 / 84 / 60 / 44 / 32 / 24 / 18 / 14 / 12
```

Pick the mode's scale from the token block above; use this global ladder when a specific mode value is not given.

Live body floors:

```
live-body-floor-pt:
  small-room-30p:       24
  auditorium-300p:      32
  read-deck-laptop:     14
```

Line-height: display (60–84 pt) 0.95; headline (32–44 pt) 1.05; subhead (24 pt) 1.15; body (14–18 pt) 1.35; caption (12 pt) 1.25.

Tracking (em thousandths): display -30, headline -15, subhead -5, body 0, caption +10, all-caps labels +40.

Measure (characters per line) should land in: display 12–24, headline 20–36, body 45–72, caption 28–42. If your body block is rendering at 90 CPL, shrink the block, not the type.

Numerals: **tabular lining** in tables, financials, dashboards, timelines, any column where alignment matters. **Proportional lining** in headlines and prose. Ban old-style numerals on projected slides — lovely in books, annoying at 40 feet.

A standard slide gets **three typographic levels max**: headline, support, annotation. A fourth level is allowed only in appendices, only for source notes. If you need five levels, you do not have hierarchy — you have sediment.

## Color

One background, one primary text color, one accent. That is three colors total. If a chart needs more, use tints/shades of the accent plus one neutral grey. Never introduce a fourth hue.

Contrast floor: **7:1** for body text (WCAG AAA), **9:1** preferred for live presentation where projection, ambient light, tinted screens, and compressed exports degrade the signal. Hero text of 32 pt or above may fall to 7:1; body text does not get that luxury.

Dark mode is for cinematic keynotes, product demos on controlled displays, and stage environments where the screen itself is a light source. Most SaaS decks should **not** default to dark mode because they are read on laptops, forwarded as PDFs, printed, and skimmed in bright rooms. Choose dark only when the brief says "stage", "OLED", or "cinematic".

Colorblind-safe pairs: blue/orange, navy/gold, teal/magenta, charcoal/acid green — but only when the luminance contrast is strong. Avoid red/green as a sole encoding; never use color as the only means of conveying meaning. Run a grayscale check routinely.

## Deck structure

Structures are not interchangeable. Use the pattern that matches the job.

| Structure | One-sentence summary | Best-fit contexts |
|---|---|---|
| SCQA | Situation, complication, question, answer. | Executive updates, consulting decks, board decks. |
| Minto Pyramid | Lead with the recommendation, group supporting evidence. | Boardroom, investor diligence. |
| Problem–Agitate–Solve | Make the pain vivid, then relieve it. | Sales, category creation, launches. |
| Duarte Sparkline | Alternate "what is" and "what could be" to create tension. | Keynotes, product launches, mission talks. |
| Heroic Arc | Audience is hero; presenter is guide. | Vision decks, fundraising with a founder story. |

Default cadence for a strong **10-slide pitch deck**:
1. Company purpose.  
2. Problem (sharp customer pain).  
3. Product / solution.  
4. Why now.  
5. Market / wedge.  
6. Traction.  
7. Business model.  
8. Go-to-market.  
9. Team.  
10. Vision + raise / next milestone.

A **5-slide executive update**: status headline, KPI delta, risk callout, decision needed, next 30/60/90. If your update has a history lesson, it is not an update.

A **30-slide technical talk**: opener → stakes → current-state pain → mental model → architecture → demo slice → evidence → edge cases → benchmark → migration path → lessons → recap → Q&A, with appendices after the live narrative.

## Slide patterns

A grammar, not a template library. Each pattern defines what the slide is for, when to use it, composition bounds, and copy limits. Compose from these; do not invent new ones on the fly.

**Marquee** — announce the deck. Opener only. Title 60–84 pt, 2–8 words; subtitle 18 pt, 0–16 words.

**Knife-Cut** — section divider. 1–4 words at 44–60 pt. No sentence, no punctuation. 96 px top/bottom space.

**Verdict** — one memorable claim. Headline 44–60 pt, 3–12 words, verbs, no period. Proof line 18 pt, ≤20 words.

**Pullquote** — borrow authority. Quote 32–44 pt, 8–40 words, max 36 CPL. Attribution 14 pt, `name, role`. One quote only.

**Number Hammer** — make one number impossible to forget. Hero numeral 84–120 pt. Unit/context 24 pt, ≤12 words. Explainer 14–18 pt, ≤20 words. One small source note in a corner.

**Counterweight** — compare two states. 6-col alias, split at center. Each side: one 24 pt heading, one 14–18 pt body, ≤3 evidence chips. ≤40 words per side.

**Triptych** — three parallel ideas. 4-col alias, one unit per third, shared baseline. Titles 1–3 words, body ≤24 words. Syntax must be parallel. No filled tiles — use spacing, not containers.

**Proof Plot** — quantitative evidence with a takeaway. Chart 8 cols, takeaway block 4 cols. Takeaway headline 24 pt, 4–10 words. Source line required. Remove non-data ink.

**System Map** — relationships, flows, architecture. 12-col grid, max 7 nodes on narrative slides (12 in appendix). Labels 14–18 pt, 1–4 words per node. Arrows move in one dominant direction.

**Runway** — sequence over time. Horizontal for 3–7 stages. Step label 18–24 pt, 1–3 words. Description 12–14 pt, ≤16 words. One time axis, one direction.

**Poster** — let an image do the emotional labor. Full-bleed photo; text in title-safe area with one light/dark scrim if needed. Headline 32–60 pt, 1–8 words.

**Crop Demo** — show product UI without drowning in chrome. Crop aggressively; one zoomed region per slide. Callout 18 pt, caption 14 pt. Never paste a full browser screenshot unless the browser matters.

**Resolution** — closing. CTA 32–44 pt, imperative verb, 2–10 words. No "Thank you" as primary. If there are three next steps, use Triptych instead.

**Dossier** — appendix, board backup. 12-col grid, 64 px margins. Headline 24 pt, body 12–14 pt, tabular lining. Citations mandatory. Up to 120 words body.

**Holding Screen** — Q&A. One label 44 pt, optional prompt 18 pt. Low-noise background. No decorative montage.

## python-pptx cheat sheet

Minimal imports and constants the generator should reach for:

```python
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

prs = Presentation()
prs.slide_width  = Inches(13.333)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]  # truly blank
```

A full-bleed background rectangle for dark modes:

```python
slide = prs.slides.add_slide(BLANK)
bg = slide.shapes.add_shape(
    MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height
)
bg.fill.solid(); bg.fill.fore_color.rgb = RGBColor(0x05, 0x07, 0x0A)
bg.line.fill.background()
```

A text block (do this instead of placeholders — placeholders drag layout baggage you will fight):

```python
tb = slide.shapes.add_textbox(Inches(0.5), Inches(0.6), Inches(12.3), Inches(1.2))
tf = tb.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = 0
tf.margin_top = tf.margin_bottom = 0
p = tf.paragraphs[0]
p.alignment = PP_ALIGN.LEFT
run = p.add_run()
run.text = "Halverline"
run.font.name = "Manrope"
run.font.size = Pt(44)
run.font.color.rgb = RGBColor(0xF5, 0xF7, 0xFA)
```

A Number Hammer (slide 2 or 3 of most keynote-dark decks):

```python
hero = slide.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(11.3), Inches(3.2))
htf = hero.text_frame
r = htf.paragraphs[0].add_run()
r.text = "$18.4M"
r.font.size = Pt(220)
r.font.name = "Manrope"
r.font.bold = True
r.font.color.rgb = RGBColor(0xF5, 0xF7, 0xFA)
```

Accent line (a thin rectangle beats `.line` for consistency):

```python
accent = slide.shapes.add_shape(
    MSO_SHAPE.RECTANGLE,
    Inches(0.5), Inches(5.9), Inches(0.6), Emu(38000)   # ~3 pt tall
)
accent.fill.solid(); accent.fill.fore_color.rgb = RGBColor(0x21, 0xD4, 0xFD)
accent.line.fill.background()
```

Charts: prefer to render the chart with matplotlib to a PNG and `add_picture` it rather than use `python-pptx`'s native chart API. Native charts look Excel-y and are painful to style; a matplotlib PNG is a fixed artifact you control completely. Direct-label the series; remove gridlines; kill legends unless absolutely required.

Speaker notes (always fill them — the deck is a stage instrument, the notes are the script):

```python
slide.notes_slide.notes_text_frame.text = "ARR hero. Pause. Let the number land."
```

## Data visualization

Only five chart types are consistently defensible on slides:

1. **Bar** — comparing categories; fastest to decode.
2. **Line** — change over time when the trend, not every data point, is the story.
3. **Dot plot** — precision with less ink; better than bars for category comparisons on a clean scale.
4. **Scatter** — relationship, clustering, outliers. Annotate or do not bother.
5. **Slope** — when only the start and end matter; cleaner than a full line chart for two-point change.

**Banned** on slides: dual-axis charts, 3D bars, pies with more than three slices, stacked area with more than four series, radar charts, donut charts with decorative holes pretending to be insight.

**Direct-label the data, not the legend, whenever possible.** If you exceed five distinct series, split into small multiples or kill series until the chart has a voice again. Apply Tufte's data-ink ratio aggressively — any redundant gridline, legend box, axis title, border, bevel, or default shadow is theft. If the graphic can lose 30% of its non-data ink without losing meaning, remove it.

A stat-hero slide is not a chart. One number, one context line, one comparator if truly necessary, one source. Do not wrap a hero number in axes or a lonely bar because software offered to.

## Imagery and icons

Use **SVG** for logos, icons, diagrams, and anything with text or sharp edges. Use **PNG** for raster interface captures. Use **photos** for evidence, atmosphere, human context. Use **illustration** only when reality is unavailable or distracting.

Icon hierarchy: Lucide first, Heroicons second, Phosphor third, Radix fourth. Keep icons on a 24 × 24 grid when they appear in slides. Match stroke weights. Never mix filled and outline icons unless the semantic distinction is structural and repeated.

AI-generated images are defensible only in concept / speculative / internal decks, and only when labeled honestly. For investor-facing or public-facing decks, treat them as guilty until verified. Known fast tells of AI sludge: extra or fused fingers, garbled signage, over-smoothed faces, default cyan-teal grade, plastic bokeh, symmetrical interiors.

Do not use stock photography of diverse smiling teams around a MacBook. Do not use business-handshake-in-front-of-glass-tower imagery. Do not use glowing-brains-made-of-circuits. Do not use pastel isometric collaborators leaning over giant charts. If you would find it on page one of a template marketplace, bury it.

## Motion and builds

Default: **no transition** between standard slides; fade between major sections if the deck is live and cinematic. Nothing else by default. Motion must guide attention or clarify sequence; if it does neither, it is pageantry.

The only three defensible builds:
1. **Fade In** — labels, callouts, progressive evidence. 0.20–0.35 s.
2. **Wipe** — process steps, timelines, directional sequences. Direction must match narrative flow.
3. **Morph / matched-move** — only for zooming into the same object state across slides (chart, map, UI crop). Never a magic trick.

Forbidden transitions by name: Cube, Rotate, Fly-In From Corners, Bounce, Dissolve With Sparkle, Random Bars, Curtains, Ferris Wheel.

## Rendering and visual QA

Always render before declaring done. Headless:

```bash
soffice --headless --convert-to pdf --outdir /tmp/render out.pptx
pdftoppm -r 100 /tmp/render/out.pdf /tmp/render/slide
```

This produces `/tmp/render/slide-01.png`, `-02.png`, etc. Open slides 1, 2, and the last one at minimum. Look for:

- text clipped off the canvas edges
- overlap between title and body blocks
- wrong font silently substituted (LibreOffice falls back when a font is missing)
- invisible text (same color as background)
- charts pushed off-canvas by an oversize legend

If any of these is present, fix in Python and re-render. Do not ship on a first render without visually checking.

## Post-generation Bounds Check

After saving, run the bundled script:

```bash
python scripts/check_bounds.py path/to/out.pptx
```

It walks every shape on every slide and asserts `(left, top, width, height)` stays inside `12,192,000 × 6,858,000` EMU. Exits 0 if clean; exits 1 with a report of violations otherwise. Example violation line:

```
slide=4 shape=TextBox 12 bounds=(11800000,6200000,1200000,1000000) violation=right>canvas,bottom>canvas
```

The fix is always: move or resize the shape. Do not "solve" a bounds violation by cropping mentally — LibreOffice renders clip as silent truncation and the judge sees it.

Re-run the check after every patch until it exits 0.

## Must-Include Self-Audit (run AFTER saving the pptx)

Before declaring the deck complete, extract every must-include bullet from the scenario brief into an explicit checklist. Run markitdown on the emitted pptx (`python -m markitdown output.pptx`) and, for each checklist item, grep/scan the output text. For each item mark: COVERED (literal phrase or close paraphrase is present), MENTIONED (referenced but vague), or MISSING.

If any item is MISSING, patch the deck: pick the best slide to add/modify, make the change, re-save, re-run this audit. Repeat until every item is COVERED. MENTIONED items should be upgraded to COVERED when feasible.

Worked example:

```
- [COVERED] ARR $18.4M — slide 3 hero number
- [MENTIONED] 94% gross margin — slide 4 footnote, not called out
- [MISSING] Top 5 logos — NOT PRESENT, must add as slide 7
```

Do NOT skip this step even if the deck looks good. Visual polish does not substitute for brief fidelity.

## Editing an existing deck

When the user hands you a .pptx and asks for an edit, do not rebuild from scratch. Open it with `python-pptx`, inspect `prs.slides`, modify the specific shapes you need, and save to a new path. Preserve the original's layout masters, slide dimensions, and theme colors — those are what make the deck look "like itself".

Inspection:

```python
from pptx import Presentation
prs = Presentation("in.pptx")
for i, slide in enumerate(prs.slides, 1):
    for s in slide.shapes:
        if s.has_text_frame:
            text = s.text_frame.text.replace("\n", " | ")
            print(f"slide {i} shape {s.shape_id} {s.name!r}: {text[:80]}")
```

Bulk text replacement:

```python
for slide in prs.slides:
    for s in slide.shapes:
        if not s.has_text_frame:
            continue
        for p in s.text_frame.paragraphs:
            for r in p.runs:
                r.text = r.text.replace("Q3'25", "Q4'25")
```

Always re-run the bounds check after an edit — a longer string can push a text frame past the canvas.

## Anti-patterns (refuse these)

Named so they stop coming back.

- **Bullet Brigade.** Seven or more bullets in identical verb+explanation syntax. Collapse to a Verdict, Triptych, or Dossier.
- **Template Tyranny.** Every slide identical layout, title top-left + three objects below. Rotate among patterns intentionally.
- **Gradient Industrial Complex.** Purple-to-blue gradient on every background. Use flat backgrounds; if you need drama, use image, contrast, or scale.
- **Emoji HR Department.** Emojis standing in for icons. Replace with a proper icon family or drop the icon.
- **Isometric Interns.** Pastel isometric people collaborating around abstract dashboards. Use a real product screenshot or nothing.
- **Cardocalypse.** Every fact lives in a floating rounded card with a soft shadow. Separate by spacing and alignment; remove containers.
- **Blob Nebula.** Decorative blobs, meshes, dot grids behind content. Flat background or one relevant image.
- **Lorem Ipsum's Revenge.** Placeholder text shipped. Grep for lorem/ipsum/placeholder/sample before saving.
- **Period Piece.** Every headline is a full sentence with a period. Convert to takeaway phrases with verbs and no periods.
- **Synergy Index.** "Solutions", "leveraging", "synergies", "best-in-class", "robust", "seamless". Replace each with a concrete noun, number, or action.
- **Excel Aftertaste.** Default blue charts, default legend, default gridlines. Restyle from scratch, add a takeaway title, label directly.
- **Font Soup.** Three or more unrelated typefaces on one slide. One display, one body, one mono maximum.
- **Teleprompter Leakage.** The slide text is the speech text. Move prose to notes; leave the skeleton.
- **Polite Shrug.** Final slide says "Thank You" and nothing else. Replace with Resolution — one ask, one next step.
- **Laptop Diversity Theatre.** Stock photo of smiling diverse team around a laptop. Use product imagery or nothing.
- **Shadow Government.** Every box, chart, image gets a drop shadow. Reserve shadows only for separating inset imagery from a same-tone background.
- **Icon Civil War.** Flat icons mixed with skeuomorphic. One family, one rendering logic.
- **Centerfold Paragraph.** Long centered body copy. Left-align body; reserve centered alignment for short ceremonial text.
- **Geist Everywhere.** Default contemporary sans plus generic near-black UI styling plus blue accent. Choose a mode on purpose. Typography is a position, not a default.

## Accessibility

WCAG AAA is the floor. 7:1 contrast for body, 9:1 preferred for live. Colorblind-safe pairs above; color never the only encoding. Minimum live font sizes: 24 pt body in small rooms, 32 pt in large rooms, 14 pt in read decks, 12 pt only for citations. For read decks, every non-decorative figure gets alt text: `[what it is] + [the takeaway] + [critical value or trend] + [timeframe/source]`.

Low-tech test that catches half the sins software misses: **squint at the slide from six feet away**. If the focal hierarchy disappears, the slide is wrong. If you cannot explain what is first, second, and third to read, the slide is wrong.

## Dependencies

- Python 3.10+
- `python-pptx` — `pip install python-pptx`
- `markitdown` — `pip install markitdown` (for the must-include self-audit)
- LibreOffice with a headless `soffice` binary (macOS: `brew install --cask libreoffice`; Linux: package manager)
- `pdftoppm` from poppler (macOS: `brew install poppler`; Linux: `poppler-utils`)
- Optional: `matplotlib` for chart PNGs

If a fonts directory is available, point LibreOffice at it so your Manrope / Public Sans / Inter calls resolve; otherwise expect silent fallback to a default sans.

## Charts

Reach for a chart when the evidence *is* the story — a revenue bridge, a retention cohort, a conversion funnel, a dashboard-scorecard of KPIs, a density grid. Do not reach for a chart to decorate a narrative slide; a Number Hammer or direct-labeled table usually wins. When the chart *is* the slide, use the bundled `charts/` pack: five native python-pptx templates, theme-aware, load-bearing.

The five templates and when to use them:

- **bar** — discrete comparisons across categories ("which bucket wins"). Grouped 2-series supported.
- **line** — trends over ordered x (time, cohort age). 1–N series; last series can be emphasized.
- **kpi** — hero-number tile with label, value, delta. Compose 2–4 in a row for a scorecard.
- **funnel** — conversion / narrowing stages (pipeline, signup drop-off). 4–7 stages.
- **heatmap** — grid of colored cells, intensity between `bg` and `primary` (hour × weekday, segment × month). Best at ≥ 4×4.

Every template exposes exactly one function with the same signature:

```python
def render(slide, data, tokens, bounds):
    """Draw chart onto `slide` inside `bounds` (x, y, w, h in EMU), styled by `tokens`."""
```

`tokens` is a dict with keys `primary`, `accent`, `text`, `muted`, `bg`, `font_display`, `font_body`, `font_mono`, `font_size_base_pt`, `radius_px`. Pull these from the mode you picked in the Mood → Mode step — charts must use the same palette and type as the rest of the deck. Never hardcode a color inside a chart call.

See `charts/INDEX.md` for the full interface, `charts/MODE_TOKENS.md` for exact token dicts per mode, and each template's `docs.md` + `example.py` for the `data` shape. Rendered per-mode previews live in `charts/<template>/renders/*.png`.

Charts in this pack are **native python-pptx shapes** — rectangles, lines, textboxes — not rasterized PNGs. They stay editable in PowerPoint, they scale without blur, and they pass `check_bounds.py`. Do not wrap them in a matplotlib `add_picture` detour.

## File layout in this skill

```
beautiful-slides/
  SKILL.md              # this file
  scripts/
    check_bounds.py     # canvas-bounds enforcer (run after save)
    render_preview.py   # soffice + pdftoppm convenience wrapper
  charts/               # five themed chart templates (bar, line, kpi, funnel, heatmap)
    INDEX.md            # shared signature + picker guide
    INTERFACE.md        # authoritative interface reference
    MODE_TOKENS.md      # per-mode token dicts
  examples/             # optional reference decks
```

## Closing

A deck is good when the audience understands the point before you explain it, remembers it after you leave, and can defend it when someone tougher than you asks for evidence. When in doubt: **if the slide still makes sense after you remove one-third of what is on it, you have not finished editing.** Say one thing, show one thing, prove one thing.
