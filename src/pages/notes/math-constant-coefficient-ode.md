---
layout: ../../layouts/NoteLayout.astro
title: 常系数线性微分方程
description: 整理常系数非齐次线性微分方程、特征方程和待定系数法。
subject: 数学分析
course: 数学分析（二）
chapter: 微分方程
source: 数学分析（2）.pdf
sourcePages: 第 1 页
pages: 原笔记第 1 页
updated: 2026-07-12
status: 已整理 · 知识点拆分
summary: 用特征方程求齐次解，再用待定系数法构造非齐次特解。
tags: [微分方程, 常系数, 特征方程]
---

## 标准形式

常系数线性微分方程：

$$
y^{(n)}+a_1y^{(n-1)}+\cdots+a_{n-1}y'+a_ny=f(x).
$$

记 $D=\frac{d}{dx}$，可写作

$$
P(D)y=f(x).
$$

## 齐次解

齐次方程 $P(D)y=0$ 对应特征方程

$$
P(\lambda)=0.
$$

若 $\lambda$ 是 $k$ 重根，对应解为

$$
e^{\lambda x},\;xe^{\lambda x},\;\ldots,\;x^{k-1}e^{\lambda x}.
$$

## 非齐次解

通解为

$$
y=y_h+y_p.
$$

当右端形如 $e^{\alpha x}P_m(x)$ 或带三角因子时，待定特解要根据 $\alpha$ 或 $\alpha\pm i\beta$ 是否为特征根来乘以 $x^s$。

## 原页对照

<div class="page-gallery">
  <figure class="source-page"><img src="/note-pages/math-analysis-p01.webp" alt="数学分析原笔记第 1 页" loading="lazy" /><figcaption>第 1 页 · 常系数线性微分方程</figcaption></figure>
</div>
