# Skill 02: Asset Extraction

## 目标

从多篇小论文 LaTeX 源码中无损提取可复用核心资产，避免扩写时丢失数学与实验细节。

## 输入

- 小论文源码目录（含 `.tex`、图像、`.bib`）
- 主题标签（如 `differentiable simulation`、`differentiable perception`）
- 资产输出目录

## 输出

- `assets/equations.json`：公式及其上下文
- `assets/algorithms.json`：伪代码 / 算法块
- `assets/figures.json`：图表路径、标题、引用关系
- `assets/citations.json`：引用键与首次出现位置
- `assets/claims.json`：关键论断及证据锚点
- `assets/references.json`：标签、引用与悬空引用
- `assets/summary.json`：抽取统计与告警摘要

## 执行步骤（Agent SOP）

1. **扫描与索引**
   - 遍历所有 `.tex` 文件并建立章节-文件映射。
2. **运行确定性抽取脚本**
   - 优先调用：
     ```bash
     python thesis-workflow-skill/scripts/extract_latex_assets.py --source <小论文源码目录> --output <资产输出目录>
     ```
   - 有主题标签时追加 `--topic "<主题>"`，可重复多次。
3. **结构化复核**
   - 抽取 `equation/align/gather` 环境与标签。
   - 抽取 `algorithm/algorithmic` 环境。
   - 抽取 `figure/table` 环境、caption、label、图像路径。
   - 抽取 `\cite{}` 键值及上下文句子。
4. **语义打标**
   - 识别与主题相关资产并打标签（task、method、assumption、evidence）。
   - 脚本只能给出初步 topic tags；最终 claim-evidence 关系需要人工/Agent 复核。
5. **一致性检查**
   - 校验标签引用是否悬空（`\ref` 指向缺失）。
   - 校验图像路径是否存在。
   - 查看 `references.json` 中的 `unresolved_refs`。
6. **写出中间件**
   - 统一写入 JSON，保留原文片段、源文件位置、行号范围。
   - 不覆盖人工维护的资产注释；需要重跑时写入新目录或先确认。

## 失败处理

- 宏展开导致解析失败：保留原始片段并记录 `parse_warning`。
- 多文件交叉引用缺失：增加 `unresolved_refs` 列表。
- 图像路径不存在：打标 `missing_asset=true`，不阻断流程。

## 完成判据（Definition of Done）

- 关键资产均可在 JSON 中追溯到源文件。
- 无未记录的解析错误。
- 输出可直接被 Skill 03 消费。
- `summary.json` 已被阅读，悬空引用和缺失图片已进入告警列表。

## 交付格式（建议）

- 资产统计表（公式/图表/伪代码/引用）
- 解析告警列表
- 下一步建议（进入 `Skill_03_Thesis_Drafting.md`）
