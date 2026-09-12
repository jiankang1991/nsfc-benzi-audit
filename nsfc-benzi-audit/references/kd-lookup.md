# NSFC Knowledge Database Lookup (kd.nsfc.cn)

Use this reference when the audit needs evidence from outside the draft: whether the topic is already funded, whether the 申请代码 routes to the right community, whether 预期成果 is over-promised, whether the applicant's own funded projects overlap the proposal, or when the draft claims "国内尚无人开展".

This surface, official-rule checks and literature verification all use external evidence. For kd coverage/count claims record the module, exact query/filter fields, year type, raw hits, screened/deduplicated sample size and access date. An individually verified project may be discussed when the total hit count is unavailable, but cannot support a frequency or coverage claim; mark that limit explicitly.

## What The Portal Exposes

国家自然科学基金大数据知识管理服务门户 <https://kd.nsfc.cn/>. Access mechanics last observed 2026-08-21. Reference consistency reviewed 2026-09-12; the portal could not be opened during that review, so no live mechanics were reverified. Re-check the form before relying on these details.

| Module | Content | Access |
| --- | --- | --- |
| 结题项目检索 | 已结题项目：批准号、名称、负责人、依托单位、项目类别、**申请代码**、批准/结题年度、资助经费、登记关键词、**成果计数**（期刊论文/会议论文/专著/专利/奖励） | Open (no login) |
| 结题报告全文 | 结题报告 / 成果报告 full text | Needs 科学基金网络信息系统 (ISIS) account |
| 资助项目检索 | 已资助（含未结题）项目清单 | Captcha-gated |
| 项目成果 | 项目产出的论文、专著、专利、获奖 | Open |
| 人员 / 机构检索、合作网络 | PI 与单位画像、合作关系网络 | Partly login-gated |
| 多维统计 | 申请/资助多维统计、成果产出统计 | Open |

Three constraints that shape every use of this surface:

- **Completion-index lag.** The 结题 module lags funding by the project duration and disclosure delay; roughly four years was a useful youth-project estimate in the recorded observations, not a universal freshness guarantee. The 资助 module includes funded/in-progress projects. State which modules and years were actually checked; a zero-hit result never establishes novelty.
- **Application-code drift.** NSFC restructured 申请代码 in recent years (rolled out by 学部, not all at once). Old 结题项目 carry the code system in force at their 批准年度. When comparing code distributions, say which years the counts came from and do not treat an old code string as current. The current annual 指南 is authoritative for the code the applicant should file under.
- **Selection bias.** Only funded projects are in the database. It shows what got funded, never what was rejected, so it cannot tell an applicant that a phrasing "works" — only that a topic is occupied.

## Query Mechanics (last observed 2026-08-21, not reverified 2026-09-12)

These decide whether a query returns anything at all. Tell the applicant, or a query comes back empty and gets misread as "no competing work".

- **结题年度 is mandatory.** The 结题项目检索 form requires one 结题年度 per query, so a multi-year sweep is one query per year. A missing 结题年度 returns 请正确输入检索条件, not zero hits.
- **Search the words that appear in project titles, not the words a paper would use.** `干涉图` returned 0; `干涉` returned 62 in the same year. NSFC titles favor 干涉测量/干涉相位/InSAR over the applicant's own method vocabulary. Run 3-5 title-level variants before concluding anything.
- **Broad title words pull in homonyms across 学部.** `干涉` also returns 量子干涉、涡干涉、光学干涉仪 from A/B 学部. Filter the hit list by 申请代码 before counting anything, or the code distribution is meaningless.
- **关键词 is the registered keyword field, matched literally.** It misses far more than the title field. Use it to confirm, never to rule out.
- **The result row already carries 申请代码 and the achievement counts**, so lookups 2 and 3 need no extra clicks: the code distribution and the 论文/专利 band come straight from the hit list.
- Results are capped (about 100 pages); a broad term gives a count, not a complete list.

## Default Mechanism: The Applicant Runs The Query

Do not automate login, captcha, or bulk collection. Emit a 查询清单 for the applicant to run in the browser (they already hold the ISIS account that unlocks full text), then parse what they paste back.

Rules:

- Ask the applicant to paste back the result list (or a screenshot/CSV), including the query string, the filters used, and the hit count. Without a total hit count, restrict discussion to verifiable individual records and mark overall coverage/counts unknown.
- If any scripting is used at all, restrict it to the open 结题项目检索 endpoint, cache every response, keep it at or below one request per second, and stop on the first 503 — the portal throttles aggressively and is a government service, not a data source to crawl.
- Tell the applicant to search with **keywords only**. Never paste the abstract or research contents of an unsubmitted draft into an external search box.

## The Five Lookups

Choose lookups that resolve the requested question. A known code or keyword is not a reason to expand a scoped internal review into external work. If queries cannot be completed, finish the accessible review with the specific verification limit.

### 1. 撞题核查 (topic collision)

- **Query**: run title-level keyword variants in both modules. For 结题项目检索 select one 结题年度 per query across the chosen completion-year range, then separately screen 批准年度 if needed. In 资助项目检索 use the available 批准年度 filters. Record both year fields; do not treat a funding-year range as a substitute for mandatory completion-year input.
- **Read**: for each hit whose 摘要 overlaps the draft, name which 研究内容 it overlaps and on which axis (对象 / 数据条件 / 方法 / 验证).
- **Convert to action**: compare verified neighboring content against the specific claimed increment. If the distinction is unsupported, identify the comparison to add or the claim to narrow. Project counts alone neither establish duplication nor identify likely reviewers; use the NOVEL card in [research-claims.md](research-claims.md#novel--novelty-priority-and-knowledge-increment).
- **On empty result**: distinguish a successfully executed query with 0 hits from invalid conditions, captcha failure, throttling or incomplete access. Report the queried module/year range and coverage limits; never infer novelty from zero hits.
- **The 结题库 alone is not enough for this lookup.** The nearest competitors are usually funded in the three or four years before submission, which is exactly the blind spot — so a 结题库-only sweep can report a crowded topic as clear. The collision check is only meaningful when the applicant also runs 资助项目检索 (项目公布), captcha and all. If only the open endpoint was run, say so and mark the result 不完整.

### 2. 申请代码校准 (code routing)

- **Query**: take 5-10 topics closest to the draft (from its own 参考文献 or its 代表作), search each by keyword without a code filter, and tally which 申请代码 the hits carry.
- **Read**: compare that distribution with the code the draft plans to file under.
- **Convert to action**: an unexpected code distribution prompts comparison with current code definitions and the project's scientific contribution. Do not escalate a historical count difference alone to a wrong-code finding; a high-priority rule issue requires a verified mismatch with the applicable code scope.
- **Caveat**: code drift (above). A code that dominated 2016 hits may not exist in the current system.

### 3. 预期成果标定 (output calibration)

- **Query**: same 申请代码 × same 项目类别 (青年/面上/地区), sample 10-20 结题项目, read their 成果 counts.
- **Read**: the realistic band of 论文/专利 output for that project type in that code.
- **Convert to action**: compare outcomes with the plan, capacity, period and a suitably matched descriptive sample. An unusually high count is a prompt to check assumptions, not a requirement to move the promise into a historical band; an output count does not measure scientific contribution.
- **Do not** report a mean as if it were a rule. Report it as "同类结题项目产出多在 X-Y 区间（样本 N，查询日期）".
- **Avoid false alarms.** When the sample does not support an over-promise concern, drop it. Do not label an otherwise justified commitment too conservative merely because its count falls below historical outputs.

### 4. 申请人自身项目连续性 (self-overlap and past performance)

- **Query**: applicant name × 依托单位 in 结题项目检索; also their 在研 project if the draft names it.
- **Read**: content overlap between the proposal and the applicant's own funded/completed projects, plus what those projects actually produced.
- **Convert to action**: explain overlap with the applicant's prior projects and the proposed knowledge increment. Compare completed work with its stated goals and circumstances rather than inferring poor performance from counts alone. This complements the duplication check in `representative-works.md`.
- **Privacy note**: only look up the applicant themselves, on their own request. Do not profile co-applicants or third parties.

### 5. 国内研究现状与文献覆盖 (domestic status, reviewer community)

- **Query**: draft topic keywords across 结题项目 + 项目成果; optionally the PI list active under the target 申请代码.
- **Read**: whether the domestic project-level activity the draft ignores exists, and whether the draft's 参考文献 covers that community's work.
- **Convert to action**: turn it into a literature-coverage finding — "该代码下 N 个相关项目的产出中，有 M 篇与内容(2)直接相关，本子一篇未引" — and, separately, into a 回避 checklist item for the applicant's own conflict declaration.
- **Hard boundary**: this is coverage checking and conflict declaration only. Never produce a named "likely reviewer" list, never suggest tailoring content to a specific person, and never suggest citing someone to curry favor.

## Also: Corpus For Calibrating This Skill

Separate from auditing a draft. 结题项目 中文摘要 are public NSFC-published text, so they can be used as calibration samples without the redaction burden that real applicant drafts carry (see `exemplar-learning.md`). Two limits before treating them as exemplars:

- A 结题摘要 is not the 申请书摘要. It is written or revised after the work is done, so it shows funded-topic shape, not the winning application's argument structure. Use it for 选题/对象/问题粒度 patterns, not as a template for 立项依据 rhetoric.
- Do not copy wording, structure, or ideas out of 结题报告 into another applicant's draft. Extract patterns; keep text.

If samples change the rules, follow the exemplar-learning procedure and record source type/scope separately from behavioral validation; do not present an absorbed-source count as a test score.

## Interpretation Rules

- 查不到 ≠ 不存在. Absence from kd is never evidence of novelty, priority, or a research gap.
- 已资助 ≠ 写得好. The database contains no rejected applications, so it cannot validate writing choices.
- Do not state 经费额度、绩效评价、单位排名 as judgments; report them as retrieved facts with the query and date.
- If the portal is unreachable, throttled, or the applicant does not run the queries, say the surface was **未核查** and keep the rest of the audit closed-world. Do not fill the gap from memory.

## Output Pattern

```markdown
### 资助格局与撞题核查

- 核查方式：<申请人自查并回传 / 未核查及原因>
- 查询记录：<模块、词/代码/类别、结题年度、批准年度、原始命中数、去重筛选后样本数、查询状态与日期>
- 撞题风险：
- 申请代码校准：<当前代码 N1 条 / 候选代码 N2 条；需按当年指南确认>
- 预期成果标定：<同类结题项目产出区间，样本 N>
- 申请人自身项目重复度：
- 覆盖限制：<实际查询的模块和年度；结题库滞后、资助库是否查询、截断/筛选/旧代码限制；未命中不证明新颖>

| 相邻已资助/已结题项目 | 年度 | 申请代码 | 与本子重合的部分 | 需要显式切分的说法 |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
```

## Query Card For The Applicant

Adapt the keywords and years; omit output/self-overlap checks that were not requested. These are separate forms, not interchangeable year filters.

```markdown
请在 https://kd.nsfc.cn/ 按下列清单检索，并回传查询条件及结果：

A. 结题项目检索
- 每次选择一个「结题年度」[Y]；按 [Y1…Y2] 逐年查询。
- 项目名称用 [K1]、[K2]、[K3] 等标题级词分别查询。撞题时可限定 [CODE]；代码校准时取消代码限制。
- 如果还需限定批准时间，另记「批准年度」条件；表单不支持时从结果中筛选，并记录筛选范围。批准年度不能代替结题年度。
- 成果标定（如请求）：同样逐个选择结题年度，加 [CODE] 与 [项目类别]，选取可比样本，回传论文/专利等数量、项目期限和筛选依据。
- 本人项目自查（仅在请求时）：同样逐个选择结题年度，用本人姓名和单位检索。

B. 资助项目检索
- 按页面实际提供的批准年度 [A1…A2]、标题级词 [K1/K2/K3] 和适用代码检索。
- 由你本人处理验证码；回传近邻项目及可见信息。摘要不可见就标不可见，不补写。
- 代码校准时取消代码限制。不要把资助检索的批准年度填法套用到结题检索。

每条查询回传：模块、查询词、代码/类别、结题年度、批准年度、日期、原始命中数；另记实际查看条数及筛选/去重后样本数。
状态分开记录：成功零命中 / 成功有命中 / 条件错误 / 验证码或访问失败 / 结果截断。
相近项目请附批准号或可核对来源、名称、年份、代码、可见摘要/成果。总数不可得时标未知，仍可分析来源明确的单个项目。
只在检索框输入必要关键词，不要粘贴未提交本子的摘要或研究内容。若表单与此记录不同，回传实际字段，不把失败当零命中。
```

## Appendix: Observed Endpoints

Recorded for diagnosis only, not as a scraping recipe. Payload field names were not verified.

| Endpoint (prefix `https://kd.nsfc.cn/api`) | Purpose | Observed behavior |
| --- | --- | --- |
| `POST /baseQuery/completionQueryResultsData` | 结题项目检索 | Responds without login; rejects malformed conditions; throttles to 503 under repeated calls |
| `GET /baseQuery/conclusionProjectInfo/{id}` | 结题项目详情 | — |
| `GET /baseQuery/completeProjectReport` | 结题报告全文 | Login-gated |
| `POST /baseQuery/supportQueryResultsData` | 资助项目检索 | Returns 验证码错误 without a captcha token |
| `POST /baseQuery/relatedAchievement`, `GET /baseQuery/resultsInfoData/{id}` | 项目成果 | — |
| `/advancedQuery/person*`, `/advancedQuery/org*`, `*CooperateQueryResultsData` | 人员/机构/合作网络 | Partly login-gated |
| `/advancedMultidimensionalStatistics/statisticsFromModel` | 多维统计 | — |
