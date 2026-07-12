---
layout: ../../layouts/NoteLayout.astro
title: 拉格朗日函数与能量积分
description: 整理有势力情形下的拉格朗日函数，以及定常保守系统的能量积分。
subject: 分析力学
course: 分析力学基础
chapter: 能量积分
source: 分析力学基础(2).pdf
sourcePages: 第 5 页
pages: 原笔记第 5 页
updated: 2026-07-12
status: 已整理 · 知识点拆分
summary: 在定常约束和保守力条件下，从拉格朗日函数得到机械能守恒。
tags: [拉格朗日函数, 能量积分, 机械能守恒]
---

## 拉格朗日函数

有势力情形下令

$$
L=T-V.
$$

第二类拉格朗日方程写成

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot q_\sigma}\right)
-\frac{\partial L}{\partial q_\sigma}=0.
$$

## 能量积分

若约束定常且势能不显含时间，则

$$
\frac{d}{dt}\left(
\sum_{\sigma=1}^{k}\dot q_\sigma
\frac{\partial L}{\partial \dot q_\sigma}
-L
\right)=0.
$$

当动能是广义速度的二次齐次函数时，

$$
\sum_{\sigma=1}^{k}\dot q_\sigma
\frac{\partial T}{\partial \dot q_\sigma}=2T.
$$

于是

$$
T+V=E=\text{常量}.
$$

## 适用条件

机械能守恒需要同时注意：

- 约束定常。
- 主动力有势。
- 势能不显含时间。
- 非保守力或非理想约束没有额外做功。

## 原页对照

<div class="page-gallery">
  <figure class="source-page">
    <img src="/note-pages/mechanics-p05.webp" alt="分析力学原笔记第 5 页" loading="lazy" />
    <figcaption>第 5 页 · 拉格朗日函数和能量积分</figcaption>
  </figure>
</div>
