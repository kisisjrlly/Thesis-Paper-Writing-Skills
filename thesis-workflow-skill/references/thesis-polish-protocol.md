# thesis-polish-protocol

This protocol integrates the useful prose-editing parts of `graduate-thesis-polish-and-write-skill/thesis-polish` into `thesis-workflow`. Use it when writing, reviewing, or patching Chinese STEM graduate thesis prose.

It is not a formatting authority. For the user's BUAA thesis, `references/buaa-format-authority.md`, the BUAA LaTeX 4.1.0 template, and BUAA writing requirements override this protocol whenever layout, spacing, captions, numbering, section structure, bibliography style, or LaTeX template usage is involved.

## Goal

Make Chinese thesis prose read like a competent BUAA graduate student wrote it: rigorous, restrained, discipline-appropriate, and free of obvious AI tone. Avoid both extremes:

- over-AI: formulaic transitions, inflated claims, list-heavy structure, translation tone;
- over-humanized: casual, shallow, under-specified prose below thesis level.

## Two Core Tests

Apply these before and after every generated or revised paragraph:

1. Deletion test: if a sentence can be removed or shortened without losing information, remove or shorten it.
2. Reference-thesis test: if the sentence or transition could not plausibly appear in the configured reference thesis, rewrite it. Use this for prose style only; BUAA controls formatting, numbering, caption placement, and template structure.

These tests outrank individual blacklist rules.

## Modes

### Writing Mode

Use when the user asks to draft, expand, write an abstract, write an introduction, write a method section, or turn notes into thesis prose.

1. Load `patterns/meta-rules.md`.
2. Load `references/buaa-format-authority.md` for any BUAA `.tex`, caption, formula-spacing, or layout-sensitive work.
3. Load only the relevant `patterns/patterns-*.md` files using the routing table in `SKILL.md`.
4. Check `<active-thesis-root>/.thesis-workflow/reference-thesis.md`. If a reference thesis is configured, prefer its fingerprint over the original file for prose style.
5. Before drafting, identify the 3-5 most likely prose failures for the current section.
6. Draft directly in compliant prose. Do not draft loosely and then cosmetically polish.
7. Re-run the two core tests and `meta-rules` K1/K2.
8. Output usable thesis text, not a description of the rules followed.

### Review Mode

Use when the user says review, polish, diagnose, check AI tone, inspect a chapter, or asks what is wrong with existing text.

1. Load `patterns/meta-rules.md` and only relevant pattern files.
2. Load `references/buaa-format-authority.md` before commenting on format.
3. Read `<active-thesis-root>/.thesis-workflow/reference-thesis.md` path fields, not the full reference thesis.
4. Read the requested scope: paragraph, section, `.tex` file, or selected line range.
5. If the user did not specify the output type, default to diagnosis for large scopes and direct rewrite for short pasted text.
6. Record each issue with location, original snippet, rule ID, severity, and concrete suggestion.
7. Use the reference-thesis fingerprint for uncertain prose-style judgments.
8. For `.tex`, change only Chinese prose unless the user asks for LaTeX repair; BUAA template conventions are not polish issues.

### Quick Checklist Mode

Use when the user says quick pass, hard rules only, final scan, or similar. Report only hard hits and skip soft stylistic suggestions.

## Reference Thesis Mechanism

The prose effect is best when the user provides one or more same-field reference theses. A reference thesis is a language and structure anchor, not a source of formatting rules unless it is itself the user's required BUAA template exemplar.

### Startup

When writing or reviewing Chinese thesis prose:

- If `<active-thesis-root>/.thesis-workflow/reference-thesis.md` has a configured path, use that as the prose style anchor.
- If the user provides a reference path in the current request, validate the path and update `<active-thesis-root>/.thesis-workflow/reference-thesis.md`.
- If `.thesis-workflow/reference-thesis.md` is missing, copy the template from `patterns/reference-thesis.md` into the active thesis project's `.thesis-workflow/` directory first.
- If no reference is configured, continue in pure-rule mode when the user wants to proceed; mention once that style anchoring is weaker without a reference thesis.

### Fingerprint

Store the compact style fingerprint at:

```text
<active-thesis-root>/.thesis-workflow/reference-thesis-fingerprint.md
```

Generate or update it when:

- a reference thesis is first configured;
- the user changes/adds/removes a reference thesis;
- the user asks to rebuild the fingerprint;
- `.thesis-workflow/reference-thesis.md` changed but the fingerprint is missing or stale.

Fingerprint schema:

```markdown
## 范例 N: <论文名或文件名>

**元信息**
- 路径：<绝对路径>
- 方向/学科：<若知道>
- 指纹生成日期：<YYYY-MM-DD>

**章引言样例**
> <2-3 段原文节选>

**方法章叙述样例**
> <1-2 段原文节选>

**本章小结样例**
> <1-2 段原文节选>

**定理/证明叙述样例**
> <若有>

**图题样例**
- 图 X-Y: <图题>

**表题样例**
- 表 X-Y: <表题>

**高频术语与句式**
- <术语或句式，尽量保留原文>

**小节命名风格**
- X.Y <小节名>

**公式叙述风格**
> <含公式前后衔接的段落>

**指纹生成者备注**
- <简短总结>
```

Prefer short original excerpts over paraphrase; paraphrase loses style signal.

### Access Ladder

Use the cheapest sufficient source:

1. Load `<active-thesis-root>/.thesis-workflow/reference-thesis-fingerprint.md`.
2. If needed, search the original reference thesis for a short phrase.
3. If still insufficient, read only the relevant chapter or page range.
4. Never load the whole reference thesis without a bounded reason.

## Output Formats

### Diagnosis

```markdown
## 审校结果

### 必改（X 条）

1. 【第 YY 行 / 第 Z 段】命中规则 B2
   原文：<片段>
   建议：<具体改法>

### 建议（X 条）

### 可选（X 条）
```

### Direct Rewrite

- Preserve the author's structure and technical content.
- Change only sentences that fail a rule, logic, grammar, or reference-thesis test.
- Keep BUAA template commands, LaTeX commands, labels, citations, and math environments intact.
- If useful, append a short list of rule IDs touched; do not self-praise.

### Patch

When editing files directly:

- inspect surrounding context before patching;
- avoid changing formulas, citation keys, labels, BUAA structural commands, and macro definitions;
- keep line-level edits narrow;
- run a compile or syntax check when the edited `.tex` file participates in a build.

## Hard Checklist

1. Do not use em dash-style rhetorical breaks; use commas or split sentences.
2. Do not use "一是/二是", "其一/其二", or similar mechanical enumerations in prose.
3. Do not use "X：Y" colon-tail sentences.
4. Do not use "值得注意的是", "不难看出", "综上所述", "本章将", or "首先...其次...最后..." as filler.
5. Replace "进行+名词" where a direct verb is cleaner.
6. Prefer "这是因为" over "原因在于" when causal explanation is needed.
7. Do not announce a framework before giving substance.
8. Do not add warm-up paragraphs before theorems.
9. Do not use bold emphasis inside thesis prose, boxed formulas for emphasis, or emoji.
10. Keep figure-caption prose concise, but preserve BUAA caption placement, numbering, and subfigure conventions.
11. Avoid mechanically stitched titles and self-invented compound terms as section titles.
12. Expand abbreviations at first use.
13. Abstracts should avoid acronym piles, colon chains, and route descriptions connected by dash punctuation.
14. For formula spacing, follow BUAA LaTeX 4.1.0. Do not add extra blank lines after display math in BUAA thesis source.
15. Proofs should not be organized as "分三部分" or `(1)(2)(3)` unless the template or discipline explicitly requires it.
16. Keep long Chinese sentences under control; vary adjacent sentence openings.
17. Let numbers carry conclusions; avoid "可以看出" before results and vague "验证了有效性" after them.
18. Never copy discussion with the user into thesis prose.
19. Align polishing with the configured reference thesis and revise conservatively.
20. Chapter summaries should be compact and thesis-like, but any required heading, numbering, or structural format follows BUAA.

## Common Traps

- Removing AI tone by making the prose too casual or too shallow.
- Copying the user's planning language into the manuscript.
- Rewriting fluent authorial prose only to replace words with synonyms.
- Creating precise-looking but nonstandard terms when accepted field terminology exists.
