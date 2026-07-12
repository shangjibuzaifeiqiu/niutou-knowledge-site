---
layout: ../../layouts/NoteLayout.astro
title: 数项级数与收敛判别法
description: 整理无穷级数定义、调和级数、正项级数判别法和交错级数判别法。
subject: 数学分析
course: 数学分析（二）
chapter: 无穷级数
source: 数学分析（2）.pdf
sourcePages: 第 8-9 页
pages: 原笔记第 8-9 页
updated: 2026-07-12
status: 已整理 · 知识点拆分
summary: 用部分和、比较、比值、根值和交错级数判别法判断数项级数收敛。
tags: [无穷级数, 正项级数, 交错级数, 收敛判别]
---

## 级数与部分和

数项级数

$$
\sum_{n=1}^{\infty}u_n
$$

的部分和为

$$
S_n=u_1+u_2+\cdots+u_n.
$$

若 $\lim_{n\to\infty}S_n=S$，则级数收敛。

## 正项级数

比值判别法：

$$
\rho=\lim_{n\to\infty}\frac{u_{n+1}}{u_n}.
$$

若 $\rho<1$ 收敛，若 $\rho>1$ 发散。

根值判别法：

$$
\rho=\lim_{n\to\infty}\sqrt[n]{u_n}.
$$

若 $\rho<1$ 收敛，若 $\rho>1$ 发散。

## 交错级数

若

$$
u_n\ge0,\qquad u_{n+1}\le u_n,\qquad \lim_{n\to\infty}u_n=0,
$$

则

$$
\sum_{n=1}^{\infty}(-1)^{n-1}u_n
$$

收敛。

## 原页对照

<div class="page-gallery">
  <figure class="source-page"><img src="/note-pages/math-analysis-p08.webp" alt="数学分析原笔记第 8 页" loading="lazy" /><figcaption>第 8 页 · 无穷级数基础</figcaption></figure>
  <figure class="source-page"><img src="/note-pages/math-analysis-p09.webp" alt="数学分析原笔记第 9 页" loading="lazy" /><figcaption>第 9 页 · 收敛判别法</figcaption></figure>
</div>
