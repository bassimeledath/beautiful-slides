# Beautiful Slides - Development Guide

A Claude Code skill for producing high-quality, editable PowerPoint decks via python-pptx.

## Quick Reference

| Topic | Doc |
|-------|-----|
| Skill definition | [skills/beautiful-slides/SKILL.md](skills/beautiful-slides/SKILL.md) |
| Ablation study | [skills/beautiful-slides/EVIDENCE.md](skills/beautiful-slides/EVIDENCE.md) |
| Chart interface | [skills/beautiful-slides/charts/INDEX.md](skills/beautiful-slides/charts/INDEX.md) |
| Mode tokens | [skills/beautiful-slides/charts/MODE_TOKENS.md](skills/beautiful-slides/charts/MODE_TOKENS.md) |

## Conventions

- **Skill source**: `skills/beautiful-slides/SKILL.md` is the canonical skill definition.
- **Path references**: Always use `${SKILL_DIR}` in SKILL.md for portable paths. Never hardcode absolute paths.
- **Chart templates**: All charts share the signature `render(slide, data, tokens, bounds)` and read styling only from the `tokens` dict.
- **Modes**: 5 visual modes (`sv-keynote`, `consulting-boardroom`, `editorial-magazine`, `craft-minimal`, `playful-marketing`). Never mix modes within a deck.

## Local Development

The symlink `.claude/skills/beautiful-slides` -> `../../skills/beautiful-slides` makes the skill available when developing in this repo.

## Repo

GitHub: `bassimeledath/beautiful-slides`
