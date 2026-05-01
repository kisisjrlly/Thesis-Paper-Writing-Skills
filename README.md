# Thesis-Paper-Writing-Skills

[中文说明](./README_zh.md)

This repository is a **personalized fork-and-rebuild** project based on:

- Upstream project: [Master-cai/Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills)

My target is not just "paper writing tips", but an **end-to-end doctoral thesis workflow**:

- Input: multiple conference/journal paper assets (LaTeX sources)
- Template: doctoral thesis `.cls`/`.tex` constraints
- Output: thesis manuscript + defense slides

In short, I want to build a **zero-friction academic production pipeline** for AI coding agents.

## Why this repository exists

The original project provides high-quality writing strategies and prompt patterns.
This fork extends it toward an **agentic SOP system** so models can execute tasks in sequence instead of one-shot generation, and enforces strict Chinese academic writing styles for graduate theses.

## Reality check (important)

Current frontier models are strong, but still constrained by context-window limits and attention decay.
If we simply provide "all small papers + one thesis template" and ask for one-shot output, common failures include:

- Hallucinated structure and missing cross-chapter consistency
- Broken or non-compilable LaTeX
- Loss of equations, pseudo-code details, or figure references

Therefore this repo is designed as **scripted multi-step Skills**, not a single "write my thesis" prompt.

## Current repository contents

All previously disparate capabilities (English paper writing tips, thesis SOP workflows, and rigorous Chinese polishing rules) have now been unified into a single terminal skill package: `thesis-workflow-skill`.

- `thesis-workflow-skill/`
  - `SKILL.md`: Main routing and usage definition.
  - `workflows/`: Automated SOP scripts 01 to 04.
  - `patterns/`: Strict formatting, vocabulary, and syntax constraints designed to remove "AI tone" from Chinese thesis writing.
  - `examples/`: Excellent narrative logic and examples (derived from older English paper resources) meant for structural inspiration.

These files are designed to seamlessly assist either in executing sequentially or simply polishing the style of standard Chinese academic texts.

## Quick usage (recommended order)

1. Start with `thesis-workflow-skill/workflows/Skill_01_Environment_Setup.md` to prepare toolchain and MCP.
2. Execute drafting or workflow generation: `Use thesis-workflow skill to draft Chapter 3...`
3. Edit or polish existing text: `Use thesis-workflow skill to review and polish the introductory paragraph of chapter 2.`

## Installation (current package)

Assume you are in repository root.

### 1) Codex

Copy skills to `$CODEX_HOME/skills/`:

```bash
mkdir -p "$CODEX_HOME/skills"
cp -R thesis-workflow-skill "$CODEX_HOME/skills/"
```

Prompt example:

```text
Use $thesis-workflow to set up my environment, extract assets from my small-paper LaTeX sources, draft my thesis chapter-by-chapter with compile checks, and generate defense slides.
```

### 2) Claude Code

Global install:

```bash
mkdir -p "$HOME/.claude/skills"
cp -R thesis-workflow-skill "$HOME/.claude/skills/"
```

Project install:

```bash
mkdir -p .claude/skills
cp -R thesis-workflow-skill .claude/skills/
```

Prompt hint: `Please use the thesis-workflow skill...`.

### 3) Gemini

```bash
mkdir -p "$HOME/.gemini/skills"
cp -R thesis-workflow-skill "$HOME/.gemini/skills/"
```

## Attribution

- Fork baseline: [Master-cai/Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills)
- Knowledge roots (open notes): [pengsida/learning_research](https://github.com/pengsida/learning_research)

This repository focuses on workflow engineering, packaging, and practical automation for doctoral thesis production.

## License

MIT License. See [LICENSE](./LICENSE).
