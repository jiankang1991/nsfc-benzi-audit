# Representative Works Audit

Use this reference when the draft lists 代表性论著 / 代表作 / 主要论文, or when the 研究基础 section leans on the applicant's publications. Two separate questions must be answered — they fail independently:

- **质量**: are these works strong enough to make the applicant credible for this project?
- **相关度**: does what these works actually did support what the draft proposes to do?

A draft can list five strong papers that are irrelevant to the proposal, or five perfectly relevant papers that are all weak middle-author workshop entries. Report the two separately.

## Titles Are Not Enough

Do not judge relevance from titles alone. Titles mislead in both directions:

- Title looks aligned but content is not: same keyword, different object, different data source/scale, different assumption, or the "method" in the title is one baseline call in an application paper.
- Title looks unrelated but content is load-bearing: the proposal's key estimator/model was actually built in a paper whose title names a different application.

So before judging relevance, obtain each work's abstract, method, data, and validation. Follow this order:

1. **Applicant-provided source first** — attached PDFs, the 附件 论著, or text already in the draft. Cheapest and most authoritative.
2. **Metadata lookup** — use the `paper-lookup` skill (OpenAlex, Crossref, Semantic Scholar, arXiv; no keys needed) to resolve title/DOI → abstract, year, venue, author list, citation count. Record the identifier and access date.
3. **Mark as unverified** — if lookup returns nothing, say `未核实` and say why. Chinese-journal, conference, and 中文核心 works are frequently unindexed; absence from a database is not evidence of absence. Never infer that a paper does not exist.

Never state impact factor, 分区, venue tier, or citation count from memory. Either it came from a lookup with a recorded source, or it is not reported.

## Quality Checks

For each listed work:

- 作者位次: 第一作者 / 通讯作者 vs 中间作者. A basis section built on middle-author works does not demonstrate the applicant's own capability. For 青年 this is decisive.
- Independence: is the work distinguishable from the advisor's or team leader's line, or does it read as the applicant riding a group program? 青年 reviewers look for an independent story.
- Recency: works clustered 5+ years before submission while the draft claims a fast-moving frontier is a mismatch worth flagging.
- Venue fit: the venue's community should overlap the likely 通讯评审 community for the chosen 申请代码.
- Coherence across the list: five works pointing in five unrelated directions read as opportunistic rather than as an accumulating research line.
- Duplication with funded work: overlap with the applicant's 在研 or 已结题 NSFC projects must be visible and explained, not hidden.

## Relevance Checks

Match each work against the draft's one-page logic map on four axes — 对象、数据/条件、方法、验证. Partial matches are the normal case; name which axis matches and which does not.

Then build the support matrix (see the report template): every 研究内容 should be reachable from at least one representative work on at least one axis. Findings worth reporting:

- 内容 with no representative work behind it on any axis → the highest-value finding in this surface. Say which content, and whether the gap is 方法能力 or 对象/数据可得性.
- All works support 内容一, nothing supports 内容二和三 → the basis is narrower than the proposal.
- A work is cited in 研究基础 but its actual content does not do what the draft implies → integrity risk, report explicitly with the source consulted.
- The works already deliver the proposed outcome → reviewers will ask what remains to be funded (same flag as `audit-surfaces.md` 前期证据过于完整).

## Calibration By Project Type

- 青年: thin or partly adjacent basis is tolerable — potential and an independent, focused story weigh more than volume. Do not demand a 面上-scale track record.
- 面上: continuity matters. Representative works should show an accumulating line that the proposal extends, plus completion status of prior NSFC projects.
- 面上 转向 (the proposal opens a new direction rather than extending the old one): a funded case has been observed where every 代表作 was 唯一一作/唯一通讯 but matched the proposal on the **方法轴 only** (modelling, estimation, and detection capability carried over from the applicant's previous direction) with no work at all on the new 对象; the 对象 axis was carried entirely by unpublished 预研 figures on real data. So "内容 with no representative work on any axis" stays the top finding, but "内容 with no representative work on the 对象 axis" is not by itself fatal — check first whether 研究基础 carries that axis with preliminary results, and whether the draft declares the switch (see the adjacent-basis strong form in `benzi-logic.md`). Silent switching is the flag; declared switching with 预研 evidence is a funded shape.
- 地区: calibrate to regional positioning; do not penalize venue tier alone.

## Optional Deep Signal

Citation context — whether a representative work is cited as a core method or only as background filler — is a genuine quality signal, but requires crawling and parsing citing PDFs (e.g. tools like CitationClaw, which need ScraperAPI/LLM/MinerU credentials). Treat this as optional and out of scope for a normal audit; a raw citation count from OpenAlex is enough for the default pass. Only pursue it if the user asks for representative-work impact analysis specifically and supplies the tooling.

## Output Pattern

```markdown
### 代表作质量与支撑度

- 质量判断（位次/独立性/时效/刊物匹配）：
- 相关度判断（对象/数据/方法/验证四轴）：
- 核查方式与来源：<PDF 原文 / paper-lookup + 标识符 + 访问日期 / 未核实及原因>
- 风险：
- 建议：

| 代表作 | 位次 | 年份/来源 | 对象 | 数据/条件 | 方法 | 支撑的研究内容 | 缺口 |
| --- | --- | --- | --- | --- | --- | --- | --- |
```

Do not fabricate publications, venues, metrics, or author positions. When the draft gives only a title and lookup fails, report the item as 未核实 and ask the applicant to supply the PDF rather than guessing.
