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
- For a draft claiming a new observation dimension or a measurement beyond an existing limit, the load-bearing preliminary figure is a **对照式实证图**: the same target rendered in the incumbent representation (where the effect is invisible) beside the proposed one (where it is obvious), plus an independent reference — optical/ground truth, or a simulation with known input whose predicted curve is overlaid on the observed one. One such panel does more work than a page of sensitivity prose. Its absence in a "new modality" draft is a real finding, because nothing else can show that the claimed signal exists in real data.

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

## Annual Plan And Expected Outcomes

Use this surface whenever the draft contains 年度研究计划 or 预期研究结果. It is where reviewers test whether the plan is executable and whether the applicant knows their own capacity.

年度计划 checks:

- 4-6 lines per year, layered, each traceable to a research content.
- Do not spend dedicated schedule time on 购买试剂 / 查阅文献 / 预试验 or on 结题 / 整理资料 / 撰文 — those are not research progress.
- Long-lead work (model building, animal-model prep, patient enrollment, data campaign, field season) is scheduled early.
- Dependencies in the content chain are respected: a content consuming another's output cannot start in the window that output is produced.
- The year-by-year effort implied by the schedule matches the budget's year distribution.

预期成果 checks:

- Outcomes are split by scientific question, not by count. "SCI 6 篇 / 专利 2 项 / 硕士 3 名" is a workload indicator, not a scientific product; the strong form names, for each key scientific question, what will be known, established, or made verifiable.
- Outcome scale must be defensible against the demonstrated basis — this is canonical 通讯评议 negative comment #5 (预期成果过高) in `current-rules.md`. Before flagging counts as over-promised, calibrate them against same-code same-category 结题项目 with lookup 3 in `kd-lookup.md`; the measured band clears a suspected over-promise as often as it confirms one.
- Deliverables such as datasets, software, platforms, standards, or atlases must say how they test a scientific claim, not only that they will be produced (see the key-project surface above).

Priority calibration: funded drafts routinely break the finer rules above — a bare 3-line-per-year plan, "撰写结题报告" occupying the last year, count-style 预期成果 — and are funded anyway. Keep these as low-priority polish unless the plan also breaks a content dependency, contradicts the research basis, or schedules long-lead work late. What actually distinguishes a strong 预期成果 block is the *ordering*: named scientific products first (物理模型 / 理论方法 / 判据 / 精度界 / 数据集), counts after. Do not lead an audit with annual-plan nitpicks.

Flag:

- An annual plan that restates the research contents once per year with no progression.
- Outcomes that promise what the research basis already delivers.
- Milestones with no verification event — no comparison, no baseline, no validation scene.

## Budget And Task Mapping

Use this surface when the draft includes 预算表, 预算说明, or a 经费需求 discussion. Budget is a logic surface, not only a compliance one: reviewers read it as a second statement of what the project actually plans to do, so a budget that disagrees with the research plan damages both.

Map every budget line to a research content or technical-route step, the same way 研究基础 is mapped:

| 预算科目 | 金额 | 对应的研究内容/方案步骤 | 测算依据 | 缺口 |
| --- | --- | --- | --- | --- |

Check:

- Each 科目 traces to a named research content or plan step. A line item serving no content is padding, or evidence of a task the draft never stated.
- Conversely, each content needing data, samples, computing, testing, fieldwork, or fabrication has a line behind it. A content that costs nothing is a common tell that it was added for structure, not for execution.
- 设备费 scale matches the project type; a 青年 draft buying large instruments is a mismatch.
- 测试化验加工费, data acquisition/annotation, and 机时 match the data and validation scale claimed in 研究方案.
- 劳务费 matches the team size and duration described in 研究基础.
- 合作转拨/外拨 implies a named collaborator whose role is visible in 研究方案 and 研究基础.
- 工作条件 and 预算 agree on what must be purchased versus what already exists.

For the rule side — 直接/间接费用 boundary, the 差旅费+会议费+国际合作交流费 测算依据 threshold, 万元 formatting — use `current-rules.md`. Do not restate amounts, caps, or 科目 names here, and report them as 需申请人按当年指南确认.

Do not invent 测算依据, equipment prices, or collaborator shares. When a number carries no stated basis, report it as 依据缺失 and leave the number to the applicant.

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

Empty-field rationale (when the research proposition really is new). "经广泛文献调研，暂未发现针对……的研究报道" cannot be *reviewed* — there is nothing there to survey. Do not stop at flagging the claim; check whether the draft replaces the missing survey with the four neighborhoods that bound the gap:

1. 物理/理论溯源 — the home field the idea is borrowed from, with its classic literature and the invariance that licenses the transfer (pair with the 跨域类比三件套 in `question-distillation.md`).
2. 邻近建模工作 — what existing models of the *same object* do cover, and the structural reason they cannot cover this: the strong form shows the gap is by construction (the incumbent model class only admits mechanism A, so the mechanism this project studies falls outside its assumptions), not merely unstudied.
3. 同现象的定性工作 — who has already *seen or displayed* the phenomenon without quantifying it, which converts "no one studied this" into the far stronger "the phenomenon is known, the quantitative mapping is missing".
4. 现有主流手段的物理局限 — the incumbent competitor's limits argued from its operating principle (what it must assume, what it must repeat, which theoretical limit bounds it), not from its measured performance.

A bare 空白声明 carrying none of the four is the real finding. Route the claim itself to the 撞题核查 in `kd-lookup.md`; note that recent funded projects sit in the 结题库 blind spot, so a null lookup does not confirm the blank.

Do not invent missing papers. If the literature appears weak, suggest search directions and keywords rather than fabricating citations.

## Policy And Integrity Triage

For policy-related issues, route to `references/current-rules.md` and verify with official sources before final wording.

Common triage items:

- Current-year project type and eligibility.
- Application code and research attribute consistency.
- AI-assisted writing declaration or other current-year AI-use requirements.
- Scientific integrity: no fabricated references, data, preliminary work, achievements, authorship, or collaborations.
- Ethics, biosafety, data security, human/animal subjects, geographic/sensitive data, field sampling, and collaboration commitments where relevant.
- Budget rule compliance only — amounts, caps, 科目 names, and formatting. The budget-to-task logic check lives in `Budget And Task Mapping` above; keep the two findings separate.

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

### 年度计划与预期成果
- 风险：
- 依据：
- 建议：

### 预算与任务映射
- 风险：
- 依据缺失的科目：
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
