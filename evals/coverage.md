# 信号→见证材料覆盖表

每组信号对应一条能让它触发（或不该触发）的材料与判据编号。没有见证的信号不是错，但**删除或降级它之前要先补材料**，再按 [维护说明](../docs/maintenance.md#规则准入修订与退役) 做有/无该行的对照实跑；否则就重演 `19917ae`——删掉的规则没有材料会触发，评测照样全绿。首次编制 2026-10-17；机制借自 gxCaesar/open-research-skills 的 `check_rule_coverage.py`（每条校验规则一个见证，无见证即报）。

状态三档：**有见证**（材料与判据都在库）；**仅运行记录**（材料不入库或已移除，只剩 `evals/runs/` 的计分）；**无见证**。编号：craft 见 [craft/rubric.md](craft/rubric.md)；mechanism 见 [mechanism/rubric.md](mechanism/rubric.md)；extended 见 [extended/](extended/README.md)；real 见 [runs/2026-09-23-real](runs/2026-09-23-real/README.md)；09-12 见 [runs/2026-09-12](runs/2026-09-12/README.md)；G 系列见 [runs/2026-10-07-borrow](runs/2026-10-07-borrow/README.md) 与 [runs/2026-10-17-borrow](runs/2026-10-17-borrow/README.md)。

## benzi-logic.md

| 信号组 | 见证 → 判据 | 状态 |
| --- | --- | --- |
| Signals, Countercheck And Grading：必改前反查、重要度与证据确定度分开、节选封顶 | craft/02 全稿无必改（T2-1…T2-8）；10-07 反例 8 组科学问题必改 0（版权材料不入库）；real A 原稿 4 条必改均有据 | 有见证 |
| Context Calibration：青年 / 面上 / 地区 / 重点 / 研究属性两类 | craft/01（青年 C）、craft/02（面上转方向，T2-3）；地区、重点/大团队 | 青年、面上有见证；**地区、重点无见证** |
| Research Attribute And Form Version：旧表单四属性与新表单两属性不混 | 09-12 revision（旧表单）；real A/B 按计划年份推断申报年度、不套 2026 规则 | 仅运行记录 |
| Core Logic Elements + Consistency Matrix：限制性定语追踪、两张矩阵 | craft/01 C1（题目定语未落实）；mechanism/01 两问题三内容不判散乱 | 有见证 |
| Data And Validation Loop：数据只在可行性出现、验证只承诺示范、资源无证据、前期结果已完成项目、需求锚点无内容承载 | craft/03 D3（仿真自证、无实测）；real A「现网验证的方案与资源均未落实」「研究基础声称核心内容已完成」 | 有见证（real 部分仅运行记录） |
| Abstract Logic Chain：摘要忠实覆盖核心问题与内容 | — | **无见证**（craft 三稿均为节选，real 缺题目/摘要） |
| Title：基于某方法的某对象研究及应用、过宽、多方法多场景、承诺应用/平台 | craft/01 C1；10-07 反例 33 个获资助题目动宾误报 ≤1（不入库） | 定语有见证；「基于…研究及应用」套式**无见证** |
| Scientific Nature + Scientific-Question Phrasing：问题写成任务、机理改名、过宽、不对应内容；名词短语标题 + 条件化正文；节选封顶 | craft/01 C4；craft/02 T2-2；10-07 节选封顶 | 有见证 |
| Research-Type Tests：机理 / 模型 / 反问题；预测研究不必补机制；反演不要求完整适定性 | craft/02 T2-8（可辨识性已讨论）；extended/claims 01–04（离散模型性质、反演先验边界、同条件测量、方法对照） | 有见证 |
| Rationale：不收敛、年代罗列、缺口未论证就「因此」、意义大问题小；六问漏斗；自身路线难点 | craft/01 C2；10-07 gap-application G1（own-route difficulty） | 有见证 |
| Research Contents And Objectives：独立工作包、目标复述内容、过宽、实验不对应问题、复述依据、写研究思路、写成目的、堆题目词、只写方法、不归题 | craft/01 C3（写成目的）；T1-3 / T2-1 / T3-3 条数不等不判 | 写成目的、条数有见证；**研究思路、只写方法、不归题、堆题目词无见证** |
| Research Content Dependency Graph：输入输出关系、最后一项是真实验证、框架句 | real A「年度计划颠倒内容依赖」；mechanism/01 | 有见证（real 部分仅运行记录）；重点项目 4–5 内容框架句**无见证** |
| Research Plan And Feasibility：复述内容无操作细节、关键数据/平台未落实、高风险无备选、只说团队经验丰富；可行性是方案的可行性 | real A「连通度阶数错误」「现网验证资源未落实」；craft/02 T2-5 / T2-6 不误报；10-17 risk-application（风险二、四应对空泛 2/2 建议改，风险三不误报；目标数据条件与方案不符、先验标定破坏独立测试 2/2 必改） | 有见证；「只说团队经验丰富」**无见证** |
| Features And Innovations：首次/显著无对比、复述内容、仅工程集成、不对应科学问题、完成时态；条数 ≥4、空泛词表、novelty risk、检索式记录 | craft/01 C5；craft/03 D4；real B「创新点引用不存在的前期实验」（截断批，仅记录）；09-28 §3.4 与 10-17 G2 查新（K1 Mironov → 必改，37 条检索式无原稿句子） | 有见证；**完成时态无见证** |
| Research Basis And Conditions：论文堆列无支撑、前期工作无关、暗示已完成、设备过大；根/干/枝叶；相邻基础需声明；无一作 SCI 不是硬伤；保姆现象 | craft/02 T2-3（相邻性已声明）；T1-1 / T2-4（无一作 SCI）；real A「相邻领域论文写成直接基础」 | 有见证；**设备过大、保姆现象无见证** |
| Common Youth Project Risks | craft/01 整体 | 有见证 |

## audit-surfaces.md

| 信号组 | 见证 → 判据 | 状态 |
| --- | --- | --- |
| Structure And Form：形审高频项、申请代码、关键词重建 | 10-07 G3（代码专项，gap-application） | 代码有见证；**关键词重建无见证** |
| Fast-Read Path：套话开头、口号、创新点出现太晚 | craft/01 C2 加分项（套话开头） | 部分有见证 |
| Figure And Visual Evidence：图文不符、八卦图、低分辨率、未提供不判缺 | craft/02 T2-7；real 原图目视（不入库） | 不判缺有见证；**八卦图、图文矛盾无见证** |
| Evidence And Validation Resources：数据丰富/平台完备无映射、合作者无证据、方便示范案例、前期证据过于完整 | real A 现网验证；T2-7 合作协议 | 仅运行记录 / 部分 |
| Key Project And Platform-Heavy Drafts | — | **无见证** |
| Annual Plan And Expected Outcomes：逐年复述、成果承诺已有、里程碑无验证事件、长周期工作排晚；成果按问题分 | real A 年度计划颠倒依赖；T1-4 末年结题至多弱 | 依赖冲突、末年结题有见证；**成果按问题分、长周期排晚无见证** |
| Budget And Task Mapping：预算—任务映射、包干制无预算、零设备费 | T1-2 / T3-2 包干制；T2-5 设备费 0 | 误报侧有见证；**预算—任务缺口正例无见证** |
| Literature And Current Status：年代罗列、「研究很少」无据、缺竞争方法、缺口不指向方法；空白声明四邻域 | craft/01 C2；craft/03 D4；09-28 §3.4 | 有见证；**四邻域无见证** |
| Policy And Integrity Triage：当年规则核实、AI 条款、伦理附件缺失不判违规 | 09-12 medical；real 不套 2026 规则 | 仅运行记录 |
| Output Pattern：编号只出现一次 | real 评分者指出重复 3–4 次 → 09-23 口径统一 | 仅运行记录 |

## question-distillation.md 与其他参考

| 信号组 | 见证 → 判据 | 状态 |
| --- | --- | --- |
| Question-Source Taxonomy / Distillation-Chain Visibility | — | **无见证** |
| Question-Quality Tests | craft/01 C4 | 部分有见证 |
| Per-Attribute Strong Forms：换赛道三件套、跨域类比三件套、新观测体制四要素 | craft/03 D1（四要素）、D2（类比未论证）；T3-1（ResNet 不要求） | 类比、四要素有见证；**换赛道无见证** |
| Difficulty Section Audit：方法假设—对象属性匹配、自身路线难点 | 10-07 G1 | 部分有见证 |
| Significance Audit：两分结构、强主张须外部证据 | — | **无见证** |
| Supporting Devices：排他性论证等 | — | **无见证** |
| Reviewer-Language Calibration：函评套话解码 | 10-07 G4（2/2 已覆盖） | 仅运行记录 |
| SKILL 步骤 4 复审：旧编号保留、撤销、无法判断 | mechanism/03（previous + comments）；09-12 revision F1–F5 | 有见证 |
| representative-works.md：方法证据分级、作者位次不是硬门槛 | 09-12 revision F5；T1-1 / T2-4 | 有见证 |
| kd-lookup.md：条件错误 / 零命中 / 结题年度、别名 | 09-12 lookup（A–D）；09-28 §3.2 | 仅运行记录 |
| geospatial-remote-sensing.md：划分独立性按泛化主张、平台需求转科学问题 | mechanism/02 问题 B（同源地块跨集）；craft/01–03 均为 SAR/遥感 | 有见证 |
| information-communication.md | real A（信息通信，不入库） | 仅运行记录 |
| medical-biomedical.md：模型按组分判断 | 09-12 medical；real B（截断） | 仅运行记录 |
| exemplar-learning.md：样本规律提炼与迁移限制 | — | **无见证** |

## 汇总

| 状态 | 组数 |
| --- | ---: |
| 有见证（含部分） | 22 |
| 仅运行记录 | 9 |
| 无见证（整组或组内点名的子项） | 15 |

无见证的子项里，下一批材料最值得先补的是：摘要逻辑链、「基于…研究及应用」题式、研究内容只写方法/不归题、预算—任务缺口正例、预期成果按问题分、空白声明四邻域、换赛道三件套、意义两分结构。
