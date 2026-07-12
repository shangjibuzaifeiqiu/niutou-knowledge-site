---
layout: ../../layouts/NoteLayout.astro
title: 曲线积分、曲面积分与场论公式
description: 整理第一类和第二类曲线积分、Green 公式、Gauss 公式、Stokes 公式和路径无关条件。
subject: 数学分析
course: 数学分析（二）
chapter: 曲线曲面积分
source: 数学分析（2）.pdf
sourcePages: 第 6-7 页
pages: 原笔记第 6-7 页
updated: 2026-07-12
status: 已整理 · 知识点拆分
summary: 把曲线曲面积分和 Green、Gauss、Stokes 三个公式放在同一组复习。
tags: [曲线积分, 曲面积分, Green公式, Gauss公式, Stokes公式]
---

## 曲线积分

第一类曲线积分：

$$
\int_L f(x,y)\,ds.
$$

若 $x=x(t),y=y(t)$，则

$$
ds=\sqrt{(x'(t))^2+(y'(t))^2}\,dt.
$$

第二类曲线积分：

$$
\int_L P\,dx+Q\,dy.
$$

## Green 公式

$$
\oint_{\partial D}P\,dx+Q\,dy
=\iint_D\left(
\frac{\partial Q}{\partial x}
-\frac{\partial P}{\partial y}
\right)dx\,dy.
$$

若区域单连通且

$$
\frac{\partial P}{\partial y}
=\frac{\partial Q}{\partial x},
$$

则曲线积分与路径无关。

## Gauss 与 Stokes

Gauss 公式：

$$
\iint_{\partial\Omega}\mathbf F\cdot\mathbf n\,dS
=\iiint_\Omega\nabla\cdot\mathbf F\,dv.
$$

Stokes 公式：

$$
\oint_{\partial S}\mathbf F\cdot d\mathbf r
=\iint_S(\nabla\times\mathbf F)\cdot\mathbf n\,dS.
$$

## 原页对照

<div class="page-gallery">
  <figure class="source-page"><img src="/note-pages/math-analysis-p06.webp" alt="数学分析原笔记第 6 页" loading="lazy" /><figcaption>第 6 页 · 曲线曲面积分</figcaption></figure>
  <figure class="source-page"><img src="/note-pages/math-analysis-p07.webp" alt="数学分析原笔记第 7 页" loading="lazy" /><figcaption>第 7 页 · Green、Gauss、Stokes 公式</figcaption></figure>
</div>
