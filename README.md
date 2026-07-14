# The Old Press · 老报纸卡片生成器

**把任何文字印成 1926 年的样子。** 金句卡、报纸剪报、通缉令、电报——复古印刷质感，支持中文，纯前端零后端，免费无水印。

Print anything as if it came off a hundred-year-old London press: quote cards, spoof newspaper clippings, wanted posters, telegrams. Pure front-end, CJK-friendly, free, no watermark.

> 2026 年了，fodey.com 该有个会中文的继任者了。

## 用法 Usage

打开网页（或本地任何静态服务器跑仓库根目录）→ 选印刷品种类 → 填字 → 选墨水主题（日版 / 煤气灯夜版 / 蒸汽波错版）→ 开印，导出 2× 高清 PNG。

```bash
# 本地跑
python3 -m http.server 8642
# → http://localhost:8642
```

## 四种印刷品

| 模板 | 用途 | 尺寸 |
|------|------|------|
| **金句卡** | 小红书 / X 分享卡，报纸头版排面 | 3:4 · 1:1 · 16:9 |
| **报纸剪报** | 梗图、跑团道具、生日贺报——撕边、首字下沉、双栏 | 860×自适应 |
| **通缉令** | 表情包、活动海报、朋友的"罪行" | 3:4 |
| **电报** | 发布公告、changelog、全大写 STOP 句读 | 16:9 · 4:3 |

## 同时是一个 agent skill

仓库自带 [SKILL.md](SKILL.md)——装进 Claude Code 等 agent 后，一句"帮我把这句话印成老报纸"就能出图，agent 还能套用整套 **Old London Editorial Noir** 风格体系写 UI 和生图 prompt：恒定的印刷基底层（halftone / letterpress / 套印偏移）+ 可换的墨水主题层。

```bash
npx skills add <this-repo-url>
```

```
SKILL.md                     风格规则 + 印刷品工单（agent 入口）
index.html                   卡片生成器本体（纯前端）
references/tokens.css        设计令牌（日/夜/蒸汽波 + 稀有度墨色）
references/textures.css      CSS 配方：网点、纸纹、套印偏移、铅字按钮
references/image-prompts.md  生图提示词 + 主题限定 negative prompt
templates/quote-card.html    URL 参数驱动的无 JS 金句卡（agent 友好）
demo/index.html              风格样张页
```

## 铁律

**印品必须经得起复印机的考验**——不靠渐变，不靠辉光，只靠网点、油墨与留白。

## License

MIT
