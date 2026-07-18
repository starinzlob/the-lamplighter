# docs/ — README 样张图 / README specimens

[中文](#中文) · [English](#english)

## 中文

主 README 引用以下四张图片。使用生成器的「开印」功能导出后，按对应文件名放入这个目录：

| 文件名 | 模板 | 主题 | 尺寸 | 状态 |
|--------|------|------|------|------|
| specimen-broadsheet.png | 整版报纸·跑团道具 | 日版 | A4 1240×1754 | 默认赛尔湾失踪案 |
| specimen-wanted.png | 通缉令 | 日版 | 3:4 | ✅ |
| specimen-clip.png | 报纸剪报 | 日版 | 860×自适应 | ✅ |
| specimen-quote-vapor.png | 金句卡 | 蒸汽波错版 | 3:4 | ✅ |

导出的 PNG 是 2× 高清图片。提交前先压缩一遍，README 加载会快很多：

```bash
cd docs && for f in specimen-*.png; do sips -Z 1400 "$f"; done
```

---

## English

The main README uses the following four images. Export them with the generator’s **开印 · PRINT** action, then place them in this directory under the matching filenames:

| Filename | Template | Theme | Size | Status |
|--------|------|------|------|------|
| specimen-broadsheet.png | Full broadsheet · tabletop prop | Daylight | A4 1240×1754 | Default Sayer Bay disappearance case |
| specimen-wanted.png | Wanted poster | Daylight | 3:4 | ✅ |
| specimen-clip.png | Newspaper clipping | Daylight | 860×adaptive | ✅ |
| specimen-quote-vapor.png | Quote card | Vapor misprint | 3:4 | ✅ |

Exported PNGs are rendered at 2× resolution. Compress them before committing so the README loads faster:

```bash
cd docs && for f in specimen-*.png; do sips -Z 1400 "$f"; done
```
