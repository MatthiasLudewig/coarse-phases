(article-higson-corona)=
# Higson corona

```{warning}
Agent-generated, not reviewed yet
```

The Higson corona records functions whose oscillation on controlled pairs
vanishes at infinity. It is usually much larger than a familiar geometric
boundary, but often maps onto such a boundary.

## Higson functions and the corona

First let $X$ be a proper metric space. For a bounded function $f$ and an
entourage $E$, put

$$
\operatorname{Var}_E(f;W)
 =\sup\{|f(x)-f(y)|:(x,y)\in E\cap(W\times W)\}.
$$

The supremum of an empty set of nonnegative variations is understood as zero.

```{prf:definition} Higson function
:label: def-higson-function

A bounded continuous function $f:X\to\mathbb C$ is a Higson function if, for
every entourage $E$ and every $\varepsilon>0$, there is a bounded $B$ such
that $\operatorname{Var}_E(f;X\setminus B)<\varepsilon$.
```

These functions form a unital $C^*$-algebra $C_h(X)\subseteq C_b(X)$ containing
$C_0(X)$ as an ideal.

```{prf:definition} Higson compactification and corona
:label: def-higson-corona

The Higson compactification is $hX=\operatorname{Spec}C_h(X)$. Evaluation
identifies $X$ with a dense open subspace of $hX$. Its remainder

$$
\nu X=hX\setminus X
 =\operatorname{Spec}\bigl(C_h(X)/C_0(X)\bigr)
$$

is the Higson corona.
```

Compact $X$ has empty corona. For a general coarse map, pullback is most
conveniently expressed using the bounded-function description below; continuity
of the map is unnecessary there. Close coarse maps induce the same map on the
corona because their pullbacks of a Higson function differ by a function
vanishing at infinity.

## Relation to the Stone–Čech compactification

The Stone–Čech compactification of the underlying topological space is
$\beta X=\operatorname{Spec}C_b(X)$. Inclusion $C_h(X)\hookrightarrow C_b(X)$
dualizes to a continuous surjection

$$
\beta X\longrightarrow hX
$$

which restricts to the identity on $X$. Thus $hX$ is a quotient of $\beta X$:
only those bounded continuous functions satisfying the Higson condition are
retained. The induced map on remainders is also surjective.

For a discrete space $C_b(X)=\ell^\infty(X)$. For a nondiscrete space,
$\operatorname{Spec}\ell^\infty(X)$ instead compactifies the set with the
**discrete** topology and should not be confused with $\beta X$ above.

## Higson-dominated coronas

```{prf:definition} Higson-dominated compactification
:label: def-higson-dominated-corona

A compactification $\overline X$ is Higson-dominated if the identity on $X$
extends to a continuous map $hX\to\overline X$. Its boundary
$\partial\overline X$ is then a continuous image of $\nu X$.
Equivalently, every restriction to $X$ of a function in $C(\overline X)$ is
Higson.
```

For $\mathbb R^n$, the radial compactification is the closed unit ball obtained
from $x\mapsto x/(1+|x|)$. Its boundary is $S^{n-1}$. If $|x-y|$ remains
bounded while $|x|,|y|\to\infty$, the images of $x$ and $y$ in the closed ball
approach each other. Uniform continuity on the compact ball therefore implies
that every continuous function on the radial compactification is Higson.
Consequently there is a surjection

$$
\nu\mathbb R^n\longrightarrow S^{n-1}.
$$

The sphere is a Higson-dominated corona, not an identification of the Higson
corona itself. For instance, a continuous extension over the origin of
$\sin(\log |x|)$ is Higson but has no limit along a radial ray.

## Coronas associated to big families

The construction of Bunke–Ludewig applies without a topology. Let $X$ be a
coarse space and $\mathcal Y$ a {prf:ref}`big family <def-big-family>`.
Define

$$
\begin{aligned}
\ell^\infty(\mathcal Y)
 &=\{f\in\ell^\infty(X):
       \lim_{Y\in\mathcal Y}\|f|_{X\setminus Y}\|=0\},\\
\ell^\infty_{\mathcal Y}(X)
 &=\{f\in\ell^\infty(X):\forall E\in\mathcal C_X,
       \lim_{Y\in\mathcal Y}\operatorname{Var}_E(f;X\setminus Y)=0\}.
\end{aligned}
$$

Limits are over inclusion in the directed family. The first algebra is an
ideal in the second.

```{prf:definition} Coarse corona of a big family
:label: def-big-family-corona

The coarse $\mathcal Y$-corona is the compact Hausdorff space defined by

$$
C(\partial^{\mathcal Y}X)
 =\ell^\infty_{\mathcal Y}(X)/\ell^\infty(\mathcal Y).
$$

```

For a proper metric space and $\mathcal Y=\mathcal B_X$, this is the Higson
corona. Passing from bounded functions to continuous functions does not change
this quotient: a partition of unity on a uniformly bounded open cover replaces
a bounded slowly varying function by a continuous one modulo a function
vanishing away from $\mathcal Y$. This is the continuous-description lemma in
Bunke–Ludewig.

For $\mathcal Y=\mathcal P(X)$ the quotient is zero and the corona is empty.
For $\mathcal Y=\partial W$, the indicator of $W$ has zero variation away from
a sufficiently thickened coarse boundary. Its class is a projection in the
corona algebra and separates the two sides at infinity, whenever both classes
are nonzero. This is one reason big-family coronas are useful for Callias-type
operators and support conditions in index theory.

## Sources

See {ref}`Roe <bib-roe-cohomology>`, §5.1, and
{ref}`Bunke–Ludewig <bib-callias>`, §3.1, including the continuous-description
lemma and the example of the coarse boundary of a subset.
