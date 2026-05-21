#!/usr/bin/env python3
"""Extract reusable thesis assets from LaTeX paper sources.

The script is intentionally conservative: it preserves raw snippets and source
locations instead of trying to fully expand TeX macros.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ENV_PATTERN = re.compile(
    r"\\begin\{(?P<env>equation\*?|align\*?|gather\*?|multline\*?|eqnarray\*?|algorithm\*?|algorithmic\*?|figure\*?|table\*?)\}"
    r"(?P<body>.*?)"
    r"\\end\{(?P=env)\}",
    re.DOTALL,
)
LABEL_PATTERN = re.compile(r"\\label\{([^}]+)\}")
REF_PATTERN = re.compile(r"\\(?:ref|eqref|autoref|cref|Cref)\{([^}]+)\}")
CITE_PATTERN = re.compile(
    r"\\(?:cite|citep|citet|citealp|parencite|textcite|autocite)"
    r"(?:\[[^\]]*\]){0,2}\{([^}]+)\}"
)
INCLUDEGRAPHICS_PATTERN = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}")
CLAIM_MARKERS = (
    "本文提出",
    "本文设计",
    "本文构建",
    "本文证明",
    "实验结果",
    "结果表明",
    "验证了",
    "证明了",
    "we propose",
    "we present",
    "we introduce",
    "we demonstrate",
    "we show",
    "results show",
    "experiments demonstrate",
)


@dataclass(frozen=True)
class SourceFile:
    path: Path
    relpath: str
    text: str
    line_starts: list[int]

    @classmethod
    def load(cls, path: Path, root: Path) -> "SourceFile":
        text = path.read_text(encoding="utf-8", errors="replace")
        starts = [0]
        starts.extend(match.end() for match in re.finditer(r"\n", text))
        return cls(path=path, relpath=path.relative_to(root).as_posix(), text=text, line_starts=starts)

    def line_for_offset(self, offset: int) -> int:
        lo, hi = 0, len(self.line_starts)
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if self.line_starts[mid] <= offset:
                lo = mid
            else:
                hi = mid
        return lo + 1


def normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def parse_balanced_arg(text: str, start: int) -> tuple[str, int] | None:
    brace = text.find("{", start)
    if brace < 0:
        return None
    depth = 0
    for index in range(brace, len(text)):
        char = text[index]
        if char == "{" and (index == 0 or text[index - 1] != "\\"):
            depth += 1
        elif char == "}" and (index == 0 or text[index - 1] != "\\"):
            depth -= 1
            if depth == 0:
                return text[brace + 1 : index], index + 1
    return None


def command_arg(text: str, command: str) -> str | None:
    command_match = re.search(rf"\\{re.escape(command)}(?:\[[^\]]*\])?", text)
    if not command_match:
        return None
    parsed = parse_balanced_arg(text, command_match.end())
    if not parsed:
        return None
    return normalize_space(parsed[0])


def context_around(text: str, start: int, end: int, radius: int = 180) -> str:
    left = max(0, start - radius)
    right = min(len(text), end + radius)
    return normalize_space(text[left:right])


def topic_tags(text: str, topics: Iterable[str]) -> list[str]:
    lowered = text.lower()
    return [topic for topic in topics if topic.lower() in lowered]


def tex_files(root: Path) -> list[Path]:
    ignored_parts = {".git", "build", "dist", "output", "outputs", "node_modules"}
    files = []
    for path in root.rglob("*.tex"):
        if ignored_parts.intersection(path.parts):
            continue
        files.append(path)
    return sorted(files)


def extract_environments(source: SourceFile, topics: list[str]) -> tuple[list[dict], list[dict], list[dict]]:
    equations: list[dict] = []
    algorithms: list[dict] = []
    figures: list[dict] = []

    for match in ENV_PATTERN.finditer(source.text):
        env = match.group("env")
        body = match.group("body")
        start_line = source.line_for_offset(match.start())
        end_line = source.line_for_offset(match.end())
        labels = LABEL_PATTERN.findall(match.group(0))
        item = {
            "id": f"{source.relpath}:{start_line}-{end_line}:{env}",
            "type": env.rstrip("*"),
            "source_file": source.relpath,
            "start_line": start_line,
            "end_line": end_line,
            "labels": labels,
            "raw": match.group(0).strip(),
            "topic_tags": topic_tags(body, topics),
        }
        if env.rstrip("*") in {"equation", "align", "gather", "multline", "eqnarray"}:
            item["context"] = context_around(source.text, match.start(), match.end())
            equations.append(item)
        elif env.rstrip("*") in {"algorithm", "algorithmic"}:
            item["caption"] = command_arg(body, "caption")
            algorithms.append(item)
        elif env.rstrip("*") in {"figure", "table"}:
            item["caption"] = command_arg(body, "caption")
            item["graphics"] = INCLUDEGRAPHICS_PATTERN.findall(body)
            figures.append(item)

    return equations, algorithms, figures


def extract_citations(source: SourceFile, topics: list[str]) -> list[dict]:
    citations: list[dict] = []
    for match in CITE_PATTERN.finditer(source.text):
        keys = [key.strip() for key in match.group(1).split(",") if key.strip()]
        citations.append(
            {
                "source_file": source.relpath,
                "line": source.line_for_offset(match.start()),
                "keys": keys,
                "context": context_around(source.text, match.start(), match.end()),
                "topic_tags": topic_tags(context_around(source.text, match.start(), match.end()), topics),
            }
        )
    return citations


def extract_claims(source: SourceFile, topics: list[str]) -> list[dict]:
    claims: list[dict] = []
    sentence_pattern = re.compile(r"[^。！？.!?\n]*(?:。|！|？|\.|!|\?)")
    for match in sentence_pattern.finditer(source.text):
        sentence = normalize_space(match.group(0))
        lowered = sentence.lower()
        if any(marker in sentence or marker in lowered for marker in CLAIM_MARKERS):
            claims.append(
                {
                    "source_file": source.relpath,
                    "line": source.line_for_offset(match.start()),
                    "text": sentence,
                    "topic_tags": topic_tags(sentence, topics),
                }
            )
    return claims[:300]


def extract_refs(source: SourceFile) -> tuple[set[str], list[dict]]:
    labels = set(LABEL_PATTERN.findall(source.text))
    refs = [
        {
            "source_file": source.relpath,
            "line": source.line_for_offset(match.start()),
            "target": match.group(1),
            "context": context_around(source.text, match.start(), match.end(), radius=90),
        }
        for match in REF_PATTERN.finditer(source.text)
    ]
    return labels, refs


def write_json(path: Path, data: object) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract structured assets from LaTeX paper sources.")
    parser.add_argument("--source", required=True, help="Directory containing prior paper .tex files.")
    parser.add_argument("--output", required=True, help="Directory for generated JSON assets.")
    parser.add_argument("--topic", action="append", default=[], help="Optional topic tag. Can be repeated.")
    args = parser.parse_args()

    source_root = Path(args.source).expanduser().resolve()
    output_root = Path(args.output).expanduser().resolve()
    if not source_root.exists() or not source_root.is_dir():
        raise SystemExit(f"Source directory does not exist: {source_root}")

    output_root.mkdir(parents=True, exist_ok=True)
    sources = [SourceFile.load(path, source_root) for path in tex_files(source_root)]

    equations: list[dict] = []
    algorithms: list[dict] = []
    figures: list[dict] = []
    citations: list[dict] = []
    claims: list[dict] = []
    all_labels: set[str] = set()
    all_refs: list[dict] = []

    for source in sources:
        eqs, algs, figs = extract_environments(source, args.topic)
        equations.extend(eqs)
        algorithms.extend(algs)
        figures.extend(figs)
        citations.extend(extract_citations(source, args.topic))
        claims.extend(extract_claims(source, args.topic))
        labels, refs = extract_refs(source)
        all_labels.update(labels)
        all_refs.extend(refs)

    unresolved_refs = [ref for ref in all_refs if ref["target"] not in all_labels]
    summary = {
        "source": str(source_root),
        "tex_files": len(sources),
        "equations": len(equations),
        "algorithms": len(algorithms),
        "figures_and_tables": len(figures),
        "citations": len(citations),
        "claims": len(claims),
        "labels": len(all_labels),
        "refs": len(all_refs),
        "unresolved_refs": len(unresolved_refs),
        "topics": args.topic,
    }

    write_json(output_root / "equations.json", equations)
    write_json(output_root / "algorithms.json", algorithms)
    write_json(output_root / "figures.json", figures)
    write_json(output_root / "citations.json", citations)
    write_json(output_root / "claims.json", claims)
    write_json(output_root / "references.json", {"labels": sorted(all_labels), "refs": all_refs, "unresolved_refs": unresolved_refs})
    write_json(output_root / "summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
