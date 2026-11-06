(article-coarse-k-theory)=
# Coarse K-theory

```{warning}
Agent-generated, not reviewed yet
```

Coarse $K$-theory is the $K$-theory of the Roe algebra, made functorial in the
underlying coarse space. Since it is covariant in the space, the same theory
is often called *coarse $K$-homology*. We use $K\mathcal X$ for its
spectrum-valued version.

## Classical group-valued definition

For a separable proper metric space $X$, choose a separable
{prf:ref}`ample module <def-ample-module>` $H_X$. The *coarse $K$-theory groups* are

$$
K\mathcal X_n(X)=K_n(C^*(X;H_X)),\qquad n\in\mathbb Z.
$$

Here $K_n$ is complex topological $K$-theory, with its two-periodic grading.
The {ref}`ample-module comparison <theorem-ample-modules>` makes these groups
independent of the chosen module under the canonical comparison in $K$-theory.

For a coarse map $f:X\to Y$, choose a covering isometry
$V:H_X\to H_Y$ after stabilization. Its support is within a controlled
neighbourhood of the graph of $f$. Conjugation $T\mapsto VTV^*$ sends locally
compact controlled operators to operators with the corresponding properties
on $Y$. Different covering choices induce the same homomorphism on $K$-theory.
This defines the covariant functor on proper metric spaces, including maps
which are not continuous; the covering construction handles the support data.

In this formulation, coarse invariance, excision, and vanishing on flasques
are the usual properties of Roe-algebra $K$-theory. The categorical formulation
below also includes $u$-continuity on general bornological coarse spaces.

## The Roe category of locally finite modules

Let $X$ now be any bornological coarse space.

```{prf:definition} Locally finite Roe category
:nonumber:
:label: def-roe-category

The *locally finite Roe category* $\mathbf C(X)$ has as objects locally finite,
point-determined geometric modules over $X$. Morphisms are the operator-norm
limits of bounded controlled operators. Composition and involution are
composition and adjoint of operators.
```

Since $\chi_BH$ is finite-dimensional for bounded $B$, every bounded operator
between these modules is locally compact. The identity is a morphism, so this
is a unital $C^*$-category. Morphisms still have to be approximable by controlled
operators; local compactness alone is not sufficient.

For a coarse map $f$, push a module forward by

$$
(f_*H)_y=\bigoplus_{x\in f^{-1}(y)}H_x,
\qquad \chi_B^{f_*H}=\chi_{f^{-1}(B)}^H.
$$

Properness preserves local finiteness, and controlledness preserves controlled
operators. On the underlying operators the pushforward functor is the identity.

```{prf:definition} Spectrum-valued coarse K-theory
:nonumber:
:label: def-coarse-k-theory

The *coarse $K$-theory spectrum* is

$$
K\mathcal X(X)=K(\mathbf C(X)),
$$

where $K$ is topological $K$-theory of $C^*$-categories. It takes values in
$KU$-module spectra, or in spectra after forgetting the module structure.
```

This is a {prf:ref}`coarse homology theory <def-stable-coarse-homology>`.
On separable proper metric spaces its homotopy groups recover the classical
ample Roe-algebra groups. Proofs of these properties are given in
[Bunke–Engel, Homotopy theory with bornological coarse spaces, Chapter 8](https://arxiv.org/abs/1607.03657).
At a point its value is $KU$. Consequently

$$
K\mathcal X(\mathbb R^d)\simeq\Sigma^d KU,\qquad
K\mathcal X_n(\mathbb R^d)\cong
\begin{cases}\mathbb Z,&n\equiv d\pmod2,\\0,&\text{otherwise}.\end{cases}
$$

The Euclidean Dirac index represents the generator in the corresponding parity.

## Using all nondegenerate modules

For a proper metric space there is also the analytic Roe-category formulation
with all separable nondegenerate $C_0(X)$-modules as objects and locally compact,
approximable finite-propagation operators as morphisms. The endomorphism algebra
of an ample object is the classical Roe algebra. Using the nonunital
$C^*$-category version of $K$-theory and its comparison with an ample object
recovers the same theory in this setting.

There is a necessary qualification: for a module with infinite-dimensional
local subspaces its identity need not be locally compact. Thus this category
is generally **nonunital**. One cannot obtain the locally finite construction
just by dropping local finiteness while retaining all controlled operators:
at a point that would introduce $\mathcal B(H)$ instead of the compact
operators. Nonunital categories require the corresponding multiplier and
$K$-theory formalism. The locally finite model avoids this issue and is the
one used here on arbitrary bornological coarse spaces.
