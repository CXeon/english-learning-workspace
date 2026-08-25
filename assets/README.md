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

提交前运行：

```sh
python3 tools/check-public-repo.py
```
