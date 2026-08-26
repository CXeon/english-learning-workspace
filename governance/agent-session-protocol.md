# Agent 课程执行与状态更新协议

## 开始

1. 检查 `git status --short`；存在未提交改动时先报告，不覆盖。
2. 按 `START_HERE.md` 读取最小上下文。
3. 检查 `state/current.md` 的 `next_session_mode`：
   - `resume`：读取已有 `lesson_path`；
   - `prepare`：按 `material_brief` 新建课程文件与其公开元数据，再开始本次课；不得读取不存在的路径。原创 AI 生成文章可以提交，须使用 `source_kind: ai_generated_original`。
4. 若本次为听力课，在开课校验前完成音频预检：
   - 文件位于 `assets/audio/<lesson-id>/`，已登记到 `assets/asset-manifest.md`，并已提交、推送到远程仓库；
   - 公开结论为 `approved`，不含未经同意的真人声音，并明确标注为 AI 合成语音；
   - `lesson.md` 的 `audio_verified` 为 `true`，`state/current.md` 的 `audio_status` 为 `ready`；
   - 实际检查文件可解码、时长大于 0，且与课程分段一一对应。
5. 音频预检未通过时，先在正式学习计时外完成生成、迁移、审核、登记、验证与远程上传；若当次无法完成，准备同等时长的完整非音频替代课。不得把技术 blocker 作为缩短或取消学习的理由。
6. 输出开课校验，等待学习者确认或回答。
7. 不启用 `superpowers:*`、`grilling` 或其他与英语教学无关的技能；不创建其规格或计划文件。

## 进行中

- 不把阅读、听力、维护和技术排障混在同一节课。
- 正式学习开始后不得生成、迁移、审核或调试音频；这些工作必须在开课校验前完成。
- 若音频维护在当次无法完成，使用开课前已准备好的完整非音频替代课，保持原定学习时长和有效练习量。
- 不得从记忆伪造历史材料原文。
- 新课只能在 `next_session_mode: prepare` 时创建；创建后要将当前状态切换为 `resume`，并写入实际 `lesson_path`。
- 新生成的合成语音可在课前维护环节加入 `assets/audio/` 并登记到资产清单；必须确认不是第三方受限内容、不是未经同意的真人声音，并优先使用 MP3。

## 结束

1. 更新本课 `result.md`；
2. 更新 `state/current.md`，使其指向唯一的下一步；
3. 更新 `state/review-queue.md`；
4. 如改变教学规则，追加 `governance/decisions.md`；
5. 若下一节标记为听力课，结束维护前必须准备、审核、登记、验证并远程上传所需音频；未就绪时不得把听力课写成唯一下一步，应改排可完整执行的非音频课。
6. 运行 `python3 tools/check-public-repo.py`；
7. 通过后创建提交。学习者已持续授权：公开审核通过的原创课程文档和 AI 合成音频默认推送到远程仓库；其他类型内容除非当次明确授权，不推送。
