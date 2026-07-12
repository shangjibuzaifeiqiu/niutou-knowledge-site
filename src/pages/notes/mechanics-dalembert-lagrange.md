---
layout: ../../layouts/NoteLayout.astro
title: 达朗贝尔原理与第二类拉格朗日方程
description: 从牛顿第二定律引入惯性力，推导达朗贝尔原理和第二类拉格朗日方程。
subject: 分析力学
course: 分析力学基础
chapter: 拉格朗日方程
source: 分析力学基础(2).pdf
sourcePages: 第 3-5 页
pages: 原笔记第 3-5 页
updated: 2026-07-12
status: 已整理 · 知识点拆分
summary: 把达朗贝尔原理转化为广义坐标下的拉格朗日方程。
tags: [达朗贝尔原理, 拉格朗日方程, 动能]
---

## 达朗贝尔原理

牛顿第二定律写作

$$
\mathbf F_i+\mathbf F_{Ni}=m_i\mathbf a_i.
$$

移项后把 $-m_i\mathbf a_i$ 看作惯性力。对任意允许虚位移作虚功，并利用理想约束力虚功为零：

$$
\sum_i(\mathbf F_i-m_i\mathbf a_i)\cdot\delta\mathbf r_i=0.
$$

## 动能恒等式

动能

$$
T=\frac12\sum_i m_i v_i^2.
$$

笔记推导使用

$$
\frac{\partial \mathbf v_i}{\partial \dot q_\sigma}
=\frac{\partial \mathbf r_i}{\partial q_\sigma},
\qquad
\frac{\partial \mathbf v_i}{\partial q_\sigma}
=\frac{d}{dt}\left(
\frac{\partial \mathbf r_i}{\partial q_\sigma}
\right).
$$

于是

$$
\sum_i m_i\mathbf a_i\cdot
\frac{\partial \mathbf r_i}{\partial q_\sigma}
=
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot q_\sigma}\right)
-\frac{\partial T}{\partial q_\sigma}.
$$

## 第二类拉格朗日方程

代回达朗贝尔原理，得到

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot q_\sigma}\right)
-\frac{\partial T}{\partial q_\sigma}
=Q_\sigma.
$$

若主动力有势，$Q_\sigma=-\frac{\partial V}{\partial q_\sigma}$，令 $L=T-V$：

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot q_\sigma}\right)
-\frac{\partial L}{\partial q_\sigma}=0.
$$

## 原页对照

<div class="page-gallery">
  <figure class="source-page"><img src="/note-pages/mechanics-p03.webp" alt="分析力学原笔记第 3 页" loading="lazy" /><figcaption>第 3 页 · 达朗贝尔原理</figcaption></figure>
  <figure class="source-page"><img src="/note-pages/mechanics-p04.webp" alt="分析力学原笔记第 4 页" loading="lazy" /><figcaption>第 4 页 · 拉格朗日方程推导</figcaption></figure>
  <figure class="source-page"><img src="/note-pages/mechanics-p05.webp" alt="分析力学原笔记第 5 页" loading="lazy" /><figcaption>第 5 页 · 方程形式总结</figcaption></figure>
</div>
