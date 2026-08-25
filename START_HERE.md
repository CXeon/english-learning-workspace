# Start Here: Agent 学习协议入口

你正在接续一套长期英语学习系统。仓库而不是聊天记录是唯一事实来源。

## 开课前必须读取

1. 本文件；
2. `governance/teaching-contract.md`；
3. `governance/agent-session-protocol.md`；
4. `state/current.md`。

然后根据 `next_session_mode` 决定下一步：

- `resume`：读取 `lesson_path` 指向的已有课程文件，然后继续该课程。
- `prepare`：读取 `material_brief`，先创建一份新的课程文件，再开始当天规定课型的学习任务。此时 `lesson_path` 可以为空，不得尝试读取不存在的文件。

除非上述文件引用，否则不要读取完整历史或全部课程。不要重做总计划。

## 禁用的技能与工作流

本仓库的英语教学不得启用、安装、调用或遵循 `superpowers:*`、`grilling`，或其他会把教学转化为开发流程、压力测试或无关自动化的技能。不要创建与这些技能有关的规格、计划、目录或文件。

如平台要求读取技能清单，仍以本仓库的教学协议为准：直接按本文件和 `governance/` 中的规则带课。

## 开课校验

读取完成后，先向学习者显示且等待确认：

```text
课型：
预计时长：
材料：
本次边界：
第一步：
```

未完成开课校验不得开始教学。每次只给学习者一个下一步任务。

## 结束协议

课程完成后，按 `agent-session-protocol.md` 更新课程结果、当前状态和复习队列；运行 `python3 tools/check_public_repo.py`；校验通过后创建本地提交。没有当次明确授权，不得 `git push`。

## 公开安全

所有被 Git 跟踪的文件都视为公开。不能确定可否公开的内容只能放入 `private/`；不要试图把私人内容“稍作脱敏”后直接提交。
