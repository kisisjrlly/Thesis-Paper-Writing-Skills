# buaa-format-authority

Use this file as the highest-priority formatting authority for this skill. The user is a BUAA student; formatting must follow `北航硕博士学位论文模版-LaTeX 4.1.0` and its bundled writing/template instructions. Imported rules from `graduate-thesis-polish-and-write-skill` are prose-style heuristics only and must not override BUAA formatting.

## Precedence

When rules conflict, apply this order:

1. The user's explicit BUAA/supervisor/college requirement.
2. `北航硕博士学位论文模版-LaTeX 4.1.0` files and docs, especially `博士毕设论文/README.md`, `博士毕设论文/main.tex`, `博士毕设论文/def/buaa.cls`, and the bundled writing-spec PDFs.
3. `patterns/patterns-latex.md`.
4. Local project conventions already present in the user's thesis source.
5. Prose-style guidance from `references/thesis-polish-protocol.md` and `patterns/*`.

Do not import another school's layout, sectioning, spacing, caption, or formula-format habits into BUAA thesis source.

## BUAA LaTeX 4.1.0 Rules

- Compile with XeLaTeX.
- Keep the BUAA `\documentclass[...] {def/buaa}` structure and options. Select thesis type, permission, print type, OS type, title length, and subject type through the documented class options instead of ad hoc formatting changes.
- Use the template-provided front-matter commands such as `\Title`, `\Subtitle`, `\Branch`, `\Degree`, `\Department`, `\Major`, `\Tutor`, `\Author`, date commands, `\Abstract`, `\Keyword`, `\Signs`, and `\Abbreviations`.
- Use `\Signs` for the main symbol table and `\Abbreviations` for abbreviation descriptions. Do not merge them back into one generic section.
- Use `\emptypage` for manual no-page-number blank pages. Do not use the removed `\beginright` command.
- Use `\Bib{def/GBT7714-2015.bst}{ref.bib}` or `\Bib{def/GBT7714-2015-NoWarning.bst}{ref.bib}` for the GB/T 7714 bibliography style.
- If references do not appear, run the bibliography step and rebuild with XeLaTeX rather than rewriting citation commands.
- Do not add extra blank lines after `equation`, `align`, `gather`, or similar display math environments. BUAA 4.1.0 explicitly warns that this can make the spacing before the following text too large.
- For subfigures, use the template's current `subcaption`-style commands and examples. Do not reintroduce obsolete `subfigure` usage.
- For tables requiring heavier three-line rules, use `\toprule[]`, `\midrule[]`, and `\bottomrule[]`.
- Avoid adding packages that duplicate or fight with packages already embedded in `buaa.cls`. Inspect the template first.
- Prefer minimal local fixes over formatting rewrites. If spacing looks wrong because of figure placement, consider the template README's advice such as inserting `\newpage` before the cramped line, then compile-check.

## What The Imported Polish Rules May Control

The integrated polish protocol may control:

- AI-tone diagnosis;
- sentence concision;
- translation-tone cleanup;
- terminology consistency;
- conservative rewriting;
- chapter/section prose coherence;
- caption wording, as long as BUAA caption placement and LaTeX structure remain intact.

It may not control:

- page layout, margins, line spacing, font size, title formats, table of contents indentation, cover/title page layout, abstract keyword formatting, page headers/footers, appendix numbering, reference layout, symbol/abbreviation section structure, figure/table numbering format, or formula spacing when BUAA specifies otherwise.

## Editing Checklist

Before editing BUAA thesis `.tex` files:

1. Locate the active `main.tex` and confirm it uses the BUAA class.
2. Read relevant nearby template examples before changing macros or environments.
3. Preserve BUAA structural commands and existing labels/citations.
4. Apply prose polish inside paragraph text only unless the user asked for format repair.
5. Compile with XeLaTeX, or report why compilation was not run.
