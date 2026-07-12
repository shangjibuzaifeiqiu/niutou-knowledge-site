---
layout: ../../layouts/NoteLayout.astro
title: 虚位移、虚功与理想约束
description: 从约束方程出发，区分实际位移和虚位移，并整理虚位移原理的基本形式。
subject: 分析力学
course: 分析力学基础
chapter: 第一章 · 虚位移
source: 分析力学基础(2).pdf
sourcePages: 第 2 页
pages: 原笔记第 2 页
updated: 2026-07-12
status: 已整理 · 待逐式复核
summary: 从约束分类、虚位移定义到虚功和理想约束，建立分析力学的第一组概念。
tags: [约束, 虚位移, 虚功, 理想约束]
---

## 约束及其分类

约束限制质点或质点系的可能运动。按是否显含时间，可分为：

- **定常约束**：约束关系不随时间显式变化。
- **非定常约束**：约束关系显含时间。

按限制方式，还可以区分双侧约束和单侧约束。前者通常写成等式，后者常以不等式表达。

## 虚位移

对含有 $n$ 个质点的质点系，完整双侧约束可写为

$$
f_j(x_1,y_1,z_1,\ldots,x_n,y_n,z_n,t)=0,
\qquad j=1,2,\ldots,s.
$$

在固定时刻 $t$，满足约束所允许的无穷小位移称为**虚位移**，记作

$$
\delta \mathbf r_i
=\delta x_i\mathbf i+\delta y_i\mathbf j+\delta z_i\mathbf k.
$$

虚位移必须满足约束的变分形式：

$$
\sum_i\left(
\frac{\partial f_j}{\partial x_i}\delta x_i+
\frac{\partial f_j}{\partial y_i}\delta y_i+
\frac{\partial f_j}{\partial z_i}\delta z_i
\right)=0.
$$

实际位移 $d\mathbf r_i$ 与虚位移 $\delta\mathbf r_i$ 的关键差别是：实际位移包含时间推进，而虚位移比较的是同一时刻约束所允许的不同位置。

## 虚功和理想约束

力在虚位移上所作的功称为虚功：

$$
\delta W=\mathbf F_i\cdot\delta\mathbf r_i.
$$

若任意允许的虚位移中，全部约束力的虚功之和为零，便称该约束为理想约束：

$$
\sum_i \mathbf F_{Ni}\cdot\delta\mathbf r_i=0.
$$

在平衡状态下，主动合力与约束力满足

$$
\mathbf F_i+\mathbf F_{Ni}=\mathbf 0.
$$

结合理想约束，可得到质点系平衡的必要条件：

$$
\sum_i \mathbf F_i\cdot\delta\mathbf r_i=0.
$$

> 修正说明：虚位移原理严格成立时需要明确质点系处于平衡状态、虚位移满足约束，并妥善处理摩擦等非理想约束力。原笔记页末也特别提示了摩擦情形。
