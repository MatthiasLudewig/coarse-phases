(article-coarse-transversality)=
# Coarse transversality

Coarse transversality expresses that several support conditions can meet only
in a bounded region, even after arbitrary controlled thickenings.

## Big families and subsets

```{prf:definition} Coarse transversality
:nonumber:
:label: def-coarse-transversality

Big families $\mathcal Y_0,\ldots,\mathcal Y_n$ on $X$ are *coarsely transverse*
if every member of $\mathcal Y_0\Cap\cdots\Cap\mathcal Y_n$ is bounded:

$$
\mathcal Y_0\Cap\cdots\Cap\mathcal Y_n\subseteq\mathcal B.
$$

Subsets $A_0,\ldots,A_n$ are *coarsely transverse* if their generated big
families are coarsely transverse.
```

For metric spaces this is equivalent to boundedness of
$(A_0)_{E_R}\cap\cdots\cap (A_n)_{E_R}$ for every finite $R$.
If all the families contain the bornology of $X$, the inclusion in the definition is an equality. 
The inclusion formulation also accommodates empty subsets and coarse spaces with several coarse components.

```{prf:definition} Coarsely transverse partition
:nonumber:
:label: def-coarsely-transverse-partition

A *coarsely transverse $n$-partition* of a proper metric space $X$ is an ordered
collection $(A_0,\ldots,A_n)$ of pairwise disjoint Borel subsets with union
$X$, which is coarsely transverse.
```

A collection of subsets $H_1,\ldots,H_n$ is a collection of *coarsely transverse half spaces* if $\partial H_1\Cap\cdots\Cap\partial H_n\subseteq\mathcal B_X$, with $\partial H_i$ the {ref}`coarse boundary <article-big-family>`.
For example, the coordinate half-spaces $H_i=\{x_i\geq0\}$ in $\mathbb R^n$
have this property. They give the partition

$$
A_0=\bigcap_{j=1}^n H_j,\qquad
A_i=H_i^c\cap\bigcap_{j=i+1}^n H_j\quad(1\leq i\leq n).
$$

## Coarse cohomology classes associated to partitions

An ordered coarsely transverse partition defines a coarse **cohomology** class.


```{prf:definition} Partition class
:nonumber:
:label: def-partition-class

Let $(A_0,\ldots,A_n)$ be a coarsely transverse partition.
 Its *partition cocycle* is the coarse cocycle $\theta_A$ defined by
$$
\theta_A(x_0,\ldots,x_n)
 =\det\bigl(A_i(x_j)\bigr)_{0\leq i,j\leq n}
 =\sum_{\sigma\in S_{n+1}}\operatorname{sgn}(\sigma)
   \prod_{i=0}^n A_i(x_{\sigma(i)}),
$$
where we also write $A_i$ for the indicator function of the subset $A_i$.
The corresponding *partition class* is its cohomology class $[\theta_A]\in HX^n(X;\mathbb R)$.
```

That this cochain is closed with respect to the Alexander--Spanier differential is a simple calculation. 
That it satisfies the support condition for coarse cochains follows from coarse transversality of the partition.

 Pairing the partition class with the coarse Chern
character of an operator $K$-class is the source of the trace formulae in
[Ludewig–Thiang, Large-scale quantization of trace I](https://arxiv.org/abs/2506.10957).

