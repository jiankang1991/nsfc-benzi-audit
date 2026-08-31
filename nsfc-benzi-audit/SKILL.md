---
name: nsfc-benzi-audit
description: Use when a user wants applicant-facing diagnosis and revision advice on a Chinese NSFC (国自然) application draft — asks for 本子把脉, 本子体检, 国自然申请书修改建议, NSFC benzi audit, 帮我看国自然本子, 标书逻辑诊断, 青年/面上/地区基金申请书修改, 对照已中本子, 从中标样本提炼写法规律, 选题撞题核查, or 申请代码选得对不对 — or wants critique of the title, abstract, key scientific questions, rationale, research contents, innovation, feasibility, research basis, 代表作/代表性论著 quality and support, or cross-section consistency. Accepts PDF/DOCX/Markdown/text or extracted draft text. This is applicant revision advice, not formal communication-review opinions; for expert review forms use nsfc-review.
---

# NSFC Benzi Audit

Use this skill to produce applicant-facing diagnosis and revision advice for NSFC application drafts. The goal is to expose logic breaks, weak scientific-question framing, mismatched sections, and high-impact fixes before submission.

Do not write a formal peer-review opinion unless the user explicitly asks for communication review; route that to `nsfc-review`. Do not fabricate facts, papers, project histories, budgets, or official rule details. Keep final advice grounded in the draft text and clearly mark uncertain extraction/OCR issues.

## Workflow

1. Locate and extract the draft.
   - For PDF input, use PDF extraction/OCR as needed. Prefer existing extracted Markdown such as `full.md` or `output.md` when available.
   - For DOCX input, extract text while preserving headings and tables where possible.
   - For extracted Markdown/text folders, prefer `output.md`, `full.md`, or the largest readable Markdown/text file; inspect images only when visual logic diagrams or tables matter.
   - If the file is scanned or extraction is noisy, state the limitation in the report and avoid treating OCR artifacts as applicant mistakes.
   - If a prior `本子诊断报告.md` (or an earlier revision list from this skill) sits next to the draft, read it before diagnosing and treat this run as a re-audit: grade each earlier 必改 item as 已改 / 未改 / 改动无效 against the current text, citing where in the new draft the change landed. Then diagnose the new draft normally. Do not re-derive the earlier findings from scratch, and do not silently drop an earlier 必改 item that is still unaddressed.

2. Identify the review scope before judging.
   - Extract project category, research attribute, application code, title, abstract, keywords, applicant/team context, and section boundaries.
   - If the user asks for a quick pass, inspect title, abstract, scientific questions, research contents, innovations, and research basis first.
   - If the user asks for full diagnosis, inspect the whole application by section.

3. Load the right references.
   - Always read `references/benzi-logic.md` before diagnosing logic or writing suggestions.
   - Read `references/audit-surfaces.md` for full diagnosis, structure/form checks, figure/readability checks, annual-plan and expected-outcome checks, budget-to-task mapping, literature-current-status checks, or policy-risk triage.
   - Read `references/question-distillation.md` when judging how well the scientific question is distilled: the 关键科学问题 importance argument, the rationale's convergence chain, the 科学问题属性 justification, drafts claiming 原创/独辟蹊径/卡脖子/瓶颈/学科交叉, drafts whose core idea is borrowed from another discipline or scale (借鉴/类比/受……启发), or when the user asks whether the 科学问题凝练得好.
   - Read `references/representative-works.md` when the draft lists 代表性论著/代表作/主要论文, or when 研究基础 leans on the applicant's publications. Do not judge those works from titles alone — get the abstract and method from the applicant's PDFs first, else via the `paper-lookup` skill, else mark them 未核实.
   - Read `references/kd-lookup.md` when the audit needs external evidence rather than draft-internal logic: 撞题/选题重复风险, 申请代码是否送对学部, 预期成果是否超额承诺, 申请人自己已资助/已结题项目的重复度与绩效, or a draft claiming 国内尚无人开展. The applicant runs the queries on kd.nsfc.cn; never automate its login or captcha, and never report a lookup result without the query string, hit count, and date.
   - Read `references/exemplar-learning.md` when the user provides already-funded/successful examples, asks to compare with "中的本子"/"中标本子", or asks to improve this skill from sample applications.
   - Read `references/information-communication.md` when the draft or provided examples involve information science, communication networks, optical networks, computer networks, data centers, remote sensing information processing, applied AI, network security, quantum communication, or related information-engineering directions.
   - Read `references/geospatial-remote-sensing.md` when the draft or provided examples involve remote sensing, GIS, geospatial intelligence, DEM/terrain/geomorphology, spatial databases, point clouds, SAR/optical/hyperspectral imagery, video GIS, camera networks, POI/trajectory/location data, city 3D modeling, or geospatial knowledge graphs.
   - Read `references/medical-biomedical.md` when the draft or provided examples involve medicine, clinical research, biomedicine, disease mechanisms, patient cohorts, specimens, animal/cell/organoid models, biomarkers, diagnostics, therapy/intervention, immunology, ethics, or biosafety.
   - Read `references/current-rules.md` when checking current-year compliance, research attributes, application-code risk, budget/ethics/scientific-integrity issues, or anything tied to official NSFC rules.
   - Use `assets/report-template.md` as the output shape unless the user requests another format.

4. If successful examples are provided, separate exemplar learning from target diagnosis.
   - Treat funded examples as pattern evidence, not as text to copy or proof of causality.
   - Anonymize names, project numbers, institutions, unpublished data, and sensitive achievements before extracting patterns.
   - Prefer patterns repeated across matched examples: same project type, similar discipline/application code, similar research attribute, or comparable career stage.
   - Apply exemplar patterns as contrastive questions: what does the target draft fail to make visible that successful examples make visible?

5. Build the one-page logic map.
   - Extract the draft's core logic elements: object/scenario, focused problem or goal, method/path, distinctive feature or innovation, and data/validation loop.
   - Extract the abstract logic chain: object/problem, method/goal, contents/innovation, achievement/significance.
   - Map these terms across title, abstract, rationale, research contents, scientific questions, innovation, feasibility, and research basis.
   - If a 科学问题属性 statement exists, map it too and check it cross-validates the key scientific questions.
   - Mark missing, vague, inconsistent, or duplicated elements.

6. Diagnose by priority, not by page order.
   - Lead with the three decisive funding factors (创新性、技术路线、前期研究基础) and the three scored axes (课题、申请人、研究条件); see `references/benzi-logic.md`. Because 会评 leans on 通讯意见 + title + abstract (see `references/current-rules.md`), weight title/abstract/通讯-facing clarity accordingly.
   - High priority: flaws likely to affect funding judgment, such as no real scientific question, engineering/technical task posing as basic research, object too broad, problem not focused, innovation unsupported, methods not tied to scientific questions, or research basis unrelated.
   - Medium priority: section-level weaknesses, such as literature review not pointing to proposed contents, research objectives not scientific enough, feasibility too generic, innovation phrased as slogans, required columns that may be missing, figures that do not match the text, or literature gaps that weaken the rationale.
   - Low priority: expression, structure, title length, repeated wording, formatting, and local polishing.

7. Give concrete revision actions.
   - For every major finding, cite the draft section or quoted phrase briefly, explain why it is a problem, and give an actionable fix.
   - Prefer rewrite recipes and replacement skeletons over generic advice.
   - When suggesting rewritten text, label it as a draft example that the applicant must verify against facts and literature.

8. Output a Markdown report.
   - Default filename: `本子诊断报告.md` next to the source draft when working in files; otherwise answer in chat.
   - Include: overall judgment, one-page logic map, prioritized fixes, prior-round re-check (when re-auditing), section-by-section findings, annual-plan/expected-outcome findings, budget-to-task mapping (when the draft carries 预算表/预算说明), structure/form checks, figure/readability checks, data/validation evidence mapping, representative-works support (when listed), funding-landscape/topic-collision checks (when kd lookups were run), literature checks, consistency matrix, candidate rewrites, official-rule status, and limits.
   - If successful examples were used, include a short exemplar-derived pattern section with transferability limits.
   - Do not paste long extracted source text. Quote only short phrases needed to support findings.

## Style

- Write in simplified Chinese unless the user asks otherwise.
- Be direct, specific, and applicant-facing: "建议将..." rather than "评审认为..." unless simulating review.
- Separate "must fix before submission" from "can polish later".
- Avoid empty comments such as "加强创新性"; say which scientific question, mechanism, model, method, experiment, or evidence must be changed.
- Preserve academic integrity: do not invent literature, data, publications, patents, collaborations, preliminary results, or official policy requirements.
- Do not copy distinctive wording, structure, data, or undisclosed ideas from successful examples into another applicant's draft.
