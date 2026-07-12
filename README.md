# 牛头的脑袋

从个人手写数学、物理 PDF 持续生长的知识网站。

## 当前工作流

1. 把新增或替换的 PDF 放入 `input/`。
2. 告诉 Codex“更新网站”。
3. Codex 先运行 `prepare-update.ps1` 检测文件变化并生成 `tmp/update-plan.md`。
4. 内容写入 `src/pages/notes/`，构建后先本地预览，再推送到 GitHub，由 Cloudflare Pages 自动发布。

原始 PDF、临时渲染图、环境变量和密钥均被 `.gitignore` 排除，不进入公开仓库。用于公开对照的压缩 WebP 页面图会放在 `public/note-pages/`。

完整复用流程见 `docs/reusable-update-workflow.md`。最省额度的请求模板见 `templates/update-request.md`。

## 免费公开部署

- GitHub：保存公开网站源码，不包含原始 PDF、临时文件或密钥。
- Cloudflare Pages：连接此 GitHub 仓库，构建命令为 `npm run build`，输出目录为 `dist`。

Cloudflare Pages 作为免费入口使用，但不承诺中国大陆所有网络环境下的稳定可达性。

## 本地命令

```powershell
npm install
npm run dev
.\prepare-update.ps1
.\update-site.ps1
```

## 内容约定

每篇 Markdown 笔记必须写明：学科、课程、章节、来源 PDF、来源页码、整理状态、更新时间和标签。明确修正必须在正文中留下说明；无法确认的公式应标记为待复核。
