# 纸张纹理 Paper textures

按文件名对号入座，缺失自动回退：`paper-<名字>.jpg` → `paper.jpg`（全局兜底）→ 纯色。

| 文件名 | 用在哪 | 混合模式 |
|--------|--------|----------|
| paper-quote.jpg  | 金句卡 | multiply |
| paper-clip.jpg   | 报纸剪报 | multiply |
| paper-paper.jpg  | 整版报纸·跑团道具 | multiply |
| paper-wanted.jpg | 通缉令 | multiply |
| paper-tele.jpg   | 电报 | multiply |
| paper-night.jpg  | 煤气灯夜版（所有模板） | soft-light |
| paper-vapor.jpg  | 蒸汽波错版（所有模板） | multiply |
| paper.jpg        | 以上任何一张缺失时的兜底 | 随主题 |

要求：≥1600×2200、画面无任何文字、亮度均匀、无明显暗角。
夜版那张要**中间调灰棕**（不要纯黑），系统会用 soft-light 自动压成夜色。

## 字体 Fonts

- `fonts/lamplighter-display.woff2`：英文报头和可变文章标题，覆盖拉丁大小写、数字及常用标点。
- `fonts/huiwen-*.woff2`：中文标题与正文回退，按 Unicode 区间分块加载。
- `fonts/lamplighter-OFL.txt`：Lamplighter Display 与其 Newsreader 上游的 SIL OFL 1.1 许可。

报头和标题必须保留为真实文字。不要把标题烘焙进背景图；用户换字时由浏览器按 `Lamplighter → Huiwen → Noto Serif SC → Georgia` 的顺序自动选取可用字形。
