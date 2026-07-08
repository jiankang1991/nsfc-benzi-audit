# NSFC Current Rules Check

Use this reference only for official-rule and current-year compliance checks. Treat it as a routing guide, not a substitute for the latest National Natural Science Foundation of China (NSFC) documents.

## Always Prefer Official Sources

When the user asks about eligibility, current application requirements, research attributes, application codes, submission rules, budget rules, ethics, scientific integrity, or deadline-sensitive details:

1. Check the current year's official NSFC guide and application notices first.
2. Use only official NSFC pages or documents for binding requirements.
3. In the report, separate "official rule risk" from "application-writing logic risk".
4. If official pages cannot be accessed, say the rule check was not verified and limit the report to draft logic.

Official starting points:

- NSFC homepage: https://www.nsfc.gov.cn/
- NSFC project guide / application guide area: use the latest annual "国家自然科学基金项目指南" and "项目申请规定" published by NSFC.
- NSFC application system notices: use when the draft depends on submission-form fields.

## Review Pipeline And Scoring (calibration, verify current year)

These are process facts and experience-value constants, not official binding text — mark them "以当年为准" when reporting, but use them to calibrate what the draft must do to survive.

Three stages:

1. 形式审查 (~45 days, ~30 checks): a formal gate. Most-frequent rejection cause is 人员超项; then wrong 申请代码 (routes to the wrong 学部), 依托单位/公章 mismatch, signature issues, and missing attachments (伦理批件, recommendation letters for applicants without a doctorate at mid rank, in-station postdoc consent, biosafety commitment, ≤5 related papers). Roughly thousands of proposals are rejected here each year.
2. 通讯评议 (函评): 3-5 "小同行" peers write the substantive verdict. Each reviewer handles 20-40 proposals. Overall rating A(优,优先资助)/B(良,可予资助)/C(中)/D(差); A-or-B share ≈ 30%, base funding rate ≈ 20%.
3. 会议评审 (会评): a 13-20 person "大同行" panel, given a pool at ~120-130% of the quota. Most panelists are not deeply familiar with a given proposal and lean on 通讯意见 + the lead reviewer's summary + the title and abstract. Decisive facts: A-类 上会 ≈ funded; B-类 上会 ≈ rejected; a proposal with 同意资助 votes not exceeding half the panel is dropped.

Implication for the audit: because 会评 rests on 通讯意见 + title + abstract, the title, abstract, and 通讯-facing clarity (bold-highlighted hypothesis/preliminary-data/feature, key-data figure) carry disproportionate weight.

Canonical 通讯评议 negative comments (audit backwards from these six):

1. Research-status understanding unclear; simply repeats prior or own work.
2. No clearly extracted key scientific question.
3. Logic unclear / just applies routine methods.
4. Performance of already-completed NSFC projects not outstanding.
5. Expected results too high/too many, beyond the applicant's demonstrated basis and ability.
6. Too many errors: broken sentences, misspelled terms, rough English abstract, missing/incorrect key references.

## Rules That Often Affect Draft Diagnosis

Check the current annual guide for exact wording before applying these:

- Project type: 青年科学基金项目、面上项目、地区科学基金项目 and special programs may have different expectations.
- Research attribute: recent NSFC application forms distinguish broad research attributes such as 自由探索类基础研究 and 目标导向类基础研究; older drafts may use the earlier four scientific-question attributes such as 鼓励探索突出原创、聚焦前沿独辟蹊径、需求牵引突破瓶颈、共性导向交叉融通. Do not mix old and current labels without noting the mismatch.
- Application code and keywords jointly select the reviewer pool: the agency picks reviewers mainly by 学科代码 and also by keywords, so a code or keyword slant toward clinical vs basic, or toward one sub-community, changes who reads it. A wrong code can send the application to reviewers who do not value the topic; the first keyword especially steers routing. Diagnose whether the draft's object, methods, keywords, and claimed contribution all match the intended reviewer community, and select the code down to its most specific (6-digit/4-digit) level.
- Scientific integrity: do not help fabricate references, preliminary results, authorship, data, or applicant achievements.
- Ethics and safety: projects involving humans, animals, biosafety, data security, field sampling, geographic/security-sensitive data, or AI/data compliance may need explicit statements and approvals.
- Budget and conditions: equipment, materials, testing, data, and collaboration claims should correspond to the research plan and current budget rules. Concrete points to check against the current-year finance rules: applicants budget 直接费用 only (设备/材料/测试加工/燃料动力等), 间接费用 is set separately; for 差旅费+会议费+国际合作交流费 combined, no itemized basis is required up to ~10% of direct costs, and exceeding ~10% requires a 测算依据 rather than being forbidden (so do not flag a >10% figure as a violation — check whether the draft provided the basis); format must use 万元 to two decimals (unit price in 元 to the integer) or it fails 形式审查. Budget principles: 目标相关性 / 政策相符性 / 经济合理性.

## Output Requirement

When official-rule issues are checked, include a short section:

```markdown
## 官方规则核查状态

- 核查来源：
- 与本子相关的规则风险：
- 未能确认或需申请人进一步确认的事项：
```

Never present a rule as current if it was inferred from old materials or memory.
