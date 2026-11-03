# 经济与制度推理语料 v0.1

> **独立数据集**：与本仓库中的 Collatz / Syracuse 数学笔记无关，单独存放于此目录。

| 项 | 内容 |
|---|---|
| 名称 | 经济与制度推理语料（Economic & Institutional Reasoning Corpus） |
| 版本 | v0.1 |
| 来源 | Ruolin 与 Claude 的对话（2026-11-03），由 Claude 整理成训练语料格式 |
| 语言 | 简体中文 |
| 条目数 | 16（ECON-01 至 ECON-16），另附 4 条纠错记录 |
| 用途 | 推理型问答语料：问题 → 推理链 → 答案 → 关键事实 → 常见错误 |
| 许可 | 未指定（使用或公开前请由作者确认） |

## 文件

| 文件 | 说明 |
|---|---|
| `econ-dialogue-corpus-v0.1.md` | 原始文本，逐字保存，未做任何修改 |
| `econ-dialogue-corpus-v0.1.jsonl` | 由原文解析得到的机器可读版本，每行一条 |
| `econ-dialogue-corpus-v0.1.en.jsonl` | 英文版（Claude 翻译），字段相同；立场与核对状态用英文值 fact/mechanism/contested、checked/common/to verify |
| `econ-corpus.html` | 可视化浏览页面（筛选、搜索、展开推理链），含审读注；右上角可切换中文 / English |

## JSONL 字段

`id`, `title`, `domains`（数组）, `difficulty`（1–5）, `stance`, `stance_tags`（事实/机制/有争议）,
`question`, `reasoning_chain`（`[{step, sub?}]`）, `answer`, `key_facts`（`[{text, status}]`）, `common_errors`。
纠错记录只在原文和 HTML 中，不在 JSONL 里。

## 概况

- 难度：2 级 6 条，3 级 6 条，4 级 4 条；没有 1 级和 5 级。
- 立场：事实 8，机制 11，有争议 3（可多选）。
- 关键事实核对状态：已核对 8，常识 19，待核对 2（共 29 处标记）。

## 审读注（整理时添加，不属于语料本身）

- **ECON-01** 第 3 步"全球理工科硕博有几百万"很可能低估了一个数量级，建议标为待核对。
- **ECON-08** 答案写了"仍有争议"，立场建议改为"机制 + 有争议"。
- **ECON-09** 第 4 步：只有偿还银行贷款才注销存款；建议写成"对银行的净还款额"。
- **ECON-13** 第 2 步容易读成单一因果链，建议改为"时间上相继发生"。
- **ECON-14** 第 4 步：增速高于利率时，债务率下降还需要基本赤字足够小。
- 字段缺失：ECON-07、ECON-14 无"关键事实"；ECON-13、15、16 无"常见错误"。
- 待核对：ECON-15 适用条件；ECON-16 中 AI 占风投 64%。
