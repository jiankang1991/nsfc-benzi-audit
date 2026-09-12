---
name: nsfc-benzi-audit
description: Diagnose or re-audit an existing Chinese NSFC application draft (国自然本子把脉、标书逻辑诊断、科学问题凝练、修改复核). Check scientific questions, task coverage, evidence, feasibility and applicable form rules; optionally compare funded examples, literature or funding records. Accept PDF/DOCX/Markdown/text. Give applicant-facing revision advice, not applications written from scratch or formal expert-review opinions.
license: MIT; see LICENSE
---

# NSFC Benzi Audit

Ground each diagnosis in the selected application and its actual claims. Keep official requirements, scientific reasoning and writing preferences distinct. Do not invent results, references, project histories, contributions or rules. No companion skill is required for text-internal review.

## 1. Establish Source And Scope

- Use the revision explicitly selected by the user. Separate target drafts, historical extractions, old reports and funded examples; filename or size is not a version identifier.
- Match reused extraction to the original title, revision and contents. Inspect original figures when judging visual evidence; OCR or converted mermaid is not authoritative. If extraction is unavailable, work on supplied readable material and identify the unexamined scope.
- Record year, exact category, form source/version, funding mode, research attribute and code when provided. Unknown metadata does not block internal logic review; it limits compliance conclusions. Missing excerpts or attachments are not proof of an omission in the application.
- Match depth to the request: quick review covers the selected core; full review examines all supplied sections; a专项 review stays within its requested subject. Review depth and report length are separate choices. Do not broaden a local question into a full application audit.

## 2. Read Only What The Task Needs

Read [benzi-logic.md](references/benzi-logic.md) for logic review and the check before issuing findings. It is the shared authority for coverage, evidence scope, priority and finding identity. Select additional references by the actual claim, not a keyword alone; read the relevant sections of long references.

| Trigger | Reference and purpose |
| --- | --- |
| Form, eligibility, codes, budget rules, ethics or integrity compliance | [current-rules.md](references/current-rules.md): dated official baseline; verify the target year/category/stage before a binding conclusion |
| Prediction, causality, models, inverse problems, measurement limits, transfer or priority claims | [research-claims.md](references/research-claims.md): use the matching claim card, including its exceptions |
| Question provenance, originality, bottlenecks, interdisciplinary argument | [question-distillation.md](references/question-distillation.md): contextual argument tests |
| Requested polishing, unclear title/abstract/rationale, reader navigation | [writing-advice.md](references/writing-advice.md): optional expression aids, not scientific requirements |
| Full review or supplied figures, resources, annual plans, outcomes, budgets, literature | [audit-surfaces.md](references/audit-surfaces.md): inspect the relevant surfaces; full review records coverage without repeating every checklist |
| Long/multiple-file draft or interrupted review | [long-draft-review.md](references/long-draft-review.md): source map, optional text index, read coverage, distant counterevidence and resumption |
| Representative works or claims based on publications | [representative-works.md](references/representative-works.md): distinguish verified bibliography, visible abstract and verified method text |
| Topic collision, code calibration, output comparison or requested self-overlap check | [kd-lookup.md](references/kd-lookup.md): applicant-run queries, module/year/status/count boundaries; no automated login or captcha |
| Funded examples or explicit skill improvement from samples | [exemplar-learning.md](references/exemplar-learning.md): transfer limits and rule admission/revision process |
| Communication/resource/protocol/security constraints | [information-communication.md](references/information-communication.md) |
| Spatial objects, sensors, geospatial data or regional/temporal generalization | [geospatial-remote-sensing.md](references/geospatial-remote-sensing.md) |
| Disease, cohorts, biological models, clinical or immune claims | [medical-biomedical.md](references/medical-biomedical.md); select prediction or mechanism guidance according to the claim |

Overlapping fields do not require loading every domain reference. For example, a remote-sensing ML draft needs geospatial and relevant statistical checks; add communication checks only if it makes communication claims. Named lookup skills are optional; use available supplied papers or general lookup tools, and mark unavailable verification accurately.

## 3. Map, Challenge, Then Diagnose

- Extract the actual object, question, sought result, approach, validation and contribution. Build the many-to-many coverage and resource maps described in the core reference; connect evidence found anywhere in the supplied material.
- Treat an apparent problem as a candidate. Before marking it 必改, recheck applicability, search for an answer or counterevidence elsewhere, distinguish unavailable material from an actual contradiction, and identify the smallest repair. Apply the core finding decision table.
- Give one issue one stable ID and one full explanation. Several affected chapters can reference the same issue. Do not demand a quota of findings; a review can conclude that no substantive change is needed within its scope.
- State impact and evidence certainty separately. An important but unverified concern belongs in a bounded confirmation request, not a confirmed violation. Recommendations may narrow an unsupported claim rather than enlarge the research plan.

## 4. Recheck Previous Opinions

Match the old report/list to the same application, including lists supplied in chat. Check every earlier 必改 item against both the current text and the validity of the old rule. Keep its ID; assign unused IDs to new issues and cross-reference merged or split ones.

Use 已解决 / 部分落实 / 仍存在 / 改动无效 / 原意见撤销或不再适用 / 材料不足无法判断, explaining the evidence boundary. A plan can be corrected in text without its execution being verified. Re-audit the current scope normally; do not preserve an error to agree with a previous reviewer.

## 5. Deliver A Usable Report

Use [report-template.md](assets/report-template.md) as an adaptable shape. Standard output gives scope, conclusion, distinct findings/actions, essential coverage or recheck evidence, and actual verification limits. Full review includes a concise coverage record; detailed matrices belong in an appendix when useful or requested. Omit empty and irrelevant sections.

Write simplified Chinese unless requested otherwise. Quote short evidence with a file/section/page/paragraph locator. Report each root issue once; chapter notes refer to its ID. Offer fact-conditional wording with placeholders only when it helps the requested revision. Do not fill a short draft with generic advice or reconstruct missing research tasks.

Default file: `本子诊断报告.md` beside the selected draft, or chat for a chat-only review. Follow a user-selected output path. Before overwriting an existing report, preserve a unique dated/revision copy; writing to a new path does not require duplicating an already preserved source report. Record the compared version and per-surface 已核查 / 部分核查 / 未核查 / 不适用 from actual work.
