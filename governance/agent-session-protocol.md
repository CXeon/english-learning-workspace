# Agent 课程执行与状态更新协议

## 开始

1. 检查 `git status --short`；存在未提交改动时先报告，不覆盖。
2. 按 `START_HERE.md` 读取最小上下文。
3. 检查 `state/current.md` 的 `next_session_mode`：
   - `resume`：读取已有 `lesson_path`；
   - `prepare`：按 `material_brief` 新建课程文件与其公开元数据，再开始本次课；不得读取不存在的路径。原创 AI 生成文章可以提交，须使用 `source_kind: ai_generated_original`。
4. 输出开课校验，等待学习者确认或回答。
5. 不启用 `superpowers:*`、`grilling` 或其他与英语教学无关的技能；不创建其规格或计划文件。

## 进行中

- 不把阅读、听力、维护和技术排障混在同一节课。
- 若音频未准备好，记录 blocker，改做协议允许的轻量回忆；不要临场生成或排障。
- 不得从记忆伪造历史材料原文。
- 新课只能在 `next_session_mode: prepare` 时创建；创建后要将当前状态切换为 `resume`，并写入实际 `lesson_path`。
- 新生成的合成语音可在课前维护环节加入 `assets/audio/` 并登记到资产清单；必须确认不是第三方受限内容、不是未经同意的真人声音，并优先使用 MP3。

## 结束

1. 更新本课 `result.md`；
2. 更新 `state/current.md`，使其指向唯一的下一步；
3. 更新 `state/review-queue.md`；
4. 如改变教学规则，追加 `governance/decisions.md`；
5. 运行 `python3 tools/check-public-repo.py`；
6. 通过后创建本地提交；除非学习者明确授权，不推送。
