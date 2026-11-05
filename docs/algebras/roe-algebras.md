(article-roe-algebras)=
# Roe algebras

An entourage specifies allowed pairs of locations. For an operator written as
a matrix over sites, this suggests constraining which matrix entries may be
nonzero. We begin with a concrete discrete metric setting.

## A discrete model

Let $X$ be a countable proper discrete metric space: each bounded subset is
finite. Take $H_X=\ell^2(X)\otimes\ell^2(\mathbb N)$ and let $P_B$ be the
projection onto the summands over $B\subseteq X$.

A bounded operator $T$ on $H_X$ has **finite propagation** if there is an $R$
such that its block $T_{xy}$ vanishes whenever $d(x,y)>R$.
It is **locally compact** if $P_BT$ and $TP_B$ are compact for every bounded $B$.

The Roe algebra $C^*(X;H_X)$ is the operator-norm closure of the locally compact,
finite-propagation operators. We retain the module $H_X$ in the notation here
to make the representation explicit. See {ref}`bib-ewert-meyer`, §2, for the
operator-algebraic setup.

## Why the coarse structure appears

Equation {eq}`eq-metric-entourage` says that finite propagation is a controlled
support condition. If $S$ has propagation at most $R$ and $T$ at most $S_0$,
then $ST$ has propagation at most $R+S_0$. This matches composition of
entourages in {prf:ref}`def-coarse-structure`.

For example, on $X=\mathbb Z$ take the bilateral shift $U$ on $\ell^2(\mathbb Z)$
and a rank-one projection $q$ on $\ell^2(\mathbb N)$. The operator
$(U+U^*)\otimes q$ has propagation one and is locally compact: restriction on
either side to finitely many sites has finite rank.

```{admonition} Roe and uniform Roe algebras
:class: dropdown

The uniform Roe algebra instead closes finite-propagation operators on
$\ell^2(X)$ (usually for a uniformly discrete bounded-geometry space).
The infinite-dimensional fibre and local compactness condition in our Roe
model are meaningful choices. The two constructions should not be silently
identified.
```

## Toward K-theory

The algebra supplies a setting for projections, unitaries, and their stable
homotopy classes. [The introduction to phases](../phases/introduction.md)
explains the role of a gapped Hamiltonian and its Fermi projection. A later
reference article will develop K-theory and the general bornological
construction; the present page only describes the discrete model.
