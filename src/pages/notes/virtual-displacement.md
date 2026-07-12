---
layout: ../../layouts/NoteLayout.astro
title: 分析力学基础：虚位移、达朗贝尔原理与拉格朗日方程
description: 从约束与虚位移出发，整理广义坐标、虚功原理、达朗贝尔原理以及第二类拉格朗日方程的推导链条。
subject: 分析力学
course: 分析力学基础
chapter: 第一章至第二章
source: 分析力学基础(2).pdf
sourcePages: 第 1-5 页，原 PDF 第 6 页为空白
pages: 原笔记第 1-5 页
updated: 2026-07-12
status: 已完整纳入 · 含原页对照
summary: 完整收录分析力学基础 PDF 的非空页面，覆盖约束、虚位移、广义坐标、虚功、达朗贝尔原理、拉格朗日方程和能量积分。
tags: [约束, 虚位移, 虚功, 达朗贝尔原理, 拉格朗日方程]
---

## 原始页结构

- 第 1 页是封面。
- 第 2 页整理约束、虚位移、虚功和理想约束。
- 第 3 页整理自由度、广义坐标、广义力、虚功的广义坐标表达以及达朗贝尔原理。
- 第 4 页继续推导第二类拉格朗日方程，并记录有势力情形与一个约束摆类例子。
- 第 5 页整理动能在广义坐标中的表达、拉格朗日方程形式和能量积分。
- 第 6 页为空白页，未作为正文图像发布。

## 约束与虚位移

约束是对质点或质点系可能运动的限制。按约束关系是否显含时间，可分为定常约束与非定常约束；按约束是否可写成等式，可分为完整约束与非完整约束。

若含有 $n$ 个质点，完整双侧约束可写成

$$
f_j(x_1,y_1,z_1,\ldots,x_n,y_n,z_n,t)=0,
\qquad j=1,2,\ldots,s.
$$

在固定时刻 $t$，满足约束所允许的无穷小位移称为虚位移，记为

$$
\delta \mathbf r_i
=\delta x_i\mathbf i+\delta y_i\mathbf j+\delta z_i\mathbf k .
$$

对约束方程作变分，虚位移应满足

$$
\sum_i\left(
\frac{\partial f_j}{\partial x_i}\delta x_i+
\frac{\partial f_j}{\partial y_i}\delta y_i+
\frac{\partial f_j}{\partial z_i}\delta z_i
\right)=0.
$$

实际位移 $d\mathbf r_i$ 与虚位移 $\delta \mathbf r_i$ 的区别是：实际位移包含时间推进，虚位移是在同一时刻比较约束允许的邻近位置。

## 虚功与理想约束

力在虚位移上的功称为虚功：

$$
\delta W=\sum_i \mathbf F_i\cdot \delta\mathbf r_i .
$$

若约束力对任意允许虚位移所作虚功之和恒为零，

$$
\sum_i \mathbf F_{Ni}\cdot \delta\mathbf r_i=0,
$$

则该约束称为理想约束。平衡时有 $\mathbf F_i+\mathbf F_{Ni}=0$，于是质点系平衡的虚功形式为

$$
\sum_i \mathbf F_i\cdot \delta\mathbf r_i=0.
$$

笔记中特别提示：存在摩擦等非理想约束时，约束力虚功一般不能直接消去。

## 广义坐标与自由度

若 $n$ 个质点受到 $s$ 个完整约束，系统自由度为

$$
k=3n-s.
$$

选取 $k$ 个独立广义坐标 $q_1,\ldots,q_k$ 后，质点位置可写为

$$
\mathbf r_i=\mathbf r_i(q_1,\ldots,q_k,t),
\qquad i=1,\ldots,n.
$$

在固定时刻作变分：

$$
\delta \mathbf r_i=\sum_{\sigma=1}^{k}
\frac{\partial \mathbf r_i}{\partial q_\sigma}\delta q_\sigma .
$$

因此虚功可化为

$$
\delta W
=\sum_i\mathbf F_i\cdot\delta\mathbf r_i
=\sum_{\sigma=1}^{k}Q_\sigma\,\delta q_\sigma,
$$

其中广义力定义为

$$
Q_\sigma=\sum_i \mathbf F_i\cdot
\frac{\partial \mathbf r_i}{\partial q_\sigma}.
$$

若 $\delta q_\sigma$ 相互独立，平衡条件 $\delta W=0$ 给出

$$
Q_\sigma=0,\qquad \sigma=1,\ldots,k.
$$

## 达朗贝尔原理

对每个质点使用牛顿第二定律：

$$
\mathbf F_i+\mathbf F_{Ni}=m_i\mathbf a_i.
$$

移项后可写成

$$
\mathbf F_i+\mathbf F_{Ni}-m_i\mathbf a_i=0.
$$

把 $-m_i\mathbf a_i$ 看作惯性力，对任意允许虚位移作虚功，并利用理想约束条件，得到达朗贝尔原理：

$$
\sum_i(\mathbf F_i-m_i\mathbf a_i)\cdot \delta\mathbf r_i=0.
$$

将 $\delta\mathbf r_i$ 展开到广义坐标中，可得

$$
\sum_{\sigma=1}^{k}
\left[
Q_\sigma-
\sum_i m_i\mathbf a_i\cdot
\frac{\partial \mathbf r_i}{\partial q_\sigma}
\right]\delta q_\sigma=0.
$$

因为 $\delta q_\sigma$ 独立，括号内系数分别为零。

## 第二类拉格朗日方程

动能

$$
T=\frac12\sum_i m_i v_i^2
$$

写成广义坐标形式后，笔记推导使用恒等式

$$
\frac{\partial \mathbf v_i}{\partial \dot q_\sigma}
=\frac{\partial \mathbf r_i}{\partial q_\sigma},
\qquad
\frac{\partial \mathbf v_i}{\partial q_\sigma}
=\frac{d}{dt}\left(
\frac{\partial \mathbf r_i}{\partial q_\sigma}
\right).
$$

由此有

$$
\sum_i m_i\mathbf a_i\cdot
\frac{\partial \mathbf r_i}{\partial q_\sigma}
=
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot q_\sigma}\right)
-\frac{\partial T}{\partial q_\sigma}.
$$

代回达朗贝尔原理，得到第二类拉格朗日方程的一般形式：

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot q_\sigma}\right)
-\frac{\partial T}{\partial q_\sigma}
=Q_\sigma,
\qquad \sigma=1,\ldots,k.
$$

若主动力有势，且势能 $V(q,t)$ 满足

$$
Q_\sigma=-\frac{\partial V}{\partial q_\sigma},
$$

令 $L=T-V$，则

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot q_\sigma}\right)
-\frac{\partial L}{\partial q_\sigma}=0.
$$

## 能量积分

若约束定常且势能不显含时间，拉格朗日函数

$$
L=T-V
$$

满足

$$
\frac{d}{dt}\left(
\sum_{\sigma=1}^{k}\dot q_\sigma
\frac{\partial L}{\partial \dot q_\sigma}-L
\right)=0.
$$

当动能是广义速度的二次齐次函数时，括号内化为

$$
T+V=E=\text{常量}.
$$

笔记中的结论是：在保守系统和定常约束下，机械能守恒。

## 待复核

原笔记第 4 页右下角的例题推导字迹较密，目前整理为“约束摆类例子，用拉格朗日方程处理”，未把每个中间符号强行定稿。后续如果你要精修这一页，可以直接按原页图像逐式校正。

## 原页对照

<div class="page-gallery">
  <figure class="source-page">
    <img src="/note-pages/mechanics-p01.webp" alt="分析力学基础原笔记第 1 页" loading="lazy" />
    <figcaption>第 1 页 · 封面</figcaption>
  </figure>
  <figure class="source-page">
    <img src="/note-pages/mechanics-p02.webp" alt="分析力学基础原笔记第 2 页" loading="lazy" />
    <figcaption>第 2 页 · 约束、虚位移与虚功</figcaption>
  </figure>
  <figure class="source-page">
    <img src="/note-pages/mechanics-p03.webp" alt="分析力学基础原笔记第 3 页" loading="lazy" />
    <figcaption>第 3 页 · 广义坐标与达朗贝尔原理</figcaption>
  </figure>
  <figure class="source-page">
    <img src="/note-pages/mechanics-p04.webp" alt="分析力学基础原笔记第 4 页" loading="lazy" />
    <figcaption>第 4 页 · 拉格朗日方程推导</figcaption>
  </figure>
  <figure class="source-page">
    <img src="/note-pages/mechanics-p05.webp" alt="分析力学基础原笔记第 5 页" loading="lazy" />
    <figcaption>第 5 页 · 动能表达与能量积分</figcaption>
  </figure>
</div>
