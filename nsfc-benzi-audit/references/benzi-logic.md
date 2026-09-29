# NSFC Application Logic Reference

Use this reference to audit the internal logic of an NSFC application draft. It uses generic proposal-diagnosis language and avoids author-specific labels.

## Diagnosis Dimensions

Assess novelty, technical route, applicant contribution and available resources. A tidy argument can still have weak evidence or an infeasible plan. These are qualitative diagnostic dimensions, not an official scoring formula or a funding forecast. Separate required form fields from optional ways to make evidence visible.

## Signals, Countercheck And Grading

The flags in this reference and its siblings are distilled from funded/rejected proposals, guidance books and expert commentary. Treat each one as a **signal that triggers a check**, not as an automatic verdict and not as something to delete when it has exceptions. Report craft problems (title, abstract, contents written as goals, hollow innovation wording, non-converging rationale): reviewers read these parts hardest, so they belong in the report even when no official rule is broken.

Before grading a candidate as 必改:

1. **Applicability** — does the signal's premise hold for this draft's actual claim, year, category and form?
2. **Countercheck** — search the rest of the supplied material (including original figures and appendices) for the missing link, evidence or explanation.
3. **Evidence boundary** — separate a contradiction visible in the text from an unseen attachment or unverified external fact.
4. **Smallest repair** — narrowing a claim, adding a cross-reference or rewriting a sentence often suffices; do not automatically add experiments or tasks.

| After countercheck | Grade |
| --- | --- |
| Core claim unsupported, key question unanswered, critical step infeasible, verified rule violated, or title/abstract promises an object/condition/result the body never delivers | 必改 |
| Important concern depends on unseen material or an unresolved external fact | 待核实: state the conditional impact |
| Section-level craft or evidence weakness a reviewer is likely to notice (contents written as purpose, hollow 首次/填补空白, rationale not converging, decorative modifier, framework hard to reconstruct) | 建议改 |
| Wording, length, heading style, figure/list counts or an inapplicable exemplar preference | 可润色: group briefly after substantive items |
| Counterevidence resolves it | Drop; if it was a prior finding, withdraw it explicitly |

Give each root issue one stable ID and explain it once; section notes and matrices reference the ID. State impact and evidence certainty separately. A review can legitimately conclude that no 必改 item exists — do not pad the list for balance.

## Scope

This logic is most suitable for 青年基金、面上项目、地区基金 and especially application-oriented basic research in engineering/materials/information-style fields. For information, communication, network, applied AI, security, quantum communication, or data-center drafts, also read `information-communication.md` and translate the logic map into a demand-constraint-model-validation chain. For remote sensing, GIS, geomorphology, spatial data, point cloud, SAR/optical/hyperspectral, video GIS, trajectory, city 3D, or geospatial knowledge-graph drafts, also read `geospatial-remote-sensing.md` and translate the logic map into a spatial-object/data-constraint/model-validation chain. For pure mathematics/theory, management, or special talent programs, keep the framework but soften the engineering examples and check field-specific norms separately. For medicine, clinical, or biomedical drafts, also read `medical-biomedical.md` and translate the logic map into a disease-mechanism-evidence chain.

## Context Calibration

Do not apply one universal writing standard to every application. First calibrate the expected burden of proof:

| Context | Audit emphasis |
| --- | --- |
| 青年项目 | A narrow independent story, 2-3 tightly linked contents, clear applicant ownership, enough basis to start but not evidence that the project is already finished. |
| 面上项目 | A deeper continuation or expansion from prior work, stronger evidence chain, clearer team/data/platform support, and a broader but still coherent system-level contribution. |
| 重点项目/大团队项目 | A broader framework is acceptable, but the draft must show a unified theoretical problem, task dependencies across subteams, shared data/platform resources, and system-level validation. Do not force it into a youth-style narrow story; instead test whether the larger scope is intellectually integrated. |
| 目标导向类基础研究 | Technical or application needs may appear prominently, but the draft must still extract a model, mechanism, relation, representation, optimization, evaluation, or law under concrete conditions. |
| 自由探索类基础研究 | Scientific question originality and conceptual depth carry more weight than immediate application scenario. |
| Application-code-heavy fields | Object, method, data, and validation scene should visibly match the selected application code and likely reviewer community. |

For goal-oriented projects, do not reject a draft merely because the wording mentions performance, prediction, detection, platform, or application. Diagnose whether it converts a task into a constrained scientific problem: `specific object + specific data/condition + specific bottleneck + model/mechanism/method question + verifiable outcome`.

Project-specific emphasis (qualitative, not scoring weights):

- 青年 C类: assess a focused independent proposal and the capacity to start. Accept field-appropriate evidence of personal contribution; do not demand a general-project publication volume or a fixed team composition.
- 面上: explain both continuity and justified changes of direction; examine prior-project overlap and remaining work.
- 地区: calibrate resources and scope to the project's regional context; do not penalize venue labels or local conditions alone.

## Research Attribute And Form Version

Use the application year and actual form, as described in `current-rules.md`. Current binary 研究属性 (自由探索类/目标导向类基础研究) and the earlier four 科学问题属性 are different fields. Do not require the historical four-category block on a current form.

For a historical form that carries it, check whether its justification is consistent with the key questions. The labels are 鼓励探索、突出原创; 聚焦前沿、独辟蹊径; 需求牵引、突破瓶颈; 共性导向、交叉融通. Two paragraphs can help explain a compound label but are not a required structure. On any form, demand-pull, originality and interdisciplinary claims can be assessed with `question-distillation.md` when the text actually makes those claims. Do not mechanically map a binary attribute to exactly one historical category.

## Core Logic Elements

Every strong application should make four elements easy to extract:

- Object/scenario: the concrete research object, system, material, organism, scene, process, dataset, or phenomenon.
- Problem/goal: the focused contradiction, bottleneck, unexplained phenomenon, or scientific goal tied to that object.
- Method/path: the scientific route used to understand or solve the problem, preferably grounded in mechanism, model, principle, or theory.
- Distinctive feature/innovation: the element that makes the project non-generic, such as a new object, new problem, new method, special condition, constraint, mechanism, scenario, or innovation.

Audit tests:

- Can the object be named in about five Chinese characters or one compact phrase?
- Is the object specific enough that its importance can be argued, not merely asserted?
- Is the problem a research problem requiring scientific explanation, not just an engineering need or implementation task?
- Does the method arise from the problem and scientific question, rather than looking like a method searching for an application?
- Does the distinctive feature illuminate the title, abstract, rationale, research contents, scientific questions, and innovations?
- Are there only one or two central distinctive elements, rather than a pile of unrelated buzzwords?

Common failures:

- Object too broad: "智能制造", "肿瘤治疗", "新能源材料" without a concrete object or scene.
- Problem not focused: many pain points are listed, but none is turned into the project's central problem.
- Method-driven story: the draft sells an algorithm/platform/technology first, then retrofits a problem.
- Distinctive feature is decorative: it appears in the title but not in research contents, mechanism, or innovation.

## Data And Validation Loop

In data-, experiment-, or platform-heavy fields, add a fifth support axis: data/validation resources. A project can have a good logical story but still feel weak if reviewers cannot see how it will be verified.

Check:

- What data, samples, instruments, field sites, benchmark datasets, simulation tools, computing resources, or collaboration channels support each research content?
- Are validation scenes concrete enough to test the claimed model or method, not just named as future applications?
- Does the draft show both controlled validation and real/scenario validation when the field expects both?
- Are evaluation metrics, baselines, controls, uncertainty/risk alternatives, and boundary conditions visible?
- Does any required data or platform depend on an unconfirmed collaboration, proprietary source, ethics approval, or security-sensitive condition?

Flag issues:

- Data are mentioned only in feasibility, not tied to contents or scientific questions.
- Validation only promises "application demonstration" without saying what hypothesis or model property will be tested.
- The project needs large-scale data, samples, hardware, or field access but gives no evidence of availability.
- Strong preliminary results appear to finish the core project rather than support the next step.
- A headline application/需求 anchor drives the whole demand-pull framing but the content carrying it has no research-basis or feasibility evidence (every *other* content is basis-mapped). A strong 需求牵引 hook with no basis on its own content is a flag.

Hypothesis-to-test mapping: the project's core claim should be expressible as one testable hypothesis (structural / environmental / interaction-evolution / composite), satisfying explanatory power, correspondence, simplicity, and above all falsifiability. Ask: can the central claim be written as a checkable hypothesis, and does the plan contain the way it will be tested (experiment/practice, an established theory, or logical self-consistency)?

## Abstract Logic Chain

Use the four-part abstract logic chain to test whether the title, abstract, and body are aligned:

- Object / problem
- Method / goal
- Contents / distinctive innovation
- Achievement / significance

The abstract should usually be four compressed moves:

1. Introduce the object and problem, including the distinctive feature if it matters.
2. State the method/path and target.
3. Summarize research contents, objectives, key scientific questions, and distinctive innovation.
4. State expected achievement and scientific/practical significance.

Diagnostic questions:

- Does the title contain object, problem/goal, method/path, and distinctive feature in a compact noun phrase?
- Does the abstract preview the same logic that later appears in research contents and scientific questions?
- Does the final significance follow from the proposed achievement, or does it jump to broad social value?

Abstract length and structure: check the target form's actual character limit and counting convention. Use the four logical moves as a writing aid, not fixed paragraphs.

- If the applicable limit is 400 characters, an illustrative allocation is 80 / 80 / 180 / 40 = 380, leaving room for transitions. The total, not each allocation, must fit the verified form limit; summarize body contents faithfully without requiring verbatim wording.
- Write in third person; no formulas or figures; do not make the abstract a near-duplicate of the research objectives.
- Flag vague quantifiers ("不同体系", "多种条件") and missing concrete parameters (ratios, temperature ranges, scales) — these should be specified or removed.
- Reusable skeletons (logic aid only; the applicant verifies every fact):
  - `采用[方法]，进行[对象]研究，阐明[机制]/揭示[规律]，为[目标]提供[思路/基础]`
  - `[对象/问题]危害大（问题）→ 主要症结在于（凝练问题）→ 前期研究发现（工作基础）→ 因而提出[假设]→ 拟用[方法]开展[内容]→ 探索/证明[目的]→ 对阐明[X]有重要意义（价值）`
- Ordering words (首先/其次/最后) are optional. The abstract should faithfully cover the core question and contents without an enforced one-to-one sentence mapping.

## Title

The title is the first display of logic. Length is field-dependent and sources disagree: aim for roughly 25-34 Chinese characters for engineering/information-style projects (element-dense "对象+问题+方法+特色" / "3+X" titles run longer), but treat titles over ~34 or under ~20 characters as a prompt for a second look, not as a hard cutoff. Do not present any single number as a universal rule.

Prefer a title that combines:

- Concrete object or scenario
- Focused problem or goal
- Method/path or mechanism
- One meaningful distinctive feature — the 修饰词/限制性定语 that must later reappear in rationale, research contents, and innovation.

Title lint checklist:

- Center word + modifier structure; the modifier carries the distinctive feature, not a generic adjective.
- Avoid a verb-object ("动宾") structure; avoid leading with a bare preposition phrase ("对……的影响研究" → reorder).
- Do not split the title with 顿号/逗号 into a list of methods and scenes.
- Kill concept repetition ("机理与原理", "探讨与研究"), concept inclusion ("强度规律与力学特性"), and hidden/implied concepts.
- Ban self-evaluation words: 新型 / 首创 / 高效 / 高品质 and similar.
- "基于[方法]的[对象]研究" is acceptable only when the method itself is the innovation; otherwise it hides the scientific issue.
- Any ambiguous or restrictive concept used in the title must be explained in the rationale.

Flag titles that:

- Use "基于某方法的某对象研究及应用" without revealing the scientific issue.
- Are too broad to imply a specific research object.
- Contain multiple methods and scenes that do not form one coherent phrase.
- Promise application, system development, or platform construction more than basic research.

## Scientific Nature

NSFC applications must be organized around scientific questions. A technical or engineering difficulty can motivate the project, but the proposal must extract the underlying scientific question.

Useful distinction:

- Engineering problem: a concrete design, manufacturing, construction, process, or application problem.
- Technical problem: a tool, implementation, or performance bottleneck encountered while solving the engineering problem.
- Scientific question: an unanswered question about mechanism, model, principle, structure, relation, influence, law, or explanatory framework.

For engineering/materials/information projects, a strong scientific question often asks how to mathematically, physically, chemically, biologically, or mechanistically describe a phenomenon or relation under specific conditions.

Key scientific questions should be:

- Rooted: point to a bottom mechanism or core relation.
- Representative: specific to the project's object/class, not a universal slogan.
- Important: if solved, they enable the stated method, goal, or innovation.
- Few: often 2 for youth projects and 2-3 for general projects — a prompt to check focus, never a grading criterion by itself.

Flag weak scientific questions that:

- Are merely research tasks: "研究...方法", "构建...系统", "开展...实验".
- Are only mechanisms renamed: "某某机理研究" without explaining what is unknown.
- Are too broad: "人工智能与复杂系统耦合机制".
- Do not correspond to research contents or innovation points.

For applied AI/remote-sensing/engineering drafts, a question may be acceptable even when it contains method words if it clearly asks about a constrained relation or failure mode, for example representation under specific spatial-temporal conditions, transfer/generation/generalization under data shift, physical consistency, optimization convergence, measurement/evaluation validity, or structure-preserving reconstruction. The red flag is not method vocabulary itself; the red flag is a question that cannot be answered except by "build the system and see if performance improves."

### Scientific-Question Phrasing

A key-scientific-question title may be an interrogative or a compact noun phrase bundling object + relation word — 机理 / 机制 / 联合测度 / 耦合 / 矛盾 / 博弈 / 协同 (e.g. "散射机理约束", "安全性与可靠性之间的博弈", "动态低时延业务与资源实时智能适配"). The constrained "how/why" lives in the body sentence beneath the title.

- Do not flag a normal noun-phrase question as "task-like" merely because it is not interrogative.
- Audit the body sentence, not the title form: does it hold a describable, computable, or verifiable relation under stated conditions? Use the interrogative "Under [conditions], how do [variables] constrain [model/mechanism]?" only as an internal test of that body sentence.
- Positive body template: `在[具体条件/前提]下，[对象/现象]的[关系/机制]如何用[数学模型/框架]描述、求解或验证`.
- Write key questions as separate itemized points and argue why each is *key* (enabling the method/goal/innovation), not merely true. The key question usually sits *behind* the mechanism — the mechanism is the result of resolving it.
- Beyond "is it a scientific question", audit "is it well-distilled" (question source, timing argument, anomaly exclusion, constraint visibility, difficulty-innovation pairing) with `question-distillation.md`.

Correlation is not mechanism. For data-/ML-driven drafts, a regression or association is not itself an explanation ("虚假回归" when the causal judgement is skipped); a statistical finding must point to the next mechanistic question. This is the symmetric constraint on the applied-AI tolerance above: method vocabulary is fine, but "we fit it and it correlates / performs better" is not a scientific answer.

## Research-Type Tests

Different draft archetypes have specific completeness tests. Apply the ones that match the draft; do not force all onto every draft.

- Mechanism-type ("××机理研究", especially process/hazard/material-evolution drafts): test whether the mechanism can be stated as 内因(structure) × 外因(environment) × 演化阶段(孕育 → 发展 → 终止) and how they interact. 机理 (process principle) ≠ 规律 (result trend) ≠ single-factor experiment ≠ structural analysis. Drafts about 防治/调控 should anchor which evolution stage they target. For molecular/biological or purely theoretical mechanisms, the equivalent test is whether the planned evidence distinguishes the proposed cause from competing explanations.
- Model-type ("建立××模型"): check 基本假设 / 状态或控制方程 / 拐点·极值·转化点判据 / 定解条件 (initial + boundary) / 求解方法 / 验证-修正-优化 / 应用. For physical/PDE-style models the two most commonly missing pieces are the 判据 and the 定解条件 — a real finding when absent. Statistical, discrete and learning models need assumptions, formulation, solver and validation instead of PDE completeness.
- Inverse-problem-type (inversion, retrieval, diagnosis, identification, 由果推因 — remote-sensing retrieval, InSAR parameter estimation, fault diagnosis): check that it is handled as an inverse problem — ill-posedness relevant to the promised recovery (existence/uniqueness/stability), regularization and priors with their influence, and how validation tests the recovered unknown rather than only the data fit. Writing an inverse problem with forward-problem logic is a named common error. A full well-posedness theorem is not a prerequisite; an unaddressed ambiguity behind a "unique" recovery claim is.
- Statistical/data/prediction-type: match sample size and validation to the claim; justify exclusions and distinguish association, prediction and causal inference. Mechanistic follow-up is required for a mechanism claim, not for a scoped prediction/calibration/statistical-method project. Random splits can suit a within-source claim; cross-region, cross-time, cross-sensor or patient-independent claims need a matching held-out design.
- Transfer/proxy-type (simulation → real, proxy object → target, one population/scale/domain → another): name what property is transferred, why its assumptions survive and what check supports the target scope. Validity in the source setting presented as target validity is the finding.
- New-measurement-modality type (新观测维度 / 新测量体制 / 突破分辨率·精度·灵敏度物理极限): check four pieces. (a) A **quantified sensitivity relation** — ∂观测量/∂待测量 with numbers under named system parameters ("在[波段/带宽/孔径]条件下，待测量变化 1 个单位 → 观测量漂移 N 个单位"), not the adjective "高灵敏". (b) A **precision-limit analysis** (CRLB / Fisher 信息 / 误差传递链 σ_观测量 → σ_中间量 → σ_待测量) with its observation/noise model, nuisance parameters and SNR/信杂比 assumptions. (c) An **observability criterion** — which targets, geometries or scales produce a usable signal under bandwidth/PRF/孔径 constraints; a modality that never says what it *cannot* see is overselling. (d) A stated **relation to the incumbent modality** — which limits it sidesteps and which it inherits. (b) may be a proposed research result (the strong form promotes it into a 关键科学问题); what is missing must then be a credible derivation/validation plan, not a finished theorem. A draft claiming to beat a physical limit with no sensitivity coefficient, no bound analysis in either basis or plan, and no way to test the limit is asserting a magic amplifier — that is the finding. See the 对照式实证图 device in `audit-surfaces.md`.

## Rationale

The rationale usually contains research significance, literature/current status, and a final project-positioning section.

For research significance, a practical four-move structure is:

1. Focus quickly on a concrete object and why it matters.
2. Show the object's focused problem or bottleneck.
3. Explain why a scientific method/path is needed and what target may be reached.
4. Summarize the proposed research and its scientific/practical significance.

For literature/current status:

- Do not write a general textbook survey.
- Organize around the proposed research contents.
- Each subsection should identify what existing studies solve, what they do not solve, and how that gap points to this project's content or method.
- The review should make the key scientific questions and innovations feel necessary.

Flag rationale sections that:

- Spend pages on background but do not converge on the project's problem.
- List literature chronologically without critical synthesis.
- Use "therefore this project..." after a gap that has not been demonstrated.
- Make national/social significance large while the scientific issue remains small.

### Rationale Six-Question Funnel

Audit the rationale as a converging funnel and find which link is missing:

1. Engineering/academic background → 2. its scientific essence and the scientific problem behind it → 3. what prior work already solved → 4. what remains unsolved → 5. what this project proposes to solve → 6. the key scientific (and technical) problems.

Distinguish the wider field question from the narrower question the project can answer. This is a focusing aid, not a strict set hierarchy or a required interrogative format.

Additional rationale checks:

- Organize the review around the relevant scientific gaps (concept / theory / method / model / mechanism). The common failure is a chronological or 国内/国外 survey that lists work without converging on what remains unsolved; re-sorting by scientific angle is usually the repair. Geographic or chronological subsections that do synthesize toward the gap are acceptable.
- The engineering phenomenon in the background must first be classified into a scientific essence (mechanics / physics / chemistry / biology / mathematics problem) before a scientific question is extracted. Different phenomena can share one essence; one phenomenon can carry several essences.
- Scientific significance must be argued from the scientific angle (concept / principle / method / model / mechanism / law and its place in the discipline). Replacing it with economic loss, national strategy, or social stability is a high-frequency deduction.
- Application prospect ≠ direct application: stress the breadth reached *after* the problem is abstracted; "the problem is only a special case with no generality" is a rejection reason.
- Background must focus to the same layer as the title's modifier (a low-permeability-grouting title should discuss low-permeability grouting, not high-speed-rail settlement). Cliché openers ("随着我国经济迅速发展……", "随着大数据时代的到来……") are filler — flag them.
- A hypothesis may arise from literature, theoretical reasoning, public data, new observations, technology or the applicant's own results. Verify its source and then separately assess the applicant's ability to test it. A 立项依据示意图 with 实线 = known / 虚线(或问号) = hypothesis is an effective device — the dashed part is where the project's innovation sits; recommend it when known and hypothesized links are hard to tell apart.
- A closing subsection such as "本项目研究思路的确立及意义" (~2 段) that concentrates gap → key question → contents → expected knowledge makes the research contents feel 呼之欲出. In a long rationale whose convergence is hard to follow, its absence is a 建议改 signal.

## Research Contents And Objectives

Research contents answer "what will be done"; objectives answer "what scientific result will be reached".

Good contents often derive from pairings among problem/goal, method, and distinctive feature:

- Mechanism/model under distinctive conditions.
- Method/path built from the mechanism/model.
- Validation or application that verifies scientific reasonableness and technical feasibility.

Objectives should use verbs such as "揭示", "阐明", "建立", "解释", "提出", "形成", and should end at a scientific target, not just product performance.

Flag issues:

- Contents are independent work packages without input/output relation.
- Objectives repeat contents rather than naming scientific achievement.
- The project is too wide for the funding period.
- Experiments or simulations are listed without saying what scientific question each resolves.

Content-confusion signals (research contents are the "施工队", the plan is the "设计院"). The 2026 flexible research-content block may legitimately combine content, goal and method, so countercheck whether each item still states *what will be studied and how*; flag when it does not:

- Contents restate the rationale or the literature/current status instead of naming what will be done.
- Contents describe research thinking/route ("研究思路") rather than concrete tasks.
- Contents are written as objectives — an item that opens with "为了……" or is carried only by goal verbs (揭示 / 探明 / 摸清 / 明确) with no object-condition-task behind it has been written as a purpose, not a task. A goal verb followed by a concrete task and route is fine.
- Contents just stack the title's phrases, or re-pose the question instead of answering how it will be studied.
- Contents write only the research *method* ("采用深度学习方法……") in place of what is studied.
- Contents do not 归题 (trace back to the title's problem). A useful test: decompose the title's problem into its sub-questions and see whether each is carried by some content.

Objectives should end at a scientific target (揭示 / 阐明 / 建立 / 解释 / 提出 / 形成), not product performance, and several objectives should be logically interlinked around the central hypothesis. Check the scope against the period and resources. Proving or disproving a hypothesis can both be valid outcomes.

Coverage, not equal counts: scientific questions, contents, objectives and validation have a many-to-many relationship. One question may need modeling, solving and validation tasks; one task may serve multiple questions. Use the map below and report only uncovered questions, unsupported objectives or tasks with no explained scientific role. Paragraph form and unequal list lengths alone are not findings.

| Scientific question | Research contents | Objective | Validation/evidence | Gap |
| --- | --- | --- | --- | --- |
| Q1 | One or several tasks | | | |
| Q2 | May share tasks with Q1 | | | |

## Research Content Dependency Graph

For strong drafts, research contents usually form a dependency graph rather than a flat task list. Extract each content item's role:

- Foundation: representation, mechanism, data construction, theoretical model, or measurement system that later contents need.
- Method/model: algorithm, model, framework, inference, optimization, or experimental method built from the foundation.
- Evaluation/feedback: quality assessment, uncertainty analysis, comparison, validation metric, or error mechanism that improves or tests the method.
- Scenario/application validation: realistic data, sample, platform, field case, or prototype used to verify generality and boundary conditions.

Audit questions:

- Does each content item have a clear input from earlier work and output to later work?
- Are research objectives mapped to contents, rather than appearing as separate slogans?
- Are key scientific questions covered by contents without one content carrying all the intellectual load?
- Is the last content a real validation of scientific claims, not only system development or demonstration?

A useful diagnosis is: "内容一提供 X，内容二基于 X 建立 Y，内容三评价/验证 Y 的 Z，内容四在 W 场景检验边界." If this sentence cannot be written, the contents are probably not integrated enough.

For key or platform-heavy projects, the dependency graph may have 4-5 contents, but it should still be reducible to a framework sentence, for example: "内容一建立共享数据/知识/时空基准，内容二形成表示或机理模型，内容三解决融合/优化/控制，内容四构建平台或方法体系，内容五在典型场景检验边界与泛化." Flag broad projects when modules are only a management work breakdown and not a scientific chain.

## Research Plan And Feasibility

The research plan should explain how each content item will be executed and how the key scientific questions will be answered.

Check for:

- A "total-then-parts" structure and a clear technical route.
- Methods, models, experiments, datasets, instruments, or analysis steps detailed enough to judge feasibility.
- Correspondence between research contents and implementation plan.
- Explicit handling of key parameters, controls, comparisons, validation metrics, and risk alternatives.
- Feasibility evidence: prior work, platform, data/source access, team skills, collaboration, and conditions.

Flag issues:

- The plan repeats research contents without operational detail.
- Key data, samples, experimental platforms, or algorithms are assumed but not secured.
- The plan relies on high-risk breakthroughs without alternatives.
- Feasibility only says "team has rich experience" without mapping evidence to tasks.

Use an evidence map for full audits (a working sheet, not report output — the report keeps gap rows only):

| Research content | Needed evidence/resource | Draft evidence | Gap |
| --- | --- | --- | --- |
| Content 1 | Prior theory/data/preliminary result |  |  |
| Content 2 | Method basis/platform/computing |  |  |
| Content 3 | Validation data/baseline/metric |  |  |

The most persuasive feasibility sections often separate theoretical feasibility, technical-route feasibility, data/sample feasibility, platform/equipment feasibility, and team/collaboration feasibility. Do not require every label, but check whether these burdens of proof are substantively covered.

Two nuances that catch weak feasibility sections:

- "可行性" is the feasibility of the *plan*, not of the project. Academic feasibility must specifically argue that the key scientific questions are solvable — not just that the topic is worth doing.
- Feasibility should also prove the applicant is the *right* PI for this problem, by tying prior work directly to the proposed contents.
- For any content that "建立模型", apply the model-type test in Research-Type Tests to the kind of model actually proposed.

## Features And Innovations

Features and innovations should come from the distinctive feature, the scientific questions, and expected breakthroughs. For the count signal see *Focus* below.

Innovation can appear as:

- New object/scenario with a genuinely new problem.
- New problem under a known object or emerging function.
- New theory, mechanism, model, method, or explanatory framework.
- Distinctive feature integrated with method to produce effects existing methods cannot achieve.

Flag issues:

- "首次", "创新性", "显著" are asserted without comparison.
- Innovation repeats research contents.
- Innovation is only engineering integration or parameter optimization.
- The innovation is not supported by key scientific questions.
- Innovation points (or research contents) written in perfect tense (构建了 / 提出了 / 发展了 / 完善了) read as already-completed work rather than a proposal.

Prefer innovation points with this internal shape:

`existing limitation -> project-specific constraint -> proposed new mechanism/model/method/evidence -> what capability or understanding becomes possible`

Flag innovation points that name only a technology stack, a fashionable model, a platform, or a performance target. Stronger innovation explains why existing approaches fail under this project's object/condition and why the proposed idea changes the explanation, model, evaluation, or boundary.

Concrete innovation rules:

- Focus: genuine innovation *claims* are usually 1–3; four or more is a signal to check for padding (team/platform, engineering integration or research contents relabeled as innovation). Count novelty claims, not lines — a combined "特色与创新之处" legitimately mixes 特色 with 创新, so separate them first. Reviewers are 小同行 大专家: one over-claimed point can discredit the rest.
- Hollow-wording signals: 率先 / 首先 / 首次 / 国际领先 / 填补空白 / 研究者很少 / 学术热点, and scope words 综合研究 / 系统研究 / 集成研究 / 多层次研究 or vague "多学科交叉 / 非线性科学". Countercheck for a concrete comparison (object, condition, assumption, what prior work cannot do). Without one, grade 建议改 and rewrite toward a specific knowledge point; with a comparable prior work already known, grade by the NOVEL risk below.
- Novelty risk: a retrieved prior report of the same work under comparable conditions is a serious 创新性 problem, often decisive with reviewers. Explain the missing distinction (object, conditions, assumptions, contribution). Do not routinely flag "no novelty search shown"; when a 首次/填补空白 claim is suspiciously broad, suggest a focused literature and kd search and keep its search limits — zero hits do not prove novelty. When you run the literature search yourself (web or lookup tools available, user asked for 查新), list every query string with its source and date, not only the works found: a "未检到" statement is bounded only by the queries behind it, and the applicant needs them to rerun the search in CNKI or kd.
- Innovation must not be carried by team organization, seminars or platform size; those support feasibility.
- Three innovation types to help classify: 学术思想 / 技术方法 / 研究模式. State features and innovations as itemized points and argue why each *is* an innovation.

## Research Basis And Conditions

Research basis should prove that the applicant can do the proposed project, but must not make it look already completed.

Check:

- Does the basis map to each major research content?
- Are representative papers, patents, datasets, preliminary experiments, and platforms relevant to this project?
- Is the gap between prior work and proposed innovation clear?
- Are work conditions and missing conditions concrete and budget-aligned?

Flag issues:

- Many publications are listed without explaining support for the proposal.
- Preliminary work is unrelated to key methods or scientific questions.
- The draft implies the core content has already been finished.
- Equipment purchase or missing conditions are too large for the project type.

Basis and personal contribution:

- A persuasive layering is 根/干/枝叶: 相关工作基础 (root context) / 直接工作基础 (trunk, with directly related outputs) / 初步结果 (enough to show 胸有成竹, not a finished project). Suggest it when the basis is an undifferentiated publication list. Evidence may be theory/proofs, journal or conference work, correspondence-author contributions, unpublished pilot data, software, instruments or verified access to resources. Judge relevance and personal contribution, not the evidence label alone.
- Require enough support to assess critical risks and the ability to start, without a fixed percentage of already-completed work. Distinguish preliminary feasibility from the proposed result; a new direction may legitimately rely on transferable capabilities.
- No first-author SCI paper, no separately labeled pre-experiment or no team table is not an automatic defect. Report the specific unproven capability or unsupported critical assumption, if any, after considering other evidence.
- For each task, distinguish literature support for the idea, applicant/team capacity and access to resources. A representative publication need not exist for every task; an unpublished pilot or existing resource can supply the missing axis.

Adjacent basis (topic-switching 面上 or a youth PI entering a new object). A track record sitting *next to* the proposal is survivable when the draft declares the adjacency itself. The funded shape observed in samples:

- split outputs into 本项目相关的预研成果 and 方法论支撑成果, labeled rather than interleaved;
- say explicitly that the second group is not this project's scientific question, and name the transferable capability it carries (信号建模 / 参数估计与精度界 / 特征分析 / 平台与数据获取);
- carry the 对象 axis with preliminary results on the *actual new object* instead of with papers.

The substantive finding is adjacent work presented as if it were direct evidence (silent switching), which reads as padding or misrepresentation. When the switch is undeclared, recommend this layout as the repair; the exact sentence and list format are the applicant's choice.

For 青年项目, assess independence through documented personal contribution, methods, data, proofs or other relevant work, and whether the plan is more than inherited from the supervisor's line. Team needs follow the tasks: a PI with students can be adequate; a specialized plan needs the corresponding expertise. Signals worth a low-priority note: a youth team inflated with senior names (保姆现象) or name-dropping that does not map to tasks. Do not prescribe senior-member percentages or penalize collaboration itself.

For 面上项目, check whether the basis explains a natural continuation: what previous project/work solved, what new bottleneck emerged, and how this application deepens or expands it without duplicating completed work.

## Consistency Matrix

For a full audit, build this matrix as a working sheet (not report output; the report carries only the gap rows, per `assets/report-template.md`), with rows:

- Title
- Abstract
- Research attribute / scientific-question framing
- Research significance
- Literature/current status
- Research contents
- Objectives
- Key scientific questions
- Research plan
- Innovation
- Research basis

Columns:

- Object/scenario
- Problem/goal
- Method/path
- Distinctive feature/innovation
- Data/validation loop
- Expected achievement/significance

Mark each cell as present, weak, missing, or inconsistent. The most valuable findings usually come from mismatches across rows.

Modifier tracking: follow each restrictive modifier (限制性定语) from the title → its explanation in the rationale (no ambiguity) → its realization in a content/plan (often a specific equation, 判据, or boundary condition) → the feature echoing the modifier and the innovation echoing the key question. This is a more operational version of "distinctive feature is decorative".

Second matrix (catches broken links the first cannot): rows = each 拟解决的科学问题, typed as 理论 / 实验 / 机理 / 模型 / 方法; columns = 研究内容 / 研究目标 / 关键科学问题 / 特色 / 研究方法 / 学术可行性. A blank row means a stated scientific question has no content, plan, or feasibility argument behind it.

## Common Youth Project Risks

- Object not concrete.
- Problem not focused to one or two core points.
- Scientific questions are not key or not scientific.
- Research contents are broad but shallow.
- Objectives do not reach scientific-goal level.
- Innovation is weaker than the applicant believes.
- Research basis is either unrelated or too close to "already done".

Youth projects usually need a coherent small story: the applicant is "directing" a focused future research plan, not merely stitching thesis papers together.
