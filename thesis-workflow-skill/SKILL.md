---
name: thesis-workflow
description: End-to-end doctoral/master thesis workflow for Chinese graduate dissertations, with BUAA thesis format as the authoritative target. Use when Codex needs to turn prior papers or LaTeX assets into a Beihang/BUAA thesis, extract equations/figures/citations from paper sources, draft or revise thesis chapters, enforce rigorous Chinese STEM dissertation style, adapt the BUAA LaTeX 4.1.0 template, generate defense Beamer slides, or review/polish existing Chinese thesis text to reduce AI-like tone while preserving academic rigor.
---

# thesis-workflow

Use this skill as a thesis production operating system, not as a one-shot writing prompt. Work incrementally, keep every claim traceable to source material, and preserve a compilable LaTeX project after each meaningful edit.

## First Decision

Classify the user's request into one primary mode:

| Mode | User intent | Load first |
| --- | --- | --- |
| Environment | Prepare a thesis workspace or toolchain | `workflows/Skill_01_Environment_Setup.md` |
| Extraction | Parse prior paper sources into reusable assets | `workflows/Skill_02_Asset_Extraction.md`, `scripts/extract_latex_assets.py` |
| Drafting | Write or expand a thesis chapter | `workflows/Skill_03_Thesis_Drafting.md`, relevant `patterns/*` |
| Polish/Review | Diagnose or rewrite existing Chinese thesis text | `references/buaa-format-authority.md`, `references/thesis-polish-protocol.md`, `patterns/meta-rules.md`, relevant `patterns/patterns-*.md` |
| Slides | Produce defense slides from a finished thesis | `workflows/Skill_04_Presentation_Gen.md` |

If the mode is clear from files or wording, proceed. Ask only for missing thesis-specific inputs that cannot be inferred safely, such as source paper paths, target chapter, template path, or reference thesis path.

## Resource Map

- `workflows/`: SOPs for the four-stage pipeline. Read only the workflow matching the active stage.
- `patterns/`: Chinese STEM dissertation style constraints. Load selectively using the routing table below.
- `examples/`: English paper-writing logic examples. Use them for structure only, then output in the Chinese dissertation style defined by `patterns/`.
- `references/buaa-format-authority.md`: Highest-priority formatting source for BUAA thesis work. Use it to override imported or generic formatting advice.
- `references/project-profile.md`: Template for project memory. Do not fill this installed-skill copy with personal thesis facts; copy/use it as `<active-thesis-root>/.thesis-workflow/project-profile.md`.
- `references/thesis-polish-protocol.md`: Prose-only Chinese writing/review protocol adapted from `graduate-thesis-polish-and-write-skill`; use it for language, AI-tone, and conservative editing, not for BUAA formatting decisions.
- `scripts/extract_latex_assets.py`: Deterministic extractor for equations, algorithms, figures/tables, citations, references, and claim-like sentences from `.tex` sources.

## Runtime State

Keep project-specific state outside the installed skill package:

- Preferred directory: `<active-thesis-root>/.thesis-workflow/`
- Project profile: `.thesis-workflow/project-profile.md`
- Reference thesis config: `.thesis-workflow/reference-thesis.md`
- Reference thesis fingerprint: `.thesis-workflow/reference-thesis-fingerprint.md`

Never write personal thesis paths, term locks, reference-thesis metadata, or fingerprint excerpts into `~/.codex/skills/thesis-workflow/` unless the user explicitly asks to modify the installed package. Treat files under `thesis-workflow-skill/references/` and `thesis-workflow-skill/patterns/reference-thesis.md` as templates.

## Non-Negotiable Workflow Rules

1. Do not generate a whole dissertation in one pass. Work by chapter, section, or a clearly bounded file set.
2. Do not invent evidence. Every formula, figure, algorithm, citation, and strong claim must come from extracted assets, user-provided context, or explicitly marked assumptions.
3. Treat BUAA LaTeX 4.1.0 and the bundled BUAA writing/template instructions as the formatting authority. Any imported polish rule, reference thesis habit, or generic LaTeX preference loses when it conflicts with BUAA.
4. Keep LaTeX compilable. After editing thesis sources, run the smallest relevant XeLaTeX build loop and fix errors minimally.
5. Preserve user writing unless asked to rewrite. In review mode, prefer diagnosis and targeted edits over wholesale replacement.
6. Never copy conversational phrasing into thesis text. Convert the user's discussion into independent academic prose.
7. Keep outputs clean. In writing mode, provide usable thesis text or patch content; avoid explaining which style rules were followed unless the user asks for a report.

## Pattern Loading

Load `patterns/meta-rules.md` for all writing or review tasks. Add only the modules needed for the current target:

| Target | Add these modules |
| --- | --- |
| General Chinese prose | `patterns-vocabulary.md`, `patterns-syntax.md` |
| Abstract, introduction, conclusion, chapter titles | `patterns-structure.md` |
| Method, derivation, theorem, proof, assumptions | `patterns-math.md` |
| Experiments, tables, figures, captions | `patterns-layout.md` |
| LaTeX source editing or BUAA template work | `references/buaa-format-authority.md`, `patterns-latex.md` |
| Reference-thesis alignment | `<active-thesis-root>/.thesis-workflow/reference-thesis.md`; then read `<active-thesis-root>/.thesis-workflow/reference-thesis-fingerprint.md` if it exists |

Use `examples/introduction.md`, `examples/method.md`, `examples/experiments.md`, and related examples only when structural guidance is needed. Do not imitate English phrasing directly.

## Stage Guidance

### Environment

Follow `workflows/Skill_01_Environment_Setup.md`. Report available tools, missing tools, and exact next actions. Do not install or rewrite system configuration unless the user explicitly wants setup changes.

### Extraction

Run the extractor when the user provides prior paper sources:

```bash
python thesis-workflow-skill/scripts/extract_latex_assets.py --source <paper_tex_dir> --output <asset_output_dir>
```

Use `--topic` for project-specific tags when useful. Inspect `summary.json` and unresolved references before drafting.

### Drafting

Before writing, read `<active-thesis-root>/.thesis-workflow/project-profile.md` and `references/buaa-format-authority.md` if available, then read the relevant extracted JSON files. If the project profile is missing, copy the template from `references/project-profile.md` into `.thesis-workflow/` and fill only user-confirmed facts. Build a chapter-level plan with:

- section purpose;
- asset IDs to reuse;
- claims and evidence;
- expected figures, tables, equations, and citations.

Then draft one section at a time. For `.tex` output, preserve labels and citations, use the BUAA template's existing macros and structure, and run a compile check before moving on.

### Polish/Review

Read `references/buaa-format-authority.md` and `references/thesis-polish-protocol.md`, then choose one of three outputs based on the user's wording:

- `diagnosis`: list concrete issues with locations, rule IDs, and suggested fixes;
- `rewrite`: provide the revised text while preserving the author's structure;
- `patch`: edit the target `.tex` file directly, changing only prose unless asked otherwise.

Use the protocol's reference-thesis mechanism from `.thesis-workflow/` when the user provides or has configured a style reference, but only for prose style. For `.tex`, do not alter math environments, citation keys, labels, BUAA template macros, or formatting conventions unless the issue is specifically about LaTeX repair.

### Slides

Follow `workflows/Skill_04_Presentation_Gen.md`. Convert the thesis into a defense narrative: problem, method, evidence, conclusion. Reuse thesis figures only after checking paths and readability.

## Quality Gates

Before finishing a substantial task, verify the relevant gates:

- `provenance`: major claims map to assets, citations, experiments, or user-provided facts;
- `style`: output passes deletion test and reference-thesis test from `patterns/meta-rules.md`;
- `format`: BUAA LaTeX 4.1.0 and bundled BUAA writing/template requirements override imported polish or generic formatting rules;
- `latex`: edited sources compile or the remaining compile blocker is clearly reported;
- `scope`: only the requested chapter/section/files were changed;
- `handoff`: next step is obvious from generated reports or file names.
