---
layout: ../../layouts/NoteLayout.astro
title: 函数项级数、一致收敛与幂级数
description: 整理函数项级数的一致收敛、Weierstrass 判别法、幂级数收敛半径和逐项运算。
subject: 数学分析
course: 数学分析（二）
chapter: 函数项级数
source: 数学分析（2）.pdf
sourcePages: 第 9-10 页
pages: 原笔记第 9-10 页
updated: 2026-07-12
status: 已整理 · 知识点拆分
summary: 把一致收敛、连续性保持和幂级数收敛半径作为函数项级数的核心工具。
tags: [函数项级数, 一致收敛, 幂级数, 收敛半径]
---

## 一致收敛

函数项级数

$$
\sum_{n=1}^{\infty}u_n(x)
$$

在集合 $D$ 上一致收敛，可用柯西准则表示：任给 $\varepsilon>0$，存在 $N$，当 $n>N$ 且 $p\ge1$ 时，对所有 $x\in D$ 都有

$$
\left|u_{n+1}(x)+\cdots+u_{n+p}(x)\right|<\varepsilon.
$$

Weierstrass 判别法：若

$$
|u_n(x)|\le M_n,\qquad x\in D,
$$

且 $\sum M_n$ 收敛，则 $\sum u_n(x)$ 在 $D$ 上一致收敛。

## 幂级数

幂级数：

$$
\sum_{n=0}^{\infty}a_n(x-x_0)^n.
$$

存在收敛半径 $R$。当 $|x-x_0|<R$ 时绝对收敛，$|x-x_0|>R$ 时发散，端点需要单独判断。

常用公式：

$$
R=\lim_{n\to\infty}\left|\frac{a_n}{a_{n+1}}\right|,
\qquad
R=\frac{1}{\lim_{n\to\infty}\sqrt[n]{|a_n|}}.
$$

幂级数在收敛区间内部可以逐项求导、逐项积分，收敛半径不变。

## 原页对照

<div class="page-gallery">
  <figure class="source-page"><img src="/note-pages/math-analysis-p09.webp" alt="数学分析原笔记第 9 页" loading="lazy" /><figcaption>第 9 页 · 函数项级数</figcaption></figure>
  <figure class="source-page"><img src="/note-pages/math-analysis-p10.webp" alt="数学分析原笔记第 10 页" loading="lazy" /><figcaption>第 10 页 · 一致收敛和幂级数</figcaption></figure>
</div>
