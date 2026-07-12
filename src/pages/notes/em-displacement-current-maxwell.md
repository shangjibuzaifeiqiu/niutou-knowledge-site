---
layout: ../../layouts/NoteLayout.astro
title: 位移电流与麦克斯韦方程组
description: 整理位移电流假说、修正后的安培环路定理、麦克斯韦方程组积分形式和微分形式。
subject: 电磁学
course: 大学物理电磁学
chapter: 麦克斯韦方程组
source: 物理·电磁学(3).pdf
sourcePages: 第 2 页
pages: 原笔记第 2 页
updated: 2026-07-12
status: 已整理 · 知识点拆分
summary: 通过位移电流补全安培环路定理，得到完整的麦克斯韦方程组。
tags: [位移电流, 麦克斯韦方程组, 电磁场]
---

## 位移电流

位移电流假说从电流连续性出发。笔记中写到

$$
\oint_S\mathbf j\cdot d\mathbf S
=-\frac{dq}{dt}
=-\iint_S\frac{\partial\mathbf P}{\partial t}\cdot d\mathbf S.
$$

因此 $\frac{\partial\mathbf P}{\partial t}$ 与传导电流密度有相同量纲。把

$$
\frac{\partial\mathbf D}{\partial t}
$$

称为位移电流密度，对应位移电流

$$
I_D=\iint_S\frac{\partial\mathbf D}{\partial t}\cdot d\mathbf S.
$$

修正后的环路定理为

$$
\oint_L\mathbf H\cdot d\mathbf l
=I+I_D
=\iint_S\left(
\mathbf j+\frac{\partial\mathbf D}{\partial t}
\right)\cdot d\mathbf S.
$$

## 麦克斯韦方程组积分形式

$$
\oint_S\mathbf D\cdot d\mathbf S
=\iiint_V\rho\,dV,
$$

$$
\oint_S\mathbf B\cdot d\mathbf S=0,
$$

$$
\oint_L\mathbf E\cdot d\mathbf l
=-\iint_S\frac{\partial\mathbf B}{\partial t}\cdot d\mathbf S,
$$

$$
\oint_L\mathbf H\cdot d\mathbf l
=\iint_S\left(
\mathbf j+\frac{\partial\mathbf D}{\partial t}
\right)\cdot d\mathbf S.
$$

## 麦克斯韦方程组微分形式

$$
\nabla\cdot\mathbf D=\rho,
\qquad
\nabla\cdot\mathbf B=0,
$$

$$
\nabla\times\mathbf E=-\frac{\partial\mathbf B}{\partial t},
\qquad
\nabla\times\mathbf H=
\mathbf j+\frac{\partial\mathbf D}{\partial t}.
$$

## 原页对照

<div class="page-gallery">
  <figure class="source-page">
    <img src="/note-pages/electromagnetism-p02.webp" alt="电磁学原笔记第 2 页" loading="lazy" />
    <figcaption>第 2 页 · 位移电流和麦克斯韦方程组</figcaption>
  </figure>
</div>
