---
layout: ../../layouts/NoteLayout.astro
title: 静电场基础与高斯定理
description: 从电荷分布和库仑定律出发，串联电场强度、叠加原理、高斯定理与极化描述。
subject: 电磁学
course: 电磁学
chapter: 静电学
source: 物理·电磁学(3).pdf
sourcePages: 第 1 页
pages: 原笔记第 1 页
updated: 2026-07-12
status: 已整理 · 待逐式复核
summary: 汇总静电场最基础的定义和积分关系，并补充电介质中的电位移矢量。
tags: [静电场, 库仑定律, 高斯定理, 电介质]
---

## 电荷与连续分布

电荷量子化写作

$$
q=ne.
$$

对连续分布的电荷，可分别使用线密度、面密度和体密度：

$$
q=\int \lambda\,dl,
\qquad
q=\iint \sigma\,dS,
\qquad
q=\iiint \rho\,dV.
$$

## 库仑定律与电场强度

真空中两个点电荷之间的作用力为

$$
\mathbf F
=\frac{1}{4\pi\varepsilon_0}
\frac{q_1q_2}{r^2}\,\mathbf e_r.
$$

由试探电荷 $q_0$ 定义电场强度：

$$
\mathbf E=\frac{\mathbf F}{q_0}.
$$

点电荷产生的场为

$$
\mathbf E
=\frac{1}{4\pi\varepsilon_0}
\frac{q}{r^2}\,\mathbf e_r.
$$

多个电荷共同存在时使用叠加原理：

$$
\mathbf E=\sum_i\mathbf E_i,
$$

连续电荷分布则写成对应的积分形式。

## 高斯定理与环路定理

真空静电场满足

$$
\oiint_S \mathbf E\cdot d\mathbf S
=\frac{Q_{\text{内}}}{\varepsilon_0},
$$

其微分形式为

$$
\nabla\cdot\mathbf E=\frac{\rho}{\varepsilon_0}.
$$

静电场是保守场，因此

$$
\oint_L\mathbf E\cdot d\mathbf l=0,
\qquad
\nabla\times\mathbf E=0.
$$

## 电介质中的描述

极化强度定义为单位体积内电偶极矩的矢量和：

$$
\mathbf P=\frac{\sum \mathbf p}{\Delta V}.
$$

线性各向同性电介质中，可写成

$$
\mathbf P=\varepsilon_0\chi_e\mathbf E.
$$

定义电位移矢量

$$
\mathbf D=\varepsilon_0\mathbf E+\mathbf P
=\varepsilon\mathbf E,
$$

从而得到介质中的高斯定理

$$
\oiint_S\mathbf D\cdot d\mathbf S=Q_{\text{自由}}.
$$

> 数值修正：库仑常量更准确地写作 $k=1/(4\pi\varepsilon_0)\approx 8.99\times10^9\ \mathrm{N\,m^2/C^2}$。
