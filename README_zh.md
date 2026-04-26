# Thesis-Paper-Writing-Skills

[English README](./README.md)

这是一个在以下项目基础上进行的**个人化 Fork + 重构**仓库：

- 上游仓库：[Master-cai/Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills)

我的目标不只是“论文写作技巧整理”，而是构建一套**博士毕设端到端自动化流水线**：

- 输入：多篇小论文 LaTeX 源码
- 模具：博士论文 `.cls` / `.tex` 模板约束
- 输出：可编译的大论文与答辩 PPT

一句话：把学术写作经验工程化为**零摩擦 Academic Agent Workflow**。

## 这个仓库想解决什么问题

原始项目已经提供了高质量的写作方法与提示词模式。
本仓库希望在此基础上进一步做成“可执行剧本”：让 AI Agent 按步骤完成任务，而不是一次性生成全部内容。

## 现实判断（Reality Check）

即使是当前最强模型，也受限于上下文窗口和长程注意力衰减。
如果只给“所有小论文 + 模板”，然后一句话要求“写完整篇博士论文”，常见问题是：

- 章节结构与逻辑链条出现幻觉
- LaTeX 代码残缺，无法稳定编译
- 公式、伪代码、图表引用在扩写中丢失

因此本仓库不走“一条 Prompt 干到底”，而是走**多阶段 SOP 技能链**。

## 核心剧本：4 个 Agentic SOP（已落地初版）

### 🎬 剧本 1：`Skill_01_Environment_Setup.md`

**目标：** 自动完成环境与工具链就绪。

预期 Agent 行为：

- 检查并安装 `uv`
- 配置 `zotero-mcp-server`
- 在工作区生成 MCP 配置（如 `.mcp.json`）
- 验证检索与工具调用链可用

### 🎬 剧本 2：`Skill_02_Asset_Extraction.md`

**目标：** 无损剥离小论文核心资产。

预期 Agent 行为：

- 用脚本/正则/Python 解析 LaTeX 源码
- 抽取核心公式、伪代码、关键图表与引用关系
- 存储为中间件（如 JSON）供后续扩写使用
- 最大化保留数学严谨性与可追溯性

### 🎬 剧本 3：`Skill_03_Thesis_Drafting.md`（核心）

**目标：** 大纲映射 + 渐进式章节扩写。

预期 Agent 行为：

- 按章节循环生成，不做一次性全量输出
- 全局术语锁定（例如统一使用 `drone`、`real-world condition constraints`）
- 将小论文的精简表达扩展为中文博士论文所需背景与论证
- 在叙事过渡中强化 `physics-informed priors` 的逻辑
- 每章后自动编译（`xelatex`），读 log 并自修复到通过

### 🎬 剧本 4：`Skill_04_Presentation_Gen.md`

**目标：** 从论文终稿自动生成答辩 PPT。

预期 Agent 行为：

- 读取最终大论文 `.tex`
- 提取 5 个核心章节并映射成 Beamer Frame 结构
- 直接复用关键对比图与实验图表
- 输出可维护、可迭代的幻灯片源码

## 当前仓库现状

目前已包含基础写作技能包：

- `research-paper-writing/`
  - `SKILL.md`：写作流程与使用规则
  - `references/`：分章节写作模板与示例
  - `agents/openai.yaml`：Agent 元信息

并已新增博士论文自动化剧本目录：

- `doctoral-thesis-workflow/`
  - `Skill_01_Environment_Setup.md`
  - `Skill_02_Asset_Extraction.md`
  - `Skill_03_Thesis_Drafting.md`
  - `Skill_04_Presentation_Gen.md`

建议按 `01 -> 02 -> 03 -> 04` 顺序执行。

## 快速开始（推荐顺序）

1. 先执行 `doctoral-thesis-workflow/Skill_01_Environment_Setup.md`，完成环境与 MCP 工具链就绪。
2. 再执行 `doctoral-thesis-workflow/Skill_02_Asset_Extraction.md`，生成结构化资产中间件。
3. 然后执行 `doctoral-thesis-workflow/Skill_03_Thesis_Drafting.md`，按章节扩写并循环编译修复。
4. 最后执行 `doctoral-thesis-workflow/Skill_04_Presentation_Gen.md`，自动生成 Beamer 答辩 PPT。

## 安装方式（当前技能包）

以下命令默认在仓库根目录执行。

### 1) Codex

```bash
mkdir -p "$CODEX_HOME/skills"
cp -R research-paper-writing "$CODEX_HOME/skills/"
cp -R doctoral-thesis-workflow "$CODEX_HOME/skills/"
```

使用示例：

```text
Use $research-paper-writing to improve my paper's Introduction.
```

端到端任务示例：

```text
Use $doctoral-thesis-workflow to set up my environment, extract assets from my small-paper LaTeX sources, draft my thesis chapter-by-chapter with compile checks, and generate defense slides.
```

### 2) Claude Code

全局安装：

```bash
mkdir -p "$HOME/.claude/skills"
cp -R research-paper-writing "$HOME/.claude/skills/"
cp -R doctoral-thesis-workflow "$HOME/.claude/skills/"
```

项目级安装：

```bash
mkdir -p .claude/skills
cp -R research-paper-writing .claude/skills/
cp -R doctoral-thesis-workflow .claude/skills/
```

建议在提示词中显式指定：`Please use the research-paper-writing skill`。
若希望跑完整流水线，建议使用：`Please use the doctoral-thesis-workflow skill`。

### 3) Gemini

```bash
mkdir -p "$HOME/.gemini/skills"
cp -R research-paper-writing "$HOME/.gemini/skills/"
cp -R doctoral-thesis-workflow "$HOME/.gemini/skills/"
```

## 致谢与来源

- Fork 基线项目：[Master-cai/Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills)
- 方法论来源（公开学习笔记）：[pengsida/learning_research](https://github.com/pengsida/learning_research)

本仓库主要贡献在于：流程工程化、提示词链设计、以及博士论文场景下的自动化实践。

## 许可证

本项目采用 MIT License，详见 [LICENSE](./LICENSE)。
