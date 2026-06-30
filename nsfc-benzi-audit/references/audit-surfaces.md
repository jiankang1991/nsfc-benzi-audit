# Supplementary Audit Surfaces

Use this reference when the user asks for a full diagnosis or when the draft includes enough material to check more than core scientific logic. These checks are inspired by common NSFC preparation workflows, but all rule-sensitive points must be verified against current official NSFC documents before being stated as binding.

## Structure And Form

Check whether the draft preserves the application form's required columns and expected section boundaries. Do not claim a heading is mandatory unless verified against the current annual guide or application template.

Look for:

- Missing or renamed major sections in the provided draft.
- Empty subsections or unfinished-marker text left in the draft.
- Project category, research attribute, application code, keywords, budget, duration, and team information not reflected consistently in the narrative.
- Ongoing projects, completed NSFC projects, representative works, collaborations, ethics/safety, and other explanatory fields that appear relevant but are absent from the provided material.
- Attachments or figures referenced in text but missing from extraction.

Report as:

- `规则风险`: only when verified against official current-year documents.
- `形式风险`: when the provided draft appears incomplete or internally inconsistent but official status was not checked.
- `材料缺口`: when more source files are needed before judging.

## Fast-Read Path

Assume reviewers may first form an impression from title, abstract, headings, figures, and research basis. Diagnose whether those elements communicate the proposal without requiring slow reconstruction.

Check:

- Title and abstract expose the same object, problem, method/path, and contribution.
- Headings are informative and parallel.
- Key claims are visible in topic sentences, not buried in long paragraphs.
- The proposal can be understood from title + abstract + rationale summary + one overview figure.
- Terminology remains consistent across sections.
- Research-content headings expose the dependency chain, not only method names.
- Research basis visibly supports the proposed contents before the reviewer has to search for it.

Flag:

- Long paragraphs without topic sentences.
- Important innovations first appearing late in the draft.
- Repeated background that delays the scientific question.
- Overuse of slogans such as "重大意义", "国际领先", "填补空白", or unsupported "首次".

## Figure And Visual Evidence

Figures should reduce reviewer effort, not decorate the draft.

Check for:

- Overview/concept figure: shows object, problem, method/path, contents, and expected output.
- Research content relationship figure: shows how tasks depend on or support each other.
- Technical route figure: maps each research content to method, data/sample, experiment/model, validation, and expected result.
- Research basis figure/table: maps prior work to proposed tasks without implying the project is already completed.
- Annual plan/Gantt-style figure: milestones are concrete and aligned with research contents.

Strong figures often act as navigation: a reviewer should be able to reconstruct "why these contents, in this order, with these data and expected outputs" from the figure plus nearby paragraph.

Flag:

- Figures not mentioned or explained in nearby text.
- Figure logic contradicts the written research contents.
- Overloaded figures with too many boxes, arrows, colors, or abbreviations.
- Low-resolution screenshots, illegible labels, inconsistent numbering, or mismatched terminology.
- Figures list modules but omit dependencies, validation data, or expected outputs.

## Evidence And Validation Resources

Use this surface when the draft depends on datasets, samples, instruments, computing resources, platforms, collaborations, field sites, or application scenarios.

Check:

- Each research content has at least one credible evidence/resource basis.
- Preliminary work is mapped to future tasks, not just listed by paper count.
- Data/sample access is concrete: source, scale, representativeness, preprocessing/annotation, permissions, and continuity.
- Validation plan names baselines, metrics, controls, comparisons, or application cases appropriate to the field.
- Computing/instrument/platform needs match the methods and budget.
- Collaborations are specific enough to support access, expertise, or verification.

Flag:

- "数据丰富", "平台完备", "基础扎实" without task-level mapping.
- Feasibility rests on a collaborator or platform that is not evidenced in the provided material.
- Validation uses only a convenient demonstration case and cannot test the core scientific claim.
- Preliminary evidence is so complete that reviewers may ask what remains to be funded.

## Literature And Current Status

The literature review should support the argument for this project, not merely prove the applicant read papers.

Check:

- Recent literature is represented where the topic is fast-moving.
- Foundational/classic work is present when needed.
- Domestic and applicant's own prior work are positioned appropriately, not overused.
- Each literature subsection ends with a gap that points to one proposed research content or scientific question.
- The cited limitations are specific: mechanism unknown, model not valid under certain conditions, data/source mismatch, unresolved relation, missing validation, etc.

Flag:

- Chronological lists without synthesis.
- Claims that "few studies exist" without evidence.
- Missing comparison with obvious competing methods or adjacent fields.
- Literature gaps that do not lead to the proposed method.
- Reference formatting inconsistency if references are provided.

Do not invent missing papers. If the literature appears weak, suggest search directions and keywords rather than fabricating citations.

## Policy And Integrity Triage

For policy-related issues, route to `references/current-rules.md` and verify with official sources before final wording.

Common triage items:

- Current-year project type and eligibility.
- Application code and research attribute consistency.
- AI-assisted writing declaration or other current-year AI-use requirements.
- Scientific integrity: no fabricated references, data, preliminary work, achievements, authorship, or collaborations.
- Ethics, biosafety, data security, human/animal subjects, geographic/sensitive data, field sampling, and collaboration commitments where relevant.
- Budget and missing-condition consistency.

Report uncertain issues as "需申请人按当年指南确认", not as definitive rule violations.

## Output Pattern

For each supplementary surface, keep findings short:

```markdown
### 形式与栏目完整性
- 风险：
- 依据：
- 建议：

### 图表与可读性
- 风险：
- 依据：
- 建议：

### 数据、验证与研究基础映射
- 风险：
- 依据：
- 建议：

### 文献与研究现状
- 风险：
- 依据：
- 建议：

### 政策与科研诚信
- 风险：
- 核查状态：
- 建议：
```
