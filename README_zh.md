# Thesis-Paper-Writing-Skills

[English README](./README.md)

这是一个在以下项目基础上进行的**个人化 Fork + 重构**仓库：

- 上游仓库：[Master-cai/Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills)

我的目标不只是“论文写作技巧整理”，而是构建一套**博士毕设端到端自动化流水线**：

- 输入：多篇小论文 LaTeX 源码
- 模具：北航硕博士学位论文模版-LaTeX 4.1.0 的 `.cls` / `.tex` 模板约束
- 输出：可编译的大论文与答辩 PPT

一句话：把学术写作经验工程化为**零摩擦 Academic Agent Workflow**。

## 项目定位与规范优先级

本仓库的目标是服务**北航博士/硕士学位论文写作**，不是做一个通用高校毕业论文模板。所有涉及论文格式、LaTeX 结构、图表编号、公式间距、参考文献样式、封面题名页、摘要关键词、符号表、缩略语说明、目录、页眉页脚等内容时，必须以以下材料为准：

1. 用户本人、导师、学院或学校给出的明确要求；
2. `北航硕博士学位论文模版-LaTeX 4.1.0/` 中的模板文件、README、`main.tex` 示例、`buaa.cls` 和配套撰写规范；
3. 本 skill 中的 `references/buaa-format-authority.md` 与 `patterns/patterns-latex.md`。

本项目也**借鉴并吸收了** [lmcggg/graduate-thesis-polish-and-write-skill](https://github.com/lmcggg/graduate-thesis-polish-and-write-skill) 的中文毕业论文行文与审校经验，包括去 AI 味、句式收束、术语一致性、范例论文指纹、诊断报告等流程。但该项目来自其他学校学生的写作实践，因此在本仓库中只作为**中文表达与审校参考**，不作为北航论文格式依据。若外校 polish 规则与北航模板或撰写规范冲突，一律以北航要求为准。

## 这个仓库想解决什么问题

原始项目已经提供了高质量的写作方法与提示词模式。
本仓库希望在此基础上进一步做成“可执行剧本”：让 AI Agent 按步骤完成资产抽取、章节扩写、编译修复、中文审校和答辩材料生成，而不是一次性生成全部内容。

## 现实判断（Reality Check）

即使是当前最强模型，也受限于上下文窗口和长程注意力衰减。
如果只给“所有小论文 + 模板”，然后一句话要求“写完整篇博士论文”，常见问题是：

- 章节结构与逻辑链条出现幻觉
- LaTeX 代码残缺，无法稳定编译
- 公式、伪代码、图表引用在扩写中丢失

因此本仓库不走“一条 Prompt 干到底”，而是走**多阶段 SOP 技能链**。

## 当前仓库现状

目前所有零散的结构（老版本的小论文技巧、学位大论文剧本、毕设写作中文硬基线）已整合为统一的终端技能包（大一统 Skill）：

- `thesis-workflow-skill/`
  - `SKILL.md`：总调度入口，规定使用方式
  - `agents/openai.yaml`：Codex 技能发现所需的界面元数据
  - `workflows/`：按步骤的 01 到 04 自动化剧本
  - `patterns/`：针对中文大论文的行文、词汇、句法与局部 LaTeX 约束；北航格式裁决权单独放在 `references/buaa-format-authority.md`
  - `examples/`：英文小论文优秀的行文逻辑和写法案例（抽取自老版本），可用于写作时的逻辑指引
  - `references/buaa-format-authority.md`：从北航 LaTeX 4.1.0 模板提炼的最高格式依据
  - `references/project-profile.md`：项目画像模板；真实项目状态应放在论文项目的 `.thesis-workflow/project-profile.md`
  - `references/thesis-polish-protocol.md`：从 `graduate-thesis-polish-and-write-skill` 改造而来的中文行文/审校协议，只管语言表达，不覆盖北航格式
  - `scripts/extract_latex_assets.py`：供资产抽取流程调用的确定性 LaTeX 解析脚本

## 详细使用指南 (Detailed Usage)

本 Skill 被设计为灵活的工具箱。你可以将它完整用于大论文的端到端构建，也可以拆开用于单独段落的审校。建议在使用各种 AI 代码助手（如 Claude Code, GitHub Copilot 终端模式, Cursor 等）时，参照以下方式提问：

### 场景一：端到端大论文生成 (按序执行 Workflows)
如果你有一堆小论文资产，想要生成大论文，请严格按 `workflows/` 目录的步骤走：
1. **环境准备**：
   > "请使用 thesis-workflow skill，运行 `Skill_01_Environment_Setup.md` 帮我配置当前的论文工作区环境。"
2. **资产抽取**：
   > "接下来执行 Skill 02 剧本，从我的 latex 原小论文目录 `./papers` 中抽取公式和图表并保存为 JSON 资产。"
3. **章节扩写**：
   > "根据 Skill 03 剧本，开始撰写第一章。请务必结合刚才抽取的资产，并应用规范目录里的全部写作风格（不准有 AI 味）。"
4. **PPT 生成**：
   > "大论文已通过编译，请执行 Skill 04 剧本生成答辩用的 Beamer PPT 源码。"

### 场景二：现有文本润色与“去 AI 味” (仅应用 Patterns)
对于你自己写的或者之前别的 AI 生成的草稿，你可以调用该技能进行严格的审查和改写，让文字真正像理科研究生的手笔。
* **Prompt 示例**：
  > "请使用 thesis-workflow skill 帮我审校以下这段背景介绍。请应用 `patterns` 目录下的中文理工科毕业论文行文规范（重点关注 meta-rules 和 patterns-syntax），只处理表达和 AI 味问题，格式仍以北航模板为准：[附上你的文本]"

### 场景三：学习小论文逻辑来撰写新章节 (Examples + Patterns)
当你毫无头绪怎么写某一个专门章节（如 Introduction 介绍或者 Method 方法）时，可以让模型借鉴 `examples` 里的成熟结构，再套用 `patterns` 的中文规范输出。
* **Prompt 示例**：
  > "请使用 thesis-workflow skill 帮我撰写第三章的方法概述。请先查阅 `examples/method.md` 中的 'Overview' 结构技巧学习行文逻辑，然后使用 `patterns` 里的中文严厉规范把这节中文草稿写出来。我的研究内容如下：..."

### 运行时状态放在哪里

skill 包本身应保持可重复安装，不存放个人论文路径、范例论文信息或风格指纹。具体论文项目的状态建议放在论文项目根目录下：

```text
.thesis-workflow/
├── project-profile.md
├── reference-thesis.md
└── reference-thesis-fingerprint.md
```

这些文件可能包含本机路径、论文规划和范例论文摘录，默认不建议推送到公开仓库。

## 安装方式（当前技能包）

以下命令默认在仓库根目录执行。

### 1) Codex

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R thesis-workflow-skill "${CODEX_HOME:-$HOME/.codex}/skills/"
```

### 2) Claude Code

全局安装：

```bash
mkdir -p "$HOME/.claude/skills"
cp -R thesis-workflow-skill "$HOME/.claude/skills/"
```

项目级安装：

```bash
mkdir -p .claude/skills
cp -R thesis-workflow-skill .claude/skills/
```

建议在提示词中显式指定：`Please use the thesis-workflow skill...`

### 3) Gemini

```bash
mkdir -p "$HOME/.gemini/skills"
cp -R thesis-workflow-skill "$HOME/.gemini/skills/"
```

## 致谢与来源

- Fork 基线项目：[Master-cai/Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills)
- 中文行文审校流程改造自：[lmcggg/graduate-thesis-polish-and-write-skill](https://github.com/lmcggg/graduate-thesis-polish-and-write-skill)。格式规范仍以北航硕博士学位论文模版-LaTeX 4.1.0 为准。
- 方法论来源（公开学习笔记）：[pengsida/learning_research](https://github.com/pengsida/learning_research)

本仓库主要贡献在于：流程工程化、提示词链设计、以及博士论文场景下的自动化实践。

## 许可证

本项目采用 MIT License，详见 [LICENSE](./LICENSE)。
