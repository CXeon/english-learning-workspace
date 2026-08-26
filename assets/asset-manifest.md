# 资产清单

资产按课程或迁移批次放在 `assets/audio/`。每个文件均须在这里留有可审计记录。

## 历史迁移：本地 AI 合成语音（2026-08-26）

来源：此前英语学习会话生成并保存在本地的合成语音；学习者已同意公开迁入。它们不含学习者或其他真人声音。每个项目选择可播放的 WAV 版本；同名 AIFF 副本不迁入。公开结论：`approved`。

| 路径 | 类型 | 来源 | 真人声音 | 公开结论 |
|---|---|---|---|---|
| assets/audio/legacy/lesson-01-chunk-1-slow.wav | synthetic_speech | legacy_local_ai_session | no | approved |
| assets/audio/legacy/lesson-01-shadow-sentence-1.wav | synthetic_speech | legacy_local_ai_session | no | approved |
| assets/audio/legacy/lesson-01-small-changes.wav | synthetic_speech | legacy_local_ai_session | no | approved |
| assets/audio/legacy/lesson-01-target-phrase.wav | synthetic_speech | legacy_local_ai_session | no | approved |
| assets/audio/legacy/lesson-02-chunk-1.wav | synthetic_speech | legacy_local_ai_session | no | approved |
| assets/audio/legacy/lesson-03-chunk-1.wav | synthetic_speech | legacy_local_ai_session | no | approved |
| assets/audio/legacy/lesson-03-final-output.wav | synthetic_speech | legacy_local_ai_session | no | approved |
| assets/audio/legacy/lesson-03-target-desks-and.wav | synthetic_speech | legacy_local_ai_session | no | approved |
| assets/audio/legacy/lesson-03-target-more-effort.wav | synthetic_speech | legacy_local_ai_session | no | approved |
| assets/audio/legacy/lesson-05-writing-tasks-chunk-1.wav | synthetic_speech | legacy_local_ai_session | no | approved |
| assets/audio/legacy/lesson-06-explaining-ideas-chunk-1.wav | synthetic_speech | legacy_local_ai_session | no | approved |
| assets/audio/legacy/lesson-07-easy-tasks-chunk-1.wav | synthetic_speech | legacy_local_ai_session | no | approved |
| assets/audio/legacy/lesson-07-easy-tasks-sentence-2.wav | synthetic_speech | legacy_local_ai_session | no | approved |
| assets/audio/legacy/lesson-07-memory-half-1.wav | synthetic_speech | legacy_local_ai_session | no | approved |
| assets/audio/legacy/lesson-07-memory-half-2.wav | synthetic_speech | legacy_local_ai_session | no | approved |
| assets/audio/legacy/lesson-07-memory-quarter-1.wav | synthetic_speech | legacy_local_ai_session | no | approved |
| assets/audio/legacy/lesson-07-memory-quarter-2.wav | synthetic_speech | legacy_local_ai_session | no | approved |
| assets/audio/legacy/lesson-08-ending-1.wav | synthetic_speech | legacy_local_ai_session | no | approved |
| assets/audio/legacy/lesson-08-ending-2.wav | synthetic_speech | legacy_local_ai_session | no | approved |
| assets/audio/legacy/lesson-08-ending-3.wav | synthetic_speech | legacy_local_ai_session | no | approved |
| assets/audio/legacy/lesson-08-ending-full.wav | synthetic_speech | legacy_local_ai_session | no | approved |
| assets/audio/legacy/lesson-08-ending-half.wav | synthetic_speech | legacy_local_ai_session | no | approved |
| assets/audio/legacy/lesson-08-unseen-test.wav | synthetic_speech | legacy_local_ai_session | no | approved |
| assets/audio/legacy/week-02-review-target-down-and.wav | synthetic_speech | legacy_local_ai_session | no | approved |
| assets/audio/legacy/week-02-review-transfer-listening.wav | synthetic_speech | legacy_local_ai_session | no | approved |

## 课程音频：Starting Before You Feel Ready（2026-08-27 审核迁移）

来源：2026-08-25 英语学习会话中，由 OpenAI ChatGPT/Codex 应用内置合成语音工具生成；GPT-5.6 Sol 负责课程编排，应用未展示实际音频模型。学习者确认生成来源并明确要求公开迁移。音频使用应用默认合成声音，不含学习者或其他真人声音，也未使用自定义或克隆声音。播放时须说明声音为 AI 生成。三个 MP3 均已验证可解码且时长大于 0。公开结论：`approved`。

| 路径 | 类型 | 来源 | 真人声音 | 公开结论 |
|---|---|---|---|---|
| assets/audio/2026-08-25-starting-before-you-feel-ready/chunk-1.mp3 | synthetic_speech | openai_chatgpt_codex_app_builtin_synthetic_speech; audio_model=not_exposed_by_app | no | approved |
| assets/audio/2026-08-25-starting-before-you-feel-ready/chunk-2.mp3 | synthetic_speech | openai_chatgpt_codex_app_builtin_synthetic_speech; audio_model=not_exposed_by_app | no | approved |
| assets/audio/2026-08-25-starting-before-you-feel-ready/chunk-3.mp3 | synthetic_speech | openai_chatgpt_codex_app_builtin_synthetic_speech; audio_model=not_exposed_by_app | no | approved |

## 未迁移的资产

| 资产 | 状态 | 原因 |
|---|---|---|
| 零时长测试音频（5 个） | excluded | 不可播放，不迁移。 |

新资产进入仓库前，需记录来源、许可、是否含真人声音与公开结论。具体存放和命名见 [assets/README.md](README.md)。
