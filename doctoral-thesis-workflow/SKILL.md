---
name: doctoral-thesis-workflow
description: Build an end-to-end doctoral thesis workflow from small-paper LaTeX assets to thesis manuscript and defense slides. Use when setting up tooling/MCP, extracting equations and figures, drafting thesis chapter-by-chapter with compile loops, and generating Beamer slides.
---

# Doctoral Thesis Workflow

## Overview

Use this skill as an orchestrator for four sequential SOP scripts:

1. `Skill_01_Environment_Setup.md`
2. `Skill_02_Asset_Extraction.md`
3. `Skill_03_Thesis_Drafting.md`
4. `Skill_04_Presentation_Gen.md`

Do not skip phases unless the user explicitly confirms prerequisites are already complete.

## Phase Routing

- Environment/toolchain/MCP issues -> load `Skill_01_Environment_Setup.md`
- Small-paper asset parsing/extraction -> load `Skill_02_Asset_Extraction.md`
- Thesis writing/expansion/compile repair -> load `Skill_03_Thesis_Drafting.md`
- Defense slide generation from thesis -> load `Skill_04_Presentation_Gen.md`

## Global Constraints

1. Enforce chapter-wise incremental drafting (no one-shot full thesis generation).
2. Keep terminology stable across the manuscript.
3. Preserve mathematical fidelity of equations and symbols.
4. Treat compilation status as a hard quality gate.
5. Keep claim-evidence alignment explicit for major conclusions.

## Terminology Lock (Default)

- `drone`
- `real-world condition constraints`
- `physics-informed priors`

If the user provides alternative terminology rules, apply them globally and log overrides.

## Recommended Execution Contract

For each phase, return:

1. Inputs consumed
2. Actions performed
3. Artifacts generated
4. Validation results
5. Remaining risks and next step

## Completion Criteria

The workflow is considered complete only when:

- Thesis source compiles successfully.
- Major claims are evidence-backed.
- Slide deck compiles and reuses key thesis assets.
