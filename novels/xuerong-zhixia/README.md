# 雪融之夏（第一至六章）

> 独立内容：小说，与仓库里的数学笔记和训练语料无关。

| 文件 | 用途 |
|---|---|
| `xuerong-zhixia-ch1-6.original.md` | 原稿，逐字保存，未修改 |
| `reader.html` | 在线阅读页（发布为 claude.ai 页面）：目录、分章阅读、字号与背景（白 / 护眼 / 夜间）、记住阅读位置 |
| `dist/xuerong-zhixia.epub` | 电子书，可导入 Apple 图书、微信读书、掌阅、多看等阅读 App |
| `dist/xuerong-zhixia.docx` | Word 版：宋体小四、首行缩进两字、1.5 倍行距、每章另起一页 |
| `dist/xuerong-zhixia.md` | 排版用的中间稿（直引号已换成中文引号） |
| `dist/cover.png` | 电子书封面 |
| `build.py`、`reader-template.html`、`epub.css` | 生成以上文件的脚本和模板 |

## 排版上唯一的改动

原稿里的英文直引号 `"…"`、`'…'` 换成了中文引号 `“…”`、`‘…’`（每行内成对替换，已核对全部成对）。其余文字与原稿逐字一致：构建后比对过，去掉引号后的全文完全相同。

## 加新章节

把新章节按同样格式（`# 第七章　标题`、`## 一、小节`）接在原稿末尾，或把 `build.py` 里的 `SRC` 指向新文件，然后运行：

```
python3 build.py
```

阅读页、电子书和 Word 会一起更新。需要已安装 pandoc 和 python-docx。
