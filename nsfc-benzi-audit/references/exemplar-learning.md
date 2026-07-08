# Learning From Funded Examples

Use this reference when the user provides already-funded or successful NSFC examples ("中的本子", "中标本子", "已获资助申请书") or asks to improve this skill from sample applications.

## Purpose

Extract transferable proposal-quality patterns, not reusable text. A funded example is evidence of a working application style under a context; it is not proof that any single phrase, section order, or rhetorical tactic caused funding.

## Intake Rules

Before analyzing examples:

- Ask the user to confirm that examples may be used for private skill improvement or diagnosis.
- Redact names, project numbers, institutions, phone/email, unpublished data identifiers, exact budgets, confidential collaborations, and sensitive achievements unless the user explicitly says they are already public.
- Keep project type, year, broad discipline/application code, research attribute, career stage, and result status if available; these fields are needed for comparison.
- Separate `exemplars` from the `target draft`. Do not diagnose a target by silently merging its facts with exemplar facts.

If confidentiality is unclear, summarize patterns without quoting source text.

## Match Before Generalizing

Prefer patterns from examples that match the target along at least two dimensions:

| Dimension | Why it matters |
| --- | --- |
| Project type | Youth, general, regional, and special programs carry different scope and basis expectations. |
| Discipline/application code | Reviewers value different evidence, methods, and writing conventions. |
| Research attribute | Free-exploration and goal-oriented basic research frame scientific questions differently. |
| Applicant stage | Youth projects need focused independence; senior applications can carry broader systems. |
| Funding year | Rules, research-attribute labels, and hot topics change. |

Mark patterns as:

- `可迁移`: repeated across matched examples and useful for the target.
- `条件迁移`: useful only for a similar field, project type, or applicant basis.
- `不可迁移`: tied to a specific dataset, platform, team, facility, or confidential result.
- `样本不足`: observed once and should not become a rule.

## Extraction Grid

For each example, extract concise notes instead of long quotes:

| Surface | What to extract |
| --- | --- |
| Title signal | Object, problem, method/path, and distinctive feature visible in the title. |
| Abstract chain | How quickly the abstract moves from problem to method, contents, innovation, and significance. |
| Scientific question | Whether questions are mechanisms, relations, models, laws, or merely tasks. |
| Rationale convergence | How literature gaps converge on the proposed contents. |
| Content architecture | Whether contents form a mechanism-method-validation chain or independent work packages. |
| Innovation evidence | What comparison makes innovation credible. |
| Research basis mapping | How prior work supports each proposed content without making the project look finished. |
| Feasibility/risk | What data, samples, platforms, controls, alternatives, and milestones are made visible. |
| Reviewer load reduction | Headings, figures, topic sentences, matrices, or summaries that reduce reconstruction effort. |

## Cross-Example Synthesis

After extracting notes, synthesize patterns with this shape:

```markdown
### 中标样本规律提炼

| 规律 | 出现范围 | 可迁移性 | 对当前本子的启发 |
| --- | --- | --- | --- |
|  |  | 可迁移 / 条件迁移 / 不可迁移 / 样本不足 |  |
```

Useful pattern types:

- How successful drafts make the scientific object narrow without making the project trivial.
- How engineering needs are converted into scientific questions.
- How research contents progress from explanation to method to validation.
- How innovation is supported by comparison rather than adjectives.
- How research basis is mapped to future work while preserving unfinished space.
- How figures and headings let a reviewer understand the application quickly.

## Applying Patterns To A Target Draft

Use exemplar patterns as diagnostic contrast:

1. State the matched context: which examples are comparable and why.
2. Identify the top three gaps between successful-example patterns and the target draft.
3. Convert each gap into a revision action: restructure, refocus, add evidence, remove unsupported claim, or rewrite a skeleton.
4. Keep suggestions fact-free unless the target draft provides the fact. Use placeholders such as `[具体对象]`, `[关键变量]`, `[前期证据]`.

Do not say "中标本子都这样写, 所以必须这样写." Say "在可比样本中, 较强写法通常把 X 提前显性化; 当前本子在 Y 处还需要补强."

## Improving This Skill From Examples

When the user's goal is to improve the skill itself:

1. Build a table of repeated patterns and failure contrasts.
2. Add only transferable rules to `references/benzi-logic.md` or `references/audit-surfaces.md`.
3. Put exemplar-specific or field-specific details in a separate reference; do not bloat `SKILL.md`.
4. Use synthetic or heavily anonymized examples if an example must be retained.
5. Re-run basic validation and test with at least one draft that was not used to derive the pattern.
6. If the absorbed sample set changes, update the README `Calibrated` badge count after the skill references are updated.

Avoid overfitting:

- Do not turn a single funded application's style into a universal rule.
- Do not encode confidential facts, original ideas, or section text.
- Do not replace current official NSFC rules with old-sample conventions.

## Common Rejection Patterns (from real reviewer comments)

Learn from failures as well as successes. These patterns are drawn from published reviewer comments on failed and B-类 near-miss proposals; use them as contrastive questions, not verdicts:

- Preliminary work must be *directly* on the proposed object/tissue/target, not merely adjacent. A proposal was rejected because the applicant's prior work was on a different organ than the one the mechanism concerned — "无前期工作基础，也无预实验结果" on the actual object.
- "现象观察层次" scores low: staying at observed correlation/phenomenon without a deeper mechanism draws "创新性较低".
- Model/system mismatch: the model must convincingly represent the disease/scenario claimed (e.g. an immunodeficient model cannot prove an immune mechanism; a cell-line-only result "欠缺说服力" for an in-vivo claim).
- Even a well-liked B-类 fails on the half-vote at 会评. Its typical sinking specifics: too many scientific questions, some research contents not set up in the literature review, and self-repetition ("同一对象在同一疾病中不同作用机制"). So: trim questions, ground every content in the rationale, and avoid restating the same story.

## Public, Redaction-Free Calibration Samples

The worked examples printed inside the public guidance books (e.g. 柔索机器人, 废弃煤矿, 受载岩体反馈特性, 高粘度超细粉体, 牻牛儿苗) are already public and may be used as calibration/illustration samples without anonymization — unlike real applicant drafts, which must be redacted.
