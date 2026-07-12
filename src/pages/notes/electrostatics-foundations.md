---
layout: ../../layouts/NoteLayout.astro
title: 电磁学：静电场、高斯定理与电势
description: 完整整理电磁学 PDF 的非空手写页，覆盖库仑定律、电场强度、电通量、高斯定理、电势与静电场基本公式。
subject: 电磁学
course: 电磁学
chapter: 静电场
source: 物理·电磁学(3).pdf
sourcePages: 第 1-2 页，原 PDF 第 3 页为空白
pages: 原笔记第 1-2 页
updated: 2026-07-12
status: 已完整纳入 · 含原页对照
summary: 完整收录电磁学 PDF 的非空页面，整理静电力、电场、电通量、高斯定理、电势、等势面和静电场环路定理。
tags: [静电场, 库仑定律, 高斯定理, 电势, 电场线]
---

## 原始页结构

- 第 1 页：静电力、电场强度、电场叠加、电场线、电通量和高斯定理的基本应用。
- 第 2 页：高斯定理的积分形式、静电场环路定理、电势、电势差、等势面和静电场基本公式。
- 第 3 页为空白页，未作为正文图像发布。

## 库仑定律与电场强度

点电荷之间的静电力满足库仑定律：

$$
\mathbf F_{12}
=\frac{1}{4\pi\varepsilon_0}
\frac{q_1q_2}{r^2}\mathbf e_r.
$$

电场强度定义为单位正试探电荷所受电场力：

$$
\mathbf E=\frac{\mathbf F}{q_0}.
$$

点电荷产生的电场为

$$
\mathbf E
=\frac{1}{4\pi\varepsilon_0}
\frac{q}{r^2}\mathbf e_r.
$$

多个点电荷的电场满足叠加原理：

$$
\mathbf E=\sum_i \mathbf E_i.
$$

连续带电体的电场写成积分形式：

$$
d\mathbf E=
\frac{1}{4\pi\varepsilon_0}
\frac{dq}{r^2}\mathbf e_r,
\qquad
\mathbf E=\int d\mathbf E.
$$

常用电荷元包括

$$
dq=\lambda dl,\qquad dq=\sigma dS,\qquad dq=\rho dV.
$$

## 电场线与电通量

电场线用于表示电场方向与强弱：切线方向为电场方向，线密度反映电场强弱。静电场线从正电荷出发，终止于负电荷或无穷远。

通过面积元 $d\mathbf S=\mathbf n\,dS$ 的电通量为

$$
d\Phi_e=\mathbf E\cdot d\mathbf S.
$$

闭合曲面的总通量为

$$
\Phi_e=\oint_S \mathbf E\cdot d\mathbf S.
$$

若电场在曲面上大小恒定且与法向夹角为 $\theta$，

$$
\Phi_e=ES\cos\theta.
$$

## 高斯定理

真空中的高斯定理积分形式为

$$
\oint_S \mathbf E\cdot d\mathbf S
=\frac{1}{\varepsilon_0}\sum q_{\mathrm{in}}.
$$

微分形式为

$$
\nabla\cdot\mathbf E=\frac{\rho}{\varepsilon_0}.
$$

使用高斯定理的关键是选择与对称性匹配的高斯面。笔记中画出了球对称与柱面对称的典型高斯面。常见结果包括：

点电荷或球对称电荷分布外部：

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

## 静电场环路定理与电势

静电场是保守场，环路积分为零：

$$
\oint_L \mathbf E\cdot d\mathbf l=0.
$$

电势差定义为单位正电荷从一点移动到另一点时电场力所作功的负值：

$$
U_a-U_b=\int_a^b \mathbf E\cdot d\mathbf l.
$$

常以无穷远为零电势点，点电荷电势为

$$
U=\frac{1}{4\pi\varepsilon_0}\frac{q}{r}.
$$

电场与电势满足

$$
\mathbf E=-\nabla U.
$$

一维情形下：

$$
E_x=-\frac{dU}{dx}.
$$

## 等势面与基本公式

等势面上各点电势相等，沿等势面移动电荷时电场力不做功。电场线处处垂直于等势面，并指向电势降低最快的方向。

笔记右侧汇总了静电学基本公式：

$$
\mathbf F=q\mathbf E,
\qquad
\mathbf E=\frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}\mathbf e_r,
$$

$$
\oint_S\mathbf E\cdot d\mathbf S
=\frac{q_{\mathrm{in}}}{\varepsilon_0},
\qquad
\oint_L\mathbf E\cdot d\mathbf l=0,
$$

$$
\mathbf E=-\nabla U.
$$

## 待复核

第 1 页右侧有若干高斯面例图和中间算式，整理稿保留了主要物理结论。若后续要把每个图对应的积分上下限逐项录入，可继续按原页对照补充。

## 原页对照

<div class="page-gallery">
  <figure class="source-page">
    <img src="/note-pages/electromagnetism-p01.webp" alt="电磁学原笔记第 1 页" loading="lazy" />
    <figcaption>第 1 页 · 静电场与高斯定理</figcaption>
  </figure>
  <figure class="source-page">
    <img src="/note-pages/electromagnetism-p02.webp" alt="电磁学原笔记第 2 页" loading="lazy" />
    <figcaption>第 2 页 · 电势、等势面与静电公式</figcaption>
  </figure>
</div>
