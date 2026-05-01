---
name: thesis-workflow
description: 端到端的学术论文工作流。包含博士/硕士中文毕业论文的自动化写作流水线（环境配置、资产提取、分章扩写、PPT生成），以及中文理工科毕业论文写作风格规范与润色规则。提取并融合了小论文的部分核心经验到大论文流程中。
user-invocable: true
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
---

# thesis-workflow: 学术论文端到端工作流与写作规范

本 Skill 旨在打造一个从早期语料加工到最终定稿、生成答辩材料的"端到端"（End-to-End）论文处理助手。既可以作为 **SOP（标准作业程序）** 按步骤执行论文的自动撰写任务，也可以作为 **审查与风格约束器** 对已有中文论文文本进行严厉去 AI 味的改写。

## 适用场景（When to use）

- **从零构建大论文**：你有一堆发表过的小论文 LaTeX 源码，希望把它们拼成一本逻辑通顺的中文大论文。
- **论文正文撰写/改写**：你写了一段文字，觉得不够学术、带有明显 AI 翻译腔，要求改成“像活人写的理工科中文论文”。
- **答辩材料生成**：大论文已完稿，需要自动提取内容制作 Beamer PPT。
- **研究记录梳理**：从小论文源码中抽取公式、数据、伪图表等资产核心，规范化存储。

## 目录库结构 

为了让你方便调用，本地资产按以下四个目录组织：

1. `workflows/`：包含按照阶段划分的自动构建流水线，推荐以 `01 -> 02 -> 03 -> 04` 的顺序运行。
2. `patterns/`：包含对于中文毕业论文强约束的句法、词汇、数学符号、结构等详细排版规则，以及 `meta-rules.md`、`reference-thesis.md` 相关的样式控制。
3. `examples/`：存放英文或中文优秀的小论文结构思路（Abstract, Introduction, Method 等技巧的浓缩）。这些材料作为启发，但在撰写中文大论文时需套用 `patterns` 的语言限制。
4. `agents/`：可选配代理模型相关设定。

---

## 一、自动化写作流水线（Workflows）

当用户希望“跑剧本”或者“从头生成”大论文时，按照这些 SOP 文档里的要求引导或自动执行：

- **阶段 01：[工具与环境准备](./workflows/Skill_01_Environment_Setup.md)**
  初始化 MCP 配置、`uv`、文献引用服务等底层支撑。
- **阶段 02：[资产无损抽取](./workflows/Skill_02_Asset_Extraction.md)**
  从小论文的 `.tex` 源码中抽走核心公式、图片指令、伪代码逻辑，转存为中间产物，保证不丢数学上的严谨性。
- **阶段 03：[章节循环扩写与编译修正](./workflows/Skill_03_Thesis_Drafting.md)** （**核心**）
  结合阶段02获取的资产与论文模板结构，一章一章地滚动扩写。每写完一章就会编译测试错误。此处**必须加载二、写作风格规范**来约束写出来的中文内容。
- **阶段 04：[Beamer 答辩幻灯片生成](./workflows/Skill_04_Presentation_Gen.md)**
  利用成品生成的最终 `.tex` 或结构化数据，倒推浓缩摘要并自动编排带有论文关键图表的答辩 PPT 源码。

---

## 二、中文写作风格严厉约束（Patterns / Polish）

当处于**阶段03**扩写，或者当用户主动要求“润色”、“检查”现有的一段文字时：

这是确保论文“不被人看穿是AI写的”生命线。你**必须同等重视**：

### 核心自测两问
写完/改完后内部默念：
1. **删除测试**：把这句话删掉或者压缩一半，信息量掉了吗？没掉就说明这是AI凑字数的废话，删去。
2. **范例测试**：这种说法会在用户指定的标准博士/硕士论文里出现吗？不会就得重写。

### 规则模块加载
不要在单一会话里加载全部 `patterns/*.md`（耗费 Token 且分散注意力），按部位加载：

- **通用基线（全场景必加载）**：[`patterns/meta-rules.md`](./patterns/meta-rules.md), [`patterns/patterns-vocabulary.md`](./patterns/patterns-vocabulary.md), [`patterns/patterns-syntax.md`](./patterns/patterns-syntax.md)
- 如果在处理**数学/方法**部分：加挂 [`patterns/patterns-math.md`](./patterns/patterns-math.md)
- 如果在处理**实验与图表**：加挂 [`patterns/patterns-layout.md`](./patterns/patterns-layout.md)
- 如果在处理**摘要、总结与标题结构**：加挂 [`patterns/patterns-structure.md`](./patterns/patterns-structure.md)

### “小论文思维”融入
在 `examples/` 目录下存放了如 `introduction.md`, `method.md` 的精华法则（虽然源自英文小论文，但逻辑通用）。
- 当遇到“引言写不深”、“过渡生硬”时，不妨检索 `examples/` 中的套路指导，然后用 `patterns` 中的中文语法规范来输出。

## 执行原则

1. **先收集背景，不要盲目输出**：你总是问清用户目前所处的阶段是什么（是要润色还是要按流程提取语料）。如果涉及风格，先问有没有参照对象（参见 `patterns/reference-thesis.md` 里的风格指纹机制）。
2. **文本生成要求“冰冷干燥纯客观”**：不使用夸张连接词（“综上所述”、“值得注意的是”），不出现空洞的分析，不用“进行了XX的分析”（直接用“分析XX”），杜绝对着定理之前硬塞情感铺垫。
3. **输出纯净**：给用户的只能是符合排版和 LaTeX（如果需要）要求的直接可用代码或纯文字。结尾不得说“我已经去除了AI味”或解释你命中了什么规则。如果在审校模式下，按要求给出“建议改写列表”加命中编号即可。