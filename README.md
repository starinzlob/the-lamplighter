# The Lamplighter · 点灯人报纸生成器

**把任何文字印成 1926 年的样子。** 金句卡、报纸剪报、通缉令、电报——复古印刷质感，支持中文，纯前端零后端，免费无水印。

Print anything as if it came off a hundred-year-old London press: quote cards, newspaper clippings, wanted posters, and telegrams. Pure front-end, CJK-friendly, free, no watermark.

> 2026 年了，fodey.com 该有个会中文的继任者了。

## 用法 Usage

打开网页（或本地任何静态服务器跑仓库根目录）→ 选印刷品种类 → 改报头和标题 → 选择标题铅字 → 选墨水主题（日版 / 煤气灯夜版 / 蒸汽波错版）→ 开印，导出 2× 高清 PNG。

```bash
# 本地跑
python3 -m http.server 8642
# → http://localhost:8642
```

## 四种印刷品

| 模板 | 用途 | 尺寸 |
|------|------|------|
| **金句卡** | 小红书 / X 分享卡，报纸头版排面 | 3:4 · 1:1 · 16:9 |
| **报纸剪报** | 梗图、单条新闻道具、生日贺报——撕边、首字下沉、双栏 | 860×自适应 |
| **整版报纸 · 跑团道具** | 主新闻 + 两条简讯 + 分类广告的完整头版，A4 可打印 | A4 · 3:4 |
| **通缉令** | 表情包、活动海报、朋友的"罪行" | 3:4 |
| **电报** | 发布公告、changelog、全大写 STOP 句读 | 16:9 · 4:3 |

## 给守密人 For Keepers 🐙

整版报纸模板就是为 **CoC（克苏鲁的呼唤）等 1920s 背景跑团**做的：一页塞下主案件 + 两条看似无关的简讯 + 一条不该回应的分类广告——线索和红鲱鱼排在同一个版面上才像真报纸。日期栏有 **🎲 年代骰子**（Arkham / Innsmouth / London / Shanghai × 1920s 随机日期），A4 尺寸导出后直接打印发给玩家。默认填的就是一个可以直接开团的示例：渔村集体失踪案。

## 同时是一个 agent skill

仓库自带 [SKILL.md](SKILL.md)——装进 Codex、Claude Code 等 agent 后，一句"帮我把这句话印成老报纸"就能出图，agent 还能套用整套 **Old London Editorial Noir** 风格体系写 UI 和生图 prompt：恒定的印刷基底层（halftone / letterpress / 套印偏移）+ 可换的墨水主题层。

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
assets/fonts/lamplighter-display.woff2  自托管标题字体（OFL）
scripts/build_lamplighter_font.py       字体构建脚本
```

## 标题和字体

- **报头文字可以修改**：`MASTHEAD` 输入框中的内容始终是可编辑的真实文字，不是图片。
- **文章标题可以修改**：剪报、整版报纸和金句模板会实时重排标题，长标题允许换行。
- **标题字体可以切换**：Lamplighter（默认）、Huiwen（中文优先）、Goudy（英文古典）。
- **字符自动回退**：Lamplighter Display 覆盖完整拉丁大小写、数字和常用标点；中文自动使用汇文明朝体，再回退到 Noto Serif SC。
- **导出仍是确定的**：导出前等待 WebFont 加载，最终 PNG 与预览使用同一字体栈。

`Lamplighter Display` 是基于 Newsreader 72pt ExtraBold 制作的半窄幅标题衍生字体，按 SIL Open Font License 1.1 分发；许可文件见 `assets/fonts/lamplighter-OFL.txt`。

## 铁律

**印品必须经得起复印机的考验**——不靠渐变，不靠辉光，只靠网点、油墨与留白。

## License

代码与模板使用 MIT；`Lamplighter Display` 使用 SIL OFL 1.1。
