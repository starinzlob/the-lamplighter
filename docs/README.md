# docs/ — README 样张图

README 引用以下四张图，用生成器「开印」导出后按名字放进来即可：

| 文件名 | 模板 | 主题 | 尺寸 | 状态 |
|--------|------|------|------|------|
| specimen-broadsheet.png | 整版报纸·跑团道具 | 日版 | A4 1240×1754 | 默认赛尔湾失踪案 |
| specimen-wanted.png | 通缉令 | 日版 | 3:4 | ✅ |
| specimen-clip.png | 报纸剪报 | 日版 | 860×自适应 | ✅ |
| specimen-quote-vapor.png | 金句卡 | 蒸汽波错版 | 3:4 | ✅ |

导出的 PNG 是 2× 高清，提交前先压一遍，README 加载会快很多：

```bash
cd docs && for f in specimen-*.png; do sips -Z 1400 "$f"; done
```
