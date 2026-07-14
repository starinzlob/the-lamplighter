# old-press · 老印刷

**Old London Editorial Noir** — a vintage-print visual style skill for AI coding agents (Claude Code / any agent that reads `SKILL.md`).

一句话：让 agent 做出来的所有东西——UI、海报、落地页、生成图——都像**从一台百年老印刷机里印出来的**：半色调网点、铅印质感、旧报纸、油墨扩散、轻微套印偏移，配上严格的瑞士网格和大量留白。

> A quiet personal archive rendered through interwar British newspaper advertising, bold halftone printing, aged newsprint, engraved London architecture, warm darkness, and restrained editorial typography.

## How it works

Two layers:

| Layer | What | Swappable? |
|-------|------|-----------|
| **Base** | The printing craft — halftone, letterpress, newsprint, ink bleed, misregistration + strict editorial grid | Never |
| **Theme** | The ink — default **Gaslight** (1920s British detective), alternate **Vapor** (90s vaporwave, still letterpressed) | Yes |

Ask for any subject and the paper stays the same; only the ink changes.

The skill also recasts UI components as print-shop objects: buttons are metal type blocks, badges are wax seals, notifications are telegrams, dark mode is the gaslit shop after hours.

## Install

```bash
npx skills add <this-repo-url>
```

Or copy the folder into your agent's skills directory (e.g. `~/.agents/skills/old-press`).

## What's inside

```
SKILL.md                     the skill — rules, typography, metaphor map, checklist
references/tokens.css        design tokens (Gaslight day/night + Vapor + rarity inks)
references/textures.css      CSS recipes: halftone, grain, misregistration, type-block button…
references/image-prompts.md  prompt suffixes + theme-scoped negative prompts
demo/index.html              type specimen page (open directly in a browser)
```

## Demo

Open `demo/index.html` — a self-contained specimen sheet showing tokens, textures, and the component metaphors in both day and night (煤气灯) modes.

## The one rule

**Would it survive being photocopied?** If a design needs gradients or glow to work, it's not old-press.

## License

MIT
