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

Ranked 形式审查 checklist (most-frequent failure first — verify current-year specifics):

- 人员超项 (members over the concurrent-project limit) — the single most common 形审 rejection.
- Wrong 申请代码 (routes to the wrong 学部).
- 依托单位 / 公章 inconsistency; missing or non-handwritten signature (笔迹一致).
- Missing attachments: 伦理批件; two recommendation letters when the applicant has only a mid-level title and no doctorate; in-station postdoc consent letter; biosafety commitment; the "≤5 related papers" attachment limit.

Keyword-reconstruction test: the keyword list should let a reader rebuild the draft's main thread. Flag first-level discipline names and over-broad words (安全、保护、曲线、工程) used as keywords; the second application code carries little weight while a wrong first code is costly.

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
- Cliché openers that carry no information: "随着我国经济迅速发展……", "随着大数据时代的到来……" and similar.

Reviewer-impression check ("酒香也怕巷子深"): a skimming reviewer should catch the load-bearing claims without slow reading. Check whether the key scientific question, the scientific hypothesis, preliminary results, and the distinctive feature are bold-highlighted, backed by one key-data figure, and reinforced by citing the applicant's own related papers.

Concept-precision check: inconsistent or misused core concepts are cited as 函评 deductions. Watch high-frequency confusions — 强度 ≠ 稳定性, 机理 ≠ 规律, over-narrowing 本构关系 to stress-strain, and 耦合 used without saying which variables couple, how, and how they are decoupled for solution. A single mixed-terminology case (e.g. "2型糖尿病" and "Ⅱ型糖尿病" both used) has been cited by a reviewer as a reason to withhold funding in a competitive year — so terminology consistency is not always a low-priority polish item.

## Figure And Visual Evidence

Figures should reduce reviewer effort, not decorate the draft.

Check for:

- Overview/concept figure: shows object, problem, method/path, contents, and expected output.
- Research content relationship figure: shows how tasks depend on or support each other.
- Technical route figure: maps each research content to method, data/sample, experiment/model, validation, and expected result.
- Research basis figure/table: maps prior work to proposed tasks without implying the project is already completed.
- Annual plan/Gantt-style figure: milestones are concrete and aligned with research contents.

Strong figures often act as navigation: a reviewer should be able to reconstruct "why these contents, in this order, with these data and expected outputs" from the figure plus nearby paragraph.

Conventions strong drafts reliably follow (expect these; flag their absence):

- One 研究思路/总体框架图 that maps 对象/需求 → 挑战 → 关键科学问题 → 研究内容 → 目标 (→ 验证) in a single graph. A draft that presents research contents as prose with no framework figure is a real finding.
- A 总-分 技术路线图 with swimlanes (e.g. 结构/科学问题/内容/方法/成果) as a clean framework diagram, not prose. Prefer 框架图 form so 研究对象、建模/实验方法、分组、观察指标、检测方法、研究目标 are 一目了然.
- One method flowchart per 研究内容; a 总图 + 分图 split is fine.
- For content chains that are bidirectional / 协同 / feedback, the content-architecture figure should show feedback arrows, not a straight pipeline.
- A 立项依据示意图 using 实线=known / 虚线(或问号)=hypothesis — the dashed part is the project's innovation.
- Research design principles to check in the route figure: 随机、对照、重复 where the field expects them.

Annual-plan do's and don'ts: 4-6 lines per year, layered; do not spend dedicated time on "购买试剂 / 查阅文献 / 预试验" or "结题 / 整理资料 / 撰文"; schedule long-lead work (model building, animal-model prep, patient enrollment) early.

Figure-fidelity caveat: when the source is a converted/extracted draft (e.g. mineru), a 流程图/示意图 may be re-rendered as broken mermaid or lost. Do not judge figure logic from a mangled mermaid block — consult the original image (the `images/` directory) before flagging figure-logic problems, and note extraction loss as a limitation rather than an applicant mistake.

Flag:

- Figures not mentioned or explained in nearby text.
- Figure logic contradicts the written research contents.
- Overloaded "八卦图 / 迷魂阵" figures — too many boxes, arrows, colors, or abbreviations that dazzle rather than guide.
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

## Key Project And Platform-Heavy Drafts

Use this surface for 重点项目, large-team projects, or drafts whose outputs include datasets, knowledge bases, software platforms, prototype systems, maps, atlases, standards, or field demonstrations.

Check:

- Whether the enlarged scope is justified by one central scientific problem rather than by a list of deliverables.
- Whether each subtask has a scientific role: shared data/knowledge foundation, representation/model, fusion/optimization/control, evaluation/feedback, or scenario validation.
- Whether team members, platforms, data sources, and field sites map to subtasks instead of being listed as general strength.
- Whether expected outputs such as datasets, maps, systems, software, or atlases are used to test scientific claims, not only to show workload.
- Whether annual plans show dependency and integration milestones, not just parallel subteam schedules.

Flag:

- A broad "system construction" project with no unifying model, mechanism, representation, taxonomy, or law.
- Many modules named by technology or deliverable, but no explanation of why they must be studied together.
- Platform/data outputs whose quality metrics, openness, annotation rules, uncertainty, or validation use are unclear.
- A team basis section that proves general strength but not who can solve which proposed bottleneck.

## Literature And Current Status

The literature review should support the argument for this project, not merely prove the applicant read papers.

Check:

- Recent literature is represented where the topic is fast-moving.
- Foundational/classic work is present when needed.
- Domestic and applicant's own prior work are positioned appropriately, not overused.
- Each literature subsection ends with a gap that points to one proposed research content or scientific question.
- The cited limitations are specific: mechanism unknown, model not valid under certain conditions, data/source mismatch, unresolved relation, missing validation, etc.

Reference rules of thumb (adjust to field norms):

- Roughly 20-30 references is a healthy band; far fewer suggests the applicant has not read the field.
- Include the newest work (submission year or the year before) and authoritative-venue work; too old-only reads as out of touch.
- Include some of the applicant's/group's own related papers, but do not over-cite them.
- English references may dominate, but keep some Chinese ones — most 通讯评审 reviewers are domestic.
- Each cited claim must be tied to a specific in-text citation point in the rationale, not just listed at the end.

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
