---
layout: ../../layouts/NoteLayout.astro
title: 二重积分、三重积分与坐标变换
description: 整理二重积分、三重积分的累次积分表达，以及极坐标、柱坐标、球坐标的体积元。
subject: 数学分析
course: 数学分析（二）
chapter: 多元积分学
source: 数学分析（2）.pdf
sourcePages: 第 5 页
pages: 原笔记第 5 页
updated: 2026-07-12
status: 已整理 · 知识点拆分
summary: 用区域类型和坐标变换确定积分限及面积元、体积元。
tags: [二重积分, 三重积分, 坐标变换]
---

## 二重积分

若

$$
D=\{(x,y)\mid a\le x\le b,\ \varphi_1(x)\le y\le\varphi_2(x)\},
$$

则

$$
\iint_D f(x,y)\,d\sigma
=\int_a^b dx\int_{\varphi_1(x)}^{\varphi_2(x)}f(x,y)\,dy.
$$

极坐标变换：

$$
x=r\cos\theta,\qquad y=r\sin\theta,\qquad d\sigma=r\,dr\,d\theta.
$$

## 三重积分

三重积分：

$$
\iiint_\Omega f(x,y,z)\,dv.
$$

柱坐标：

$$
x=r\cos\theta,\quad y=r\sin\theta,\quad z=z,
\qquad dv=r\,dr\,d\theta\,dz.
$$

球坐标：

$$
x=r\sin\varphi\cos\theta,\quad
y=r\sin\varphi\sin\theta,\quad
z=r\cos\varphi,
$$

$$
dv=r^2\sin\varphi\,dr\,d\varphi\,d\theta.
$$

## 原页对照

<div class="page-gallery">
  <figure class="source-page"><img src="/note-pages/math-analysis-p05.webp" alt="数学分析原笔记第 5 页" loading="lazy" /><figcaption>第 5 页 · 多元积分和坐标变换</figcaption></figure>
</div>
