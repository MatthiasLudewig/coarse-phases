(article-controlled-derivation)=
# Controlled derivation

```{warning}
Agent-generated, not reviewed yet
```

Controlled derivations are infinitesimal operations which enlarge the support
of an observable by a fixed entourage. 
In a local matrix net they can be
written as sums of local commutators.

## Definition

Let $\mathcal A$ be a {prf:ref}`local matrix net <def-local-matrix-net>` on
$X$, and work on its algebraic union $\mathcal A_X^{\mathrm{alg}}$.

```{prf:definition} Controlled derivation
:nonumber:
:label: def-controlled-derivation

A *controlled $*$-derivation* is a complex-linear map
$D:\mathcal A_X^{\mathrm{alg}}\to\mathcal A_X^{\mathrm{alg}}$ satisfying

$$
D(ab)=D(a)b+aD(b),\qquad D(a^*)=D(a)^*,
$$

and, for some entourage $E$,

$$
D(\mathcal A_B)\subseteq\mathcal A_{B_E}
\quad\text{for every bounded }B.
$$

```

The real vector space of controlled $*$-derivations is a real Lie algebra under
commutator. Composing control entourages controls the Lie bracket. Complex
linear combinations give the corresponding complex Lie algebra of algebraic
derivations; a general complex multiple need not preserve the $*$-condition.

No bound on the global operator norm of $D$ is assumed. Nor does this algebraic
definition alone assert that $D$ generates a strongly continuous dynamics on
the completed quasi-local algebra.

## Local generation

```{prf:definition} Locally generated derivation
:nonumber:
:label: def-locally-generated-derivation

A derivation is *locally generated* if there are self-adjoint
$h_i\in\mathcal A_{B_i}$ with the family $(B_i)$ locally finite and uniformly
bounded, such that

$$
D(a)=i\sum_i[h_i,a].
$$

Here *local finiteness* means that each bounded subset meets only finitely many
$B_i$, and *uniform boundedness* means
$\bigcup_i(B_i\times B_i)\in\mathcal C_X$.
```

Only finitely many commutators are nonzero for each local observable. Uniform
boundedness refers to the supports; it is not a uniform bound on $\|h_i\|$.

For local matrix nets, controlled and locally generated derivations coincide.
The full statement and proof are on
{ref}`Controlled derivations are locally generated <theorem-controlled-derivations>`.
The proof uses normalized local implementers and the exact-support
decomposition furnished by conditional expectations. It does not require a
uniform bound on the dimensions of the point algebras.

## Uniformly finite body order

For the following algebraic construction, use complex derivations and write
local implementers as $\operatorname{ad}(h)(a)=[h,a]$, without a
self-adjointness requirement. Let $\Lambda$ be the locally finite support of
the point algebras of $\mathcal A$.

```{prf:definition} Uniformly finite body order
:nonumber:
:label: def-finite-body-controlled-derivation

A controlled derivation has *uniformly finite body order* if it admits a
presentation

$$
D=\sum_i\operatorname{ad}(h_i),\qquad
h_i\in\mathcal A_{F_i},\quad F_i\subseteq\Lambda,
$$

where the family $(F_i)$ is locally finite and uniformly bounded, and there
is a finite integer $k_D$ such that $|F_i|\leq k_D$ for every $i$.
Denote these derivations by $\mathfrak d_{\mathrm{fb}}(\mathcal A)$.
```

The bound may depend on the derivation. There is no bound on the norms of the
implementers or on the dimensions of the point algebras. The cardinality
counts physical sites, even when a point algebra has several tensor factors.
Equivalently, the nonzero terms in the
{ref}`exact-support decomposition <article-spin-system>` have uniformly
bounded cardinality: decomposing each $h_i$ by partial traces only replaces
$F_i$ by its subsets.

This is a complex Lie subalgebra. Terms with disjoint supports commute, and a
bracket of terms supported on $F$ and $G$ is supported on $F\cup G$.
If the original bounds are $k$ and $\ell$, the new bound is at most
$k+\ell$. The unions of intersecting supports remain uniformly bounded and
locally finite. Extending a derivation by zero on an additional tensor factor
preserves finite body order.

Onsite and two-site interactions are examples. On a discrete metric space of
bounded geometry, every controlled derivation has uniformly finite body order:
the number of sites in a support of fixed diameter is uniformly bounded.
For arbitrary coarse spaces, controlled supports can have unbounded
cardinality, so this can be a proper subalgebra of all controlled derivations.

## Stable vanishing in a ray direction

For a product $X=Y\otimes\mathbb N$, uniformly finite-body controlled
derivations have stably vanishing positive-degree Lie algebra homology, without
a bounded-geometry assumption on $Y$. One auxiliary local matrix net can be
chosen for all positive degrees simultaneously. The full statement and proof
are on {ref}`Stable vanishing for finite-body controlled derivations
<theorem-finite-body-stable-vanishing>`.

The theorem also kills classes in the homology of the full controlled
derivation algebra that come from this subalgebra. Its proof does not establish
stable vanishing for all controlled derivations on arbitrary $Y$: the
finite-body condition is used to keep the chain homotopies algebraic.
Degree zero is excluded, since a Lie algebra homomorphism induces the identity
on $H_0(-;\mathbb C)=\mathbb C$.

## Results of Higson–Kato

[Higson–Kato](https://arxiv.org/abs/2607.08455) study a stabilized
**complex algebraic** Lie algebra
$\mathfrak{lgd}(X)$ for a proper discrete metric space $X$. Starting with
finite matrix algebras at the sites, they take a direct limit over all local
multiplicity functions. Their generators have uniformly bounded support, but
the multiplicities may be unbounded across $X$. The suspension and computation
below are Theorems 7.2.1 and 7.2.6 of their paper.

Their homology is Lie algebra homology with trivial complex coefficients.
It has a Hopf algebra structure; the primitive part consists of classes $v$
with coproduct $v\otimes1+1\otimes v$. Their suspension result identifies

$$
\operatorname{Prim}H_p(\mathfrak{lgd}(\mathbb Z^{n-1});\mathbb C)
 \cong
\operatorname{Prim}H_{p+1}(\mathfrak{lgd}(\mathbb Z^n);\mathbb C)
\quad(n,p\geq1).
$$

The resulting computation is

$$
\operatorname{Prim}H_p(\mathfrak{lgd}(\mathbb Z^n);\mathbb C)
\cong
\begin{cases}
\mathbb C,&p=n+3,n+5,n+7,\ldots,\\
0,&\text{otherwise}.
\end{cases}
$$

The full homology is recovered from the graded commutative Hopf algebra
structure: primitive generators in odd degree contribute exterior factors,
and those in even degree contribute polynomial factors. Their argument
combines a half-space Eilenberg swindle with a Hochschild–Serre spectral
sequence. They also study the subalgebra fixing a chosen product state.

These results concern the stabilized algebraic Lie algebra. They do not by
themselves identify the homology of a fixed finite-spin system, nor a
completion used to construct Hamiltonian time evolution. The algebraic homology
calculation alone does not settle these questions.
