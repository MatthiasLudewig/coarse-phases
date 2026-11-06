(article-coarse-transversality)=
# Coarse transversality

```{warning}
Agent-generated, not reviewed yet
```

Coarse transversality expresses that several support conditions can meet only
in a bounded region, even after arbitrary controlled thickenings.

## Big families and subsets

```{prf:definition} Coarse transversality
:nonumber:
:label: def-coarse-transversality

Big families $\mathcal Y_0,\ldots,\mathcal Y_n$ on $X$ are coarsely transverse
if every member of $\mathcal Y_0\Cap\cdots\Cap\mathcal Y_n$ is bounded:

$$
\mathcal Y_0\Cap\cdots\Cap\mathcal Y_n\subseteq\mathcal B_X.
$$

Subsets $A_0,\ldots,A_n$ are coarsely transverse if their generated big
families are coarsely transverse.
```

For metric spaces this is equivalent to boundedness of
$E_R[A_0]\cap\cdots\cap E_R[A_n]$ for every finite $R$.
If all the families contain $\mathcal B_X$, the inclusion in the definition
is an equality. The inclusion formulation also accommodates empty subsets
and coarse spaces with several coarse components.

```{prf:definition} Coarsely transverse partition
:nonumber:
:label: def-coarsely-transverse-partition

A coarsely transverse $n$-partition of a proper metric space $X$ is an ordered
collection $(A_0,\ldots,A_n)$ of pairwise disjoint Borel subsets with union
$X$, which is coarsely transverse.
```

A collection of half-spaces $H_1,\ldots,H_n$ is coarsely transverse if
$\partial H_1\Cap\cdots\Cap\partial H_n\subseteq\mathcal B_X$, with
$\partial H_i$ the {ref}`coarse boundary <article-big-family>`.
For example, the coordinate half-spaces $H_i=\{x_i\geq0\}$ in $\mathbb R^n$
have this property. They give the partition

$$
A_0=\bigcap_{j=1}^nH_j,\qquad
A_i=H_i^c\cap\bigcap_{j=i+1}^nH_j\quad(1\leq i\leq n).
$$

## Coarse classes associated to partitions

An ordered coarsely transverse partition defines a coarse **cohomology** class.
It pairs with coarse homology; the partition alone does not specify a coarse
homology cycle.

For a proper metric space, let $CX^n(X;\mathbb C)$ consist of the locally
bounded Borel functions $\theta:X^{n+1}\to\mathbb C$ such that, for each $R$,

$$
\operatorname{supp}(\theta)\cap
\{(x_0,\ldots,x_n):d(x_i,x_j)\leq R\text{ for all }i,j\}
$$

is bounded. The differential is the Alexander–Spanier coboundary

$$
(\delta\theta)(x_0,\ldots,x_{n+1})
 =\sum_{j=0}^{n+1}(-1)^j\theta(x_0,\ldots,\widehat{x_j},\ldots,x_{n+1}).
$$

Its cohomology is denoted $HX^n(X;\mathbb C)$.

```{prf:definition} Partition class
:nonumber:
:label: def-partition-class

Let $(A_0,\ldots,A_n)$ be a coarsely transverse partition, and write
$\chi_i=\mathbf1_{A_i}$. Its partition cocycle is

$$
\theta_A(x_0,\ldots,x_n)
 =\det\bigl(\chi_i(x_j)\bigr)_{0\leq i,j\leq n}
 =\sum_{\sigma\in S_{n+1}}\operatorname{sgn}(\sigma)
   \prod_{i=0}^n\chi_i(x_{\sigma(i)}).
$$

The partition class is $[\theta_A]\in HX^n(X;\mathbb C)$.
```

This uses the unnormalised alternating product of indicator functions.
If $\theta_A$ is nonzero on an $R$-controlled tuple, every coordinate is within
$R$ of every member of the partition. Coarse transversality therefore gives
precisely the required bounded-support condition. Moreover,

$$
\delta(\chi_0\wedge\cdots\wedge\chi_n)
 =\mathbf1\wedge\chi_0\wedge\cdots\wedge\chi_n=0,
$$

since $\mathbf1=\sum_i\chi_i$. This proves that the displayed cochain is closed.
Permuting the ordered partition multiplies its class by the sign of the
permutation.

The pairing with {ref}`ordinary coarse homology <article-ordinary-coarse-homology>`
is, on an atomic chain $c=\sum c_{x_0,\ldots,x_n}(x_0,\ldots,x_n)$,

$$
\langle\theta,c\rangle
 =\sum c_{x_0,\ldots,x_n}\theta(x_0,\ldots,x_n).
$$

Only finitely many terms contribute, by control, local finiteness, and the
support condition on $\theta$. In the measure model the sum is replaced by
$\int\theta\,d\mu$. The differential and boundary are adjoint, so this gives
a pairing on (co)homology. Pairing the partition class with the coarse Chern
character of an operator $K$-class is the source of the trace formulae in
[Ludewig–Thiang, Large-scale quantization of trace I](https://arxiv.org/abs/2506.10957).

For $X=\mathbb Z$, the partition $A_0=\{k<0\}$, $A_1=\{k\geq0\}$ pairs to
$1$ with the coarse cycle $\sum_{k\in\mathbb Z}(k,k+1)$. This fixes the
orientation convention in the simplest case.
