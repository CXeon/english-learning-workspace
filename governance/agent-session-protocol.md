# Agent 课程执行与状态更新协议

## 开始

1. 检查 `git status --short`；存在未提交改动时先报告，不覆盖。
2. 按 `START_HERE.md` 读取最小上下文。
3. 输出开课校验，等待学习者确认或回答。

## 进行中

- 不把阅读、听力、维护和技术排障混在同一节课。
- 若音频未准备好，记录 blocker，改做协议允许的轻量回忆；不要临场生成或排障。
- 不得从记忆伪造历史材料原文。

## 结束

1. 更新本课 `result.md`；
2. 更新 `state/current.md`，使其指向唯一的下一步；
3. 更新 `state/review-queue.md`；
4. 如改变教学规则，追加 `governance/decisions.md`；
5. 运行 `python3 tools/check_public_repo.py`；
6. 通过后创建本地提交；除非学习者明确授权，不推送。
