# Medical And Biomedical NSFC Reference

Use this reference when auditing NSFC drafts in medicine, clinical research, biomedicine, disease mechanism, biomarkers, diagnostics, therapy, intervention, specimens, cohorts, animal models, cells, organoids, immunology, or ethics-sensitive human/animal studies.

Treat successful medical examples as pattern evidence only. Do not copy disease-specific wording, undisclosed data, project structure, or team claims. The patterns below are transferable only when the target draft has comparable project type, discipline, research attribute, and evidence burden.

## Calibration

Medical and biomedical proposals often need to prove two things at once:

- Scientific question: the draft is not only treating, detecting, predicting, or screening, but explaining a disease mechanism, causal relation, biological process, model, marker logic, or intervention principle.
- Medical relevance: the mechanism or method is anchored in a real disease subtype, clinical phenotype, patient population, sample source, diagnostic/prognostic endpoint, or treatment bottleneck.

Do not force an engineering-style "system construction" standard onto medical drafts. Prefer a disease-centered chain:

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
| Data/validation loop | Human sample/data discovery or validation plus mechanistic perturbation and model-level functional verification. |
| Significance | Mechanistic understanding first; diagnostic, prognostic, preventive, or therapeutic value second. |

Flag "clinical importance" that is large but disconnected from the proposed mechanism. The proposal should narrow broad disease burden into a specific unsolved scientific question.

## Scientific Questions

Strong medical scientific questions often ask:

- How a molecule, cell state, pathway, immune component, microenvironment, genetic/epigenetic event, metabolism process, or microbiome factor regulates a disease phenotype.
- Why a clinical subtype, disease stage, treatment response, recurrence, metastasis, resistance, prognosis, or immune state occurs under a specified biological context.
- Which causal chain links a clinical observation or omics signal to a mechanism and a testable intervention/marker.
- How a biomarker, target, model, or therapy principle works and where its boundary conditions are.

Weak versions:

- Only asks whether a factor is associated with prognosis, expression, diagnosis, or treatment response.
- Presents screening, sequencing, database mining, or model construction as the scientific question.
- Uses "clinical significance" as a final appendix without a defined endpoint, population, or validation method.
- Claims a therapeutic target before proving disease relevance, causal mechanism, and model fit.
- Lists multiple pathways, markers, drugs, and models without one governing hypothesis.

For applicant-facing revision, push the wording from "研究 X 在疾病中的作用" toward:

`X 在 [疾病/亚型/病程/治疗背景] 中通过 [机制/通路/细胞过程] 调控 [表型/终点] 的作用及机制`

Only use this skeleton as a logic aid; the applicant must verify all factual claims.

## Medical Evidence Chain

Audit whether the draft builds a cross-scale evidence chain rather than isolated work packages.

Common strong patterns:

- Clinical observation or unmet need identifies the disease phenotype and endpoint.
- Public datasets, own cohort, specimens, or omics screen produce a candidate factor or mechanism clue.
- Cell/primary-cell/organoid experiments perturb the candidate and test molecular mechanism.
- Animal or disease model verifies phenotype, intervention effect, immune context, metastasis, survival, or toxicity as appropriate.
- Human samples or clinical data validate expression, stratification, prognosis, treatment response, or diagnostic value.

Common dependency graph:

`Content 1: clinical/data discovery or candidate validation -> Content 2: causal mechanism -> Content 3: in vivo/model verification -> Content 4: clinical significance, biomarker, drug, or intervention validation`

For youth projects, this may be compressed to 2-3 contents. Do not demand a full translational pipeline if it exceeds the project type. Do demand that every content has a clear input/output relation.

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

For immunology or immunotherapy, inspect whether the model can actually represent the immune mechanism being claimed. Immunodeficient tumor models cannot by themselves prove T-cell, NK-cell, checkpoint, or microenvironment mechanisms.

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

Because these observations may come from a small or field-specific sample batch, label them as "可迁移", "条件迁移", or "样本不足" when reporting.

## Common Findings

Use concise applicant-facing language:

- `医学问题没有收束`: 临床负担写得很大，但没有收敛到本项目要解释的具体机制/病程/治疗耐受问题。
- `样本链条不够清楚`: 提到了病例或标本，但缺少来源、分组、终点、随访、统计或伦理说明。
- `机制跳跃`: 从表达相关或数据库筛选直接跳到靶点/治疗价值，中间缺少因果扰动和模型验证。
- `模型不匹配`: 细胞或动物模型不能支撑所声称的疾病亚型、免疫机制、转移/复发或治疗场景。
- `临床意义后置`: 临床验证只放在最后一项，没有说明它如何反向支撑科学问题和创新点。
- `前期基础未映射`: 论文、平台和样本很多，但没有说明分别支撑哪个研究内容。
