# Thesis-Paper-Writing-Skills

[中文说明](./README_zh.md)

This repository is a **personalized fork-and-rebuild** project based on:

- Upstream project: [Master-cai/Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills)

My target is not just “paper writing tips”, but an **end-to-end doctoral thesis workflow**:

- Input: multiple conference/journal paper assets (LaTeX sources)
- Template: doctoral thesis `.cls`/`.tex` constraints
- Output: thesis manuscript + defense slides

In short, I want to build a **zero-friction academic production pipeline** for AI coding agents.

## Why this repository exists

The original project provides high-quality writing strategies and prompt patterns.
This fork extends it toward an **agentic SOP system** so models can execute tasks in sequence instead of one-shot generation.

## Reality check (important)

Current frontier models are strong, but still constrained by context-window limits and attention decay.
If we simply provide “all small papers + one thesis template” and ask for one-shot output, common failures include:

- Hallucinated structure and missing cross-chapter consistency
- Broken or non-compilable LaTeX
- Loss of equations, pseudo-code details, or figure references

Therefore this repo is designed as **scripted multi-step Skills**, not a single “write my thesis” prompt.

## Agentic SOPs (initial version implemented)

### 🎬 Skill 01 — `Skill_01_Environment_Setup.md`

**Goal:** bootstrap environment and tooling automatically.

Expected agent behavior:

- check/install `uv`
- configure `zotero-mcp-server`
- generate workspace MCP config files (e.g. `.mcp.json`)
- verify retrieval/toolchain readiness

### 🎬 Skill 02 — `Skill_02_Asset_Extraction.md`

**Goal:** lossless extraction of reusable assets from small papers.

Expected agent behavior:

- parse LaTeX sources with scripts/regex/Python
- extract equations, algorithm blocks, key figures/tables, and citations
- serialize into machine-readable intermediates (e.g. JSON)
- preserve mathematical rigor for downstream expansion

### 🎬 Skill 03 — `Skill_03_Thesis_Drafting.md` (core)

**Goal:** outline mapping + progressive chapter drafting.

Expected agent behavior:

- draft chapter-by-chapter, not one-shot
- enforce terminology constraints globally (e.g. “drone”, “real-world condition constraints”)
- expand compact paper language into thesis-level narrative context
- strengthen physics-informed priors framing when transitioning from paper assumptions
- run compile loops after each chapter (`xelatex`), inspect logs, and self-repair until compile passes

### 🎬 Skill 04 — `Skill_04_Presentation_Gen.md`

**Goal:** generate defense slides from thesis source.

Expected agent behavior:

- read finalized thesis `.tex`
- map five core chapters to Beamer frame structure
- reuse key comparison plots/figures directly from thesis assets
- output a maintainable `.tex` slide deck

## Current repository contents

At this stage, the repository includes the base writing skill package:

- `research-paper-writing/`
  - `SKILL.md`: writing workflow and usage rules
  - `references/`: section-level guides and templates
  - `agents/openai.yaml`: agent metadata

And the new doctoral-thesis SOP scripts:

- `doctoral-thesis-workflow/`
  - `Skill_01_Environment_Setup.md`
  - `Skill_02_Asset_Extraction.md`
  - `Skill_03_Thesis_Drafting.md`
  - `Skill_04_Presentation_Gen.md`

These files are designed to be executed in sequence (`01 -> 02 -> 03 -> 04`).

## Quick usage (recommended order)

1. Start with `doctoral-thesis-workflow/Skill_01_Environment_Setup.md` to prepare toolchain and MCP.
2. Run `doctoral-thesis-workflow/Skill_02_Asset_Extraction.md` to build structured intermediate assets.
3. Execute `doctoral-thesis-workflow/Skill_03_Thesis_Drafting.md` chapter by chapter with compile loops.
4. Finish with `doctoral-thesis-workflow/Skill_04_Presentation_Gen.md` to generate Beamer slides.

## Installation (current package)

Assume you are in repository root.

### 1) Codex

Copy skills to `$CODEX_HOME/skills/`:

```bash
mkdir -p "$CODEX_HOME/skills"
cp -R research-paper-writing "$CODEX_HOME/skills/"
cp -R doctoral-thesis-workflow "$CODEX_HOME/skills/"
```

Prompt example:

```text
Use $research-paper-writing to improve my paper's Introduction.
```

End-to-end workflow example:

```text
Use $doctoral-thesis-workflow to set up my environment, extract assets from my small-paper LaTeX sources, draft my thesis chapter-by-chapter with compile checks, and generate defense slides.
```

### 2) Claude Code

Global install:

```bash
mkdir -p "$HOME/.claude/skills"
cp -R research-paper-writing "$HOME/.claude/skills/"
cp -R doctoral-thesis-workflow "$HOME/.claude/skills/"
```

Project install:

```bash
mkdir -p .claude/skills
cp -R research-paper-writing .claude/skills/
cp -R doctoral-thesis-workflow .claude/skills/
```

Prompt hint: `Please use the research-paper-writing skill`.
For full pipeline tasks, use: `Please use the doctoral-thesis-workflow skill`.

### 3) Gemini

```bash
mkdir -p "$HOME/.gemini/skills"
cp -R research-paper-writing "$HOME/.gemini/skills/"
cp -R doctoral-thesis-workflow "$HOME/.gemini/skills/"
```

## Attribution

- Fork baseline: [Master-cai/Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills)
- Knowledge roots (open notes): [pengsida/learning_research](https://github.com/pengsida/learning_research)

This repository focuses on workflow engineering, packaging, and practical automation for doctoral thesis production.

## License

MIT License. See [LICENSE](./LICENSE).
