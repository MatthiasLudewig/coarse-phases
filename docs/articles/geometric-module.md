(article-geometric-module)=
# Geometric module

```{warning}
Agent-generated, not reviewed yet
```

A geometric module is a Hilbert space on which subsets of a space can act as
support projections. For a fixed coarse space $X$ it is also called an
$X$-module. There are a point-determined coarse model and a topological model;
the latter also accommodates continuum spaces such as $L^2(M)$.

## Hilbert-space-valued controlled objects

Take Hilbert spaces with isometric embeddings and direct sum as the symmetric
monoidal operation. A local controlled object assigns a closed subspace $H_B$
to each bounded subset, with

$$
H_{B\sqcup C}\cong H_B\oplus H_C\qquad(B\cap C=\varnothing),
$$

and continuity under directed unions. Its global Hilbert space is the completed
union of these subspaces. By the
{ref}`point-object description <theorem-local-objects-points>`, it has the form
$H=\bigoplus_{x\in X}H_x$ and $H_B=\bigoplus_{x\in B}H_x$.

```{prf:definition} Point-determined geometric module
:nonumber:
:label: def-geometric-module

A point-determined geometric module over $X$ is a Hilbert space with an
orthogonal decomposition $H=\bigoplus_{x\in X}H_x$. Write $\chi_B$ for the
projection onto $\bigoplus_{x\in B}H_x$. It is locally finite if
$\chi_BH$ is finite-dimensional for every bounded $B$.
```

Equivalently, one has a projection-valued measure on all subsets of $X$ which
is determined by its singleton projections. A more general finitely additive
projection-valued measure on $\mathcal P(X)$ need not be determined on points;
we specify this condition whenever the discrete model is used.

A bounded operator $T:H\to H'$ is $E$-controlled if
$\chi'_CT\chi_B=0$ whenever $C\cap E[B]=\varnothing$. This is the
Hilbert-space version of a controlled morphism. Direct sums of finite-dimensional
fibers on locally finite supports provide the objects used in the categorical
construction of {ref}`coarse K-theory <article-coarse-k-theory>`.

## Nondegenerate representations of continuous functions

For a locally compact Hausdorff space $X$, the usual topological definition is
a Hilbert space $H$ with a nondegenerate representation

$$
\rho:C_0(X)\longrightarrow\mathcal B(H),\qquad
\overline{\rho(C_0(X))H}=H.
$$

We also call $(H,\rho)$ an $X$-module. The spectral theorem extends $\rho$
canonically to bounded **Borel** functions, giving projections
$\chi_B=\rho(\mathbf1_B)$ for Borel sets $B$.
On a discrete space every function is Borel, so all bounded functions act.
On a general space the spectral theorem does not supply values for arbitrary
nonmeasurable functions.

For a discrete $X$, the topological and point-determined descriptions agree.
For a nondiscrete $X$ they describe different models: multiplication on
$L^2(\mathbb R)$ is nondegenerate but its singleton projections are all zero.
One can pass to a coarse discretization when comparing the resulting operator
algebras; one should not identify the two representations literally.

## Ample modules

```{prf:definition} Ample topological module
:nonumber:
:label: def-ample-module

A nondegenerate $X$-module $(H,\rho)$ is ample if $\rho(f)$ is compact only
when $f=0$.
```

In particular an ample representation is faithful. On a countable discrete
space, $\ell^2(X)\otimes\ell^2(\mathbb N)$ with its multiplication action is
ample. The module $\ell^2(X)$ with one-dimensional point fibers is not ample.
On a positive-dimensional Riemannian manifold, multiplication on $L^2(M)$ is
ample: a nonzero continuous function is bounded away from zero on a nonempty
open set, whose $L^2$-space is infinite-dimensional.

Local finiteness and ampleness serve different purposes. A locally finite
module over a discrete space has finite-dimensional point fibers, whereas
ampleness forces those fibers to be infinite-dimensional.

## Comparison of ample modules

For a separable proper metric space, any two separable ample modules are
isomorphic by a controlled unitary. The precise statement and a proof by a
uniformly bounded Borel partition are given in
{ref}`Controlled unitary equivalence of ample modules <theorem-ample-modules>`.
Conjugation by such a unitary identifies their Roe algebras.

This is a coarse isomorphism of modules, not necessarily an intertwiner of
the $C_0(X)$-representations. For example, an atomic ample representation and
a nonatomic one need not be unitarily equivalent as representations.
The comparison explains why the Roe algebra is often written $C^*(X)$ without
mentioning a module, although the algebra identification involves a choice.
