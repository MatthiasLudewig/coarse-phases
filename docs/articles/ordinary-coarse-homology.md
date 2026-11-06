(article-ordinary-coarse-homology)=
# Ordinary coarse homology

```{warning}
Agent-generated, not reviewed yet
```

Ordinary coarse homology is built from locally finite chains whose simplices
have uniformly controlled diameter. The local finiteness condition permits
infinite chains, while the control condition retains the large-scale geometry.

## The chain-complex-valued functor

Let $X$ be a coarse space and $A$ an abelian group. Write a chain formally as

$$
c=\sum_{(x_0,\ldots,x_n)\in X^{n+1}}
       c(x_0,\ldots,x_n)(x_0,\ldots,x_n),\qquad c(x_0,\ldots,x_n)\in A.
$$

No convergence of this sum is intended.

```{prf:definition} Locally finite controlled chain
:label: def-coarse-chain

A chain is locally finite if, for each bounded $B\subseteq X$, only finitely
many tuples with nonzero coefficient have a coordinate in $B$. It is controlled
if there is an entourage $E$ such that every pair of coordinates of every
nonzero tuple lies in $E$. Let $CX_n(X;A)$ be the group of chains satisfying
both conditions.
```

The boundary is the alternating deletion of coordinates:

$$
\partial(x_0,\ldots,x_n)
 =\sum_{j=0}^n(-1)^j(x_0,\ldots,\widehat{x_j},\ldots,x_n),
\qquad n>0,
$$

and $\partial:C X_0\to0$ is zero. The coefficient of any fixed tuple in this
formula is a finite sum, because a singleton is bounded and the original chain
is locally finite. The boundary preserves local finiteness and control, and
$\partial^2=0$.

A coarse map $f:X\to Y$ induces a chain map by

$$
f_*(x_0,\ldots,x_n)=(f(x_0),\ldots,f(x_n)).
$$

Properness makes the sums over fibers finite, and controlledness preserves the
control condition. Thus

$$
CX(-;A):\mathrm{BornCoarse}\longrightarrow\mathrm{Ch}(\mathrm{Ab})
$$

is a functor. Ordered tuples are used here; repeated vertices are permitted.
Passing to the normalized chain complex gives the same homology.

Close coarse maps give chain-homotopic maps. Explicitly, the usual prism
operator is

$$
P(x_0,\ldots,x_n)=\sum_{i=0}^n(-1)^i
(f(x_0),\ldots,f(x_i),g(x_i),\ldots,g(x_n)),
$$

and satisfies $\partial P+P\partial=g_*-f_*$. Closeness supplies a uniform
control for its support.

## The classical homology groups

```{prf:definition} Ordinary coarse homology
:label: def-ordinary-coarse-homology

The ordinary coarse homology groups with coefficients in $A$ are

$$
HX_n(X;A)=H_n(CX_\bullet(X;A)).
$$

The derived version is the image of $CX_\bullet(X;A)$ in the stable
$\infty$-category obtained by inverting quasi-isomorphisms of chain complexes.
```

The derived functor is a {prf:ref}`coarse homology theory
<def-stable-coarse-homology>`. In particular, its homology groups satisfy coarse
invariance, excision, vanishing on flasques, and $u$-continuity. The raw chain
complex need not literally be zero on a flasque space; it becomes zero after
passing to the derived category.

For a big family $\mathcal Y$, take the subcomplex

$$
CX_\bullet(\mathcal Y;A)
 =\bigcup_{Y\in\mathcal Y}CX_\bullet(Y;A).
$$

Its chains must be supported in one member of the family. Since filtered
colimits are exact in abelian groups,
$HX_n(\mathcal Y;A)=\operatorname*{colim}_{Y\in\mathcal Y}HX_n(Y;A)$.

For the point, $HX_0(*;A)=A$ and all higher groups vanish. The ray has zero
coarse homology. On the line, the chain
$\sum_{k\in\mathbb Z}(k,k+1)$ is a cycle and represents the orientation
class in $HX_1(\mathbb Z;\mathbb Z)\cong\mathbb Z$. Its coefficients are
locally finite, even though the chain has infinite support.

## The measure model used for trace pairings

For proper metric spaces and complex coefficients, the supplied
Ludewig–Thiang manuscript also uses locally finite complex regular Borel measures
on $X^{n+1}$ supported within a fixed neighbourhood of the multidiagonal.
The boundary is the alternating sum of pushforwards along coordinate-deletion
maps. An atomic chain embeds as a sum of Dirac measures.

The two models have the same homology: they agree on proper discrete spaces,
and both are invariant under measurable coarse equivalences to a discretization.
The measure model is useful for continuous spaces and operator kernels; the
atomic model above works directly on all bornological coarse spaces. For
measures, local finiteness means finite total variation on compact subsets.

{ref}`Coarsely transverse partitions <article-coarse-transversality>` define
cohomology classes paired with these chains or measures. This is separate
from specifying an orientation or a homology class on $X$.

## Sources

See {ref}`Bunke–Engel <bib-bunke-engel>`, §6.3, and
{ref}`Ludewig–Thiang <bib-large-scale-trace>`, §3.1, for the measure model and
its comparison with locally finite atomic chains.
