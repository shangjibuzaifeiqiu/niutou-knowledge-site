# 牛头的脑袋 - 项目规则

## 目标

把 `input/` 中的个人手写数学、物理 PDF 整理成可追溯、可增量更新的公开知识网站。原始资料始终保持私有。

## 当用户说“更新网站”

1. 先阅读并执行 `docs/reusable-update-workflow.md`。
2. 运行 `prepare-update.ps1`，根据 SHA-256 判断新增或变化的 PDF，并生成 `tmp/update-plan.md`。
3. 只处理 `tmp/update-plan.md` 中 `needs_transcription` 列出的页面。
4. PDF 是扫描页时，必须视觉检查原页；不要依赖文本提取。
5. 把内容整理到 `src/pages/notes/`，保留来源文件和页码。一个 PDF 不是一个知识点页面，必须按概念、公式组或章节小节拆分成多个页面。
6. 明显错误可以修正，但必须在正文中添加“修正说明”。不确定内容标记为待复核，不要猜测。
7. 更新 `config/sources.json` 的 `processed_pages` 和 `src/pages/updates.astro`。
8. 运行 `update-site.ps1`，确认静态构建成功。
9. 发布前检查桌面和移动端页面；原始 PDF、截图、密钥不得进入 `public/` 或 Git。

## 内容结构

主层级为“学科 → 课程 → 章节 → 知识点”。每个知识点页面必须有标题、摘要、学科、课程、章节、来源、页码、状态、更新时间和标签。一份 PDF 可以对应多个知识点页面。

## 设计约定

保持米白、薄荷绿、浅蓝的清新风格。优先保证中文正文和 KaTeX 数学公式的可读性；所有页面都要支持窄屏布局。
