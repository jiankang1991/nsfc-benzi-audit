# Scientific-Question Distillation Quality (凝练科学问题)

Use this reference when auditing how well a draft *distills* its scientific question: the 拟解决的关键科学问题 importance argument, the rationale's convergence chain, the 科学问题属性 justification, or any draft claiming 原创/独辟蹊径/卡脖子/交叉. It extends `benzi-logic.md`'s "is this a scientific question" test with "is this question well-distilled" tests.

Source: distilled from the NSFC-authored case book《凝练科学问题案例》(81 funded-case narratives, each with named expert commentary). These are calibration heuristics from exemplary cases, not official rules. They judge distillation quality in an existing draft — do not demand that a draft literally reorganize its headings into the book's case format.

## Question-Source Taxonomy

The book's preface names six recurring distillation modes. Classify the draft's 问题来源 into one (or a combination) and apply the matching strong-form test below; these are examples, not an exhaustive taxonomy or a gate that every proposal must pass:

1. 好奇引导 — curiosity about an unexplained phenomenon.
2. 无穷追问 — iterating questions along a chain of prior results ("随之产生的科学问题是……").
3. 反常深挖 — an anomaly or theory-practice contradiction.
4. 范式变革 — a paradigm/technology shift reopens old questions.
5. 同行之议 — organized consensus (双清论坛, 学部战略研讨) converges the question.
6. 透视需求 — abstracting a scientific question out of an application need.

## Distillation-Chain Visibility

These chains illustrate how evidence can motivate a question; adapt the links to the actual question source and claims. Neither a fixed sequence nor the applicant's own preliminary conclusion is mandatory:

General chain: 背景/方向 → 已有知识、观察或理论依据 → 科学问题 → 困难/局限 → 创新思路 → 知识增量 → 适用时的应用价值.

需求牵引 example: 应用需求 → 具体障碍 → 研究切入点及其证据 → 关键科学问题. Published results, theory and own prior work can each supply the evidence.

Question provenance and applicant readiness are separate. A question may follow from published theory, literature contradictions, public data, curiosity, demand or the applicant's own findings. Test the evidential link that the draft actually claims; do not require a personal preliminary discovery for every question. Own-work discovery → hypothesis → pilot is one useful form, particularly for unpublished anomaly claims.

Distillation-process evidence (加分项, prompt to add if absent on 交叉/重点 drafts): organized refinement traces such as workshop/研讨 rounds, deep post-mortems of failures or accidents, or prior cross-disciplinary outputs.

## Question-Quality Tests

- 三准确 (the baseline bar, from a reviewer writing in explicit application-review voice): 概念阐述准确 / 科学问题描述准确 / 潜在困难把握准确. Imprecise core concepts, a question statement that misplaces the field's actual frontier, or difficulties that stay at slogan level each independently sink credibility.
- 时机论证: when the argument relies on a new instrument, data window or technology shift, explain why it makes the question tractable now. Do not require such a window for every original theoretical idea.
- 反常立题须排除平凡解释: when the question is founded on an anomaly or theory-practice contradiction supported only by anecdotal or unpublished observation, the draft must explicitly rule out trivial causes (measurement error, parameter freedom, sample bias). Model sentence shape: "这不可能由观测误差导致，因为……". A contradiction already established by systematic published study counts as satisfied — do not demand the exclusion sentence again.
- 约束显式化: a well-posed question states its own boundary conditions (resource, precision, scale, scene). A question with no stated constraints tends toward slogan.
- 多问题关系: explain how the questions contribute to a coherent project, whether through dependency or complementary aspects. Judge coverage and achievable scope, not an exemplary count or a required serial order.
- 能力跃迁重述: a well-distilled question can be restated as "从 X 到 Y" capability jumps (从定性到定量 / 从宏观到微观 / 从静态到动态). If the only possible restatement is "提高性能/精度", distillation is incomplete.
- 可延展性: strong significance arguments show the solved question radiating beyond the applicant's own sub-direction ("宽广的科学价值"). A question whose payoff is confined to one narrow niche is answerable but may not be 值得支持. Absence = prompt to argue, not auto-defect. Same root as 方法论可迁移性 in the significance audit below — when both are absent, report them as one finding, not two.
- 定性→定量跃迁: for mechanism drafts, check whether the proposal commits to quantitative deliverables (model, coefficients, governing equations, criteria) beyond qualitative description; "突破定性描述的瓶颈" is a recurring exemplary-case selling point.

## Per-Attribute Strong Forms

`benzi-logic.md` explains historical four-category attributes. The patterns here can strengthen arguments, but are not necessary conditions for originality or mandatory current fields. On a historical form, a short classification statement may help when its justification is unclear.

Form-version mapping: current binary 研究属性 does not map one-to-one onto the historical four categories. Choose tests from the actual claims and research context; either binary attribute may involve frontier, interdisciplinary or novel-method work. Do not request a four-category self-classification if the form does not carry that field.

- 鼓励探索、突出原创: check a concrete knowledge increment and credible comparison with prior work. A published impossibility claim or a well-defined longstanding gap can strengthen the case, but neither is a prerequisite for originality.
- 聚焦前沿、独辟蹊径: when the draft claims to *replace* a mainstream route (换赛道), check the 换赛道三件套 — (a) name the mainstream route, (b) argue its dead end is *structural/principled* (quadratic growth, a scaling relation, a transform that itself causes the cost — not mere engineering immaturity), (c) show point by point how the new route resolves that dead end. Missing (b) means the new route is a parallel alternative: that can still be novel, but then grade the 换赛道/独辟蹊径 wording as over-claimed (建议改) and compare the two routes under the same conditions instead.
- 需求牵引、突破瓶颈: select the following checks according to the actual bottleneck claim.
  - 瓶颈量化: any claimed 瓶颈/极限/失配 needs numbers (current value, limit value, ratio, order of magnitude). "性能不足/效果不佳" alone is an unproven bottleneck. The numbers often live inside a figure rather than body text — check the original image before flagging (see the figure-fidelity caveat in `audit-surfaces.md`).
  - 结构性极限: when claimed, distinguish a principled limit from current implementation or resource limitations. Demand-led questions need not prove that all optimization on the existing route is futile.
  - 抽象动作: show the explicit move from engineering pain point to a mechanism/principle-level formulation (痛点 → 本质原因 → "归结起来就是……机制/规律/方法" question). Stopping at "研制××系统/平台" is the failure the book's preface names: "把基础研究做成无目标的应用研究".
  - 科学/技术分栏: the 关键科学问题 list itself must contain no technical-task phrasing; flag only when technical attack items are mixed *into* the scientific-question list (technical work legitimately living in 研究内容/技术路线 already satisfies the separation — do not demand a separate "技术难题" heading).
- 共性导向、交叉融通: four checks.
  - 交叉产物: the crossing itself must yield a new concept, hypothesis, or evidence type that no single discipline had ("人机冲突", a new proxy signal) — listing participating disciplines and methods is the 拼盘 weak form.
  - 双向反哺: strong cases give both the necessity (why this problem's nature requires the crossing) and the return contribution to the borrowed discipline ("为复杂系统涌现机理的研究带来了新的视角"). One-way application of a mature method to a new scene is the weak form of 交叉融通 — and per the sharpest reviewer comment in the case book, "特定方法在具体场景中的应用" without naming which existing model/assumption it extends is not 方法创新. Missing return contribution is a 建议改 signal, not by itself a defect of the science.
  - 配对-突破映射: each claimed discipline pairing should map to a named "从 X 到 Y" dimension jump; pairings with no jump = 拼盘嫌疑.
  - 层间失配定位: a high-quality common-cause question often sits at the *interface* where two mature layers/disciplines mismatch, rather than inside either one.

## Difficulty Section (困难) Audit

Possible difficulty forms — choose those supported by the problem; no separate difficulty heading or fixed count is required:

- (a) Relevant existing methods and their failure mechanisms: each existing method + its specific failure mechanism *on this object*. "存在不足/难以满足" without mechanism is hollow.
- (b) Intrinsic-object difficulty: NP-hardness, unobservability, scale crossing, un-experimentable conditions.
- (c) Resource difficulty (queue, cohort, compute) counts *only* when bound to scientific-argument validity (causal ordering, statistical power, comparability) — otherwise it is workload, not difficulty.

Additional tests:

- 方法假设-对象属性匹配: when claiming "现有理论不适用", list the theory's enabling assumptions and point to the one this object violates (渐近规模假设 vs 有限规模; 区域/变量一致假设 vs 跨区域需求). This is the strongest form of (a).
- 困难-创新对应: innovation points should pair off with declared difficulties (many-to-many allowed) — the exemplary-case formula is "基于以上困难分析，提出针对性的创新手段". An innovation answering no difficulty, or a critical difficulty no innovation answers, is a real finding; unequal counts alone are not. Reviewer version: creativity must be "对着自己困难定制的" — stacking generically new technology is not innovation.
- 创新点不得由团队组织充当: a 创新点 section whose main content is team composition, seminars, or leadership is a question not yet distilled to method level; organization may support feasibility, never innovation.
- 方法论新意底线: each method-type innovation answers "它扩展/松弛了哪个既有模型或假设"; "某方法用于某场景取得 X% 提升" is application, not scientific innovation.

## Significance (意义) Audit

- 两分结构: 知识体系增量 first, 应用价值 second. The increment must name concrete deliverables (new tool, theory, parameter set, dataset, criteria) — "推动学科发展/填补空白" scores zero. This refines the "scientific angle" significance rule in `benzi-logic.md`.
- 方法论可迁移性: one sentence stating which class of neighboring problems the method transfers to. Exemplary cases and multiple named reviewers treat this as an independent merit axis; absence = prompt to add. Same root as 可延展性 above — merge into one finding when both are absent.
- 强主张须外部证据: "范式转移/国际领先/开辟新赛道" claims need third-party evidence (independent adoption, published commentary, follow-up citations, authoritative lists). Without it, downgrade to ordinary innovation phrasing.

## Supporting Devices Worth Checking

- 代理对象三件套: replacing the target object with a proxy (模式材料/模式疾病/简化体系, and equally 合成数据/仿真数据代理真实观测、简化基准代理真实场景 in information disciplines) requires (a) a mechanism-homology assumption, (b) a concrete advantage list for the proxy, (c) a stated path migrating results back to the original object.
- 试金石验证场景: the chosen validation scene should be simultaneously the most demanding test *and* have both a well-characterized region (for checking) and an unknown region (for prediction). Validation only on convenient or self-made scenes is the weak form.
- 跨尺度直推警报: when the target quantity and the measured quantity sit several organizational levels apart (基因→生态系统, 微观参量→宏观性能), require a named bridging quantity or normalization; direct extrapolation is a named "科学陷阱".
- 跨域类比三件套: when the core idea is borrowed from another field or scale ("借鉴[另一学科]的定律/成像原理/统计力学……"), the analogy must be cashed out, not invoked. Check (a) a dimension-by-dimension **同构性对照表** with both columns filled — 物理对象 / 几何尺度 / 激励源 / 相互作用 / 观测现象 / 反演目标 is a workable row set (equivalent equations or prose that cover the same dimensions count); (b) an **不变性论证** saying why the law survives the transfer (尺度不变性、量纲关系、同一支配方程), ideally with the source field's own history showing the law already crossed one scale; (c) the **失配维度自陈** — what does not carry over (有限规模取代理想无穷、真实对象不满足源领域的理想化假设、观测条件受限). Gate the device on the analogy's *role*, not on the word: 借鉴/类比/受……启发 appears in most drafts as an ordinary design choice (借鉴某个成熟网络结构、借鉴另一学科的一种成熟算法思想) and needs none of this. Apply the three pieces only when the borrowed law does argumentative work — the stated 研究思路, the first 创新点, or the reason the project is claimed feasible ("该规律在源领域成立，故在此成立"). There, missing (b) is a real finding; a filled table is one of the cheapest ways to make an otherwise unreviewable 原创 claim checkable by a 小同行. Distinct from 跨尺度直推警报 above: that one guards a causal chain inside one domain, this one guards a mechanism borrowed across domains.
- 反筛/阴性对照: any project whose goal is 选择性/特异性 must contain a counter-screen or negative-control design.
- 指标三段论: when the scientific question targets a measure/index itself, require (a) an observable behavior distortion the current index causes, (b) its theoretical root cause, (c) a first-principles reconstruction with a computable path.
- 排他性论证: when one route is chosen among several candidates, name the alternatives and the exclusion reason for each (physical, resource, 国情). Unargued route choice weakens 技术路线 credibility.
- 机理指导替代试错: for process/工艺-flavored drafts, the scientific-question payoff is often "以机理指导替代试错"; check the draft claims (and can support) this, not just parameter search.

## Reviewer-Language Calibration

Positive lexicon used by the book's named reviewers (target register for strong drafts; if the draft self-claims these without a supporting entity, flag as hollow): 独辟蹊径 / 化繁为简、直击肯綮 / 敏锐抓住 / 睿智的选择 / 高屋建瓴 / 基础性+前沿性+挑战性 / 原创性+普适性+引领性 / 可延展性突出 / 既聚焦国际前沿又着眼区域特色 / 逻辑严密.

Weak-praise warning signs (in simulated review or self-assessment): purely stylistic praise ("语言通顺、条理性强") appearing before substance, and hedged verdicts (力求 / 有望 / 如能……则) — both mark unresolved substance gaps; find and fix the gap they point at.
