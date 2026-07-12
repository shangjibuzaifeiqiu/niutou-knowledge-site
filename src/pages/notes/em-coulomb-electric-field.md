---
layout: ../../layouts/NoteLayout.astro
title: 库仑定律与电场强度
description: 整理静电力、电场强度、电场叠加原理以及点电荷和连续带电体的电场表达。
subject: 电磁学
course: 大学物理电磁学
chapter: 静电场
source: 物理·电磁学(3).pdf
sourcePages: 第 1 页
pages: 原笔记第 1 页
updated: 2026-07-12
status: 已整理 · 知识点拆分
summary: 从库仑定律到电场强度定义，建立静电场计算的基本模型。
tags: [库仑定律, 电场强度, 点电荷, 叠加原理]
---

## 库仑定律

两个点电荷之间的静电力为

$$
\mathbf F_{12}=
\frac{1}{4\pi\varepsilon_0}
\frac{q_1q_2}{r^2}\mathbf e_r .
$$

力的大小与两电荷电量乘积成正比，与距离平方成反比，方向沿两电荷连线。同性相斥，异性相吸。

## 电场强度

电场强度定义为单位正试探电荷受到的电场力：

$$
\mathbf E=\frac{\mathbf F}{q_0}.
$$

点电荷 $q$ 在距离 $r$ 处产生的电场为

$$
\mathbf E=
\frac{1}{4\pi\varepsilon_0}
\frac{q}{r^2}\mathbf e_r.
$$

## 叠加原理

多个点电荷共同产生的电场为各点电荷电场的矢量和：

$$
\mathbf E=\sum_i\mathbf E_i.
$$

连续带电体可分割为电荷元 $dq$：

$$
d\mathbf E=
\frac{1}{4\pi\varepsilon_0}
\frac{dq}{r^2}\mathbf e_r,
\qquad
\mathbf E=\int d\mathbf E.
$$

常用电荷元：

$$
dq=\lambda dl,\qquad dq=\sigma dS,\qquad dq=\rho dV.
$$

## 待复核

本页只对应原笔记左侧静电学开头。电磁学同一 PDF 中的静磁学、电磁感应和麦克斯韦方程组已拆到独立知识点页面。

## 原页对照

<div class="page-gallery">
  <figure class="source-page">
    <img src="/note-pages/electromagnetism-p01.webp" alt="电磁学原笔记第 1 页" loading="lazy" />
    <figcaption>第 1 页 · 库仑定律、电场强度和电场叠加</figcaption>
  </figure>
</div>
