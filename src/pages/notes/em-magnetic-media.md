---
layout: ../../layouts/NoteLayout.astro
title: 磁介质、磁化强度与磁场强度
description: 整理磁化强度、磁化电流、磁场强度 $\mathbf H$ 和磁介质中的安培环路定理。
subject: 电磁学
course: 大学物理电磁学
chapter: 磁介质中的磁场
source: 物理·电磁学(3).pdf
sourcePages: 第 1 页
pages: 原笔记第 1 页
updated: 2026-07-12
status: 已整理 · 知识点拆分
summary: 用 $\mathbf H=\mathbf B/\mu_0-\mathbf M$ 把磁介质中的磁场方程写成自由电流形式。
tags: [磁介质, 磁化强度, 磁场强度, 磁化电流]
---

## 磁化强度

磁化强度定义为

$$
\mathbf M=\frac{\sum\mathbf m}{\Delta V}.
$$

笔记记录的磁化电流密度关系：

$$
\mathbf j_s=\mathbf M\times\mathbf n,
\qquad
\mathbf j=\nabla\times\mathbf M.
$$

## 磁介质中的环路定理

总电流包含自由电流和磁化电流。由环路定理可整理为

$$
\oint_L\left(\frac{\mathbf B}{\mu_0}-\mathbf M\right)\cdot d\mathbf l
=\sum I_{\mathrm{free}}.
$$

定义磁场强度

$$
\mathbf H=\frac{\mathbf B}{\mu_0}-\mathbf M,
$$

则

$$
\oint_L\mathbf H\cdot d\mathbf l=\sum I_{\mathrm{free}}.
$$

线性磁化下

$$
\mathbf M=\chi_m\mathbf H,
$$

所以

$$
\mathbf B=\mu_0(1+\chi_m)\mathbf H=\mu\mathbf H,
\qquad
\mu_r=\frac{\mu}{\mu_0}.
$$

## 原页对照

<div class="page-gallery">
  <figure class="source-page">
    <img src="/note-pages/electromagnetism-p01.webp" alt="电磁学原笔记第 1 页" loading="lazy" />
    <figcaption>第 1 页 · 磁介质和磁场强度</figcaption>
  </figure>
</div>
