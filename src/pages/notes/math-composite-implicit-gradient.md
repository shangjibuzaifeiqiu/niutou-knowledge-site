---
layout: ../../layouts/NoteLayout.astro
title: 复合函数求导、隐函数求导与梯度
description: 整理多元复合函数链式法则、隐函数求导公式、方向导数和梯度。
subject: 数学分析
course: 数学分析（二）
chapter: 多元函数微分学
source: 数学分析（2）.pdf
sourcePages: 第 3-4 页
pages: 原笔记第 3-4 页
updated: 2026-07-12
status: 已整理 · 知识点拆分
summary: 把链式法则、隐函数公式和梯度统一为多元微分的计算工具。
tags: [链式法则, 隐函数, 方向导数, 梯度]
---

## 复合函数链式法则

若

$$
z=f(u,v),\qquad u=u(x,y),\qquad v=v(x,y),
$$

则

$$
\frac{\partial z}{\partial x}
=\frac{\partial z}{\partial u}\frac{\partial u}{\partial x}
+\frac{\partial z}{\partial v}\frac{\partial v}{\partial x},
$$

$$
\frac{\partial z}{\partial y}
=\frac{\partial z}{\partial u}\frac{\partial u}{\partial y}
+\frac{\partial z}{\partial v}\frac{\partial v}{\partial y}.
$$

## 隐函数求导

若 $F(x,y)=0$ 确定 $y=y(x)$，且 $F_y\ne0$：

$$
\frac{dy}{dx}=-\frac{F_x}{F_y}.
$$

若 $F(x,y,z)=0$ 确定 $z=z(x,y)$：

$$
\frac{\partial z}{\partial x}=-\frac{F_x}{F_z},
\qquad
\frac{\partial z}{\partial y}=-\frac{F_y}{F_z}.
$$

## 方向导数与梯度

方向导数：

$$
\frac{\partial f}{\partial \mathbf l}
=\nabla f\cdot\mathbf l.
$$

梯度：

$$
\nabla f=
\left(
\frac{\partial f}{\partial x},
\frac{\partial f}{\partial y},
\frac{\partial f}{\partial z}
\right).
$$

梯度方向是函数增长最快的方向，其模长等于最大方向导数。

## 原页对照

<div class="page-gallery">
  <figure class="source-page"><img src="/note-pages/math-analysis-p03.webp" alt="数学分析原笔记第 3 页" loading="lazy" /><figcaption>第 3 页 · 链式法则和隐函数</figcaption></figure>
  <figure class="source-page"><img src="/note-pages/math-analysis-p04.webp" alt="数学分析原笔记第 4 页" loading="lazy" /><figcaption>第 4 页 · 方向导数和梯度</figcaption></figure>
</div>
