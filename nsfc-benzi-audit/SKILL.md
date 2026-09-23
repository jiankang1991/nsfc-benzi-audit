---
name: nsfc-benzi-audit
description: Use for applicant-facing diagnosis or re-audit of a Chinese NSFC (国自然) application draft — 本子把脉、本子体检、帮我看国自然本子、申请书修改建议、标书逻辑诊断、青年/面上/地区基金申请书修改、对照已中本子、科学问题凝练、代表作支撑、选题撞题核查 or 申请代码检查. Accepts PDF/DOCX/Markdown/text and checks title, abstract, rationale, key scientific questions, research contents, innovation, feasibility, research basis and cross-section consistency, calibrated to the application year and form. Does not write applications from scratch or provide formal expert-review opinions.
license: MIT; see LICENSE
---

# NSFC Benzi Audit

Produce applicant-facing diagnosis and revision advice grounded in the supplied draft. Expose substantive logic breaks, weak evidence and high-impact fixes. Do not fabricate literature, results, project histories, budgets or official requirements.

This workflow gives applicant revision advice. If the user requests formal communication review, identify that separate scope and use a suitable review skill only if available. No companion skill is required for draft-internal diagnosis.

## Workflow

1. Select the source and establish the review scope.
   - Prioritize the source and revision explicitly identified by the user. Separate target drafts, funded examples, old reports, templates and notes. Never select a draft merely because it is the largest Markdown file or named `full.md`/`output.md`.
   - Reuse extracted text only after matching its title, revision and contents to the selected original. Record source path/version and extraction provenance. If multiple plausible drafts cannot be distinguished, ask which one to use.
   - For PDF/DOCX, use available extraction/OCR tools and preserve headings and tables. If extraction is unavailable, state the limitation and work on readable supplied material; do not invent a tool or require a named companion skill.
   - Inspect original figures when judging visual logic or evidence, including preliminary results. Converted mermaid/OCR is not authoritative. Missing extraction is a material gap, not proof that the applicant omitted content.
   - Record application year, exact project category (including 青年 A/B/C where known), form version/source, funding mode (包干制/预算制/待确认), research attribute, application code and source completeness. Keep historical-example years separate from the target year.
   - Use questions, goals and methods as analytical dimensions wherever they occur. Require separate headings only when the applicable form requires them. If year or form is unknown, continue content diagnosis and mark rule applicability unresolved.
   - For a quick pass, focus on title, abstract, scientific questions, contents, innovation and basis. For full diagnosis, cover all supplied sections. A 专项 request (one chapter, one question) stays within that scope. Do not report absent attachments or omitted excerpts as confirmed defects in the original application.
   - For long or multi-file drafts, keep section/page locators and a running list of candidate findings with their locations while reading; before closing, revisit only unresolved candidates and report any source ranges you could not read.

2. Load the relevant references.
   - Always read `references/benzi-logic.md` for logic diagnosis, writing advice and the signal → countercheck → grading table used for every finding.
   - Read `references/current-rules.md` before judging form, year/category compliance, research attributes, application codes, budgets, ethics or integrity requirements. It contains a dated 2026 baseline; verify rules for the target year and stage.
   - Read `references/audit-surfaces.md` for full diagnosis, figures, validation, annual plans, outcomes, budgets, literature or form checks.
   - Read `references/question-distillation.md` for question-source and distillation quality, or claims of 原创/独辟蹊径/瓶颈/交叉/跨域类比. Its strong forms apply when the draft actually makes that claim; they are not mandatory headings for every draft.
   - Read `references/representative-works.md` when the draft lists representative works or relies on publications. Prefer supplied PDFs, then available DOI/publisher/preprint lookup tools. A literature/citation lookup skill is an optional integration if installed. Distinguish bibliographic verification, abstract access and full-method verification; mark remaining evidence 未核实.
   - Read `references/kd-lookup.md` for topic collision, code calibration, output comparisons or applicant-requested self-overlap checks. The applicant runs portal queries; never automate login or captcha. Record module, query, year fields, date, error/zero-hit status and counts before making coverage claims.
   - Read `references/exemplar-learning.md` for funded/successful examples or improvement from sample applications. Use matched contexts, anonymized patterns and transferability limits; do not copy facts or distinctive wording into the target.
   - Read `references/information-communication.md` for information science, communications, networks, applied AI, security, quantum communication or related information engineering.
   - Read `references/geospatial-remote-sensing.md` for remote sensing, GIS, SAR/InSAR, optical/hyperspectral imagery, DEM/terrain, point clouds, spatial databases/graphs, trajectories, video GIS or city 3D models.
   - Read `references/medical-biomedical.md` for medicine, cohorts/specimens, disease mechanisms, cell/animal/organoid models, biomarkers, interventions, ethics or biosafety.
   - Use `assets/report-template.md` as an adaptable report shape unless the user requests another format.

3. Build the logic and evidence maps.
   - Extract object/scenario, problem/goal, method/path, innovation, validation and expected significance; track them across title, abstract, rationale, contents, objectives, questions, route and basis.
   - Include the actual research attribute and any historical scientific-question statement when relevant, without mixing their form versions.
   - Build a many-to-many question–content–objective–validation map. Report uncovered questions or tasks with no explained scientific role, not unequal item counts. Supporting methods and validation tasks can share a question.
   - Distinguish the source of a question (literature, theory, observation, own work, demand) from the applicant's capacity to study it. Assess personal contribution, available resources and preliminary evidence in field-appropriate forms; no universal first-author SCI or pre-experiment threshold.

4. Recheck prior findings when a prior report/list is supplied in files or chat.
   - First match it to the same application. Check every earlier 必改 item against both the new text and the applicable evidence/rule, then diagnose the current draft normally. Keep old IDs; give new issues unused IDs and cross-reference merged or split ones.
   - Use 已解决 / 部分落实 / 仍存在 / 改动无效 / 原意见撤销或不再适用 / 材料不足无法判断. Explain withdrawals, changed scope and incomplete evidence. Do not silently drop old items or preserve an incorrect finding merely because an earlier report said it.

5. Diagnose by impact and give concrete actions.
   - Assess novelty, route, applicant contribution and resources. These are diagnosis dimensions, not fixed scoring weights or funding predictions.
   - Use the reference flags actively: they encode what reviewers repeatedly penalize (title/abstract drift, rationale not converging, contents written as purposes, questions that are tasks, hollow 首次/填补空白, decorative modifiers, silent topic switches, unquantified bottlenecks, uncashed analogies). Treat each hit as a candidate, run the countercheck in `benzi-logic.md`, then grade it 必改 / 待核实 / 建议改 / 可润色.
   - 必改: unanswered key questions, unsupported core innovation, broken coverage, infeasible critical steps, title/abstract promises the body never delivers, or verified material rule violations. 建议改: section-level craft or evidence weaknesses a reviewer is likely to notice. 可润色: wording and presentation preferences. Item counts, heading style and figure counts alone never reach 必改.
   - Give each root issue one stable ID and one full explanation; section notes reference the ID. For each finding cite the location/short phrase, explain its consequence and give the smallest actionable fix. Separate verified official requirements, logic/evidence risks and presentation suggestions. Do not pad findings; a draft can have no 必改 item.
   - Use fact-conditional revision skeletons with placeholders, not invented results or ready-made application claims. Label proposed expressions for applicant verification.

6. Write the report and preserve its evidence trail.
   - Default filename: `本子诊断报告.md` next to the selected draft; otherwise answer in chat. Before replacing an existing report, preserve it under a unique dated/revision filename and record which prior report was compared.
   - Include scope, overall assessment, one-page logic map, the prioritized finding list, prior-item recheck when applicable, and rewrite skeletons for 必改 items. For full diagnosis add a compact correspondence table (gap rows only) and one-line statuses for surfaces actually involved. The finding list carries all explanation; every other section is a one-line verdict, and each ID appears at most once outside the list. Per-chapter notes only when the user asks for them. If the user asks for a short answer (one paragraph, one chapter, a chat message), use that length; review depth and report length are separate choices.
   - Populate optional sections only when relevant. Record 已核查 / 部分核查 / 未核查 / 不适用 per surface, with evidence scope, sources and dates. Generate limitations from actual work rather than copying blanket disclaimers.
   - Write in simplified Chinese unless asked otherwise. Keep advice applicant-facing, quote only short supporting phrases, and separate 必改 from 可润色.
