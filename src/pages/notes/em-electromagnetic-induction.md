---
layout: ../../layouts/NoteLayout.astro
title: 电磁感应与自感互感
description: 整理法拉第电磁感应定律、动生电动势、感生电动势、自感和互感。
subject: 电磁学
course: 大学物理电磁学
chapter: 电磁感应
source: 物理·电磁学(3).pdf
sourcePages: 第 2 页
pages: 原笔记第 2 页
updated: 2026-07-12
status: 已整理 · 知识点拆分
summary: 用磁通量变化统一描述动生电动势、感生电动势、自感和互感。
tags: [电磁感应, 法拉第定律, 自感, 互感]
---

## 法拉第电磁感应定律

总感应电动势：

$$
\mathcal E=-n\frac{d\Phi}{dt}
=\mathcal E_{\mathrm{mot}}+\mathcal E_{\mathrm{ind}}.
$$

动生电动势：

$$
\mathcal E_{\mathrm{mot}}
=\int(\mathbf v\times\mathbf B)\cdot d\mathbf l.
$$

感生电动势：

$$
\mathcal E_{\mathrm{ind}}
=-\iint_S\frac{\partial\mathbf B}{\partial t}\cdot d\mathbf S,
\qquad
\mathcal E_{\mathrm{ind}}
=\oint_L\mathbf E_{\mathrm{ind}}\cdot d\mathbf l.
$$

由此得到

$$
\nabla\times\mathbf E
=-\frac{\partial\mathbf B}{\partial t}.
$$

## 自感与互感

自感电动势：

$$
\mathcal E_L=-L\frac{di}{dt}.
$$

自感磁能：

$$
E=\frac12Li^2.
$$

互感电动势：

$$
\mathcal E_{12}=-M\frac{di_1}{dt},
\qquad
\mathcal E_{21}=-M\frac{di_2}{dt}.
$$

互感能量项：

$$
E=MI_1I_2.
$$

## 原页对照

<div class="page-gallery">
  <figure class="source-page">
    <img src="/note-pages/electromagnetism-p02.webp" alt="电磁学原笔记第 2 页" loading="lazy" />
    <figcaption>第 2 页 · 电磁感应、自感和互感</figcaption>
  </figure>
</div>
