# 纸张纹理 / Paper textures

[中文](#中文) · [English](#english)

## 中文

按文件名匹配纹理；缺失时依次回退：`paper-<名字>.jpg` → `paper.jpg`（全局兜底）→ 纯色。

| 文件名 | 用在哪 | 混合模式 |
|--------|--------|----------|
| paper-quote.jpg | 金句卡 | multiply |
| paper-clip.jpg | 报纸剪报 | multiply |
| paper-paper.jpg | 整版报纸·跑团道具 | multiply |
| paper-wanted.jpg | 通缉令 | multiply |
| paper-tele.jpg | 电报 | multiply |
| paper-night.jpg | 煤气灯夜版（所有模板） | soft-light |
| paper-vapor.jpg | 蒸汽波错版（所有模板） | multiply |
| paper.jpg | 以上任何一张缺失时的兜底 | 随主题 |

要求：至少 1600×2200、画面无任何文字、亮度均匀、无明显暗角。

夜版纹理应为**中间调灰棕色**，不要使用纯黑；系统会通过 soft-light 自动压成夜色。

### 字体

- `fonts/lamplighter-display.woff2`：英文报头和可变文章标题，覆盖拉丁大小写、数字及常用标点。
- `fonts/huiwen-*.woff2`：中文标题与正文回退，按 Unicode 区间分块加载。
- `fonts/lamplighter-OFL.txt`：Lamplighter Display 与其 Newsreader 上游的 SIL OFL 1.1 许可。

报头和标题必须保留为真实文字。不要把标题烘焙进背景图；用户修改文字时，浏览器会按 `Lamplighter → Huiwen → Noto Serif SC → Georgia` 的顺序自动选择可用字形。

---

## English

Textures are matched by filename. Missing files fall back in this order: `paper-<name>.jpg` → `paper.jpg` (global fallback) → a flat color.

| Filename | Used for | Blend mode |
|--------|--------|----------|
| paper-quote.jpg | Quote card | multiply |
| paper-clip.jpg | Newspaper clipping | multiply |
| paper-paper.jpg | Full broadsheet · tabletop prop | multiply |
| paper-wanted.jpg | Wanted poster | multiply |
| paper-tele.jpg | Telegram | multiply |
| paper-night.jpg | Gaslight night edition, all templates | soft-light |
| paper-vapor.jpg | Vapor misprint, all templates | multiply |
| paper.jpg | Fallback when any texture above is missing | Depends on theme |

Requirements: at least 1600×2200, no text in the image, even brightness, and no obvious vignette.

The night-edition texture should use a **mid-tone gray-brown**, not pure black. The system darkens it automatically with soft-light blending.

### Fonts

- `fonts/lamplighter-display.woff2`: English masthead and variable article headlines; covers Latin uppercase and lowercase, numbers, and common punctuation.
- `fonts/huiwen-*.woff2`: Chinese headline and body fallback, loaded in Unicode-range chunks.
- `fonts/lamplighter-OFL.txt`: SIL OFL 1.1 license for Lamplighter Display and its Newsreader upstream.

Mastheads and headlines must remain live text. Do not bake titles into background images; when the user edits copy, the browser selects available glyphs in this order: `Lamplighter → Huiwen → Noto Serif SC → Georgia`.
