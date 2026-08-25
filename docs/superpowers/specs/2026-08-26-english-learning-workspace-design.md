# English Learning Workspace 设计规格

日期：2026-08-26  
状态：**待用户审阅，尚未实施**  
目标仓库：`github.com/CXeon/english-learning-workspace`（公开）

## 1. 问题与目标

英语学习不能继续依赖某一个聊天线程或某一种模型的上下文。额度中断、切换 Agent、上下文压缩或模型替换，都不应使课程状态、教学方法或下一步丢失。

本仓库是英语学习的唯一事实来源（source of truth），包括：

- 教学协议、学习偏好和规格调整的原因；
- 每节课的材料、结果、经审核的公开资产和复盘；
- 当前学习状态、待复习词块和阶段指标；
- 可被 Codex、Claude、Zcode 和其他 Agent 共同遵守的启动、执行、结束和交接流程；
- 用 Git 保存的、可追溯的变更历史。

本仓库公开，因此“可公开发布”是所有被 Git 跟踪内容的默认前提。未确定是否适合公开的内容不能提交。

## 2. 已确认的教学事实

### 学习者约束与目标

- 截止目标：2026-12-31 前明显提升听、说、读、写；优先目标是较轻松地阅读并表达。
- 通常工作时间：9:30–18:30，偶尔加班。
- 工作日可稳定学习 20–30 分钟，周末每次 45–60 分钟；加班日使用 8–10 分钟保底课。
- 不以应试为目标；优先保持兴趣和可持续性，漏课不补双倍任务。
- 兴趣：新闻、科普、商业、个人成长、小说、非虚构。

### 初始基线（2026-07-24）

| 能力 | 基线 |
|---|---|
| 阅读 | 约 60–65 词/分钟；约 7 个不确定词；能概括主旨和论证结构。 |
| 写作 | A2 左右；能表达简单观点和原因。 |
| 听力 | 熟悉主题的连续英语无文本时，理解低于 20%。 |
| 口语 | 未准备时连续表达 30 秒较困难。 |

### 已确认的教学协议

1. 核心闭环：`适级阅读 → 配套音频 → 跟读/复述 → 短写作 → 间隔回忆`。
2. 工作日的阅读课与听力课默认分开；只有学习者明确要求加练时才能合并。
3. 听力优先使用上一节已经读过的材料；音频必须在课程前可播放，技术排查不占学习时间。
4. 每份核心材料只选 3–5 个高价值词块；按第 1、3、7、14 天主动回忆。
5. 反馈先判断意思是否清楚；每次最多纠正 2–3 个高价值问题；所有词汇解释必须给出词性、本文语境义和原句搭配/例句。
6. 初期听力使用 10–15 秒分段：盲听 → 对照英文文本 → 跟读 → 关闭文本复听 → 简短复述。
7. 课程以“学习者作答后只给一个下一任务”为节奏，不在一节课内临时扩大范围。
8. 凌晨睡前完成的课，计入前一个学习日。

## 3. 架构原则

### 3.1 最小上下文加载

正常开课只能加载以下文件：

1. `START_HERE.md`
2. `governance/teaching-contract.md`
3. `state/current.md`
4. `state/current.md` 指向的本节课程文件

历史课程、长期指标、决策日志和资产索引仅在被上述文件明确引用时读取。不得复制整个仓库或整段聊天历史到 Agent 上下文。

### 3.2 一个规则源，多平台入口

`START_HERE.md` 是平台无关的唯一入口协议。`AGENTS.md`、`CLAUDE.md` 以及未来的工具适配文件只能引用它，不能复制或改写教学规则。

### 3.3 当前状态只有一个权威文件

`state/current.md` 是唯一的“下一节课从哪里继续”的权威来源。其他文件可以记录历史，但不能与它竞争当前状态。

### 3.4 公开优先与私密隔离

仓库中的跟踪文件都视为可公开发布。`private/` 是本地私密隔离区，必须被永久忽略；它可以存放未审核录音和私人反思，但不是远程备份。

## 4. 目标目录结构

```text
english-learning-workspace/
├── README.md
├── START_HERE.md
├── AGENTS.md
├── CLAUDE.md
├── .gitignore
├── .githooks/
│   └── pre-commit
├── .github/workflows/
│   └── public-audit.yml
├── governance/
│   ├── teaching-contract.md
│   ├── agent-session-protocol.md
│   ├── public-content-policy.md
│   └── decisions.md
├── state/
│   ├── current.md
│   ├── metrics.md
│   └── review-queue.md
├── lessons/
│   └── 2026/
│       └── YYYY-MM-DD-topic/
│           ├── lesson.md
│           ├── result.md
│           └── assets/
├── assets/
│   ├── audio/
│   └── asset-manifest.md
├── private/                 # 本地目录；永不提交
├── tools/
│   └── check-public-repo.py
└── docs/
    └── superpowers/specs/
```

## 5. 文件契约

### `START_HERE.md`

长度不超过约 120 行。它要求任何 Agent：

1. 先读本文件和四个最小上下文文件；
2. 输出“开课校验”；
3. 严格按当前课型和时长带课；
4. 结束时更新指定文件、运行校验、创建本地提交；
5. 默认不推送远程，除非用户明确授权。

开课校验的固定格式：

```text
课型：
预计时长：
材料：
本次边界：
第一步：
```

### `state/current.md`

使用 YAML front matter，正文不超过约 80 行：

```yaml
updated: 2026-08-25
phase: phase-2
lesson_status: listening_in_progress
current_lesson: lessons/2026/2026-08-25-starting-before-you-feel-ready/lesson.md
next_step: "盲听第 3 段，不看文本；记录可辨认词块。"
next_lesson_type: listening
target_minutes: 15
audio_status: verified
review_due:
  - "wait until they feel fully ready"
  - "before starting an important task"
blockers: []
```

正文固定记录：本次完成内容、下次的唯一第一步、目前最重要的学习观察、不可违反的课型边界。当前迁移后应反映 2026-08-25 的未完成听力课。

### 每节课的 `lesson.md`

必须包含：

```yaml
id: 2026-08-25-starting-before-you-feel-ready
date: 2026-08-25
type: reading_then_listening
status: listening_in_progress
source_kind: original
source_url: null
public_release: pending_review
copyright_status: original_or_authorized_only
contains_personal_voice: false
audio_verified: true
```

正文包含原文、目标词块、阅读/听力任务、音频路径和复习计划。若第三方材料没有明确的再发布许可，只记录来源链接和学习者自己的摘要，不复制全文或音频。

### 每节课的 `result.md`

记录学习者实际回答、量化指标、只保留 2–3 个高价值纠错点、下一课建议，以及是否已同步 `state/current.md`。

### `governance/decisions.md`

所有教学规格变化采用追加记录：日期、变化、原因、观察到的效果、影响的文件。不得只靠聊天中的临时约定改变教学方法。

## 6. Agent 生命周期

### 开始

1. 检查工作区是否干净；如有未提交改动，先报告而不覆盖。
2. 读取最小上下文集。
3. 输出开课校验并只等待学习者的本次作答。
4. 若音频不可用，记录为 blocker，改用协议允许的替代活动；不得在课中花时间调试。

### 进行中

- 每次只给一个可完成的任务。
- 不自行合并阅读课、听力课和技术维护任务。
- 不从历史推测材料原文；找不到原文时明确说明并新建后续材料。
- 词汇解释必须包含词性和语境义。

### 结束

1. 更新本课 `result.md`；
2. 更新 `state/current.md` 与 `review-queue.md`；
3. 如规则改变，追加 `decisions.md`；
4. 运行公开审核；
5. 审核通过后，创建一个描述清晰的本地提交；
6. 输出变更摘要与推送状态。没有用户明确指令时，不推送。

## 7. 公开内容审核

### 分层防护

1. **路径阻止**：`.gitignore` 忽略 `private/`、`.env`、密钥、令牌、系统临时文件、原始个人录音。
2. **本地预提交审核**：只扫描暂存内容，拒绝敏感文件名、常见密钥模式、私钥块、超出阈值的文件和缺少公开元数据的资产。
3. **GitHub Actions 复核**：每次 push 和 pull request 重跑同一审核；结果失败时显示明确错误。
4. **人工语义审核**：自动扫描无法识别私人日记、过度暴露个人信息或无授权教材。每个新增可公开资产必须有人工/Agent 的公开结论。

### 初始禁止项

- `.env`、`*.pem`、`*.key`、`id_rsa*`、访问令牌和账号凭据；
- `private/` 下的任何内容；
- 没有明确公开许可的第三方教材、文章、音频和视频；
- 未明确同意公开的真人录音；
- 大于 5 MB 的新二进制文件（初版暂不用 Git LFS）。

### 审核结果

`tools/check-public-repo.py` 将输出：`PASS`、`WARN` 或 `FAIL`。`FAIL` 阻止提交；`WARN` 需要用户确认后才能提交。后续实现可接入成熟的秘密扫描器，但不依赖外部服务才能完成基础检查。

## 8. Git 规则

- 每次正式课程结束至多一个提交，例如：`lesson: record 2026-08-25 listening progress`。
- 教学规格变化独立提交，例如：`governance: separate reading and listening sessions`。
- 迁移历史采用独立提交，便于回滚。
- 默认只本地提交；`git push` 需要用户在当次对话中明确同意。
- 初版不启用 Git LFS；若未来有合法且需要版本化的大音频/视频，再单独设计 LFS 迁移。
- 公开仓库初始不添加开源许可证；除非用户另行选择许可证，公开可见不等于允许他人任意再分发。

## 9. 迁移清单

### 必须迁移

- 原学习计划中的目标、约束、阶段安排、材料规则、听力流程、词汇和纠错偏好；
- 2026-07-24 初始基线；
- 2026-07-27 至 2026-08-25 的课程指标、周报、观察和词块；
- 当前状态：`Starting Before You Feel Ready` 的阅读已完成；第 1、2 段听力已练；下一步是第 3 段盲听；
- 有效音频的文件名和可播放状态。

### 不重建、不迁移或需审核后迁移

- 早期课程的完整英文原文：现有本地记录只有标题、指标与部分词块；没有单独原文文件，不得从聊天记忆重造后伪装为原件。
- 零时长音频，明确排除：
  - `audio-player-test.aiff`
  - `audio-player-test.wav`
  - `lesson-09-audio-check.aiff`
  - `starting-before-you-feel-ready.aiff`
  - `starting-before-you-feel-ready.wav`
- 所有可播放音频：先记录资产清单和生成来源，确认可以公开分发后才加入公开仓库。特别是经第三方在线 TTS 生成的 MP3，默认 `pending_review`。

## 10. 验收标准

实施完成后，任一支持文件读取的 Agent 都能在不读取完整历史的情况下：

1. 在 5 个文件以内确定学习者是谁、当前进行到哪里、下一步是什么；
2. 正确说出本次课型、时长和禁止事项；
3. 在课程结束后只更新规定的状态、结果和复习文件；
4. 在尝试提交敏感内容、未声明来源的资产或过大文件时被阻止；
5. 在额度中断后，用同一仓库从下一个明确步骤继续，而不是重新规划整套学习方案。

## 11. 实施顺序（用户审阅后）

1. 创建基础目录、入口协议和公开政策；
2. 创建状态/课程模板与公开审核脚本；
3. 安装本地 Git hook 和 GitHub Actions；
4. 分批迁移计划、历史进度、词块与当前状态；
5. 审核并按来源状态迁移有效音频；
6. 运行验收检查；
7. 由用户确认后推送第一版到 GitHub。
