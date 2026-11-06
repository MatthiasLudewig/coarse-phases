(article-controlled-derivation)=
# Controlled derivation

```{warning}
Agent-generated, not reviewed yet
```

Controlled derivations are infinitesimal operations which enlarge the support
of an observable by a fixed entourage. In a local matrix net they can be
written as sums of local commutators.

## Definition

Let $\mathcal A$ be a {prf:ref}`local matrix net <def-local-matrix-net>` on
$X$, and work on its algebraic union $\mathcal A_X^{\mathrm{alg}}$.

```{prf:definition} Controlled derivation
:nonumber:
:label: def-controlled-derivation

A controlled $*$-derivation is a complex-linear map
$D:\mathcal A_X^{\mathrm{alg}}\to\mathcal A_X^{\mathrm{alg}}$ satisfying

$$
D(ab)=D(a)b+aD(b),\qquad D(a^*)=D(a)^*,
$$

and, for some entourage $E$,

$$
D(\mathcal A_B)\subseteq\mathcal A_{E[B]}
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

A derivation is locally generated if there are self-adjoint
$h_i\in\mathcal A_{B_i}$ with the family $(B_i)$ locally finite and uniformly
bounded, such that

$$
D(a)=i\sum_i[h_i,a].
$$

Here local finiteness means that each bounded subset meets only finitely many
$B_i$, and uniform boundedness means
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
