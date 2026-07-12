---
layout: ../../layouts/NoteLayout.astro
title: 电势、电势差与等势面
description: 整理静电场环路定理、电势定义、电势与电场的关系以及等势面的几何意义。
subject: 电磁学
course: 大学物理电磁学
chapter: 静电场
source: 物理·电磁学(3).pdf
sourcePages: 第 2 页
pages: 原笔记第 2 页
updated: 2026-07-12
status: 已整理 · 知识点拆分
summary: 从静电场保守性出发，用电势描述电场并建立 $\mathbf E=-\nabla U$。
tags: [电势, 电势差, 等势面, 保守场]
---

## 静电场环路定理

静电场是保守场，沿闭合路径的环路积分为零：

$$
\oint_L\mathbf E\cdot d\mathbf l=0.
$$

这意味着静电力做功只与起点和终点有关，与路径无关。

## 电势与电势差

电势差可写为

$$
U_a-U_b=\int_a^b\mathbf E\cdot d\mathbf l.
$$

若取无穷远处电势为零，点电荷的电势为

$$
U=\frac{1}{4\pi\varepsilon_0}\frac{q}{r}.
$$

电场与电势满足

$$
\mathbf E=-\nabla U.
$$

一维情形为

$$
E_x=-\frac{dU}{dx}.
$$

## 等势面

等势面上各点电势相同，沿等势面移动电荷时电场力不做功。电场线垂直于等势面，并指向电势降低最快的方向。

## 基本公式组

$$
\mathbf F=q\mathbf E,
\qquad
\mathbf E=\frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}\mathbf e_r,
$$

$$
\oint_S\mathbf E\cdot d\mathbf S
=\frac{q_{\mathrm{in}}}{\varepsilon_0},
\qquad
\oint_L\mathbf E\cdot d\mathbf l=0,
$$

$$
\mathbf E=-\nabla U.
$$

## 原页对照

<div class="page-gallery">
  <figure class="source-page">
    <img src="/note-pages/electromagnetism-p02.webp" alt="电磁学原笔记第 2 页" loading="lazy" />
    <figcaption>第 2 页 · 电势、等势面和静电公式</figcaption>
  </figure>
</div>
