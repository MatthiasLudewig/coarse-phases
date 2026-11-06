(article-spin-system)=
# Spin system and local nets

```{warning}
Agent-generated, not reviewed yet
```

A spin system assigns a finite-dimensional matrix algebra to each bounded
region of a coarse space. Disjoint regions carry independent tensor factors.
This is the algebra-valued instance of a local controlled object, but it can
be defined without the categorical terminology.

## Independent definition

Let $X$ be a coarse space.

```{prf:definition} Local matrix net
:label: def-local-matrix-net

A local matrix net on $X$ assigns a full matrix algebra $\mathcal A_B$ to each
bounded $B\subseteq X$, with compatible unital injective $*$-homomorphisms for
inclusions, such that:

1. $\mathcal A_\varnothing=\mathbb C$;
2. for disjoint bounded $B,C$, the two local algebras commute and multiplication
   gives $\mathcal A_B\otimes\mathcal A_C\cong\mathcal A_{B\sqcup C}$;
3. if $(B_i)$ is directed with bounded union $B$, then
   $\operatorname*{colim}_i\mathcal A_{B_i}\cong\mathcal A_B$.

A spin system, in the present convention, is a local matrix net.
```

The tensor product is unambiguous for matrix algebras. For a general subset
$Y\subseteq X$, let $\mathcal A_Y^{\mathrm{alg}}$ be the union of the local
algebras over bounded subsets of $Y$, and let $\mathcal A_Y$ be its norm
completion. The global algebra $\mathcal A_X$ is the quasi-local algebra.
Keeping the algebraic union distinct from its completion is useful when
working with {ref}`derivations <article-controlled-derivation>`.

Choose a locally finite subset $\Lambda\subseteq X$ and integers $q_x\geq2$
for $x\in\Lambda$. Then

$$
\mathcal A_B=\bigotimes_{x\in B\cap\Lambda}M_{q_x}(\mathbb C)
$$

defines a local matrix net. Every local matrix net has this form up to a
propagation-zero isomorphism, as proved in
{ref}`the point-object proposition <theorem-local-objects-points>`. No uniform
bound on the $q_x$ is imposed here.

## Relation to controlled objects and morphisms

Taking unital algebras as coefficient objects and tensor product as monoidal
operation identifies the preceding definition with the matrix-algebra case of
{prf:ref}`local controlled objects <def-local-controlled-object>`.

A controlled homomorphism $\varphi:\mathcal A\to\mathcal B$ is a unital
$*$-homomorphism of quasi-local algebras with

$$
\varphi(\mathcal A_B)\subseteq\mathcal B_{E[B]}
$$

for every bounded $B$, for one fixed entourage $E$. It restricts to a map of
the algebraic unions. The local matrix nets and these morphisms form a
symmetric monoidal category. Controlled isomorphisms, with controlled inverses,
form its maximal subgroupoid. A {ref}`quantum cellular automaton
<article-quantum-cellular-automaton>` is an automorphism in this subgroupoid.

## Conditional expectations for subsets

Each matrix algebra has a unique normalized trace. Their compatible tensor
products determine a tracial state $\tau_Y$ on $\mathcal A_Y$ for every
subset $Y$. Locality gives a canonical identification

$$
\mathcal A_X\cong\mathcal A_Y\otimes\mathcal A_{X\setminus Y}.
$$

```{prf:definition} Conditional expectation onto a subset
:label: def-subset-conditional-expectation

The conditional expectation onto $\mathcal A_Y$ is

$$
\mathbb E_Y=\mathrm{id}_{\mathcal A_Y}\otimes\tau_{X\setminus Y}:
\mathcal A_X\longrightarrow\mathcal A_Y.
$$

```

It is a unital completely positive contraction, fixes $\mathcal A_Y$, and
satisfies $\mathbb E_Y(bac)=b\mathbb E_Y(a)c$ for $b,c\in\mathcal A_Y$.
Furthermore,
$\mathbb E_Y\mathbb E_Z=\mathbb E_{Y\cap Z}$ and
$\mathbb E_Y(\mathcal A_B)\subseteq\mathcal A_{B\cap Y}$.
All these statements follow first on finite tensor products by partial trace
and then on the completion by continuity.

Write $\mathcal A_x^\circ=\ker\tau_x$ for $x\in\Lambda$, and set
$\mathcal A_F^\circ=\bigotimes_{x\in F}\mathcal A_x^\circ$, with
$\mathcal A_\varnothing^\circ=\mathbb C\mathbf1$. Then

$$
\mathcal A_X^{\mathrm{alg}}
 =\bigoplus_{F\subseteq\Lambda,\ F\text{ finite}}\mathcal A_F^\circ.
$$

This is a direct sum of vector spaces, not a decomposition into subalgebras.
On its $F$-summand, $\mathbb E_Y$ is the identity if $F\subseteq Y$ and zero
otherwise. This exact-support decomposition is used in the proof that
{ref}`controlled derivations are locally generated <theorem-controlled-derivations>`.

## Sources

See the author's {ref}`Local nets and gapped systems <bib-systems-notes>`,
the sections on local nets and conditional expectations, and the
{ref}`QCA manuscript <bib-qca-notes>`, §2.2.
