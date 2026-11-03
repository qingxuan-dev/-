# 量子力学推理语料 v0.1

> **独立数据集**：与本仓库的 Collatz 笔记、经济推理语料互不相关，单独存放于此目录。

| 项 | 内容 |
|---|---|
| 名称 | 量子力学推理语料（Quantum Mechanics Reasoning Corpus） |
| 版本 | v0.1 |
| 来源 | Ruolin 2026-11-03 的提问，及 Claude 据此整理的《量子力学笔记：从你的问题出发》 |
| 整理 | Claude 把笔记扩写为训练语料格式，并用网络搜索核对关键事实（2026-11-03） |
| 语言 | 简体中文 |
| 条目数 | 22（QM-01 至 QM-22），另附 10 条纠错记录 |
| 许可 | 未指定（公开发布前请由作者确认） |

## 文件

| 文件 | 说明 |
|---|---|
| `quantum-mechanics-notes-original.md` | 原始笔记，逐字保存，未修改 |
| `qm-reasoning-corpus-v0.1.jsonl` | 训练用语料，每行一条 |
| `qm-reasoning-corpus-v0.1.md` | 同一内容的可读版，含纠错记录 |
| `qm-reasoning-corpus-v0.1.en.jsonl` | 英文版（Claude 翻译），字段相同；type、credibility、status 用英文值 |
| `qm-reasoning-corpus-v0.1.en.md` | 英文可读版，含纠错记录 |
| `qm-corpus.html` | 可视化页面：科普小计算 + 语料浏览 + 使用说明；右上角可切换中文 / English |

## 字段

`id`, `title`, `domains`, `difficulty`(1–5), `type`(概念/纠错/计算/事实/前沿/有争议/学习),
`credibility`(已确立/前沿/推测/建议), `user_intuition`, `verdict`, `question`, `reasoning_chain`(string[]),
`answer`, `key_facts`([{text, status, source, url?}]), `common_errors`, `check`。

核对状态：`已核对` 本次用搜索核对并附链接（7 处）；`常识` 教科书或广为人知，未逐条重查（23 处）；`待核对` 0 处。

## 相对原笔记的修正

1. 重子–光子比：原文“每十亿个光子几个重子”，实为 η ≈ 6.1×10⁻¹⁰，约每 100 亿个光子 6 个重子。
2. GRW 与引力无关；与引力相关的是 Diósi–Penrose 模型（2020 年格兰萨索实验已排除其无参数版本）。
3. 湮灭产生两个 511 keV 光子仅适用于自旋单态；三重态正电子素产生三个光子。
4. 狄拉克 1930 年空穴理论曾把空穴当作质子，1931 年才提出反电子。
5. 位置、动量是无穷维、连续谱的算符，不只是“矩阵”。
6. 中性粒子（光子、π⁰）可以是自身的反粒子。

## 已核对来源

- ALPHA-g, Nature 621, 716 (2023) — https://news.berkeley.edu/2023/09/27/antimatter-embraces-earth-falling-downward-like-normal-matter/
- BASE, Nature 601, 53 (2022) — https://cerncourier.com/a/base-breaks-new-ground-in-matter-antimatter-tests/
- η (Planck 2018) — https://arxiv.org/abs/1912.01132
- LHCb 重子 CP 破坏, Nature 643, 1223 (2025) — https://home.cern/news/news/physics/new-piece-matter-antimatter-puzzle
- Moreva et al., PRA 89, 052122 (2014) — https://arxiv.org/abs/1310.4691
- GW170817, ApJL 848, L13 (2017) — https://arxiv.org/abs/1710.05834
- Diósi–Penrose 格兰萨索检验 (2020) — https://physicsworld.com/a/physicists-place-fresh-limits-on-gravitys-role-in-wavefunction-collapse/
