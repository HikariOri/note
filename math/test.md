# 函数连续性与微分

## 向量空间（Vector Space）

<!-- 定义：函数的连续性 -->
<div class="math-env definition" data-name="Continuity of Functions">

设函数 $f$ 在点 $x_0$ 的某个邻域内有定义。如果 

$$
\lim_{x \to x_0} f(x) = f(x_0)
$$

则称函数 $f$ 在点 $x_0$ 处**连续**。

</div>

<!-- 定义：一致连续 -->
<div class="math-env definition" data-name="Uniform Continuity">

设函数 $f$ 在区间 $I$ 上有定义。如果对于任意 $\epsilon > 0$，存在 $\delta > 0$，使得对于 $I$ 中任意两点 $x_1, x_2$，当 $|x_1 - x_2| < \delta$ 时，都有 $|f(x_1) - f(x_2)| < \epsilon$，则称 $f$ 在 $I$ 上**一致连续**。

</div>

<!-- 定义：导数 -->
<div class="math-env definition" data-name="Derivative">

设函数 $f$ 在点 $x_0$ 的某个邻域内有定义。如果极限

$$
f'(x_0) = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h}
$$

存在，则称 $f$ 在点 $x_0$ 处可导，该极限值称为 $f$ 在点 $x_0$ 处的导数。

</div>

<!-- 引理：连续函数的性质 -->
<div class="math-env lemma">

设 $f$ 在点 $x_0$ 连续，且 $f(x_0) > 0$。那么存在 $x_0$ 的某个邻域 $U(x_0)$，使得对所有 $x \in U(x_0)$，都有 $f(x) > 0$。

</div>

<!-- 引理：有界性引理 -->
<div class="math-env lemma">

闭区间 $[a,b]$ 上的连续函数必定有界。

</div>

<!-- 定理：中间值定理 -->
<div class="math-env theorem" data-name="Intermediate Value Theorem">

设 $f$ 在闭区间 $[a,b]$ 上连续，且 $f(a) \neq f(b)$。那么对于 $f(a)$ 和 $f(b)$ 之间的任意值 $c$，存在 $\xi \in (a,b)$ 使得 $f(\xi) = c$。

</div>

<!-- 定理：最值定理 -->
<div class="math-env theorem" data-name="Extreme Value Theorem">

设 $f$ 在闭区间 $[a,b]$ 上连续，则 $f$ 在 $[a,b]$ 上必定达到其最大值和最小值。

</div>

<!-- 定理：罗尔定理 -->
<div class="math-env theorem" data-name="Rolle's Theorem">

设函数 $f$ 满足：

1. 在闭区间 $[a,b]$ 上连续；
2. 在开区间 $(a,b)$ 内可导；
3. $f(a) = f(b)$。


则至少存在一点 $\xi \in (a,b)$，使得 $f'(\xi) = 0$。

</div>

<!-- 推论：零点存在定理 -->
<div class="math-env corollary" data-name="Zero Existence Theorem">

设 $f$ 在 $[a,b]$ 上连续，且 $f(a) \cdot f(b) < 0$，则至少存在一点 $c \in (a,b)$ 使得 $f(c) = 0$。

</div>

<!-- 推论：拉格朗日中值定理 -->
<div class="math-env corollary" data-name="Mean Value Theorem">

设函数 $f$ 在 $[a,b]$ 上连续，在 $(a,b)$ 内可导，则存在 $\xi \in (a,b)$ 使得

$$
f'(\xi) = \frac{f(b) - f(a)}{b - a}
$$

</div>

<!-- 证明示例 -->
<div class="math-env proof">

零点存在定理的证明：

不失一般性，设 $f(a) < 0 < f(b)$。令 $c = 0$，显然 $f(a) < c < f(b)$。由中间值定理，存在 $\xi \in (a,b)$ 使得 $f(\xi) = c = 0$。因此方程 $f(x) = 0$ 在区间 $(a,b)$ 内至少有一个根。$\square$

</div>

<!-- 例子：多项式零点 -->
<div class="math-env example">

考虑多项式 $p(x) = x^3 - 2x - 5$。计算得 $p(2) = 8 - 4 - 5 = -1 < 0$ 和 $p(3) = 27 - 6 - 5 = 16 > 0$。由零点存在定理，方程 $x^3 - 2x - 5 = 0$ 在区间 $(2,3)$ 内至少有一个实根。

</div>

<!-- 例子：三角函数应用 -->
<div class="math-env example">

证明方程 $\cos x = x$ 在区间 $(0, \pi/2)$ 内有解。

解：考虑函数 $f(x) = \cos x - x$。显然 $f(0) = 1 > 0$，$f(\pi/2) = 0 - \pi/2 < 0$。由于 $f(x)$ 连续且 $f(0) \cdot f(\pi/2) < 0$，由零点存在定理知存在 $c \in (0, \pi/2)$ 使得 $f(c) = 0$，即 $\cos c = c$。

</div>

<!-- 练习：基础题 -->
<div class="math-env exercise">

利用 $\epsilon$-$\delta$ 定义证明函数 $f(x) = 3x + 2$ 在点 $x_0 = 1$ 处连续。

</div>

<!-- 练习：中等题 -->
<div class="math-env exercise">

设 $f(x) = \begin{cases} x^2 \sin(1/x), & x \neq 0 \\ 0, & x = 0 \end{cases}$。证明 $f$ 在 $x = 0$ 处可导，并求出 $f'(0)$。

</div>

<!-- 练习：综合题 -->
<div class="math-env exercise">

证明：若 $f$ 在 $[a,b]$ 上连续且严格单调递增，则 $f$ 的反函数 $f^{-1}$ 在 $[f(a), f(b)]$ 上连续且严格单调递增。

</div>

<!-- 说明：几何直观 -->
<div class="math-env remark">

中间值定理的几何意义是：连续函数的图像是"一笔画成"的，不能有跳跃或断裂。因此从一个函数值连续变化到另一个函数值时，必须经过中间的每一个值。

</div>

<!-- 说明：历史背景 -->
<div class="math-env remark">

历史注记：中间值定理最早由波尔查诺（Bolzano）在1817年严格证明，因此有时也称为波尔查诺定理。这个定理是实数完备性的一个重要体现。

</div>

<!-- 命题：连续性的等价条件 -->
<div class="math-env proposition">

函数 $f$ 在点 $x_0$ 连续的充分必要条件是：对于任意包含 $f(x_0)$ 的开区间 $V$，都存在包含 $x_0$ 的开区间 $U$，使得 $f(U) \subset V$。

</div>

<!-- 命题：可导与连续的关系 -->
<div class="math-env proposition">

若函数 $f$ 在点 $x_0$ 可导，则 $f$ 在点 $x_0$ 连续。但反之不一定成立。

</div>



考虑多项式 $p(x) = x^3 - 2x - 5$。计算得 $p(2) = 8 - 4 - 5 = -1 < 0$ 和和和和和和 $p(3) = 27 - 6 - 5 = 16 > 0$。由零点存在定理，方程 $x^3 - 2x - 5 = 0$ 在区间 $(2,3)$ 内至少有一个实根。