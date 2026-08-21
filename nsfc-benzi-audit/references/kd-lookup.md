# NSFC Knowledge Database Lookup (kd.nsfc.cn)

Use this reference when the audit needs evidence from outside the draft: whether the topic is already funded, whether the 申请代码 routes to the right community, whether 预期成果 is over-promised, whether the applicant's own funded projects overlap the proposal, or when the draft claims "国内尚无人开展".

Everything else in this skill is a closed-world text audit: it judges the draft against itself. This surface is the only one that brings in external facts, so it is also the one where fabrication risk is highest. Every statement produced from this surface must carry a query string, a hit count, and an access date, or it does not go in the report.

## What The Portal Exposes

国家自然科学基金大数据知识管理服务门户 <https://kd.nsfc.cn/>. Observed 2026-08-21; re-check before relying on access details.

| Module | Content | Access |
| --- | --- | --- |
| 结题项目检索 | 已结题项目：批准号、名称、负责人、依托单位、项目类别、申请代码、批准/结题年度、资助经费、中文摘要、关键词 | Open (no login) |
| 结题报告全文 | 结题报告 / 成果报告 full text | Needs 科学基金网络信息系统 (ISIS) account |
| 资助项目检索 | 已资助（含未结题）项目清单 | Captcha-gated |
| 项目成果 | 项目产出的论文、专著、专利、获奖 | Open |
| 人员 / 机构检索、合作网络 | PI 与单位画像、合作关系网络 | Partly login-gated |
| 多维统计 | 申请/资助多维统计、成果产出统计 | Open |

Three constraints that shape every use of this surface:

- **~4-year blind spot.** Abstracts and full text appear only after 结题. A project funded in year N surfaces around N+4 (青年 3 年 + 结题公开延迟). The freshest collision signal lives in 资助项目检索, which is captcha-gated. So a clean 撞题 result is weak evidence; a positive hit is strong evidence.
- **Application-code drift.** NSFC restructured 申请代码 in recent years (rolled out by 学部, not all at once). Old 结题项目 carry the code system in force at their 批准年度. When comparing code distributions, say which years the counts came from and do not treat an old code string as current. The current annual 指南 is authoritative for the code the applicant should file under.
- **Selection bias.** Only funded projects are in the database. It shows what got funded, never what was rejected, so it cannot tell an applicant that a phrasing "works" — only that a topic is occupied.

## Default Mechanism: The Applicant Runs The Query

Do not automate login, captcha, or bulk collection. Emit a 查询清单 for the applicant to run in the browser (they already hold the ISIS account that unlocks full text), then parse what they paste back.

Rules:

- Ask the applicant to paste back the result list (or a screenshot/CSV), including the query string, the filters used, and the hit count. Without the hit count, findings are unquotable.
- If any scripting is used at all, restrict it to the open 结题项目检索 endpoint, cache every response, keep it at or below one request per second, and stop on the first 503 — the portal throttles aggressively and is a government service, not a data source to crawl.
- Tell the applicant to search with **keywords only**. Never paste the abstract or research contents of an unsubmitted draft into an external search box.

## The Five Lookups

Ranked by how much they change the revision list. Run 1 and 2 whenever the draft's 申请代码 and keywords are known; the rest on demand.

### 1. 撞题核查 (topic collision)

- **Query**: draft keywords (2-4 terms, one at a time) × 申请代码 × 批准年度 last 5-8 years, in both 结题项目检索 and 资助项目检索.
- **Read**: for each hit whose 摘要 overlaps the draft, name which 研究内容 it overlaps and on which axis (对象 / 数据条件 / 方法 / 验证).
- **Convert to action**: overlap is not a veto — it is a demand for an explicit differentiation sentence. Write the fix as "在创新点第 N 条后补一句，说明相对 [某已资助方向] 新增的变量/关系/边界". If three or more funded projects cover the same object with the same method, the finding escalates: the 通讯评审人 is plausibly one of those PIs, and an undifferentiated draft reads as a rerun.
- **On empty result**: report "在 kd 已结题库中未命中，但存在约 4 年数据盲区，不能据此声称新颖". Never convert an empty result into a novelty claim.

### 2. 申请代码校准 (code routing)

- **Query**: take 5-10 topics closest to the draft (from its own 参考文献 or its 代表作), search each by keyword without a code filter, and tally which 申请代码 the hits carry.
- **Read**: compare that distribution with the code the draft plans to file under.
- **Convert to action**: if the draft's chosen code holds few or no comparable projects while a sibling code holds many, this is a high-priority finding — a wrong code sends the application to a 学部 and reviewer pool that does not value the topic, and it is decided before any reviewer reads a word. Report the counts, name the candidate code, and tell the applicant to confirm against the current annual 指南 rather than against the historical distribution.
- **Caveat**: code drift (above). A code that dominated 2016 hits may not exist in the current system.

### 3. 预期成果标定 (output calibration)

- **Query**: same 申请代码 × same 项目类别 (青年/面上/地区), sample 10-20 结题项目, read their 成果 counts.
- **Read**: the realistic band of 论文/专利 output for that project type in that code.
- **Convert to action**: if the draft promises well above the band, this maps directly onto canonical 通讯评议 negative comment #5 (预期成果过高，超出申请人基础与能力). Recommend restructuring 预期成果 by scientific question rather than by count, and bringing the counts into the observed band.
- **Do not** report a mean as if it were a rule. Report it as "同类结题项目产出多在 X-Y 区间（样本 N，查询日期）".

### 4. 申请人自身项目连续性 (self-overlap and past performance)

- **Query**: applicant name × 依托单位 in 结题项目检索; also their 在研 project if the draft names it.
- **Read**: content overlap between the proposal and the applicant's own funded/completed projects, plus what those projects actually produced.
- **Convert to action**: overlap must be visible and explained in the draft, not hidden — reviewers run exactly this query. Weak output on a completed NSFC project maps to canonical negative comment #4 (已完成项目绩效不突出), and the draft should address it rather than leave the reviewer to find it. This feeds the duplication check in `representative-works.md`.
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

If absorbed samples change the skill's rules, follow the exemplar-learning update procedure and the README `Calibrated` badge convention.

## Interpretation Rules

- 查不到 ≠ 不存在. Absence from kd is never evidence of novelty, priority, or a research gap.
- 已资助 ≠ 写得好. The database contains no rejected applications, so it cannot validate writing choices.
- Do not state 经费额度、绩效评价、单位排名 as judgments; report them as retrieved facts with the query and date.
- If the portal is unreachable, throttled, or the applicant does not run the queries, say the surface was **未核查** and keep the rest of the audit closed-world. Do not fill the gap from memory.

## Output Pattern

```markdown
### 资助格局与撞题核查

- 核查方式：<申请人自查并回传 / 未核查及原因>
- 查询式与命中数：<关键词 × 代码 × 年度区间 → N 条>（查询日期：）
- 撞题风险：
- 申请代码校准：<当前代码 N1 条 / 候选代码 N2 条；需按当年指南确认>
- 预期成果标定：<同类结题项目产出区间，样本 N>
- 申请人自身项目重复度：
- 盲区声明：kd 仅收录已结题项目，存在约 4 年数据盲区；申请代码体系近年有调整，旧项目沿用旧代码。

| 相邻已资助/已结题项目 | 年度 | 申请代码 | 与本子重合的部分 | 需要显式切分的说法 |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
```

## Query Card For The Applicant

Hand this over when the surface is requested; the applicant runs it and pastes results back.

```markdown
请在 https://kd.nsfc.cn/ 依次执行以下检索，并把结果列表（含命中条数）回传：

1. 撞题：在「结题项目检索」和「资助项目检索」中，用关键词 [K1]、[K2]、[K3] 分别检索，
   限定申请代码 [CODE]，批准年度 [近 5-8 年]。回传命中条数 + 与本子相近的项目名称和摘要。
2. 代码校准：用同样的关键词检索，但**不限定申请代码**，回传命中项目各自挂的申请代码分布。
3. 成果标定：检索申请代码 [CODE] + 项目类别 [青年/面上/地区] 的结题项目，抽 10-20 项，
   回传它们的论文/专利产出数量。
4. 自查：用你本人姓名 + 依托单位检索结题项目，回传你自己已结题项目的名称、摘要与产出。

注意：检索框里只输关键词，不要粘贴未提交本子的摘要或研究内容原文。
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
