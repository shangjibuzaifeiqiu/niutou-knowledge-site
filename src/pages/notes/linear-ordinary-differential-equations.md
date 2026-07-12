---
layout: ../../layouts/NoteLayout.astro
title: 数学分析（二）：微分方程、多元微积分与无穷级数
description: 完整整理数学分析 PDF 的非空手写页，覆盖常系数线性微分方程、多元函数微分学、多元积分、曲线曲面积分和级数理论。
subject: 数学分析
course: 数学分析（二）
chapter: 综合整理
source: 数学分析（2）.pdf
sourcePages: 第 1-10 页，原 PDF 第 11 页为空白
pages: 原笔记第 1-10 页
updated: 2026-07-12
status: 已完整纳入 · 含原页对照
summary: 完整收录数学分析 PDF 的非空页面，整理为微分方程、多元函数微分学、多元积分、曲线曲面积分、无穷级数和函数项级数六组知识块。
tags: [微分方程, 多元函数, 重积分, 曲线积分, 无穷级数, 一致收敛]
---

## 原始页结构

- 第 1 页：常系数非齐次线性微分方程与待定系数法。
- 第 2-4 页：多元函数微分学，包括极限、连续、偏导、全微分、链式法则、隐函数和方向导数。
- 第 5-7 页：多元积分学，包括二重积分、三重积分、坐标变换、曲线积分、曲面积分及场论公式。
- 第 8-10 页：无穷级数与函数项级数，包括收敛判别、一致收敛、幂级数和收敛域。
- 第 11 页为空白页，未作为正文图像发布。

## 常系数非齐次线性微分方程

常系数线性微分方程可写为

$$
y^{(n)}+a_1y^{(n-1)}+\cdots+a_{n-1}y'+a_ny=f(x).
$$

记微分算子为 $D=\frac{d}{dx}$，方程可记成

$$
P(D)y=f(x).
$$

齐次方程 $P(D)y=0$ 的解由特征方程

$$
P(\lambda)=0
$$

决定。若 $\lambda$ 是单根，对应 $e^{\lambda x}$；若 $\lambda$ 是 $k$ 重根，对应

$$
e^{\lambda x},\; xe^{\lambda x},\;\ldots,\;x^{k-1}e^{\lambda x}.
$$

非齐次方程通解为

$$
y=y_h+y_p,
$$

其中 $y_h$ 是齐次通解，$y_p$ 是非齐次方程的一个特解。待定系数法中，若右端为

$$
f(x)=e^{\alpha x}P_m(x)
$$

或含三角函数的同类表达，应按特征根是否与 $\alpha$ 或 $\alpha\pm i\beta$ 重合来乘以适当的 $x^s$。

## 多元函数的极限与连续

多元函数极限的定义强调点 $(x,y)$ 从任意路径趋向 $(x_0,y_0)$ 时函数值趋向同一常数：

$$
\lim_{(x,y)\to(x_0,y_0)} f(x,y)=A.
$$

若沿不同路径得到不同极限，则极限不存在。常用判断方式包括：

- 令 $y=kx$、$y=x^2$ 等不同路径比较。
- 使用夹逼估计。
- 转为极坐标，令 $r\to 0$ 判断与角度 $\theta$ 是否无关。

连续性要求函数在该点有定义、极限存在，且极限等于函数值：

$$
\lim_{\mathbf x\to \mathbf x_0}f(\mathbf x)=f(\mathbf x_0).
$$

## 偏导数、全微分与可微性

二元函数的偏导数定义为

$$
f_x(x_0,y_0)=
\lim_{\Delta x\to 0}
\frac{f(x_0+\Delta x,y_0)-f(x_0,y_0)}{\Delta x},
$$

$$
f_y(x_0,y_0)=
\lim_{\Delta y\to 0}
\frac{f(x_0,y_0+\Delta y)-f(x_0,y_0)}{\Delta y}.
$$

若函数在点处可微，则增量可写成

$$
\Delta z=A\Delta x+B\Delta y+o(\rho),
\qquad
\rho=\sqrt{(\Delta x)^2+(\Delta y)^2}.
$$

此时

$$
dz=f_x\,dx+f_y\,dy.
$$

可微推出连续，也推出偏导存在；偏导存在不能反推可微。若偏导在邻域内存在并在该点连续，则函数在该点可微。

## 复合函数与隐函数求导

若

$$
z=f(u,v),\qquad u=u(x,y),\qquad v=v(x,y),
$$

则链式法则为

$$
\frac{\partial z}{\partial x}
=\frac{\partial z}{\partial u}\frac{\partial u}{\partial x}
+\frac{\partial z}{\partial v}\frac{\partial v}{\partial x},
$$

$$
\frac{\partial z}{\partial y}
=\frac{\partial z}{\partial u}\frac{\partial u}{\partial y}
+\frac{\partial z}{\partial v}\frac{\partial v}{\partial y}.
$$

若隐函数由

$$
F(x,y)=0
$$

确定，且 $F_y\ne 0$，则

$$
\frac{dy}{dx}=-\frac{F_x}{F_y}.
$$

若

$$
F(x,y,z)=0
$$

确定 $z=z(x,y)$，则

$$
\frac{\partial z}{\partial x}=-\frac{F_x}{F_z},
\qquad
\frac{\partial z}{\partial y}=-\frac{F_y}{F_z}.
$$

## 方向导数与梯度

方向导数描述函数沿单位方向 $\mathbf l=(\cos\alpha,\cos\beta,\cos\gamma)$ 的变化率：

$$
\frac{\partial f}{\partial \mathbf l}
=\nabla f\cdot \mathbf l.
$$

梯度为

$$
\nabla f=
\left(
\frac{\partial f}{\partial x},
\frac{\partial f}{\partial y},
\frac{\partial f}{\partial z}
\right).
$$

梯度方向是函数增长最快的方向，其模长等于最大方向导数。

## 二重积分与三重积分

二重积分表示区域上函数的累积量：

$$
\iint_D f(x,y)\,d\sigma.
$$

直角坐标下，若

$$
D=\{(x,y)\mid a\le x\le b,\ \varphi_1(x)\le y\le \varphi_2(x)\},
$$

则

$$
\iint_D f(x,y)\,d\sigma
=\int_a^b dx\int_{\varphi_1(x)}^{\varphi_2(x)}
f(x,y)\,dy.
$$

极坐标变换为

$$
x=r\cos\theta,\qquad y=r\sin\theta,\qquad d\sigma=r\,dr\,d\theta.
$$

三重积分为

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

## 曲线积分与曲面积分

第一类曲线积分：

$$
\int_L f(x,y)\,ds.
$$

若曲线参数方程为 $x=x(t),y=y(t)$，则

$$
ds=\sqrt{(x'(t))^2+(y'(t))^2}\,dt.
$$

第二类曲线积分：

$$
\int_L P\,dx+Q\,dy.
$$

格林公式将平面区域边界上的第二类曲线积分转为区域上的二重积分：

$$
\oint_{\partial D}P\,dx+Q\,dy
=\iint_D\left(\frac{\partial Q}{\partial x}
-\frac{\partial P}{\partial y}\right)\,dx\,dy.
$$

空间中常用公式包括高斯公式与斯托克斯公式：

$$
\iint_{\partial\Omega}\mathbf F\cdot \mathbf n\,dS
=\iiint_\Omega \nabla\cdot\mathbf F\,dv,
$$

$$
\oint_{\partial S}\mathbf F\cdot d\mathbf r
=\iint_S(\nabla\times\mathbf F)\cdot\mathbf n\,dS.
$$

笔记中还记录了保守场判别：若在单连通区域中

$$
\frac{\partial P}{\partial y}
=\frac{\partial Q}{\partial x},
$$

则曲线积分与路径无关，并可由势函数计算。

## 无穷级数

数项级数

$$
\sum_{n=1}^{\infty}u_n
$$

的部分和为

$$
S_n=u_1+u_2+\cdots+u_n.
$$

若 $\lim_{n\to\infty}S_n=S$，则级数收敛，否则发散。

调和级数

$$
\sum_{n=1}^{\infty}\frac1n
$$

发散。笔记用分组估计说明部分和可超过任意给定数。

正项级数常用判别法：

- 比较判别法：与已知收敛或发散的正项级数比较。
- 比值判别法：

$$
\rho=\lim_{n\to\infty}\frac{u_{n+1}}{u_n}.
$$

若 $\rho<1$ 收敛，若 $\rho>1$ 发散。

- 根值判别法：

$$
\rho=\lim_{n\to\infty}\sqrt[n]{u_n}.
$$

若 $\rho<1$ 收敛，若 $\rho>1$ 发散。

交错级数若满足

$$
u_n\ge 0,\qquad u_{n+1}\le u_n,\qquad \lim_{n\to\infty}u_n=0,
$$

则

$$
\sum_{n=1}^{\infty}(-1)^{n-1}u_n
$$

收敛。

## 函数项级数与一致收敛

函数项级数

$$
\sum_{n=1}^{\infty}u_n(x)
$$

在集合 $D$ 上逐点收敛，是指对每个固定 $x\in D$，数项级数收敛。

一致收敛可用柯西准则表达：任给 $\varepsilon>0$，存在 $N$，当 $n>N$ 且 $p\ge 1$ 时，对所有 $x\in D$ 都有

$$
\left|u_{n+1}(x)+\cdots+u_{n+p}(x)\right|<\varepsilon.
$$

Weierstrass 判别法：若

$$
|u_n(x)|\le M_n,\qquad x\in D,
$$

且

$$
\sum_{n=1}^{\infty}M_n
$$

收敛，则 $\sum u_n(x)$ 在 $D$ 上一致收敛。

一致收敛保持连续性：若 $u_n(x)$ 连续且 $\sum u_n(x)$ 一致收敛，则和函数连续。

## 幂级数

幂级数写作

$$
\sum_{n=0}^{\infty}a_n(x-x_0)^n.
$$

存在收敛半径 $R$，使得

$$
|x-x_0|<R
$$

时绝对收敛，$|x-x_0|>R$ 时发散；端点需要单独判断。

若极限存在，可用

$$
R=\lim_{n\to\infty}\left|\frac{a_n}{a_{n+1}}\right|
$$

或

$$
R=\frac{1}{\lim_{n\to\infty}\sqrt[n]{|a_n|}}
$$

求收敛半径。

幂级数在收敛区间内部可逐项求导、逐项积分，且收敛半径不变。

## 待复核

第 1 页和第 4 页含有多处教材截图和密集例题，整理稿已提取主要结论与公式。若后续要把每道例题逐行录入，可以以本页底部原页图像为基准继续精修。

## 原页对照

<div class="page-gallery">
  <figure class="source-page"><img src="/note-pages/math-analysis-p01.webp" alt="数学分析原笔记第 1 页" loading="lazy" /><figcaption>第 1 页 · 常系数线性微分方程</figcaption></figure>
  <figure class="source-page"><img src="/note-pages/math-analysis-p02.webp" alt="数学分析原笔记第 2 页" loading="lazy" /><figcaption>第 2 页 · 多元函数极限与连续</figcaption></figure>
  <figure class="source-page"><img src="/note-pages/math-analysis-p03.webp" alt="数学分析原笔记第 3 页" loading="lazy" /><figcaption>第 3 页 · 偏导、全微分与隐函数</figcaption></figure>
  <figure class="source-page"><img src="/note-pages/math-analysis-p04.webp" alt="数学分析原笔记第 4 页" loading="lazy" /><figcaption>第 4 页 · 高阶偏导与方向导数</figcaption></figure>
  <figure class="source-page"><img src="/note-pages/math-analysis-p05.webp" alt="数学分析原笔记第 5 页" loading="lazy" /><figcaption>第 5 页 · 二重积分与三重积分</figcaption></figure>
  <figure class="source-page"><img src="/note-pages/math-analysis-p06.webp" alt="数学分析原笔记第 6 页" loading="lazy" /><figcaption>第 6 页 · 曲线曲面积分与场论公式</figcaption></figure>
  <figure class="source-page"><img src="/note-pages/math-analysis-p07.webp" alt="数学分析原笔记第 7 页" loading="lazy" /><figcaption>第 7 页 · Green、Gauss、Stokes 相关公式</figcaption></figure>
  <figure class="source-page"><img src="/note-pages/math-analysis-p08.webp" alt="数学分析原笔记第 8 页" loading="lazy" /><figcaption>第 8 页 · 无穷级数与正项级数</figcaption></figure>
  <figure class="source-page"><img src="/note-pages/math-analysis-p09.webp" alt="数学分析原笔记第 9 页" loading="lazy" /><figcaption>第 9 页 · 判别法与函数项级数</figcaption></figure>
  <figure class="source-page"><img src="/note-pages/math-analysis-p10.webp" alt="数学分析原笔记第 10 页" loading="lazy" /><figcaption>第 10 页 · 一致收敛与幂级数</figcaption></figure>
</div>
