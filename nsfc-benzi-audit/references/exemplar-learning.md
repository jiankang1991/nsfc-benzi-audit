# Learning From Funded Examples

Use this reference when the user provides already-funded or successful NSFC examples ("中的本子", "中标本子", "已获资助申请书") or asks to improve this skill from sample applications.

## Purpose

Extract transferable proposal-quality patterns, not reusable text. A funded example is evidence of a working application style under a context; it is not proof that any single phrase, section order, or rhetorical tactic caused funding.

## Intake Rules

Before analyzing examples:

- Use supplied examples within the diagnosis or improvement scope already authorized by the user. Clarify intended use only if ambiguous; do not re-request permission already supplied.
- Redact names, project numbers, institutions, phone/email, unpublished data identifiers, exact budgets, confidential collaborations, and sensitive achievements unless the user explicitly says they are already public.
- Keep project type, year, broad discipline/application code, research attribute, career stage, and result status if available; these fields are needed for comparison.
- Separate `exemplars` from the `target draft`. Do not diagnose a target by silently merging its facts with exemplar facts.

If confidentiality is unclear, summarize patterns without quoting source text.

## Match Before Generalizing

Match the dimensions that affect the particular inference; counting any two matches is not enough. The same year/category does not make a field-specific evidence requirement transferable to another kind of research:

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
2. Identify any consequential differences after checking whether the target already supplies equivalent evidence. There may be no gap, and no quota of three is required.
3. Convert each gap into a revision action: restructure, refocus, add evidence, remove unsupported claim, or rewrite a skeleton.
4. Keep suggestions fact-free unless the target draft provides the fact. Use placeholders such as `[具体对象]`, `[关键变量]`, `[前期证据]`.

Do not say "中标本子都这样写, 所以必须这样写." Say "在可比样本中, 较强写法通常把 X 提前显性化; 当前本子在 Y 处还需要补强."

## Improving This Skill From Examples

When the user authorizes skill improvement, separate observation, candidate rule and admitted diagnostic criterion. An observation that a funded example uses a format is evidence that the format occurred; repeated occurrence does not prove its absence is a defect.

For a rule capable of producing a 必改 opinion, maintain a short record:

| Field | What must be explicit |
| --- | --- |
| ID and canonical location | One maintained home; other references link to it rather than restating a stronger version |
| Claim and applicability | What the applicant must actually be claiming for the criterion to apply; relevant year/field/scope |
| Supporting evidence | Source type, available source locator, and why it supports this inference; distinguish formal rule, logical criterion and observed writing preference |
| Exceptions/counterexample | A plausible valid proposal that superficially matches the trigger but must not be rejected |
| Failure and smallest repair | The consequence when the criterion is violated; clarification/claim narrowing may suffice |
| Validation and supersession | Cases used to derive it, independently tested cases, actual outcomes, and any old rule/wording it replaces |

Core coverage/evidence/priority rules belong in [benzi-logic.md](benzi-logic.md); claim-family burdens in [research-claims.md](research-claims.md); official requirements in [current-rules.md](current-rules.md); writing devices in [writing-advice.md](writing-advice.md). Domain references specialize actual evidence conditions. A candidate without adequate support remains a contextual question or sample note, not a high-priority gate.

Before admitting or changing a rule, search the entrypoint, references, report template and examples for the same concept, including contrary exceptions. Update the canonical source and its callers together; remove or narrow the superseded wording instead of appending another override. Retire a rule when its basis is invalidated or its scope no longer applies, recording why.

Validate syntax/resources separately from behavior. Test a substantive failure and a plausible non-failure; at least one input should not have been used to derive the rule. For comparative evaluation, freeze raw materials and scoring criteria before observing outputs, provide the same request and tools to fresh contexts with and without the skill, and judge findings against source evidence. Do not insert the desired diagnosis into the draft text. Record scope, misses, unsupported strong opinions, source locators and usable repairs; output length alone is not quality.

Use synthetic or properly anonymized artifacts for retained tests. Report the source type, scope, supporting/contrasting observations and validation separately. Absorbed-source counts, repeated runs and independently held-out cases are different quantities; none alone establishes accuracy or funding success.

Avoid overfitting:

- Do not turn a single funded application's style into a universal rule.
- Do not encode confidential facts, original ideas, or section text.
- Do not replace current official NSFC rules with old-sample conventions.

## Common Rejection Patterns (from real reviewer comments)

Learn from failures as well as successes. These patterns are drawn from published reviewer comments on failed and B-类 near-miss proposals; use them as contrastive questions, not verdicts:

- A failed case had no relevant basis on the target tissue. Use this to ask what evidence supports transfer to the new object, not to require all prior work to be directly on it. Adjacent methods plus credible new-object validation can support a change of direction.
- A mechanism claim supported only by association may leave its causal inference unresolved. Apply CAUSAL to that claim; do not demand a mechanism from a scoped statistical-method study.
- Model/system mismatch: inspect the biological components or scenario conditions needed for the exact claim. An immune model lacking the required component needs reconstitution or complementary evidence; do not reject all immune mechanisms solely from the label 免疫缺陷. See `medical-biomedical.md` for model-specific boundaries.
- Near-miss comments can reveal unaddressed questions, contents not motivated in the rationale or unexplained duplication. Diagnose these substantive issues rather than inferring funding prospects from an A/B label or requiring a fixed number of questions.

## Public, Redaction-Free Calibration Samples

The worked examples printed inside the public guidance books (e.g. 柔索机器人, 废弃煤矿, 受载岩体反馈特性, 高粘度超细粉体, 牻牛儿苗) are already public and may be used as calibration/illustration samples without anonymization — unlike real applicant drafts, which must be redacted. The same applies to the 81 named cases in the NSFC-authored《凝练科学问题案例》(结构超滑, 单原子催化, 交换移植非渐近分析, 静态 CT 安检, 草莓果形, 人机紧耦合人因安全, …) and their named expert commentaries, which back `question-distillation.md`.

kd.nsfc.cn 的结题项目公开中文摘要同样属于这一类（免脱敏），但只反映选题形态，不等于申请书摘要——用法与限制见 `kd-lookup.md`。
