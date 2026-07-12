---
layout: ../../layouts/NoteLayout.astro
title: 广义坐标、虚功与广义力
description: 整理自由度、广义坐标、虚功表达和广义力定义。
subject: 分析力学
course: 分析力学基础
chapter: 虚功原理
source: 分析力学基础(2).pdf
sourcePages: 第 2-3 页
pages: 原笔记第 2-3 页
updated: 2026-07-12
status: 已整理 · 知识点拆分
summary: 用广义坐标把虚功写成 $\delta W=\sum Q_\sigma\delta q_\sigma$。
tags: [广义坐标, 虚功, 广义力, 自由度]
---

## 自由度与广义坐标

若 $n$ 个质点受到 $s$ 个完整约束，系统自由度为

$$
k=3n-s.
$$

选取独立广义坐标 $q_1,\ldots,q_k$ 后，

$$
\mathbf r_i=\mathbf r_i(q_1,\ldots,q_k,t).
$$

固定时刻的虚位移为

$$
\delta \mathbf r_i=\sum_{\sigma=1}^{k}
\frac{\partial \mathbf r_i}{\partial q_\sigma}\delta q_\sigma.
$$

## 虚功与广义力

力的虚功为

$$
\delta W=\sum_i\mathbf F_i\cdot\delta\mathbf r_i.
$$

代入广义坐标展开：

$$
\delta W
=\sum_{\sigma=1}^{k}Q_\sigma\delta q_\sigma,
$$

其中广义力为

$$
Q_\sigma=\sum_i\mathbf F_i\cdot
\frac{\partial \mathbf r_i}{\partial q_\sigma}.
$$

若 $\delta q_\sigma$ 独立，平衡时有

$$
Q_\sigma=0,\qquad \sigma=1,\ldots,k.
$$

## 原页对照

<div class="page-gallery">
  <figure class="source-page"><img src="/note-pages/mechanics-p02.webp" alt="分析力学原笔记第 2 页" loading="lazy" /><figcaption>第 2 页 · 虚功和理想约束</figcaption></figure>
  <figure class="source-page"><img src="/note-pages/mechanics-p03.webp" alt="分析力学原笔记第 3 页" loading="lazy" /><figcaption>第 3 页 · 广义坐标与广义力</figcaption></figure>
</div>
