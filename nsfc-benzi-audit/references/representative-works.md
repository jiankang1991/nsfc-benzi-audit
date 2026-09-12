# Representative Works Audit

Use this reference when the draft lists 代表性论著 / 代表作 / 主要论文, or when the 研究基础 section leans on the applicant's publications. Two separate questions must be answered — they fail independently:

- **质量**: are these works strong enough to make the applicant credible for this project?
- **相关度**: does what these works actually did support what the draft proposes to do?

A draft can list strong works that are irrelevant to the proposal, or relevant works whose evidence quality or personal contribution is unclear. Assess those separately; neither venue nor author position alone establishes quality.

## Titles Are Not Enough

Do not judge relevance from titles alone. Titles mislead in both directions:

- Title looks aligned but content is not: same keyword, different object, different data source/scale, different assumption, or the "method" in the title is one baseline call in an application paper.
- Title looks unrelated but content is load-bearing: the proposal's key estimator/model was actually built in a paper whose title names a different application.

Before judging relevance, obtain evidence appropriate to the claim:

1. Prefer applicant-supplied PDFs or accessible source text. Inspect methods, data and validation before making method-level support claims.
2. Use available DOI resolution, publisher pages, official preprint repositories or bibliographic services. An installed `paper-lookup` skill is optional, not a package dependency. If unavailable, use ordinary browsing/lookup tools; if those are unavailable too, continue the internal audit and mark external verification incomplete.
3. Record separate levels: **书目已核实** (identity/year/authors/venue), **摘要可见**, **方法全文已核实**, **未核实**. A bibliographic record establishes existence but not the full method; an abstract supports only the claims it actually states. A missing index entry is not proof that a paper does not exist.

Record identifier, source and access date. For partial access, give a limited support judgment and name the missing evidence; request a PDF only when needed for the conclusion. Never invent metrics or author contributions.

Service authentication/quotas may change. As checked 2026-09-12, [OpenAlex](https://help.openalex.org/api/authentication/) allows limited keyless use and offers a larger budget with a key. Check each service's current access terms rather than assuming all listed services are unlimited or key-free. Never state impact factor, 分区 or citation counts from memory.

## Quality Checks

For each listed work:

- Personal contribution: author position is one clue; inspect the supplied contribution statement, methods, software/data ownership and field conventions. Middle authorship, correspondence authorship or conference publication alone cannot establish or refute independent capability.
- Independence: identify the applicant's actual contribution and ownership. Collaboration with an advisor/team is compatible with independent contribution; inspect evidence rather than infer dependence from the relationship.
- Recency: assess whether the cited methods and capabilities remain relevant to the actual proposed step; age alone is not evidence of obsolescence.
- Venue context: use field conventions to interpret the work and its contribution, not as a prestige threshold or a demand to publish for a presumed reviewer community.
- Coherence across the list: identify which capabilities each work supports. A diverse list is not evidence of opportunism; an unexplained capability gap should be tied to the proposed task.
- Duplication with funded work: overlap with the applicant's 在研 or 已结题 NSFC projects must be visible and explained, not hidden.

## Relevance Checks

Match each work against the draft's one-page logic map on four axes — 对象、数据/条件、方法、验证. Partial matches are the normal case; name which axis matches and which does not.

Build the support matrix against all available evidence, not just publications. Preliminary results, proofs, code, platform access and collaborators can support a content without a corresponding representative paper. Findings worth reporting:

- A content lacking relevant evidence or required resources after considering both works and other basis → identify the specific capability, assumption or access gap. No matching publication alone is not a defect.
- All publications support one content → inspect other basis for the remaining contents before concluding that the proposal exceeds the applicant's capability.
- A work's verified content does not support its attributed result → report the specific attribution mismatch and source; do not infer intent or fabrication without evidence.
- If verified prior work already delivers the specific proposed advance, identify what remains new; distinguish completed components from planned advances using [EVD](benzi-logic.md#evd--evidence-readiness-and-resource-support).

## Calibration By Project Type

- 青年: thin or partly adjacent basis is tolerable — potential and an independent, focused story weigh more than volume. Do not demand a 面上-scale track record.
- 面上: continuity matters. Representative works should show an accumulating line that the proposal extends, plus completion status of prior NSFC projects.
- 面上 转向: method-level prior work may support a new object if the proposal explains the transfer, available resources and remaining uncertainty. Inspect any preliminary evidence on the new object; neither a matching publication nor a prescribed declaration sentence is mandatory. Misrepresenting adjacent work as direct evidence is a substantive problem.
- 地区: calibrate to regional positioning; do not penalize venue tier alone.

## Optional Deep Signal

Citation context can help explain influence if verifiable citing text is available. Treat citation counts as descriptive context, not a sufficient quality measure or a funding threshold. Detailed impact analysis is optional and requires suitable access; do not make extra crawlers or API credentials a prerequisite for the normal audit.

## Output Pattern

Use this table only when a work-level comparison is useful. Keep method-verification limits explicit, and reference existing finding IDs for gaps already explained elsewhere.

```markdown
### 代表作质量与支撑度

- 质量判断（位次/独立性/时效/刊物匹配）：
- 相关度判断（对象/数据/方法/验证四轴）：
- 核查方式与来源：<逐项记录书目已核实/摘要可见/方法全文已核实/未核实，以及标识符、来源、日期>
- 风险：
- 建议：

| 代表作 | 位次 | 年份/来源 | 对象 | 数据/条件 | 方法 | 支撑的研究内容 | 缺口 |
| --- | --- | --- | --- | --- | --- | --- | --- |
```

Do not fabricate publications, venues, metrics, or author positions. When the draft gives only a title and lookup fails, report the item as 未核实 and ask the applicant to supply the PDF rather than guessing.
