# 2026-10-17 借鉴前预注册（gxCaesar/open-research-skills）

来源：github.com/gxCaesar/open-research-skills @c79bac6（Apache-2.0，2026-09-23），10 个 skill 的插件集；基金 skill `writing-funding-proposals` 是工作区模板加记录完整性校验器，语料全为合成的 AI-for-biology 案例，无中文申请书。评估报告（skill-borrow 口径）另存，台账行已记入 my-cc-skills `skill-borrow/references/evaluated-sources.md`。本目录只记录两条待 RED 的候选规则与两条文档侧采纳项的预注册判据；本页写于任何实跑之前。

## 文档侧采纳（RED 已在记录，不另实跑）

| 项 | RED | 落点 | 预注册失败判据 |
| --- | --- | --- | --- |
| A1 信号→见证材料覆盖表 | `19917ae` 删掉写作规则后评测全绿，`c279fbe` 回退（[maintenance 2026-09-14](../../../docs/maintenance.md)）；当日计数：benzi-logic / audit-surfaces / question-distillation 的 Flag 条目 81 条，craft 判据预设问题 9 条、陷阱 15 条、real 埋雷 9 处 | `evals/coverage.md`（新建）；`docs/maintenance.md` 规则退役节加一句 | 覆盖表「无见证」行 < 1 则本条无用，撤 |
| A2 对照运行记录三项 | [2026-09-23 real](../2026-09-23-real/README.md) 自记「报告格式差异明显，只能算半盲」；评分者与被测同模型家族；运行记录只写「当日 skill 快照」，无 commit 与 fixture 哈希 | `evals/README.md` 新节 | 此后任一对照运行缺三项之一，记为不合规运行，不得作为检出率/误报证据 |

A2 的三项：评分前对两臂报告施同一去模板化规则（剥标题、状态表、编号前缀，统一为平铺条目）并记每份改写次数；评分者模型家族不同于被测（本机可走 codex-audit）；输入清单含 skill 快照 commit、每个 fixture 的 sha256、交给子代理的文件列表。

## 待 RED 的候选规则

| 候选 | 材料 | 请求 | 成立条件（成立才借） | 落点 | GREEN 判据 |
| --- | --- | --- | --- | --- | --- |
| G1 风险应对空泛：备选只写「进一步优化模型 / 调整参数 / 增加数据」，无触发信号、无检查时点、无科学处置 | 待写 `risk-application.md`：青年 C 类节选，含研究方案与「风险分析与应对」节；3 条风险空泛，1 条陷阱写实（触发信号 + 检查年度 + 仍回答原问题的替代路线） | 完整体检（同 craft request） | 干净子代理 2 次，当日快照，不联网，看不到本页；**两次都未点名**空泛备选 / 无触发时点才成立；任一次点名即「现行已覆盖」，不借 | `benzi-logic.md` Research Plan And Feasibility 的 Flag 加一条，建议改档；audit-surfaces 优先级口径不变（单独不构成必改） | 2/2 建议改点名并给最小改法（补触发与处置，不加实验）；陷阱风险不被点名；craft/01 C1–C5 全检出且 C4 必改、craft/02 必改仍为 3 项、craft/03 D1–D3 必改 D4 建议改 |
| G2 联网查新检索式不含原稿句子 | craft/02 原稿 | 「做查新，允许联网，不做完整体检」（同 [2026-09-28 §3.4](../2026-09-28-borrow/README.md)） | 干净 1 次；报告列出的检索式中任一条含 ≥15 个连续字符与原稿相同即成立 | `benzi-logic.md` Novelty risk 加一句：检索式用对象/方法/条件的关键词组合，不粘贴原稿句子、摘要或研究内容（同 `kd-lookup.md` 门户规则） | 检索式全为关键词组合，且仍列出全部检索式、来源与日期 |

## 实跑结果（2026-10-17，预注册之后）

输入清单：skill 快照 `9a6010b`；`risk-application.md` sha256 前 16 位 `e16d53d151c6d684`；`../../craft/02/application.md` sha256 前 16 位 `4a053d553d5f9680`。每次运行一个独立上下文，只给请求与材料副本，禁读 evals/ 与 docs/，看不到本页。报告全文留在 scratchpad，不入库。

| 候选 | run a | run b | 结论 |
| --- | --- | --- | --- |
| G1 风险应对空泛 | F5 建议改：风险二「进一步调整模型参数」、风险四「积极协调……必要时增加训练数据」「都是套话，与写得很具体的风险三形成反差」；风险一的空洞应对并入 F1 必改（召回指标无分级样本支撑） | F11 建议改：同样点名风险二、四为套话；风险一并入 F4 必改 | **两次都点名，现行已覆盖，不借**。陷阱风险三两次均未判问题（run b 仅一句可润色：EPI 0.7 阈值可补来源） |
| G2 检索式不含原稿句子 | 37 条检索式（WebSearch 27、Semantic Scholar 5、Crossref 5），`check_queries.py` 以 15 连续字符比对原稿：命中 1 条，重合部分为期刊名「Remote Sensing of Environment」，非原稿句子；降到 10 字仍只此一条 | — | **未成立，不借**。现行 Novelty risk 条下的检索式已是关键词组合 |

附带观察（不计分）：埋点稿另有 4 处作者未刻意埋设的缺陷，两次运行均以必改检出且编号对应——研究目标「1 m 星载全极化」与方案中 ALOS-2/UAVSAR 数据不符；内容一用两区样本标定先验再在 Ridgecrest「独立测试」；科学问题二「替代变化检测」无任何对照基线；严重损毁召回 85% 无分级样本数。两份报告 8,174 / 8,720 字。G2 运行另找到 Mironov 2015/2017/2019、Zheng 2018/2019、Konings 2015 等先行工作并判两条「现有局限」陈述为必改，与 09-28 §3.4 结果同向。

## 状态

- A1 已落地：[coverage.md](../../coverage.md)。A2 已落地：[evals/README.md](../../README.md) 「对照运行的记录要求」。
- G1、G2 均不借；`risk-application.md` 保留为「研究方案：高风险无备选 / 应对空泛」与「先验标定破坏独立测试」的见证材料。
