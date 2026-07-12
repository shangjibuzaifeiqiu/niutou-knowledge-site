---
layout: ../../layouts/NoteLayout.astro
title: 常系数线性微分方程
description: 二阶线性方程的叠加原理、常系数齐次方程与欧拉方程的解题框架。
subject: 数学分析
course: 数学分析
chapter: 常微分方程
source: 数学分析（2）.pdf
sourcePages: 第 1 页
pages: 原笔记第 1 页
updated: 2026-07-12
status: 已整理 · 待逐式复核
summary: 用特征方程统一理解常系数齐次线性微分方程，并整理实根、重根和复根三类情形。
tags: [微分方程, 叠加原理, 特征方程, 欧拉方程]
---

## 二阶齐次线性方程

一般形式为

$$
y''+p(x)y'+q(x)y=0.
$$

线性齐次方程满足叠加原理：若 $y_1,y_2$ 都是方程的解，则

$$
C_1y_1+C_2y_2
$$

仍是方程的解。当 $y_1,y_2$ 线性无关时，它们构成二阶方程通解的一组基础。

## 常系数齐次方程

$n$ 阶常系数方程写为

$$
y^{(n)}+a_1y^{(n-1)}+\cdots+a_ny=0.
$$

令 $y=e^{\lambda x}$，得到特征方程

$$
\lambda^n+a_1\lambda^{n-1}+\cdots+a_n=0.
$$

特征根决定通解的形式：

1. 若 $\lambda$ 是 $k$ 重实根，对应解为
   $$e^{\lambda x},xe^{\lambda x},\ldots,x^{k-1}e^{\lambda x}.$$
2. 若 $\alpha\pm i\beta$ 是 $k$ 重共轭复根，对应实解组为
   $$x^j e^{\alpha x}\cos\beta x,\quad x^j e^{\alpha x}\sin\beta x,\qquad j=0,\ldots,k-1.$$

## 欧拉方程

欧拉方程常写作

$$
x^ny^{(n)}+a_1x^{n-1}y^{(n-1)}+\cdots+a_ny=f(x).
$$

作变量替换 $t=\ln x$，并记 $D=d/dt$。利用

$$
x^ky^{(k)}=D(D-1)\cdots(D-k+1)y,
$$

即可把欧拉方程化为关于 $t$ 的常系数线性微分方程。

> 整理提示：叠加原理直接适用于齐次线性方程；非齐次方程的解相加时，右端项也会相加，不能忽略这一点。
