(article-coarse-spaces)=
# Coarse spaces: the idea

A metric measures individual distances. A coarse structure remembers which
families of pairs have a uniformly bounded separation. This is useful when
locality matters but an exact numerical distance is incidental.

## From a metric to controlled sets

For a metric space $(X,d)$ and $R\geq0$, set

```{math}
:label: eq-metric-entourage

E_R=\{(x,y)\in X\times X:d(x,y)\leq R\}.
```

The metric coarse structure consists of the subsets of some $E_R$. Taking
inverses preserves $E_R$, while the triangle inequality gives
$E_R\circ E_S\subseteq E_{R+S}$. These facts explain the inverse and
composition axioms in {prf:ref}`def-coarse-structure`.

Use the bornology of metrically bounded subsets. If $B$ lies in a ball of radius
$S$, then $E_R[B]$ lies in a ball with the same centre and radius $R+S$.
This gives the compatibility required below.

## The reference definition, recalled

The canonical statement is {prf:ref}`def-coarse-space`. We recall its text here
for convenience; the reference page is the target for citations.

````{admonition} Coarse space — definition recalled
:class: definition-recall

```{include} ../_snippets/coarse-space.inc.md
```
````

## A basic example

On $\mathbb Z$, a controlled set can contain pairs arbitrarily far from the
origin, provided their separation is uniformly bounded. Thus
$\{(n,n+1):n\in\mathbb Z\}$ is controlled, whereas
$\{(0,n):n\in\mathbb Z\}$ is not. The set of sites involved need not be bounded.

This distinction is central for a lattice Hamiltonian: nearest-neighbour
couplings can occur throughout an infinite sample while retaining a single
propagation bound. [Roe algebras](../algebras/roe-algebras.md) turn this observation
into an operator-algebraic construction.

## Changing the space

{prf:ref}`thm-lattice-line` shows that $\mathbb Z$ and $\mathbb R$ are coarsely
equivalent. The [reference on maps](../reference/coarse-maps.md) states exactly
what this means. A change of geometry and a deformation of a Hamiltonian are
different operations; their relationship must be established in each model.
