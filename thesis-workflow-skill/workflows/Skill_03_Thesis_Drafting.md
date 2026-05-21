# Skill 03: Thesis Drafting (Core)

## 目标

将小论文资产映射到博士论文模板，按章节渐进式扩写并保持可编译。

## 输入

- 博士论文模板（如北航学位论文 `buaa.cls`、主 `main.tex`、各独立章节 `tex/*.tex`）
- Skill 02 输出的资产 JSON
- 北航格式约束（**必须先查阅 `references/buaa-format-authority.md` 与 `patterns/patterns-latex.md`，以北航硕博士学位论文模版-LaTeX 4.1.0 为最高格式依据**）
- 术语约束与写作风格约束（外校 polish 规则仅用于中文表达和审校，不用于覆盖北航格式）
- 项目画像（优先读取 `references/project-profile.md`，缺失时根据用户确认的信息临时建立）

## 术语锁定（Term Lock）

- 只使用用户确认或 `references/project-profile.md` 中记录的术语锁定。
- 不把某个示例项目的术语当作通用规则。
- 如果同一概念在小论文中出现多个译法，先列出冲突表，再请用户或项目画像确定唯一写法。

## 输出

- 按章节增量生成的论文 `.tex`
- 每章 claim-evidence 对齐表
- 编译日志与修复记录

## 执行步骤（Agent SOP）

1. **大纲映射**
   - 读取 `summary.json`、`equations.json`、`figures.json`、`citations.json`、`claims.json`。
   - 将资产映射到“问题定义—方法—实验—讨论”章节结构。
   - 先形成 chapter outline 和 claim-evidence map，再开始写正文。
2. **章节级循环生成（禁止一口气全量）**
   - 每轮仅处理一个章节。
   - 每章先生成段落骨架，再填充公式、图表与引用。
   - 每节输出前记录将使用的资产 ID 或来源行号。
3. **叙事扩写策略**
   - 将小论文精简表达扩写为博士论文背景、动机与方法细节。
   - 保留数学严谨性，不随意改写符号系统。
   - 使用 `examples/` 学结构，不照搬英文表达。
   - 使用 `patterns/` 约束中文风格，避免 AI 腔和翻译腔；涉及格式时只服从北航模板。
4. **自动编译闭环**
   - 每章完成后触发 `xelatex` 编译。
   - 若失败，解析 `.log` 定位错误并自动修复。
   - 直到“本章增量可编译”再进入下一章。
5. **一致性检查**
   - 术语一致性（drone / constraints / priors）。
   - 图表、公式、引用跨章编号一致。

## 失败处理

- 编译报错（缺包、引用、编码）：优先最小修复，不大改结构。
- 章节过长导致上下文退化：分节切片写作，并回填摘要段。
- 证据不足：自动下调断言强度，标记“待补实验”。
- 术语冲突：停止扩写相关段落，先更新术语锁定表。

## 完成判据（Definition of Done）

- 全文章节可连续编译。
- 关键结论均有实验或理论证据支撑。
- 术语锁定策略在全稿满足一致性。

## 建议交付物

- `thesis/` 下完整源码
- `logs/compile-fixes.md`（编译修复记录）
- `reports/claim_evidence_map.md`
