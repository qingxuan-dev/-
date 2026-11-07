# 雪融之夏（第一至十七章）

> 独立内容：小说，与仓库里的数学笔记和训练语料无关。

| 文件 | 用途 |
|---|---|
| `xuerong-zhixia-ch1-6.original.md`、`…-ch7.original.md`、`…-ch8.original.md` 至 `…-ch17.original.md` | 原稿，逐字保存，未修改（每批新章节一个文件） |
| `reader.html` | 在线阅读页（发布为 claude.ai 页面）：目录、分章阅读、字号与背景（白 / 护眼 / 夜间）、记住阅读位置、中文 / English 切换 |
| `en/ch1.md` … `en/ch17.md` | 英文译稿（Claude 翻译），与原稿逐段对应；书名 *Snowmelt Summer* |
| `dist/snowmelt-summer.en.epub` | 英文电子书 |
| `dist/xuerong-zhixia.epub` | 电子书，可导入 Apple 图书、微信读书、掌阅、多看等阅读 App |
| `dist/xuerong-zhixia.docx` | Word 版：宋体小四、首行缩进两字、1.5 倍行距、每章另起一页 |
| `dist/xuerong-zhixia.md` | 排版用的中间稿（直引号已换成中文引号） |
| `dist/cover.png` | 电子书封面 |
| `blurbs.json` | 目录页的简介、每章一句钩子、人物一句话（中英文），改这里即可 |
| `art/` | 六个人物头像（从提供的角色图裁出，去掉了图里的文字） |
| `build.py`、`reader-template.html`、`epub.css` | 生成以上文件的脚本和模板 |

## 排版上唯一的改动

原稿里的英文直引号 `"…"`、`'…'` 换成了中文引号 `“…”`、`‘…’`（每行内成对替换，已核对全部成对）。其余文字与原稿逐字一致：构建后比对过，去掉引号后的全文完全相同。

作者确认过的改动：第十一章“四年了”改为“两年了”（初二造缸到高一冬天，时间线对齐），英文版同步。第十三章按作者要求润色了几处过短、停顿太多的对话（共 11 处，只改说话，不改情节），作者交来的原样保存在 `submitted/xuerong-zhixia-ch13.submitted.md`，可以直接比对。第十四章按作者确认改了四处：“能量不守恒”→“动能不守恒”，叶知夏说的“那缸红龙”→“那缸金龙鱼”，苏棠“上次在店里”→“听说…上次在店里”（她当时不在场），并补了一句网课晚自习没人管；原样见 `submitted/xuerong-zhixia-ch14.submitted.md`。第十五章按作者确认改了两处：“旧冰箱”→“小冰箱”（第十四章送去的是新冰箱），“去年秋天”→“去年冬天”（第十一章交报告时已下雪）；第十一章补了一段公司也接饭店、超市等定做软件的活，为第十五章的 B 端业务铺垫。第十六章按作者确认把“二月最后那几天”改为“三月中旬”（时间线）。第十七章按作者意思改了两处：叶知行“不是不会写代码，是会的那几样不对路”（会 Python、C++，不会写游戏）；陈曦说出酵素的事时交代是顾雪融私聊告诉他的。第一至七章按作者要求做了一轮对话润色（10 处）并修正第二章补课的数学比喻（题目开口朝上，原来的抛球比喻是开口朝下，改成翠鸟扎水），改前的版本存在 `submitted/` 里的 `before-dialogue-pass` 文件。第八至十四章随后也做了一轮（53 处，主要是删减“没说话 / 看了很久 / 停了一下”这类重复节拍，换成具体动作或一句废话），对照见 `submitted/dialogue-pass-ch8-14.md`，第一至七章的对照见 `submitted/dialogue-pass-ch1-7.md`。

## 加新章节

把新章节按同样格式（`# 第十八章　标题`、`## 一、小节`）存成新文件 `xuerong-zhixia-ch18.original.md`（文件名里的数字是这批第一章的章号），在 `blurbs.json` 里给新章加一句钩子，然后运行：

```
python3 build.py
```

阅读页、电子书和 Word 会一起更新。需要已安装 pandoc 和 python-docx。

英文版：每章一个文件 `en/chN.md`，必须和原稿逐段对应（章、小节、段落数都相同），构建时会自动核对，对不上就停止并指出哪一节。还没翻译的新章节在英文目录里显示为 “Translation coming”。

译名：叶知行 Ye Zhixing，顾雪融 Gu Xuerong，叶知夏 Ye Zhixia，何叔 Uncle He，陈叔 Uncle Chen，梅姐 Sister Mei，苏棠 Su Tang，林小满 Lin Xiaoman，陈曦 Chen Xi，王教官 Instructor Wang，老周 Old Zhou，孙老师 Mr. Sun，顾建国 Gu Jianguo，阿彪 Abiao，竹竿 Beanpole，胖子 Chubby，吴老师 Mr. Wu，郑欣 Zheng Xin（Ms. Zheng），阿姨 Auntie，融融 Rongrong；猫：年糕 Rice Cake，煤球 Briquette，三花 Calico，拖把 Mop，殿下 Your Highness，蓝白 Blue-and-White；游戏《噩梦侵袭》Nightmare Raid，账号“冬眠” Hibernation；叶仕龙 Ye Shilong，市长 the mayor，刘总 Mr. Liu，马总 Mr. Ma，小程序“城里事” Town Matters，北城片区 the North City Area；周叔 Uncle Zhou；锯缘青蟹 mud crab，黑魔神 Black Devil（snakehead），红龙 red arowana；甜甜 Tiantian，钟南山 Zhong Nanshan，顾同学 Miss Gu；李老师 Ms. Li，群“后街有猫” Back Street Cats，蟹公寓 crab apartment，钉钉 DingTalk；苏宇 Su Yu，苏磊 Su Lei，大刘 Big Liu，晓雯 Xiaowen，《年糕减肥》Rice Cake’s Diet，酵素 enzyme drink；冬眠的游戏内聊天写成 `**<冬眠> ……**`（单独一行），阅读页按消息样式显示；黄英俊 Huang Yingjun（竹竿本名），王警官 Officer Wang，马主任 Director Ma，曦神 Xi the Great，犯罪记录 Criminal Record。
