# NSFC Application Logic Reference

Use this reference to audit the internal logic of an NSFC application draft. It uses generic proposal-diagnosis language and avoids author-specific labels.

## Scope

This logic is most suitable for 青年基金、面上项目、地区基金 and especially application-oriented basic research in engineering/materials/information-style fields. For pure mathematics/theory, management, or special talent programs, keep the framework but soften the engineering examples and check field-specific norms separately. For medicine, clinical, or biomedical drafts, also read `medical-biomedical.md` and translate the logic map into a disease-mechanism-evidence chain.

## Context Calibration

Do not apply one universal writing standard to every application. First calibrate the expected burden of proof:

| Context | Audit emphasis |
| --- | --- |
| 青年项目 | A narrow independent story, 2-3 tightly linked contents, clear applicant ownership, enough basis to start but not evidence that the project is already finished. |
| 面上项目 | A deeper continuation or expansion from prior work, stronger evidence chain, clearer team/data/platform support, and a broader but still coherent system-level contribution. |
| 目标导向类基础研究 | Technical or application needs may appear prominently, but the draft must still extract a model, mechanism, relation, representation, optimization, evaluation, or law under concrete conditions. |
| 自由探索类基础研究 | Scientific question originality and conceptual depth carry more weight than immediate application scenario. |
| Application-code-heavy fields | Object, method, data, and validation scene should visibly match the selected application code and likely reviewer community. |

For goal-oriented projects, do not reject a draft merely because the wording mentions performance, prediction, detection, platform, or application. Diagnose whether it converts a task into a constrained scientific problem: `specific object + specific data/condition + specific bottleneck + model/mechanism/method question + verifiable outcome`.

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

## Title

The title is the first display of logic. It should usually be around 20-34 Chinese characters for engineering-style projects, unless field conventions differ.

Prefer a title that combines:

- Concrete object or scenario
- Focused problem or goal
- Method/path or mechanism
- One meaningful distinctive feature

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
- Few: usually 2 for youth projects and 2-3 for general projects.

Flag weak scientific questions that:

- Are merely research tasks: "研究...方法", "构建...系统", "开展...实验".
- Are only mechanisms renamed: "某某机理研究" without explaining what is unknown.
- Are too broad: "人工智能与复杂系统耦合机制".
- Do not correspond to research contents or innovation points.

For applied AI/remote-sensing/engineering drafts, a question may be acceptable even when it contains method words if it clearly asks about a constrained relation or failure mode, for example representation under specific spatial-temporal conditions, transfer/generation/generalization under data shift, physical consistency, optimization convergence, measurement/evaluation validity, or structure-preserving reconstruction. The red flag is not method vocabulary itself; the red flag is a question that cannot be answered except by "build the system and see if performance improves."

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

Use an evidence map for full audits:

| Research content | Needed evidence/resource | Draft evidence | Gap |
| --- | --- | --- | --- |
| Content 1 | Prior theory/data/preliminary result |  |  |
| Content 2 | Method basis/platform/computing |  |  |
| Content 3 | Validation data/baseline/metric |  |  |

The most persuasive feasibility sections often separate theoretical feasibility, technical-route feasibility, data/sample feasibility, platform/equipment feasibility, and team/collaboration feasibility. Do not require every label, but check whether these burdens of proof are substantively covered.

## Features And Innovations

Features and innovations should come from the distinctive feature, the scientific questions, and expected breakthroughs. Usually 2-3 points are enough.

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

Prefer innovation points with this internal shape:

`existing limitation -> project-specific constraint -> proposed new mechanism/model/method/evidence -> what capability or understanding becomes possible`

Flag innovation points that name only a technology stack, a fashionable model, a platform, or a performance target. Stronger innovation explains why existing approaches fail under this project's object/condition and why the proposed idea changes the explanation, model, evaluation, or boundary.

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

For 青年项目, check whether the basis proves applicant independence: first/corresponding work, self-owned datasets or methods, clear personal contribution, and a future plan not merely inherited from the supervisor/team.

For 面上项目, check whether the basis explains a natural continuation: what previous project/work solved, what new bottleneck emerged, and how this application deepens or expands it without duplicating completed work.

## Consistency Matrix

For a full audit, create a matrix with rows:

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

## Common Youth Project Risks

- Object not concrete.
- Problem not focused to one or two core points.
- Scientific questions are not key or not scientific.
- Research contents are broad but shallow.
- Objectives do not reach scientific-goal level.
- Innovation is weaker than the applicant believes.
- Research basis is either unrelated or too close to "already done".

Youth projects usually need a coherent small story: the applicant is "directing" a focused future research plan, not merely stitching thesis papers together.
