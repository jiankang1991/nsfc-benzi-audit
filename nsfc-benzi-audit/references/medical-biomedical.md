# Medical And Biomedical NSFC Reference

Use this reference when auditing NSFC drafts in medicine, clinical research, biomedicine, disease mechanism, biomarkers, diagnostics, therapy, intervention, specimens, cohorts, animal models, cells, organoids, immunology, or ethics-sensitive human/animal studies.

Treat successful medical examples as pattern evidence only. Do not copy disease-specific wording, undisclosed data, project structure, or team claims. The patterns below are transferable only when the target draft has comparable project type, discipline, research attribute, and evidence burden.

First choose the actual claim family in [research-claims.md](research-claims.md): PRED for prediction/statistical validity, CAUSAL for mechanisms, and TRANSFER for extrapolation. The mechanism chains below apply to mechanism claims. The finding decision in [benzi-logic.md](benzi-logic.md) controls scope, counterchecking and priority.

## Calibration

Medical and biomedical proposals often need to prove two things at once:

- Scientific question: identify the knowledge sought in a disease mechanism, causal relation, statistical/diagnostic model, marker validity or intervention principle. A prediction-method project need not claim a disease mechanism.
- Medical relevance: the mechanism or method is anchored in a real disease subtype, clinical phenotype, patient population, sample source, diagnostic/prognostic endpoint, or treatment bottleneck.

For a disease-mechanism project, a useful chain is:

`clinical problem or disease subtype -> biological mechanism or causal hypothesis -> model/experiment/data evidence -> human sample or clinical relevance validation -> expected marker/target/diagnostic/therapeutic value`

For purely clinical trials, treatment protocols, real-world studies, or medical-device style work, check whether the application still fits NSFC basic-research framing and route rule-sensitive claims to `current-rules.md`.

## Core Logic Elements

Extract the medical version of the usual logic map:

| Logic element | Medical/biomedical reading |
| --- | --- |
| Object/scenario | Disease, subtype, population, phenotype, cell type, pathway, immune state, organ/tissue, sample, model system. |
| Problem/goal | Unexplained pathogenesis, resistance, recurrence, poor prognosis, diagnostic ambiguity, immune escape, marker failure, model gap, or treatment bottleneck. |
| Method/path | Clinical specimens, cohort/data mining, omics, perturbation, cellular mechanism, animal/organoid model, drug/biomarker validation, statistics. |
| Distinctive feature | New disease subtype, mechanism, target, marker, model, intervention principle, validation resource, or cross-scale evidence chain. |
| Data/validation loop | Evidence matched to the claim: cohort/model evaluation for predictive validity, discriminating causal evidence for mechanisms, relevant human/clinical evidence for an extrapolation claim. |
| Significance | The scientific result and its relevant diagnostic, prognostic, preventive or therapeutic use. |

Flag "clinical importance" that is large but disconnected from the proposed mechanism. The proposal should narrow broad disease burden into a specific unsolved scientific question.

## Scientific Questions

Strong medical scientific questions often ask:

- How a molecule, cell state, pathway, immune component, microenvironment, genetic/epigenetic event, metabolism process, or microbiome factor regulates a disease phenotype.
- Why a clinical subtype, disease stage, treatment response, recurrence, metastasis, resistance, prognosis, or immune state occurs under a specified biological context.
- Which causal chain links a clinical observation or omics signal to a mechanism and a testable intervention/marker.
- How a biomarker, target, model, or therapy principle works and where its boundary conditions are.

Weak versions:

- Uses association alone to assert a causal mechanism or therapeutic target, without evidence supporting that stronger inference.
- Presents screening, sequencing, database mining, or model construction as the scientific question.
- Uses "clinical significance" as a final appendix without a defined endpoint, population, or validation method.
- Claims a therapeutic target before proving disease relevance, causal mechanism, and model fit.
- Lists multiple pathways, markers, drugs, and models without one governing hypothesis.

For an actual mechanism claim, the following can clarify the proposed relation:

`X 在 [疾病/亚型/病程/治疗背景] 中通过 [机制/通路/细胞过程] 调控 [表型/终点] 的作用及机制`

Only use this skeleton as a logic aid; the applicant must verify all factual claims.

## Medical Evidence Chain

For cross-scale mechanism or translation claims, inspect the chain supporting that inference. For predictive/statistical claims, use the relevant evaluation boundary instead.

Common strong patterns:

- Clinical observation or unmet need identifies the disease phenotype and endpoint.
- Public datasets, own cohort, specimens, or omics screen produce a candidate factor or mechanism clue.
- Cell/primary-cell/organoid experiments perturb the candidate and test molecular mechanism.
- Animal or disease model verifies phenotype, intervention effect, immune context, metastasis, survival, or toxicity as appropriate.
- Human samples or clinical data validate expression, stratification, prognosis, treatment response, or diagnostic value.

Common dependency graph:

`Content 1: clinical/data discovery or candidate validation -> Content 2: causal mechanism -> Content 3: in vivo/model verification -> Content 4: clinical significance, biomarker, drug, or intervention validation`

This is an example architecture, not a task-count or full-translational-pipeline requirement. Check scientific roles and claimed dependencies; complementary parallel studies can be coherent.

## Samples, Cohorts, Endpoints, And Statistics

When samples, patients, cohorts, specimens, clinical databases, or retrospective/prospective material appear, check whether the draft gives enough detail to judge feasibility and validity:

- Source: hospital/biobank/database, collection period, disease subtype, tissue/fluid type, control source, and whether future collection is needed.
- Inclusion/exclusion: diagnosis criteria, stage/risk group, treatment status, recurrence/metastasis status, age/sex or other relevant stratification.
- Scale: sample size, expected new cases, grouping balance, rare-subtype feasibility, missing data, and whether discovery and validation sets are separated.
- Endpoints: survival, recurrence, response, metastasis, immune infiltration, pathology score, biomarker threshold, diagnostic accuracy, toxicity, or other clinically meaningful outcome.
- Statistics: power or rationale for sample size when appropriate, covariates/confounders, multiple testing, model validation, survival analysis, randomization/blinding for intervention or animal studies when applicable.
- Governance: ethics approval, informed consent, data privacy, sample export/sharing limits, and biosafety.

Do not invent missing approvals or sample numbers. If official compliance status is uncertain, mark it as "需申请人按当年指南、医院伦理和单位要求确认."

## Models And Experiments

Check model fit, not just experiment quantity:

- Cell model: disease subtype, genetic background, phenotype, passage/identity, contamination control, and whether multiple lines or primary cells are needed.
- Animal model: immune-competent versus immunodeficient choice, transgenic/xenograft/orthotopic/metastasis model fit, sex/age, endpoint, humane endpoint, intervention schedule, and sample size rationale.
- Organoid/PDX/primary system: whether it better represents patient heterogeneity and whether access is credible.
- Perturbation: knockdown/knockout/overexpression, rescue experiment, dose/time response, off-target control, and causal interpretation.
- Omics/bioinformatics: discovery versus validation split, batch effects, annotation, pathway inference, multiple-comparison control, and independent validation.
- Drug/therapy/diagnostic work: mechanism, target engagement, pharmacodynamics/pharmacokinetics when relevant, toxicity, comparator, combination rationale, and translational boundary.

For immune-mechanism claims, identify strain/genotype, retained and missing immune components, reconstitution status and the mechanism actually tested. Nude mice retain NK activity whereas NSG lack functional NK cells; neither the broad label 免疫缺陷 nor a model name alone determines all mechanistic support. Flag a specific missing component/unsupported inference after checking controls and complementary evidence. Sources checked 2026-09-12: [JAX model selection](https://www.jax.org/news-and-insights/jax-blog/2020/may/top-tips-selecting-the-best-immunodeficient-mouse-model-for-your-research), [NSG FAQ](https://www.jax.org/jax-mice-and-services/find-mice/nsg-portfolio/frequently-asked-nsg-questions).

## Variant-Specific Checks

Use these checks when the medical draft is not a standard molecule-pathway-disease proposal. They are contrastive questions; do not force every item into every draft.

- Clinical prediction, AI, imaging, or warning models: identify the decision point, target population, label/ground truth, cohort source, information available at prediction, evaluation separation and claimed utility. Match internal, temporal, prospective or external validation to the promised use; do not require all of them. A question about calibration, model validity, diagnostic principles or decision rules need not add a disease-mechanism experiment.
- Nursing, psychology, health service, public-health, or behavioral intervention work: define population, scenario, intervention component, comparator/usual care, outcome scale, follow-up window and randomization/blinding where applicable. Inspect a mediator or mechanism when the project makes that causal claim; do not add it solely because the proposal is basic research.
- Traditional medicine, formula, natural-product, or syndrome-based work: translate syndrome, formula, herb, or compound claims into a testable material basis and mechanism chain. Check quality control, batch/compound identity, dose-response, target engagement, pathway perturbation, model fit, and whether efficacy claims are separated from mechanistic claims.
- Biomaterials, nanomedicine, molecular imaging, or theranostic work: link material/probe design to biological mechanism and disease endpoint. Check biodistribution, targeting specificity, safety/toxicity, clearance, comparator, imaging ground truth, therapeutic synergy, and the boundary between platform novelty and disease-relevant scientific question.
- Antimicrobial, infection, implant, or wound-material work: connect local microenvironment triggers, release kinetics, host response, pathogen/biofilm model, tissue repair, and safety. Do not accept "new material plus antibacterial test" as sufficient without a mechanism and clinically matched model.
- Regional, joint, key, or other non-standard project types: calibrate scope, resources, platform, collaboration, and expected breadth against the project type instead of judging them only by youth/general-project compactness.

## Feasibility And Research Basis

Medical feasibility is strongest when prior work and resources map to proposed contents:

- Clinical access: patient flow, biobank, specimen preservation, clinical database, follow-up continuity, pathology/diagnosis support.
- Mechanistic basis: preliminary expression/association data, perturbation data, pathway clue, model result, or pilot intervention.
- Platform: flow cytometry, sequencing, animal facility, pathology, imaging, organoid/PDX, bioinformatics, drug synthesis or screening as needed.
- Team structure: clinician, basic scientist, statistician/bioinformatician, pathologist, animal/model expert, medicinal chemist or pharmacologist when relevant.
- Boundary from prior work: what is already proven, what remains unknown, and why the funded period is still needed.

Flag feasibility sections that only list hospital rank, equipment, papers, or project history without mapping them to sample access, model feasibility, mechanism methods, or clinical validation.

## Transferable Patterns From Funded Medical Examples

Use these as contrastive questions, not as rules:

- The strongest examples make the clinical disease burden quickly converge on one mechanistic bottleneck, rather than staying at broad disease importance.
- They often use preliminary evidence in layers: public/own data, cell perturbation, animal/model phenotype, and human specimen or clinical relevance.
- Their research contents are not a flat list of methods; each later content depends on the previous discovery or mechanism.
- Their feasibility sections connect clinical resources, specimen banks, animal/model systems, and team expertise to specific tasks.
- Their innovation points explain the new disease mechanism, target, model, or intervention principle, not only that a method or marker is "first."
- Strong cross-domain medical examples make the technical platform serve a clinical or biological question: the proposal explains why a specific delivery route, model, material, imaging probe, scale, or intervention logic is necessary for the disease problem.

Because these observations may come from a small or field-specific sample batch, label them as "可迁移", "条件迁移", or "样本不足" when reporting.

## Common Findings

Use concise applicant-facing language only after the core countercheck. These are example issue names, not findings to populate for every draft; reuse existing IDs for the same root issue:

- `医学问题没有收束`: 临床负担写得很大，但没有收敛到本项目要解释的具体机制/病程/治疗耐受问题。
- `样本链条不够清楚`: 提到了病例或标本，但缺少来源、分组、终点、随访、统计或伦理说明。
- `机制跳跃`: 从表达相关或数据库筛选直接跳到靶点/治疗价值，中间缺少因果扰动和模型验证。
- `模型不匹配`: 细胞或动物模型不能支撑所声称的疾病亚型、免疫机制、转移/复发或治疗场景。
- `临床外推缺口`: 所声称的临床适用范围缺少对应验证；验证放在最后一项本身不是问题。
- `前期基础未映射`: 论文、平台和样本很多，但没有说明分别支撑哪个研究内容。
- `模型构建替代科学问题`: 预测、AI、影像或预警模型写得完整，但缺少要解释的机制、决策原则、验证终点或临床应用边界。
- `技术平台抢主线`: 纳米材料、递送体系、影像探针或诊疗一体化设计很复杂，但没有说明它为什么是解决该疾病科学问题的必要路径。
- `干预要素不闭环`: 护理、心理、健康服务或行为干预提出了方案，但人群、对照、终点、随访、实施机制和统计验证没有形成闭环。
- `中医药机制未转译`: 方药、证候或天然产物停留在经验疗效描述，缺少物质基础、质量控制、剂量-效应、靶点扰动和模型验证。
