---
name: old-press
description: 'Old London Editorial Noir — a vintage-print visual style for vibe coding. Everything looks like it came off an old printing press: halftone dots, letterpress texture, aged newsprint, ink bleed, slight misregistration, strict editorial grid. Default theme is 1920s British detective (gaslight); swappable ink layers (e.g. vaporwave) print on the same paper. Use when building UI, posters, landing pages, or writing image-generation prompts and the user asks for 复古印刷 / 老报纸 / 铅字 / 英伦侦探 / halftone / letterpress / vintage print / editorial noir style, or says "用我的风格 / in my style".'
---

# old-press · 老印刷

Everything you make should look like it was **printed on a hundred-year-old press** — not rendered on a screen. This skill has two layers:

1. **Base layer (constant)** — the printing craft: paper, ink, dots, imperfection. Never remove it.
2. **Theme layer (swappable ink)** — what's printed on the paper. Default: *Gaslight* (1920s–30s British detective). Alternate: *Vapor* (90s vaporwave, still printed on old paper).

If the user names a different subject/era, **keep the base layer, swap only the theme layer.**

---

## 1 · Base layer — the press

Every output must carry at least three of these material cues:

- **Halftone dots** — bold, visible dot screens on images and large fills
- **Letterpress / screen-print texture** — uneven ink coverage, slight impression
- **Aged newsprint / parchment** — warm off-white paper, grain, fold wear
- **Ink bleed** — edges slightly soft, never vector-crisp
- **Misregistration** — one accent layer offset ~1–2px, like a mis-aligned print pass
- **Low-fidelity printing** — embrace roughness; "clean vector perfection" is a bug

Layout is the counterweight: **strict Swiss grid, strong hierarchy, generous negative space, centered composition**. Rough materials, disciplined typography — that contrast *is* the style.

Load `references/textures.css` for ready-made CSS recipes (halftone, grain, misregistration, drop caps, column rules).

## 2 · Typography

| Role | Face | Web stack |
|------|------|-----------|
| Headlines (EN) | NYT Cheltenham spirit | `"Cheltenham", "Sorts Mill Goudy", "Playfair Display", Georgia, serif` |
| Headlines (CN) | 宋体报纸味 | `"Songti SC", "Noto Serif SC", "SimSun", serif` |
| Masthead | Blackletter | `"UnifrakturMaguntia", serif` |
| Typewriter / footnotes / tech | Mono | `"Special Elite", "Courier New", Courier, monospace` |
| British classics (alternates) | Caslon · Baskerville · Johnston · Gill Sans · Clarendon | |

Detail rules: old-style figures (`font-feature-settings: "onum"`), small caps (`"smcp"`) with letterspacing for labels, drop caps on lead paragraphs, column rules between text columns, newspaper decks under headlines.

## 3 · Theme layer

### Gaslight (default) — 1920s British detective

Mood: quiet, mysterious, melancholy but warm. Gas lamps, fog, Victorian brick, typewriters, brass, pocket watches. References: Sherlock Holmes, Peaky Blinders, The Third Man, old Scotland Yard.

Tokens in `references/tokens.css` — day mode on cream paper, night mode (`body.night`) as gaslit dark. Core inks:

```
paper #E9E3D3 · ink #2C2924 · ink-deep #1E1C17 · red #8E2F27
brass #A8842C · muted #5C574A · faded #6A6452 · rule #8F8975 · desk #37332A
```

**Negative list (Gaslight theme only, not global):** no neon, no cyberpunk, no Y2K, no futuristic, no plastic, no high saturation, no glossy digital finish, no bright RGB lighting, no perfect ink registration.

### Vapor (alternate) — 90s vaporwave, letterpressed

Lavender / cyan / magenta — but **de-saturated as if screen-printed on old newsprint**, never glowing. The neon ban obviously does not apply here; the "printed, not lit" rule still does.

### Rarity inks (optional accents, from the type-bureau system)

黑墨 black `#2b2620` · 红墨 red `#a63a2b` · 烫金 gold-foil `#b8860b` · 错版 misprint violet `#5d4a9c` — use as a tiered accent scale (common → rare) for badges, cards, gacha-like reveals.

## 4 · Metaphor mapping (UI)

Don't decorate components — **recast them as print-shop objects**:

| Component | Becomes |
|-----------|---------|
| Button | Metal type block（铅字块）— slight impression on press |
| Badge / achievement | Wax seal（火漆印） |
| Notification / toast | Telegram（电报体，全大写 mono，STOP 作句读） |
| Input field | Typewriter paper line |
| Divider | Column rule |
| Tag / chip | Classified-ad box |
| Loading state | "Printing…" — ink rolling on |
| Footer | Colophon（版权页） |
| Dark mode | 煤气灯夜版 — the shop after hours, not "dark theme" |

## 5 · Print jobs — one-line deliverables

The repo root `index.html` is a self-contained card generator (serve the repo root with any static server, or use the deployed site). When the user asks for a finished image, don't restyle from scratch — drive the generator:

| User asks | Template | Default size |
|-----------|----------|--------------|
| 金句卡 / quote share card | `quote` | 1080×1440 (3:4) |
| 报纸剪报 / newspaper clipping, spoof headline | `clip` | 860×auto |
| 跑团道具 / TTRPG handout, CoC front page | `paper` | 1240×1754 (A4) |
| 通缉令 / wanted poster | `wanted` | 1080×1440 |
| 电报 / announcement, changelog, status card | `tele` | 1280×720 |

Agent workflow: serve repo root → open `index.html` → select template and fill fields (tab buttons carry `data-id`, inputs carry `data-k`) → set theme (`day`/`night`/`vapor`) → screenshot the `#stage` element at full size, or call `htmlToImage.toPng(document.querySelector('#stage'),{pixelRatio:2})`. `templates/quote-card.html` also accepts URL params (`?q=…&by=…&theme=night`) for zero-JS driving.

## 6 · Image-generation prompts

Always append the material suffix:

```
halftone, bold halftone dots, screen printing, letterpress, old newspaper
texture, low-fi print, ink bleed, misregistration, paper grain, aged paper
```

For Gaslight also add theme + negative prompt from `references/image-prompts.md`. One-line style definition for any generator:

> Old London Editorial Noir — a quiet personal archive rendered through interwar British newspaper advertising, bold halftone printing, aged newsprint, engraved London architecture, warm darkness, and restrained editorial typography.

## 7 · Checklist before shipping

- [ ] Would this survive being photocopied? (If it needs gradients/glow to work — redo)
- [ ] At least 3 material cues from §1 present
- [ ] Grid strict, whitespace generous, hierarchy obvious at arm's length
- [ ] Accent color used like a second ink pass — one, sparingly, slightly misregistered
- [ ] Nothing looks "clean vector perfect"
