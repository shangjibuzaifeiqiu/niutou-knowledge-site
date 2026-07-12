# 牛头的脑袋：可复用更新工作流

这个流程的目标是：每次只处理新增或变化的笔记页，保留原页对照，减少重复上传和重复视觉识别，从而节省额度。

## 你每次要做什么

1. 把新增 PDF 放入 `input/`。
2. 如果是替换旧 PDF，文件名尽量保持不变。
3. 对 Codex 说：`更新网站，按 docs/reusable-update-workflow.md 执行`。
4. 如果只是修正某个公式，直接说清楚：`修正 数学分析 第 10 页 幂级数收敛半径公式`。

不要反复上传已经整理过的 PDF；仓库会用 SHA-256 判断文件是否变化。

## Codex 每次必须执行的固定步骤

1. 运行：

```powershell
python .\scripts\register_pdfs.py
python .\scripts\prepare_update.py
```

2. 只查看 `tmp/update-plan.md` 标记为 `needs_transcription` 的页面。
3. 对每个待处理页面，先完整扫描页面中的所有栏目和分区，再按知识点拆分，不确定的符号写入“待复核”。
4. 把整理稿写入 `src/pages/notes/`。一个 PDF 是资料源，不是一个知识点页面；一章或一学期的 PDF 必须拆成多个知识点页面。
5. 把公开原页图写入 `public/note-pages/`，不要把原始 PDF 放进 `public/`。
6. 更新：

- `config/sources.json`
- `data/manifest.json`
- `src/pages/updates.astro`

7. 运行：

```powershell
.\update-site.ps1
```

8. 发布前检查：

- 构建成功
- `dist/` 中没有 `.pdf`、`.env` 或密钥
- 新增页面能在本地返回 200
- KaTeX 公式和原页图引用存在

9. 提交并推送到 GitHub，Cloudflare Pages 会自动部署。

## 额度节省规则

- 不重新识别 `processed_pages` 中已经处理过且 PDF 哈希未变化的页面。
- 对只需要改错的页面，优先让用户指出页码和位置，不重新整理整份 PDF。
- 每页先生成本地图片，再只把相关页面交给 GPT 视觉识别。
- 空白页、封面页只登记，不做长篇转写。
- 一个知识点保留一个长期 Markdown 文件；一个 PDF 可以映射到多个 Markdown 文件。
- 如果一页里同时包含多个章节，例如静电学、静磁学、电磁感应，必须拆到不同知识点页面，而不是按页或按 PDF 合并。
- 不为同一公式反复生成多种解释，先保留“原式 + 整理式 + 待复核”。

## 内容整理标准

每篇笔记必须包含：

- 来源 PDF 和页码范围
- 原始页结构
- 按概念整理后的正文
- 关键公式，使用 KaTeX Markdown 语法
- 明确的“待复核”或“修正说明”
- 原页对照图

拆分粒度建议：

- 定义和基本公式可以单独成页。
- 一组强相关公式可以成页，例如“Biot-Savart 定律与安培环路定理”。
- 不同章节不要混在同一页，例如静电场、静磁学、电磁感应、麦克斯韦方程组应拆开。
- 资料源、页码和原页图可以在多个知识点页面中复用。

## 发布后的检查

Cloudflare Pages 部署完成后检查：

- `https://niutou-knowledge-site.pages.dev/`
- `/library/`
- 更新过的 `/notes/.../`
- `/updates/`

如果国内网络打不开，先区分是 Cloudflare 访问问题还是构建失败。构建失败看 Cloudflare 部署日志；访问不稳属于免费 Pages 的网络限制。
