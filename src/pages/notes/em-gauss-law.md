---
layout: ../../layouts/NoteLayout.astro
title: 电通量与高斯定理
description: 整理电场线、电通量、高斯定理及其在对称电场中的用法。
subject: 电磁学
course: 大学物理电磁学
chapter: 静电场
source: 物理·电磁学(3).pdf
sourcePages: 第 1-2 页
pages: 原笔记第 1-2 页
updated: 2026-07-12
status: 已整理 · 知识点拆分
summary: 用电通量和高斯面把对称电荷分布的电场计算转化为面积分。
tags: [电通量, 高斯定理, 高斯面, 对称性]
---

## 电场线

电场线的切线方向表示电场方向，线密度反映电场强弱。静电场线从正电荷出发，终止于负电荷或无穷远。

## 电通量

通过面积元 $d\mathbf S=\mathbf n\,dS$ 的电通量为

$$
d\Phi_e=\mathbf E\cdot d\mathbf S.
$$

闭合曲面 $S$ 的总通量为

$$
\Phi_e=\oint_S\mathbf E\cdot d\mathbf S.
$$

若电场在曲面上大小恒定，且与法向夹角为 $\theta$：

$$
\Phi_e=ES\cos\theta.
$$

## 高斯定理

真空中高斯定理的积分形式为

$$
\oint_S\mathbf E\cdot d\mathbf S
=\frac{1}{\varepsilon_0}\sum q_{\mathrm{in}}.
$$

微分形式为

$$
\nabla\cdot\mathbf E=\frac{\rho}{\varepsilon_0}.
$$

在电介质中，笔记引入电位移矢量

$$
\mathbf D=\varepsilon_0\mathbf E+\mathbf P,
$$

并写成

$$
\oint_S\mathbf D\cdot d\mathbf S=\sum q_{\mathrm{free}}.
$$

线性各向同性电介质中

$$
\mathbf P=\varepsilon_0\chi_e\mathbf E,\qquad
\mathbf D=\varepsilon_0(1+\chi_e)\mathbf E=\varepsilon\mathbf E.
$$

使用高斯定理时，核心不是公式本身，而是选择合适的高斯面，使 $\mathbf E\cdot d\mathbf S$ 在曲面上可以简化。

## 典型结果

点电荷或球对称带电体外部：

$$
E\cdot 4\pi r^2=\frac{q}{\varepsilon_0},
\qquad
E=\frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}.
$$

无限长均匀带电直线：

$$
E\cdot 2\pi r l=\frac{\lambda l}{\varepsilon_0},
\qquad
E=\frac{\lambda}{2\pi\varepsilon_0 r}.
$$

无限大均匀带电平面：

$$
2ES=\frac{\sigma S}{\varepsilon_0},
\qquad
E=\frac{\sigma}{2\varepsilon_0}.
$$

## 原页对照

<div class="page-gallery">
  <figure class="source-page">
    <img src="/note-pages/electromagnetism-p01.webp" alt="电磁学原笔记第 1 页" loading="lazy" />
    <figcaption>第 1 页 · 电通量和高斯定理例图</figcaption>
  </figure>
  <figure class="source-page">
    <img src="/note-pages/electromagnetism-p02.webp" alt="电磁学原笔记第 2 页" loading="lazy" />
    <figcaption>第 2 页 · 高斯定理和基本公式</figcaption>
  </figure>
</div>
