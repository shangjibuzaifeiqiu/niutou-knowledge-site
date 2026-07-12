---
layout: ../../layouts/NoteLayout.astro
title: Biot-Savart 定律与安培环路定理
description: 整理电流元磁场、磁场高斯定理、安培环路定理和典型电流磁场结果。
subject: 电磁学
course: 大学物理电磁学
chapter: 静磁学
source: 物理·电磁学(3).pdf
sourcePages: 第 1 页
pages: 原笔记第 1 页
updated: 2026-07-12
status: 已整理 · 知识点拆分
summary: 从 Biot-Savart 定律和安培环路定理计算直导线、圆电流和螺线管磁场。
tags: [静磁学, Biot-Savart定律, 安培环路定理, 磁场]
---

## Biot-Savart 定律

电流元产生的磁感应强度：

$$
d\mathbf B=
\frac{\mu_0}{4\pi}
\frac{I\,d\mathbf l\times\mathbf e_r}{r^2}.
$$

## 磁场高斯定理

磁场无源：

$$
\oint_S\mathbf B\cdot d\mathbf S=0,
\qquad
\nabla\cdot\mathbf B=0.
$$

## 安培环路定理

真空中稳恒电流的安培环路定理：

$$
\oint_L\mathbf B\cdot d\mathbf l=\mu_0\sum I_i.
$$

## 典型电流磁场

有限长直导线在一点的磁场：

$$
B=\frac{\mu_0 I}{4\pi a}(\cos\theta_1-\cos\theta_2).
$$

无限长直导线：

$$
B=\frac{\mu_0 I}{2\pi a}.
$$

圆电流轴线上一点：

$$
B=\frac{\mu_0IR^2}{2(R^2+x^2)^{3/2}},
$$

圆心处：

$$
B=\frac{\mu_0 I}{2R}.
$$

长直螺线管内部：

$$
B=\mu_0 nI.
$$

## 原页对照

<div class="page-gallery">
  <figure class="source-page">
    <img src="/note-pages/electromagnetism-p01.webp" alt="电磁学原笔记第 1 页" loading="lazy" />
    <figcaption>第 1 页 · 静磁学、Biot-Savart 和安培环路定理</figcaption>
  </figure>
</div>
