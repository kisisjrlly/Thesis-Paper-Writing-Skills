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

## 当前仓库现状

目前所有零散的结构（老版本的小论文技巧、学位大论文剧本、毕设写作中文硬基线）已整合为统一的终端技能包（大一统 Skill）：

- `thesis-workflow-skill/`
  - `SKILL.md`：总调度入口，规定使用方式
  - `workflows/`：按步骤的 01 到 04 自动化剧本
  - `patterns/`：针对中文大论文的严格排版、词汇、句法等“去 AI 味”和格式润色约束
  - `examples/`：英文小论文优秀的行文逻辑和写法案例（抽取自老版本），可用于写作时的逻辑指引

建议按工作流阶段顺序执行，或在单纯撰写与润色中文论文段落时直接调用 `thesis-workflow-skill` 请求审校模式。

## 快速开始（推荐顺序）

1. 从 `thesis-workflow-skill/workflows/Skill_01_Environment_Setup.md` 开始，完成环境与 MCP 工具链就绪。
2. 扩展或生成内容：`Use thesis-workflow skill to draft Chapter 3...`
3. 对现有文字进行改写：`Use thesis-workflow skill to review and polish the introductory paragraph of chapter 2.`

## 安装方式（当前技能包）

以下命令默认在仓库根目录执行。

### 1) Codex

```bash
mkdir -p "$CODEX_HOME/skills"
cp -R thesis-workflow-skill "$CODEX_HOME/skills/"
```

使用示例：

```text
Use $thesis-workflow to set up my environment, extract assets from my small-paper LaTeX sources, draft my thesis chapter-by-chapter with compile checks, and generate defense slides.
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
- 方法论来源（公开学习笔记）：[pengsida/learning_research](https://github.com/pengsida/learning_research)

本仓库主要贡献在于：流程工程化、提示词链设计、以及博士论文场景下的自动化实践。

## 许可证

本项目采用 MIT License，详见 [LICENSE](./LICENSE)。
