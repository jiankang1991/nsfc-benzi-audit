<p align="center">
  <img src="assets/nsfc-bamai-banner.svg" alt="NSFC 本子把脉" width="100%">
</p>

<h1 align="center">NSFC 本子把脉</h1>

<p align="center">
  <strong>给国自然申请书做一次结构化体检：找逻辑断点，给修改抓手。</strong>
</p>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-0027ff?style=flat-square&labelColor=0B0A1A"></a>
  <a href="https://github.com/jiankang1991/nsfc-benzi-audit/commits/main"><img alt="Last commit" src="https://img.shields.io/github/last-commit/jiankang1991/nsfc-benzi-audit?style=flat-square&labelColor=0B0A1A&color=ab0d88"></a>
  <img alt="Agent Skills" src="https://img.shields.io/badge/Agent_Skills-compatible-ff004d?style=flat-square&labelColor=0B0A1A">
  <img alt="Calibrated: 67" src="https://img.shields.io/badge/Calibrated-67-4f46e5?style=flat-square&labelColor=0B0A1A">
</p>

`nsfc-benzi-audit` 是一个用于国家自然科学基金（NSFC/国自然）申请书初稿诊断的 Agent Skill。它面向已经有草稿的申请人，帮助从题目、摘要、立项依据、关键科学问题、研究内容、创新点、研究基础、图表、文献和形式栏目等角度生成修改建议。

它不是代写工具，不承诺申请成功，也不替代申请人自己的科学判断、同行专家建议、依托单位要求和基金委官方指南。

## 快速开始

```text
Use $nsfc-benzi-audit to audit this NSFC application draft.
```

把申请书 PDF、DOCX、Markdown、纯文本，或核心片段贴给 Agent。若提供已中本子作为对照样本，先做匿名化处理，并说明项目类型、获资助年份、粗略学科/申请代码和研究属性。

## 适用场景

- 青年、面上、地区等项目申请书已有初稿，需要做结构性体检。
- 想检查题目、摘要、关键科学问题和创新点是否互相支撑。
- 想把评审人快速阅读时可能卡住的问题提前暴露出来。
- 想生成一份可执行的“优先修改清单”，而不是泛泛润色。
- 手头有已中/已获资助本子，想在匿名化后提炼可迁移写法规律，用来对照当前草稿。
- 医学、临床或生物医学本子需要额外检查疾病机制、样本/队列、模型体系、伦理、生物安全和转化验证链条。

## 不适用场景

- 从零代写申请书。
- 编造论文、数据、前期基础、合作单位或实验结果。
- 复制已中本子的原文、未公开思路、数据、图表或保密研究基础。
- 替代当年官方指南、申请系统和单位科研管理部门要求。
- 输出正式通讯评审意见。

## 安装

推荐用 Skills CLI 一行安装。`npx` 会临时运行 npm 上的 `skills` 命令，从 GitHub 拉取本仓库中的 skill；这不要求本项目本身发布成 npm 包。

Codex：

```bash
npx skills add jiankang1991/nsfc-benzi-audit -g -a codex -y
```

Claude Code：

```bash
npx skills add jiankang1991/nsfc-benzi-audit -g -a claude-code -y
```

如果想让 CLI 自动检测本机已安装的 Agent，也可以用：

```bash
npx skills add jiankang1991/nsfc-benzi-audit -g -y
```

没有 Node.js/npx，或网络环境无法访问 GitHub 时，也可以手动安装。将 `nsfc-benzi-audit/` 目录复制到对应 Agent Skills 目录：

```bash
# Codex
mkdir -p ~/.codex/skills
cp -a nsfc-benzi-audit ~/.codex/skills/

# Claude Code
mkdir -p ~/.claude/skills
cp -a nsfc-benzi-audit ~/.claude/skills/
```

然后在对话中使用：

```text
Use $nsfc-benzi-audit to audit this NSFC application draft.
```

## 推荐输入

最小输入可以是一段申请书核心内容：

```markdown
项目类型：青年 / 面上 / 地区
研究属性：自由探索类基础研究 / 目标导向类基础研究 / 不确定
申请代码：
题目：
摘要：
研究内容：
研究目标：
拟解决的关键科学问题：
特色与创新之处：
研究基础简述：
你最担心的问题：
```

若提供已中本子作为对照样本，建议同时说明项目类型、获资助年份、粗略学科/申请代码、研究属性，并先去除姓名、单位、项目编号、联系方式、未公开数据和敏感成果。

也可以输入 PDF、DOCX、Markdown、纯文本，或从 PDF 转出的文本/Markdown。若涉及真实申请书，注意不要公开个人信息、项目编号、未公开数据、合作单位和敏感成果。

## 输出内容

默认输出一份 Markdown 诊断报告，通常包括：

- 总体判断
- 一页逻辑图
- 优先修改清单
- 分章节诊断
- 形式与栏目完整性
- 图表与可读性
- 数据、验证与研究基础映射
- 文献与研究现状
- 政策与科研诚信
- 信息通信类专项检查（如适用）
- 医学、伦理与样本链条（如适用）
- 一致性矩阵
- 中标样本对照（如提供）
- 摘要、关键科学问题、创新点的改写骨架
- 官方规则核查状态与诊断限制

## 示例

示例文件在 `examples/`：

- `mini-draft.md`：一个本子核心片段示例。
- `mini-report.md`：对应的诊断报告示例。

## 文件结构

```text
nsfc-benzi-audit/
├── SKILL.md
├── agents/openai.yaml
├── assets/report-template.md
└── references/
    ├── benzi-logic.md
    ├── audit-surfaces.md
    ├── information-communication.md
    ├── medical-biomedical.md
    ├── exemplar-learning.md
    └── current-rules.md
```

`SKILL.md` 负责触发和工作流，`references/` 存放诊断判据，`assets/report-template.md` 是默认报告结构。

## 修改示例

下面是几个常见修改例子，展示这个 skill 会从哪些角度给出建议。

| 覆盖能力 | 修改前 | 修改后 | 针对性意见和建议 |
| --- | --- | --- | --- |
| 题目聚焦 | 面向复杂场景的多源智能感知与高效识别方法研究 | 面向[具体场景]的[研究对象]跨源表征与[核心科学问题]研究 | 题目不要同时堆入场景、技术、应用和效果。优先保留“对象/场景 + 问题 + 方法路径”，删去泛化形容词。 |
| 摘要逻辑链 | 本项目拟研究 A、B、C 三类方法，提升精度和效率，具有重要意义。 | 针对[对象]在[场景]中存在的[科学障碍]，拟从[机理/模型]入手，开展三项研究，阐明[关键关系]，形成[可验证结果]。 | 摘要应先让评审看到科学问题，再列研究内容；避免写成任务清单或效果承诺。 |
| 关键科学问题 | 如何构建高精度模型并提升识别效果？ | [变量/机制]如何影响[对象]的[表征/耦合/演化]，以及这种关系如何约束[模型或方法]？ | 把“做一个模型”改成可研究、可验证的机制或关系问题。技术路线可以解决问题，但不应替代科学问题。 |
| 研究内容衔接 | 研究数据构建、模型设计、平台实现和实验验证。 | 内容一回答[机制问题]；内容二建立[模型方法]；内容三在[场景]中验证[假设与边界]。 | 研究内容要逐项回应关键科学问题，形成“问题-内容-方法-验证”的闭环，避免工程流程堆叠。 |
| 创新点表达 | 首次提出某方法，显著提升性能，填补研究空白。 | 创新在于：将已有[方法/理论]从[已有条件]推进到[项目条件]，并通过[约束/机制/验证]解决[现有缺口]。 | 少用“首次、显著、填补空白”等口号。说明相对现有研究的新变量、新关系、新证据或新适用边界。 |
| 研究基础映射 | 申请人发表多篇论文，研究基础扎实，能够保障项目完成。 | 前期工作 1 支撑内容一；前期工作 2 支撑内容二；仍需补充[缺口]的预实验或对比验证。 | 研究基础不要只罗列成果，要映射到每个研究内容；主动暴露还需补强的证据，反而更可信。 |
| 文献与形式核查 | 国内外研究很多，现有方法仍有不足；申请代码和研究属性未在正文中呼应。 | 每个研究现状小节以“已有研究解决了什么、在本项目条件下还缺什么、因此引出哪项内容”收束；正文术语与申请代码、研究属性保持一致。 | 文献综述要服务立项依据，不只是证明读过文献。形式/政策问题只提示申请人按当年指南和系统核查，不替代官方判断。 |

## 设计原则

- 只做诊断和修改建议，不做事实编造。
- 区分“写作逻辑风险”和“官方规则风险”。
- 对政策、资格、AI 使用声明、伦理、安全、预算等问题，以当年 NSFC 官方指南为准。
- 对 OCR 或格式提取错误保持谨慎，不把文本提取问题直接归责给申请人。

## 免责声明

- 本项目仅供学习、研究和申请书自查参考，不保证申请成功。
- 使用者必须遵守 NSFC 科研诚信要求和 AI 使用规范。
- 不应用 AI 直接生成申请书；所有 AI 辅助内容都必须由申请人逐项核实、修改和负责。
- 政策、申请条件、格式要求和申报规则以基金委当年官方指南和申请系统为准。
