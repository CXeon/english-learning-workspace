# 学习资产

这里保存可公开、可复用的课程资产。文章正文放在相应课程的 `lessons/<year>/<lesson-id>/lesson.md`；音频放在 `assets/audio/<lesson-id>/`。历史迁移文件保留在 `assets/audio/legacy/`。

## 新增原创 AI 文章

1. 在课程目录创建 `lesson.md` 和 `result.md`。
2. 为 `lesson.md` 填写完整 front matter，原创大模型材料使用：

```yaml
source_kind: ai_generated_original
source_url: null
copyright_status: original_learning_material
public_release: approved
contains_personal_voice: false
audio_verified: false
```

3. 只写与学习有关的中性内容；不要把私人工作细节、日记或聊天记录原样放入文章。

## 新增合成语音

1. 在 `assets/audio/<lesson-id>/` 存放音频，优先 MP3；WAV 也可接受。
2. 单个二进制文件不得超过 5 MB；不要提交同一内容的多种格式副本。
3. 在 [asset-manifest.md](asset-manifest.md) 记录文件路径、生成来源、真人声音状态和公开结论。
4. 仅提交允许公开再分发的合成语音；不确定服务条款或来源时，放入被 Git 忽略的 `private/`。
5. OpenAI ChatGPT/Codex 应用内置工具生成的默认合成语音，可将来源记为 `openai_chatgpt_codex_app_builtin_synthetic_speech`；若应用未展示具体音频模型，如实记录 `audio_model: not_exposed_by_app`，不得把负责课程编排的文本模型误记为音频模型。
6. 面向学习者播放或公开展示时，明确说明该声音为 AI 生成，并在迁移后立即验证文件可解码且时长大于 0。
7. 通过公开审核后，将课程原创文档和 AI 合成音频纳入提交并推送到远程仓库；这是学习者对该类资产的持续授权。

提交前运行：

```sh
python3 tools/check-public-repo.py
```
