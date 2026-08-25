# English Learning Workspace

一个可被不同 AI Agent 接续维护的英语学习工作区。仓库是学习状态、教学规范和经审核课程资产的唯一事实来源。

## 开始

任何 Agent 或学习者均先阅读 [START_HERE.md](START_HERE.md)。不要仅凭聊天历史开始课程。

## 公开仓库边界

仓库所有跟踪内容都会公开。敏感信息、私人反思和未经同意公开的录音只能放在 `private/`，该目录永不提交。原创 AI 文章和来源可说明的合成语音可以提交；详见 [公开内容政策](governance/public-content-policy.md) 和 [学习资产说明](assets/README.md)。

## 本地检查

```sh
python3 tools/check-public-repo.py
git config core.hooksPath .githooks
```

默认只在本地提交；推送到远程前需要学习者明确同意。
