---
name: lamplighter
description: 'Create finished articles and export-ready newspaper images in The Lamplighter / Old London Editorial Noir style. Use for 1920s British newspaper stories, private-editorial essays, clipping cards, front pages, quote cards, wanted posters, and telegrams. Covers editorial voice, fact handling, article structure, live typography, template field mapping, artwork boundaries, browser composition, PNG export, and visual QA.'
---

# The Lamplighter · 点灯人

This is an **execution skill**, not a mood board. Given a topic, rough note, link,
quotation, announcement, or fictional premise, the agent must be able to:

1. establish the editorial intent and factual boundary;
2. write a complete piece in the Lamplighter voice;
3. compose it with the correct live fonts in the bundled generator;
4. export a readable, verified PNG;
5. return both the final copy and the image.

The house style is **Old London Editorial Noir**: an interwar British private
newspaper with disciplined editorial hierarchy, physical newsprint, visible
halftone and letterpress flaws, quiet film-noir atmosphere, and modern
readability. It must never collapse into generic brown “retro”.

## 1 · Authority and required files

Before making a visual, read the user's persistent design canon when available:
`/Users/zhangxiabin/.codex/design.md`. The canon overrides examples in this
repository. An explicit user direction overrides both.

Use the repository as a working press, not merely as reference:

| File | Purpose |
|------|---------|
| `index.html` | Main five-template generator and PNG export |
| `assets/fonts/lamplighter-display.woff2` | Self-hosted Latin display face |
| `assets/fonts/lamplighter.css` | Lamplighter `@font-face` declaration |
| `assets/fonts/huiwen-mincho/result.css` | Bundled CJK newspaper face |
| `references/tokens.css` | Paper, ink, theme, and font tokens |
| `references/textures.css` | Halftone, grain, ink and edge recipes |
| `references/image-prompts.md` | Optional illustration prompt fragments |
| `templates/quote-card.html` | URL-driven lightweight quote-card route |

Do not redesign the generator for a content-only request. Fill and drive it.

## 2 · Input contract and defaults

Extract these values from the request when provided:

- **subject** — what happened or what the piece is about;
- **intent** — report, reflection, announcement, satire, prop, or quotation;
- **truth mode** — factual, supplied-source summary, personal essay, or fiction;
- **language** — Chinese, English, or bilingual;
- **audience** — public reader, private archive, social feed, or TTRPG table;
- **format** — clipping, front page, quote, wanted poster, or telegram;
- **date/place/byline** — if important;
- **output ratio** — if the destination imposes one.

If these are not specified, infer them without stopping:

- Chinese request → Chinese article with restrained English newspaper furniture.
- A normal story or commentary → `clip` for short copy, `paper` for a full article.
- A single sentence or aphorism → `quote`.
- A launch/status announcement → `tele` only when brevity suits the message.
- A character joke or accusation → `wanted`.
- Default edition → Gaslight day edition; use night only for nocturnal or sombre
  material. Never choose Vapor unless the user requests it or the subject clearly
  calls for 1990s printed vaporwave.
- Default publication → `The Lamplighter`; it may be changed by the user.

Ask a question only when a missing fact would materially change truthfulness or
the required output. Otherwise make a conservative editorial assumption and
state it with the delivery.

## 3 · Truth, sourcing, and fictional material

The old-newspaper voice is not permission to invent facts.

- For current events, products, public claims, prices, dates, or named people,
  verify against primary or authoritative sources before writing.
- Preserve the user's supplied facts. Correct obvious inconsistencies or flag
  them; do not silently turn uncertainty into certainty.
- Attribute reports with natural newspaper language: `据……公布`, `本报查阅……`,
  `according to…`, `records reviewed by The Lamplighter show…`.
- Do not fabricate quotations, eyewitnesses, statistics, locations, dates,
  source names, or URLs.
- Clearly label fictional/TTRPG output as fiction in the accompanying delivery,
  even when the newspaper artifact itself stays in character.
- Satire may exaggerate tone, never impersonate a real news outlet or present a
  damaging invented allegation about a real person as fact.
- Keep a source list beside the copy for factual pieces. The visual may be
  concise, but the delivery must retain traceability.

## 4 · Editorial voice

Write as a **private newspaper editor, observant correspondent, and collector of
small evidence**. The voice is composed, specific, quietly cinematic, and a
little wry. It is not a marketing page, costume drama, or parody of archaic
English.

### House qualities

- Lead with a concrete event, object, place, time, or human consequence.
- Prefer exact nouns and active verbs to decorative adjectives.
- Let mystery come from selection and pacing, not from vague claims.
- Use short declarative sentences around longer reported passages.
- Keep the emotional temperature low: melancholy and warmth are undertones.
- A dry observation is welcome; punchlines, memes, and theatrical slang are not.
- Contemporary subjects may keep their real vocabulary: AI, API, GitHub, model
  names, software commands, and proper nouns must not be translated into fake
  Victorian euphemisms.
- End on an image, consequence, unresolved detail, or editorial observation —
  not a sales CTA.

### Chinese voice

- Use clear modern Chinese with the cadence of an edited newspaper column.
- Prefer `本报讯——` only for reports; do not begin every essay with it.
- Avoid overusing `据悉`, `震惊`, `重磅`, `史诗级`, `赋能`, `颠覆`, `引爆`,
  `不得不说`, and empty four-character idiom chains.
- Use full-width Chinese punctuation in Chinese prose. Keep product and person
  names in their official form.
- A bilingual deck should translate the idea naturally, not mechanically mirror
  every word of the headline.

### English voice

- Use contemporary, literate British editorial English; archaic words such as
  `whilst`, `thereupon`, and `most curious` are accents, not a default dialect.
- Prefer sentence case for long headlines. All caps is reserved for mastheads,
  short kickers, labels, telegrams, and brief poster language.
- Avoid clickbait formulas, breathless superlatives, marketing jargon, and
  imitation of The New York Times wording or brand identity.

### Headline system

Use this hierarchy:

1. **Kicker** — section/place/date; 2–8 words or a short Chinese label.
2. **Headline** — one claim or image; concrete, compact, no terminal full stop.
3. **Deck** — adds context, consequence, or tension; never repeats the headline.
4. **Lead** — answers what happened and why the reader should continue.
5. **Body** — evidence, chronology, detail, counterpoint, consequence.
6. **Close** — a resonant factual detail or measured observation.

Useful headline patterns:

- Event + consequence: `最后一盏煤气灯熄灭，街角仍有人等候`
- Object + discovery: `A Ledger Found Beneath the Floorboards`
- Place + change: `雾中的车站换了新的时刻表`
- Quiet contrast: `The Machine Shipped at Midnight; the City Slept On`

Do not stack more than one colon, dash, or question in a headline. Do not use an
ellipsis as a substitute for a point of view.

## 5 · Article structures and copy budgets

Write to the template's physical capacity. These are practical targets, not a
reason to pad weak material.

| Template | Use | Copy target |
|----------|-----|-------------|
| `quote` | one durable line, excerpt, aphorism | quote 12–40 Chinese chars or 8–28 English words; byline 2–6 words |
| `clip` | short report, launch note, mini essay | headline 8–24 Chinese chars / 4–12 English words; deck 16–50 chars / 8–22 words; body 180–360 Chinese chars / 120–240 words |
| `paper` | full article or TTRPG front page | headline 8–22 Chinese chars / 4–11 words; deck 18–60 chars / 8–24 words; main body 450–750 Chinese chars / 300–520 words; each brief 60–130 chars; ad 30–80 chars |
| `wanted` | fictional accusation or character card | name 1 line; crime 20–80 chars; reward 1 short line |
| `tele` | urgent announcement or status | 12–38 English words or 20–65 Chinese chars; maximum 4 clauses |

For a `paper` article, draft in this order:

1. headline and deck;
2. lead paragraph containing the central event;
3. two to four paragraphs of evidence/scene/context;
4. one closing detail;
5. two briefs that enrich the world without repeating the lead;
6. one classified ad that acts as atmosphere or a subtle secondary clue.

For factual work, briefs and classified ads must also be factual or clearly
labelled editorial/fictional. Never hide invented claims in secondary furniture.

## 6 · Typography — role, language, and fallback

All editorial text remains **live text until export**. Never bake a headline,
body paragraph, source, date, or byline into generated artwork.

| Role | Required face / stack | Rules |
|------|-----------------------|-------|
| Latin masthead | `Lamplighter Display` via `var(--masthead)` | Brand-sized display use only; usually one line |
| English headline | `Lamplighter Display` via `var(--display-en)` | Default strong newspaper cut |
| Chinese headline | `Huiwen-mincho`, `Noto Serif SC`, `Songti SC`, serif | Never imitate Blackletter with Chinese glyphs |
| Mixed headline | Lamplighter first, then Huiwen/Noto fallback | Each script keeps its natural glyph design |
| English body | `Sorts Mill Goudy`, Georgia, serif | Calm readable prose, never Lamplighter |
| Chinese body | `Noto Serif SC`, `Songti SC`, `SimSun`, serif | Preserve dense newspaper rhythm without crowding |
| Labels/telegraph | `Special Elite`, `Courier New`, mono | Short metadata and telegrams only |

### Headline font selector

- `lamplighter` — default for English or mixed titles; strongest house identity.
- `mincho` — default for Chinese-first titles; also suitable for sober literary
  or historical Chinese material.
- `classic` — use for quieter English essays, quotations, or bookish material.

### Typesetting rules

- `Lamplighter Display` covers Latin uppercase/lowercase, numerals,
  punctuation, and Western European text. Do not assume it contains CJK.
- Masthead wording is editable; `The Lamplighter` is only the house default.
- Long mastheads must remain on one line and use the generator's automatic size
  reduction. Do not manually squeeze with negative tracking or CSS transforms.
- Article headlines may wrap into two or three balanced lines. Rewrite before
  reducing them to an unreadable size.
- English short labels may use small caps or uppercase with modest tracking.
  Do not put long English paragraphs in all caps.
- English headline + Chinese deck: Chinese is smaller and steadier. Chinese
  headline + English deck follows the same supporting hierarchy.
- Keep letter-spacing at `0` for editorial headlines and body unless a component
  already defines restrained spacing for a short label.
- Use old-style figures where supported, drop caps only on article leads, and
  column rules only between real reading columns.
- Before any PNG export, wait for `document.fonts.ready`; preview and export must
  use the same computed font stack.
- Never replace the WebFont with an alphabet specimen image.

The house face is `assets/fonts/lamplighter-display.woff2`, a modified
semi-condensed display cut derived from Newsreader ExtraBold under SIL OFL 1.1.
When redistributing it, preserve `assets/fonts/lamplighter-OFL.txt` and do not
claim the Newsreader or New York Times names as this product's identity.

## 7 · Visual system — the press layer

Every output should look **printed, not rendered**, while remaining readable.
Carry at least three material cues:

- coarse, visible halftone dots on images or selected large fills;
- uneven letterpress/screen-print ink coverage;
- cool grey or cream newsprint grain and local paper wear;
- localized ink bleed at dark edges;
- one restrained accent pass offset roughly 1–2 px;
- occasional fold, edge, or show-through marks.

The counterweight is a strict grid: strong hierarchy, generous negative space,
clear reading order, straight rules, and centered or deliberately asymmetric
composition. Rough material plus disciplined typography is the style.

### Gaslight day edition (default)

`paper #E9E3D3 · ink #2C2924 · deep #1E1C17 · burgundy #8E2F27 ·
brass #A8842C · muted #5C574A · rule #8F8975`

Mood: quiet, mysterious, melancholy but warm. Use fog, rain, gaslight, Victorian
brick, stations, ledgers, typewriters, pocket watches, maps, and restrained
architectural engraving only when they serve the story.

### Gaslight night edition

Use for genuinely nocturnal, archival, or sombre pieces. It is a print shop
after hours, not a generic dark UI. Preserve paper/ink contrast.

### Vapor edition

Muted lavender, cyan, and magenta screen-printed on old paper. It may borrow
1990s motifs, but must look printed rather than glowing.

### Prohibited visual shortcuts

No generic sepia overlay, neon, cyberpunk, Y2K, glossy 3D, plastic, glassmorphism,
purple-blue SaaS gradients, giant rounded cards, uniform noise over the whole
page, steampunk clutter, Soviet emblems, red-star/wheat-wreath marks, illegible
darkness, or clean-vector perfection.

## 8 · Artwork and image-generation boundary

The current generator is deliberately text-led. A finished newspaper **image**
means the composed newspaper exported as PNG; it does not require a generated
illustration. Do not add decorative artwork simply to prove an image tool was
used.

When the story genuinely benefits from an illustration or paper asset:

1. Decide the narrative job: evidence photo, architecture, object study,
   advert, or background paper — never “vintage decoration”.
2. Generate only the raster artwork. Do not include words, headlines, captions,
   dates, logos, UI, borders, or page layout in the generated bitmap.
3. Keep the subject recognizable and leave negative space for live type.
4. Apply the prompt skeleton in `references/image-prompts.md`, including coarse
   halftone, low-fidelity newsprint, local ink bleed, slight misregistration,
   cool grey paper, charcoal ink, and a restrained burgundy accent.
5. Reject fake letters, illegible faces, modern objects in historical fiction,
   glossy gradients, uniform sepia, and over-dark crops.
6. Save reusable paper textures as `assets/paper.jpg` or a scoped override:
   `assets/paper-quote.jpg`, `paper-clip.jpg`, `paper-paper.jpg`,
   `paper-wanted.jpg`, `paper-tele.jpg`, `paper-night.jpg`, or
   `paper-vapor.jpg`.
7. Reopen the generator and verify that the asset supports, rather than reduces,
   text contrast. The live layout always owns the words.

Base prompt skeleton:

```text
interwar British newspaper illustration, 1920s–1930s London, [specific subject],
coarse visible halftone dots, letterpress ink, low-fidelity raw newsprint,
localized ink bleed, slight misregistration, architectural engraving or press
photograph, cool gray paper, charcoal black ink, restrained burgundy accent,
quiet film-noir atmosphere, highly legible subject, generous negative space,
no words, no headline, no caption, no logo, no modern digital gloss
```

## 9 · Template field map

Drive `index.html` through its real controls. Template tabs use `data-id`; text
controls use `data-k`; the font selector is `#headline-font`; theme is `#theme`;
size is `#size`; export is `#print`; composed output is `#stage`.

| Template `data-id` | Required `data-k` fields |
|--------------------|--------------------------|
| `quote` | `mast`, `q`, `by`, `date` |
| `clip` | `kicker`, `head`, `deck`, `body` |
| `paper` | `mast`, `date`, `head`, `deck`, `body`, `brief1h`, `brief1`, `brief2h`, `brief2`, `ad` |
| `wanted` | `name`, `crime`, `reward`, `apply` |
| `tele` | `msg`, `from`, `date` |

Default sizes:

- `quote`: 1080×1440; alternatives 1080×1080 and 1280×720.
- `clip`: 860 px wide, automatic height.
- `paper`: 1240×1754 A4; alternative 1080×1440.
- `wanted`: 1080×1440.
- `tele`: 1280×720; alternative 1200×900.

## 10 · End-to-end article → PNG workflow

Follow every stage. Do not stop after writing copy or after opening the preview.

### A. Prepare the edition

1. Parse the request with §2 and decide truth mode.
2. Research/verify if §3 requires it; retain source URLs outside the artwork.
3. Choose one template and one output size based on §5 and §9.
4. Draft headline, deck, article, secondary furniture, date, and byline.
5. Edit once for facts and once for house voice. Remove unsupported claims,
   repeated ideas, clickbait, and pseudo-Victorian clutter.
6. Count against the template budget. Shorten the writing before shrinking type.

### B. Start the press

From the repository root:

```sh
python3 -m http.server 8642 --bind 127.0.0.1
```

Open `http://127.0.0.1:8642/index.html` in a browser. Do not open the HTML as a
`file://` URL because font and export behaviour must be tested over HTTP.

### C. Compose the page

1. Select the template tab by its `data-id`.
2. Fill every relevant `data-k` field with the final edited copy.
3. Select the headline font according to §6.
4. Select theme and output size. Use day edition unless the story justifies a
   different ink treatment.
5. Wait for `document.fonts.ready` and for any paper image to finish loading.
6. Inspect `#stage` at full size, not only its scaled panel preview.

For a URL-driven quote card, the supported shortcut is:

```text
templates/quote-card.html?mast=The%20Lamplighter&q=...&by=...&theme=night
```

URL-encode all values. The main generator is preferred for other templates.

### D. Preflight

Check all of the following before export:

- headline, names, dates, numbers, quotations, and proper nouns match the copy;
- no placeholder text remains;
- CJK and Latin both render with the intended fallback and no tofu boxes;
- masthead is one line; headline wraps intentionally with no orphaned word;
- no text is clipped, overlapped, hidden under texture, or outside `#stage`;
- article columns have a clear reading order and an acceptable final line;
- illustration contains no generated fake text;
- theme retains sufficient contrast and at least three physical print cues;
- the result resembles a private British newspaper, not a generic retro poster.

If content overflows, fix it in this order: tighten the copy → improve line
breaks → select a larger template → only then make a restrained size adjustment.
Never solve overflow by scaling the entire page into unreadability.

### E. Export

Click `#print`. The generator waits for fonts and calls:

```js
htmlToImage.toPng(document.querySelector('#stage'), { pixelRatio: 2 })
```

The downloaded filename begins `lamplighter-<template>-`. Keep that PNG as the
master export. For an agent-managed delivery, place files under:

```text
output/<yyyy-mm-dd>-<short-slug>/
  <short-slug>.png
  <short-slug>.md
  sources.md          # factual pieces only
```

The Markdown file contains the exact final headline, deck, body, secondary copy,
template, theme, font choice, and image dimensions. Do not discard the editable
copy after producing the bitmap.

### F. Verify the exported file

Reopen the PNG and verify:

- it is a valid non-empty PNG at the intended pixel dimensions;
- crop boundaries and rough edges are intact;
- fonts match the browser preview;
- all text is readable at 100% and at a social-feed thumbnail size;
- no browser chrome, control panel, focus ring, or loading state appears;
- factual source notes exist beside the deliverable when required.

If the PNG differs from preview, wait again for fonts and textures, repaint the
stage, and re-export. If the browser blocks a download, capture **only** `#stage`
at its intrinsic dimensions; never use a full-window screenshot as the final.

## 11 · Delivery contract

Return the outcome, not a design lecture. A complete handoff contains:

1. the finished PNG as a directly accessible file;
2. the editable copy or Markdown source;
3. one sentence naming template, theme, headline face, and dimensions;
4. source links for factual articles, or a clear `fictional prop` label;
5. any assumption that materially shaped the article.

Do not claim completion if only the copy, preview, or font specimen exists.

## 12 · Final acceptance checklist

- [ ] Truth mode is explicit; factual claims and quotes are supported.
- [ ] Copy sounds like an editor/observer, not marketing or costume parody.
- [ ] Headline, deck, lead, body, and close have distinct jobs.
- [ ] Copy fits the selected template without microscopic text.
- [ ] Masthead and article title remain independently editable live text.
- [ ] Correct Lamplighter/Huiwen/Goudy role and CJK fallback are visible.
- [ ] At least three local print-material cues are present.
- [ ] Grid, hierarchy, whitespace, and reading order remain disciplined.
- [ ] Generated artwork, if any, contains no required editorial text.
- [ ] `document.fonts.ready` and asset loading completed before export.
- [ ] Exported PNG was reopened and checked at full and thumbnail scale.
- [ ] Editable copy and sources/fiction label accompany the final image.
