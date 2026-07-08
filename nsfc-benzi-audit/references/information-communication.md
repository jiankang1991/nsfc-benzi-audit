# Information And Communication Applications

Use this reference when the draft or examples involve information science, communication networks, optical networks, computer networks, data centers, remote sensing information processing, applied AI, network security, quantum communication, or related NSFC information-engineering directions.

The goal is not to force every information proposal into one template. Use these checks to decide whether an application-oriented information draft has converted a demand or performance bottleneck into a reviewable basic-research problem.

## Context Calibration

Information and communication proposals often carry strong application language: 5G/B5G, URLLC, data centers, cloud-edge systems, optical networks, security, resource scheduling, target recognition, or platform verification. This is acceptable for goal-oriented basic research only when the draft exposes:

- the concrete scenario or system boundary;
- the measurable demand, constraint, or failure mode;
- the model, mechanism, representation, optimization, or control question behind the demand;
- the data, simulator, platform, benchmark, or scenario that can verify the claim.

Do not flag a proposal merely because it mentions algorithms, performance, deployment, platforms, or engineering metrics. Flag it when performance improvement is the only scientific answer.

## Demand-To-Question Conversion

Strong information drafts commonly convert application demand into scientific questions through this chain:

`scenario demand -> constrained bottleneck -> variable/relation/model -> method or mechanism -> measurable validation`

Audit questions:

- Does the draft name the demand as a concrete constraint, such as latency, reliability, throughput, blocking probability, key success rate, resource utilization, generalization, uncertainty, or safety risk?
- Is the bottleneck framed as a relation to be modeled or optimized, not only as a system to be built?
- Are key variables visible: traffic dynamics, resource coupling, topology, channel condition, task load, failure type, data shift, spectrum/time-slot/key/computing resource, or security risk?
- Does the proposed method answer why the relation behaves as it does, or only report that a new algorithm may perform better?
- Are evaluation metrics and boundary conditions sufficient to judge whether the scientific question has been answered?

Weak signs:

- "Improve accuracy/efficiency/reliability" appears without a specific condition or baseline.
- The key scientific question is "how to construct a high-performance model/system".
- National strategy, standards, or industrial demand is long, but the scientific bottleneck remains one sentence.
- The draft lists fashionable methods without explaining why existing methods fail under this project's constraint.

Science-elevation devices (audit that at least one is present — these are how funded info-comm drafts turn scheduling/networking from a task into science):

- Unified mathematical description of heterogeneous multi-resources (e.g. 频谱/时隙/密钥, or 算力/路由/波长) plus mining their intrinsic constraint or coupling.
- An analytic performance model (e.g. 阻塞率解析模型) plus a theoretical-condition proof (e.g. 严格无阻塞条件).
- Framing the target as an unknown quantitative relation φ that must be modeled/fitted rather than assumed ("准确关系难以量化" as the science itself).
- A supply-consumption / balance constraint (e.g. 密钥供给 vs 消耗).
- Relational SQ nouns: 博弈 / 矛盾 / 协同 / 耦合 between two objectives or resources.

## Content Architecture Patterns

Information and communication examples often use one of these content dependency chains:

- `architecture -> model -> optimization/control -> platform or scenario validation`
- `mechanism/representation -> algorithm -> evaluation/feedback -> realistic validation`
- `high reliability -> low latency -> large scale/resource reuse`
- `data construction -> feature/representation -> transfer/generalization -> benchmark validation`

Audit questions:

- Can each research content be assigned a role: architecture, model, mechanism, optimization, control, evaluation, or validation?
- Does a later content depend on outputs from an earlier content, or are the contents just parallel algorithms?
- Does the final content validate the model/mechanism under the stated constraints, rather than only demonstrate an application system?
- If the project has 4 contents, is the fourth a necessary integration/validation step for the scientific claims?

For youth projects, three tightly linked contents are usually easier to defend than four broad modules. For general projects, four contents can work when the first two establish theory/model, the third optimizes or controls resources, and the fourth verifies system-level boundary conditions.

## Scientific Questions

Good information-field scientific questions often ask about:

- adaptation between dynamic demand and constrained resources;
- coupling among communication, computing, sensing, spectrum, time, energy, security, or key resources;
- reliability-latency-cost tradeoffs under failures or uncertainty;
- representation/generalization under cross-source, cross-domain, open-world, or non-stationary data;
- physical, protocol, topology, or security constraints that change model behavior;
- evaluation validity, uncertainty, and boundary conditions.

Real funded info-comm SQs are noun phrases (e.g. "安全性与可靠性之间的博弈", "动态低时延业务与资源实时智能适配"), not interrogatives. Use the shape below only to test the *body sentence* beneath the noun-phrase title; do not flag a noun-phrase SQ as task-like for being non-interrogative:

`Under [specific scenario/condition], how do [variables/resources/failures/data shifts] constrain [model/mechanism/control/representation], and how can this relation be described, optimized, or verified?`

Flag questions whose body can only be answered by "we will build it and compare performance".

## Literature And Rationale

For information proposals, literature review is persuasive when it is organized by bottleneck, not by technology chronology.

Check whether each subsection ends with:

- what existing work can already solve;
- the condition under which it fails or becomes insufficient;
- why that gap leads to one proposed research content;
- what metric, model, or scenario will test the gap.

For fast-moving AI/network/security topics, suggest that applicants explicitly compare with obvious adjacent methods or standards, but do not invent missing references.

## Validation And Feasibility

A credible validation chain should make three levels visible:

- controlled validation: simulation, benchmark, ablation, theoretical bound, convergence, or complexity analysis;
- scenario validation: real traffic/data, field scene, open platform, prototype, or industry-style workload;
- resource feasibility: data/source access, simulator, computing platform, experimental network, instrument, collaborator, or prior codebase.

Strong research-basis sections map prior work to future tasks. A useful local pattern is:

`previous result -> capability gained -> proposed content supported -> remaining gap`

Flag:

- prior papers are listed by venue only, without task-level mapping;
- the validation dataset/platform appears only in feasibility and not in the research contents;
- a collaborator, enterprise, open platform, or sensitive dataset is essential but not evidenced;
- the preliminary work appears to have already completed the central algorithm or platform.

## Innovation

Innovation points should not be method names alone. Ask whether each innovation states:

- existing limitation under the project's scenario;
- the project-specific constraint or variable;
- the new model, mechanism, representation, optimization, or control idea;
- the capability or understanding made possible;
- the planned evidence for the claim.

In information drafts, "first use of a model", "combined algorithm", "platform implementation", or "higher performance" is usually weak unless tied to a new constrained relation, resource coupling, theoretical property, or validation boundary.

Integration must be cashed out as a mechanism: when the spine is 一体化 / 协同 / 融合 (e.g. 通算融合, 通感一体), verify it resolves to a joint/unified objective, a shared resource model, or an explicit coupling mechanism — not a bundling slogan.

Figure conventions: expect the framework and 总-分 技术路线 figures from `audit-surfaces.md`, plus architecture figures (e.g. multi-plane SDN, resource-scheduling/blocking flowcharts) and a "研究对象-需求-科学问题-内容-目标-验证" relationship figure. Flag an info-comm draft that argues an architecture→model→optimization→validation chain with no framework figure.

## Report Add-On

When diagnosing an information or communication draft, add a short field-specific check:

```markdown
### 信息通信类专项检查
- 需求是否转成科学问题：
- 约束/变量/指标是否清楚：
- 内容依赖链是否成立：
- 验证数据、平台和评价指标是否支撑核心问题：
- 研究基础到任务的映射缺口：
```
