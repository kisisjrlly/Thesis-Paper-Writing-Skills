# Thesis-Paper-Writing-Skills

[中文说明](./README_zh.md)

This repository is a **personalized fork-and-rebuild** project based on:

- Upstream project: [Master-cai/Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills)

My target is not just "paper writing tips", but an **end-to-end doctoral thesis workflow**:

- Input: multiple conference/journal paper assets (LaTeX sources)
- Template: the BUAA/Beihang graduate thesis LaTeX 4.1.0 `.cls`/`.tex` constraints
- Output: thesis manuscript + defense slides

In short, I want to build a **zero-friction academic production pipeline** for AI coding agents.

## Project Goal And Rule Priority

This repository targets **BUAA/Beihang doctoral and master thesis writing**, not a generic university thesis template. For anything involving thesis format, LaTeX structure, figure/table numbering, equation spacing, bibliography style, cover/title pages, abstract keywords, symbol tables, abbreviations, table of contents, headers, footers, or other formal layout requirements, follow this priority:

1. Explicit requirements from the user, supervisor, college, or university;
2. Files and documentation under `北航硕博士学位论文模版-LaTeX 4.1.0/`, especially the README, `main.tex`, `buaa.cls`, and bundled writing specifications;
3. This skill's `references/buaa-format-authority.md` and `patterns/patterns-latex.md`.

This project also **borrows and adapts** Chinese thesis prose-review ideas from [lmcggg/graduate-thesis-polish-and-write-skill](https://github.com/lmcggg/graduate-thesis-polish-and-write-skill), including AI-tone diagnosis, sentence tightening, terminology consistency, reference-thesis fingerprints, and review-report workflows. That project was written from another school's thesis-writing experience, so in this repository it is used only as **Chinese prose and review guidance**, not as a BUAA formatting authority. If an imported polish rule conflicts with the BUAA template or BUAA writing requirements, the BUAA rule wins.

## Why this repository exists

The original project provides high-quality writing strategies and prompt patterns.
This fork extends it toward an **agentic SOP system** so models can execute asset extraction, chapter drafting, compile repair, Chinese prose review, and defense-material generation in sequence instead of one-shot generation.

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
  - `agents/openai.yaml`: UI metadata for Codex skill discovery.
  - `workflows/`: Automated SOP scripts 01 to 04.
  - `patterns/`: Chinese prose, vocabulary, syntax, and local LaTeX constraints for thesis writing; BUAA formatting authority is separated in `references/buaa-format-authority.md`.
  - `examples/`: Excellent narrative logic and examples (derived from older English paper resources) meant for structural inspiration.
  - `references/buaa-format-authority.md`: Highest-priority BUAA formatting authority derived from the BUAA LaTeX 4.1.0 template.
  - `references/project-profile.md`: Project-profile template; real project state belongs in the thesis project's `.thesis-workflow/project-profile.md`.
  - `references/thesis-polish-protocol.md`: Prose-only Chinese thesis writing/review protocol adapted from `graduate-thesis-polish-and-write-skill`.
  - `scripts/extract_latex_assets.py`: Deterministic LaTeX asset extractor used by the extraction workflow.

These files are designed to seamlessly assist either in executing sequentially or simply polishing the style of standard Chinese academic texts.

## Detailed Usage Guide

This Skill acts as a flexible toolbox. You can run the entire pipeline end-to-end (best for piecing together an entire thesis), or invoke specific modules purely for text polishing and structuring. Try using the following example prompts with your code agent (e.g. Claude Code, Codex, Cursor):

### Scenario 1: End-to-End Thesis Generation (Run Workflows in sequence)
When transforming prior publications into a full thesis, ask your agent to follow the SOP scripts step-by-step:
1. **Setup**:
   > "Use the thesis-workflow skill and run `Skill_01_Environment_Setup.md` to configure my workspace."
2. **Asset Extraction**:
   > "Now run the Skill 02 workflow script to extract equations and figures from my previous papers located at `./papers`."
3. **Progressive Drafting**:
   > "Execute Skill 03 to start drafting Chapter 1. Use the extracted assets and make sure to strictly enforce the terminology and Chinese style patterns."
4. **Presentation Slides**:
   > "The thesis compiles successfully. Finally, run Skill 04 to generate Beamer defense slides."

### Scenario 2: Text Polishing and "De-AI-fication" (Apply strictly Patterns)
If you already have text (either human-written or AI-generated) that feels unnatural or overly verbose, use the strict Chinese academic writing patterns to fix it.
* **Prompt Example**:
  > "Use the thesis-workflow skill to review and polish the following text. Apply the Chinese prose, vocabulary, and syntax rules from the `patterns/` directory to reduce AI-like tone, while keeping BUAA formatting governed by the BUAA template: [your text]"

### Scenario 3: Drafting New Sections from Scratch (Learn Examples + Apply Patterns)
When you don't know how to structure a section (e.g., Introduction or Method overview), you can combine the logical templates in `examples/` with the strict writing rules in `patterns/`.
* **Prompt Example**:
  > "Use the thesis-workflow skill to draft my Chapter 3 Method overview. First read `examples/method.md` to learn the logical structure (such as the 'three elements'), then apply the strict Chinese academic rules from the `patterns/` folder to generate the final Chinese text. Use this context: ..."

### Runtime State

The installed skill package should stay reproducible. Do not store personal thesis paths, reference-thesis metadata, or style fingerprints inside `~/.codex/skills/thesis-workflow`. Keep project-specific state under the active thesis project instead:

```text
.thesis-workflow/
├── project-profile.md
├── reference-thesis.md
└── reference-thesis-fingerprint.md
```

These files may contain local paths, thesis plans, and reference-thesis excerpts, so they should not be pushed to a public repository by default.

## Installation (current package)

Assume you are in repository root.

### 1) Codex

Copy skills to `$CODEX_HOME/skills/`:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R thesis-workflow-skill "${CODEX_HOME:-$HOME/.codex}/skills/"
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
- Chinese prose polishing workflow adapted from: [lmcggg/graduate-thesis-polish-and-write-skill](https://github.com/lmcggg/graduate-thesis-polish-and-write-skill). Formatting remains governed by the BUAA LaTeX 4.1.0 template.
- Knowledge roots (open notes): [pengsida/learning_research](https://github.com/pengsida/learning_research)

This repository focuses on workflow engineering, packaging, and practical automation for doctoral thesis production.

## License

MIT License. See [LICENSE](./LICENSE).
