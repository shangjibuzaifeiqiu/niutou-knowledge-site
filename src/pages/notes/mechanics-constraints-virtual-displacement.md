---
layout: ../../layouts/NoteLayout.astro
title: 约束与虚位移
description: 整理约束分类、虚位移定义，以及虚位移必须满足的约束变分条件。
subject: 分析力学
course: 分析力学基础
chapter: 约束与虚位移
source: 分析力学基础(2).pdf
sourcePages: 第 2 页
pages: 原笔记第 2 页
updated: 2026-07-12
status: 已整理 · 知识点拆分
summary: 分清实际位移和虚位移，为虚功原理和拉格朗日方程打基础。
tags: [约束, 虚位移, 完整约束]
---

## 约束

约束是对质点或质点系可能运动的限制。按是否显含时间，可分为定常约束和非定常约束；按是否能写成等式，可分为完整约束和非完整约束。

完整双侧约束可写成

$$
f_j(x_1,y_1,z_1,\ldots,x_n,y_n,z_n,t)=0,
\qquad j=1,2,\ldots,s.
$$

## 虚位移

虚位移是在固定时刻 $t$ 下，满足约束所允许的无穷小位移：

$$
\delta \mathbf r_i
=\delta x_i\mathbf i+\delta y_i\mathbf j+\delta z_i\mathbf k.
$$

对约束方程取变分：

$$
\sum_i\left(
\frac{\partial f_j}{\partial x_i}\delta x_i+
\frac{\partial f_j}{\partial y_i}\delta y_i+
\frac{\partial f_j}{\partial z_i}\delta z_i
\right)=0.
$$

实际位移 $d\mathbf r_i$ 包含时间推进，虚位移 $\delta\mathbf r_i$ 比较的是同一时刻约束允许的邻近位置。

## 原页对照

<div class="page-gallery">
  <figure class="source-page">
    <img src="/note-pages/mechanics-p02.webp" alt="分析力学原笔记第 2 页" loading="lazy" />
    <figcaption>第 2 页 · 约束与虚位移</figcaption>
  </figure>
</div>
