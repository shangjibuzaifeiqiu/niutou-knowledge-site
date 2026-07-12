---
layout: ../../layouts/NoteLayout.astro
title: 多元函数极限、连续与可微
description: 整理多元函数极限判别、连续性、偏导数、全微分和可微性的关系。
subject: 数学分析
course: 数学分析（二）
chapter: 多元函数微分学
source: 数学分析（2）.pdf
sourcePages: 第 2-4 页
pages: 原笔记第 2-4 页
updated: 2026-07-12
status: 已整理 · 知识点拆分
summary: 区分偏导存在、连续和可微三个层次，避免用错充分必要条件。
tags: [多元函数, 极限, 连续, 偏导数, 可微]
---

## 极限与连续

多元函数极限要求从任意路径趋向同一点时函数值趋向同一常数：

$$
\lim_{(x,y)\to(x_0,y_0)}f(x,y)=A.
$$

若沿不同路径得到不同结果，则极限不存在。常用路径包括 $y=kx$、$y=x^2$，也可转为极坐标判断 $r\to0$ 时是否与角度有关。

连续性要求

$$
\lim_{\mathbf x\to\mathbf x_0}f(\mathbf x)=f(\mathbf x_0).
$$

## 偏导数

$$
f_x(x_0,y_0)=
\lim_{\Delta x\to0}
\frac{f(x_0+\Delta x,y_0)-f(x_0,y_0)}{\Delta x},
$$

$$
f_y(x_0,y_0)=
\lim_{\Delta y\to0}
\frac{f(x_0,y_0+\Delta y)-f(x_0,y_0)}{\Delta y}.
$$

## 全微分与可微

若

$$
\Delta z=A\Delta x+B\Delta y+o(\rho),
\qquad
\rho=\sqrt{(\Delta x)^2+(\Delta y)^2},
$$

则函数可微，且

$$
dz=f_x\,dx+f_y\,dy.
$$

关系链：

- 可微推出连续。
- 可微推出偏导存在。
- 偏导存在不能推出可微。
- 偏导在邻域存在并在该点连续，是可微的充分条件。

## 原页对照

<div class="page-gallery">
  <figure class="source-page"><img src="/note-pages/math-analysis-p02.webp" alt="数学分析原笔记第 2 页" loading="lazy" /><figcaption>第 2 页 · 多元函数极限与连续</figcaption></figure>
  <figure class="source-page"><img src="/note-pages/math-analysis-p03.webp" alt="数学分析原笔记第 3 页" loading="lazy" /><figcaption>第 3 页 · 偏导数与全微分</figcaption></figure>
  <figure class="source-page"><img src="/note-pages/math-analysis-p04.webp" alt="数学分析原笔记第 4 页" loading="lazy" /><figcaption>第 4 页 · 高阶偏导和方向导数</figcaption></figure>
</div>
