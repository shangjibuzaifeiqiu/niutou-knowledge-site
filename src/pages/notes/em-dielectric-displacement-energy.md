---
layout: ../../layouts/NoteLayout.astro
title: 电介质、电位移矢量与静电场能量
description: 整理电介质中的极化强度、电位移矢量、高斯定理和静电场能量密度。
subject: 电磁学
course: 大学物理电磁学
chapter: 电介质中的静电场
source: 物理·电磁学(3).pdf
sourcePages: 第 1 页
pages: 原笔记第 1 页
updated: 2026-07-12
status: 已整理 · 知识点拆分
summary: 用 $\mathbf D=\varepsilon_0\mathbf E+\mathbf P$ 描述电介质中的静电场，并记录能量密度公式。
tags: [电介质, 极化强度, 电位移矢量, 静电能]
---

## 极化强度

电介质中引入极化强度

$$
\mathbf P=\frac{\sum \mathbf p}{\Delta V}.
$$

线性各向同性电介质中

$$
\mathbf P=\varepsilon_0\chi_e\mathbf E.
$$

## 电位移矢量

电位移矢量定义为

$$
\mathbf D=\varepsilon_0\mathbf E+\mathbf P.
$$

因此

$$
\mathbf D=\varepsilon_0(1+\chi_e)\mathbf E=\varepsilon\mathbf E,
\qquad
\varepsilon_r=\frac{\varepsilon}{\varepsilon_0}.
$$

电介质中的高斯定理：

$$
\oint_S\mathbf D\cdot d\mathbf S=\sum q_{\mathrm{free}}.
$$

## 静电场能量

笔记记录的能量形式：

$$
W_e=\frac12\sum_i q_iU_i,
$$

静电场能量密度：

$$
w_e=\frac12\mathbf D\cdot\mathbf E
=\frac12\varepsilon_r\varepsilon_0E^2.
$$

## 原页对照

<div class="page-gallery">
  <figure class="source-page">
    <img src="/note-pages/electromagnetism-p01.webp" alt="电磁学原笔记第 1 页" loading="lazy" />
    <figcaption>第 1 页 · 电介质、电位移矢量和静电场能量</figcaption>
  </figure>
</div>
