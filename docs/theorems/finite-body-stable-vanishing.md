(theorem-finite-body-stable-vanishing)=
# Stable vanishing for finite-body controlled derivations

```{warning}
Agent-generated, not reviewed yet
```

This page proves stable vanishing of positive-degree Lie algebra homology
for {prf:ref}`uniformly finite-body controlled derivations
<def-finite-body-controlled-derivation>` in a ray direction. The auxiliary
local matrix net is independent of the homology class and the homological
degree. A proof is supplied below; the unrestricted controlled-derivation
statement is not asserted.

## Statement

```{prf:theorem} Stable vanishing in a ray direction
:nonumber:
:label: thm-finite-body-stable-vanishing

Let $Y$ be a bornological coarse space, and let
$X=Y\otimes\mathbb N$, where $\mathbb N=\{0,1,2,\ldots\}$ has its usual
metric coarse structure and finite-set bornology. Give $X$ the
{prf:ref}`product coarse structure and product bornology
<def-coarse-tensor-product>`.

For every {prf:ref}`local matrix net <def-local-matrix-net>` $\mathcal A$
on $X$, there is a local matrix net $\mathcal B$ on $X$ such that
extension by zero on the $\mathcal B$-factor induces the zero map

$$
H_q\bigl(\mathfrak d_{\mathrm{fb}}(\mathcal A);\mathbb C\bigr)
\longrightarrow
H_q\bigl(\mathfrak d_{\mathrm{fb}}(\mathcal A\otimes\mathcal B);
\mathbb C\bigr)
\qquad(q>0).
$$

Here the Lie algebras consist of complex algebraic derivations on the
algebraic local algebras, and homology is algebraic Chevalley–Eilenberg
homology with trivial coefficients. The same $\mathcal B$ works for every
$q>0$. No bounded-geometry assumption on $Y$, uniform bound on local matrix
dimensions, or norm bound on interactions is imposed.
```

Composing with inclusion into the full controlled-derivation algebra gives
zero there as well. Equivalently, every class in the image of

$$
H_q\bigl(\mathfrak d_{\mathrm{fb}}(\mathcal A);\mathbb C\bigr)
\longrightarrow H_q\bigl(\operatorname{Der}_c(\mathcal A);\mathbb C\bigr)
$$

is killed by this same stabilization, for $q>0$.

## Algebraic homotopies for paired tensor factors

We first give the algebraic justification for the swaps used in the proof.
The distinction between a tensor factor and its physical site is important:
several independently labelled factors may occupy the same site.

Consider disjoint pairs of equal matrix factors, with each pair located at
at most two sites. Assume that their supports form a locally finite,
uniformly bounded family. Add one spectator factor $M_2(\mathbb C)$ at
one endpoint of each pair. All these factors define a local matrix net.
Let $U$ swap the two factors in every pair and fix the spectators and all
unpaired factors. This gives a controlled algebra automorphism, with
controlled inverse: a local observable meets only finitely many pairs, and
each affected factor can move only to the other endpoint of its pair.

```{prf:lemma} Homological invariance of paired-factor swaps
:nonumber:
:label: lem-finite-body-paired-swaps

Let $\phi:\mathfrak g\to\mathfrak d_{\mathrm{fb}}(\mathcal M)$ be a
Lie algebra homomorphism into a net containing the pairs and spectators
just described. Suppose that, for each $D\in\mathfrak g$, $\phi(D)$ has
a locally finite, uniformly controlled interaction presentation such that
every term meets at most $k_D$ of the paired blocks, for some finite $k_D$.

Then $\phi$ and $\operatorname{Ad}_U\circ\phi$ induce the same map in
algebraic Lie algebra homology. Here $\operatorname{Ad}_U$ denotes the
induced conjugation of derivations.
```

```{prf:proof}
For a pair $M_d\otimes M_d$, the flip is implemented on
$\mathbb C^d\otimes\mathbb C^d$ by an involution whose negative
eigenspace has dimension $d(d-1)/2$. Tensoring with the spectator identity
makes that dimension $d(d-1)$, which is even. Split this negative eigenspace
into two-dimensional subspaces. On each use

$$
-I_2=
\left(
\begin{pmatrix}1&1\\0&1\end{pmatrix}
\begin{pmatrix}1&0\\-1&1\end{pmatrix}
\begin{pmatrix}1&1\\0&1\end{pmatrix}
\right)^2.
$$

Extend by the identity on the positive eigenspace. Thus the implementing
matrix of each block is a product of six exponentials $\exp(N_j)$ with
$N_j^2=0$. This number is independent of $d$.

For one of the six positions, sum the associated inner derivations over all
blocks:

$$
\varepsilon=\sum_b\operatorname{ad}(N_b).
$$

This is a controlled derivation of body order at most two. The block
generators commute because their tensor factors are disjoint, even when
their physical supports overlap. Also
$(\operatorname{ad}N_b)^3=0$ on the local algebra. If an interaction term
meets at most $k$ blocks, the multinomial expansion therefore gives

$$
(\operatorname{ad}\varepsilon)^{2k+1}
       \bigl(\operatorname{ad}(h)\bigr)=0.
$$

The same bound applies to the entire locally finite sum representing
$\phi(D)$, since $k_D$ is uniform over its terms. This proves local
nilpotence on the source image; local nilpotence on the entire target Lie
algebra is not needed.

For completeness, take the Chevalley–Eilenberg sign convention
$d(x\wedge y)=[x,y]$. Write $L_\varepsilon$ for the action of
$\operatorname{ad}\varepsilon$ on exterior chains and
$\iota_\varepsilon(c)=\varepsilon\wedge c$. Then

$$
d\iota_\varepsilon+\iota_\varepsilon d=L_\varepsilon.
$$

If $F=C_*(\phi)$, the formula

$$
H(c)=\sum_{j\ge0}\frac{1}{(j+1)!}
       \iota_\varepsilon L_\varepsilon^jF(c)
$$

is a finite sum for each chain $c$, and satisfies

$$
dH+Hd=\exp(L_\varepsilon)F-F.
$$

Conjugating a term changes only the blocks it already meets, so the same
argument applies successively to all six positions. If the original term
has body order at most $a$ and meets at most $k$ blocks, the transformed
term occupies at most $a+2k$ sites. Supports remain controlled and locally
finite. Thus the entire homotopy stays in the algebraic chains of
$\mathfrak d_{\mathrm{fb}}(\mathcal M)$, proving the lemma.
```

## Proof of stable vanishing

Write $\mathfrak g=\mathfrak d_{\mathrm{fb}}(\mathcal A)$ and
$s(y,n)=(y,n+1)$. For any local matrix net $\mathcal C$, its shifted net
has bounded-region algebra

$$
(s_*^j\mathcal C)_V=\mathcal C_{(s^j)^{-1}(V)}.
$$

The shift is injective, controlled, and proper. Shifting identifies the
global algebraic algebras, relocates the interaction supports, and preserves
body order. Simultaneous shifts preserve a common control entourage in
the product coarse structure. Every bounded subset of $X$ is contained in
$B\times\{0,\ldots,N\}$ for some bounded $B\subseteq Y$ and finite $N$.
These observations ensure local finiteness in the constructions below.

### A fixed enlargement comparing the telescope with its tail

Form primary copies $P_j=s_*^j\mathcal A$ for $j\ge0$ and auxiliary
copies $Q_j=s_*^j\mathcal A$ for $j\ge1$. Keep their point factors
separately labelled, including when they occupy the same point of $X$.
Their tensor product is a local matrix net, since only finitely many layers
meet any bounded set.

On the primary copies put

$$
S(D)=\sum_{j\ge0}D^{P_j},\qquad
R(D)=\sum_{j\ge1}D^{P_j}.
$$

Each sum is finite when applied to a local observable. The copied
interactions have a common control and body-order bound, and their family
is locally finite. Different copies commute, so $S$ and $R$ are Lie algebra
homomorphisms. If $i$ denotes the inclusion in $P_0=\mathcal A$, then

$$
S=i+R,\qquad [i(D),R(D')]=0.
$$

Perform two layers of swaps. In the first, for every original point factor
$\mathcal A_x$ and every $j\ge0$, swap its copy in $P_j$ with its copy
in $Q_{j+1}$. In the second, swap corresponding factors of $Q_j$ and $P_j$
for every $j\ge1$. Within each layer the pairs are disjoint as tensor
factors. Their physical displacements are respectively one vertical step
and zero. Their supports form locally finite families. Include separate
spectators for each layer, placed at the upper endpoint.

The resulting net has the form $\mathcal D=\mathcal A\otimes\mathcal K$.
The composite swap carries $S$ to $R$ and $R$ acts entirely in $\mathcal K$.
A copied interaction involving at most $k_D$ original sites meets at most
$k_D$ pairs in each layer. Applying the
{prf:ref}`paired-factor swap lemma <lem-finite-body-paired-swaps>` to
these source images gives

$$
S_*=R_*:
H_*(\mathfrak g;\mathbb C)\longrightarrow
H_*\bigl(\mathfrak d_{\mathrm{fb}}(\mathcal A\otimes\mathcal K);
\mathbb C\bigr).
$$

### One enlargement through any fixed degree

We show by induction on $r\ge1$ that the inclusion

$$
i_r:\mathfrak g\longrightarrow
\mathfrak d_{\mathrm{fb}}(\mathcal A\otimes\mathcal K^{\otimes r})
$$

kills homology in degrees $1,\ldots,r$.

The diagonal of a Lie algebra induces a coproduct on its homology. By the
Künneth isomorphism, a class $c\in H_q(\mathfrak g;\mathbb C)$, $q>0$,
has coproduct of the form

$$
\Delta c=c\otimes1+1\otimes c+
\sum_{a=1}^{q-1}\sum_\nu u_{a,\nu}\otimes v_{q-a,\nu},
$$

where the sum is finite. The map induced by $i+R$ is obtained by applying
this coproduct and then the map from the two commuting images.

For $q=1$ there are no mixed terms, so $S_*=R_*$ implies $(i_1)_*=0$.
Suppose the claim holds for $r-1$. Reserve the last $\mathcal K$-factor
for $R$, and let the other $r-1$ factors enlarge the initial $\mathcal A$.
There is a commuting-sum Lie algebra homomorphism

$$
\begin{aligned}
\mathfrak d_{\mathrm{fb}}(\mathcal A\otimes\mathcal K^{\otimes(r-1)})
\oplus\mathfrak g
&\longrightarrow
\mathfrak d_{\mathrm{fb}}(\mathcal A\otimes\mathcal K^{\otimes r}),\\
(D,D')&\longmapsto D+R(D').
\end{aligned}
$$

For $1\le q\le r$, every mixed term in $\Delta c$ has first degree
$a\le r-1$ and is killed by the induction hypothesis. Consequently the
extended maps satisfy

$$
S_*c=(i_r)_*c+R_*c.
$$

The equality $S_*=R_*$ persists under enlargement, so $(i_r)_*c=0$.
The fresh tensor factors are essential here: they make the lower-degree
fillings commute with the copy of $R$. This proves the induction for all
classes in the indicated degrees, not just for primitive classes.

### A single enlargement in all positive degrees

Let $\mathcal L$ have one factor $M_2(\mathbb C)$ at each nontrivial site
of $\mathcal A$, and trivial factors elsewhere. Define

$$
\mathcal E=
\mathcal A\otimes\bigotimes_{r\ge1}
s_*^r\bigl(\mathcal A\otimes\mathcal K^{\otimes r}\otimes\mathcal L\bigr).
$$

This is a local matrix net. A bounded set of height at most $N$ meets only
the packages with $r\le N$, and each of those is a local matrix net.
Write $\mathcal E=\mathcal A\otimes\mathcal B$.

Fix $r\ge1$. Pair each original $\mathcal A_x$ with its copy at $s^r(x)$
in the $r$-th package. Use the corresponding factor of $s_*^r\mathcal L$
as spectator. These pairs are disjoint as tensor factors, locally finite,
and controlled with vertical displacement $r$. Every interaction from
$\mathfrak g$ meets at most its body-order bound of pairs. The swap lemma
therefore identifies, on homology, the original inclusion into
$\mathfrak d_{\mathrm{fb}}(\mathcal E)$ with the inclusion through the
$r$-th package.

The latter factors through $i_r$, followed by shift and tensor extension,
so it is zero in degrees $1,\ldots,r$. Since $r$ is arbitrary and
$\mathcal E$ is fixed, the original inclusion is zero in every positive
degree. This proves the theorem.

## Scope of the conclusion

The vertical shift makes $Y\otimes\mathbb N$
{ref}`flasque <article-flasque-coarse-space>`. The theorem supplies a stable
vanishing statement in this setting, rather than asserting that the
homology of a fixed net itself vanishes. No conclusion about completed
Lie algebras or Hamiltonian time evolution is made.

For arbitrary $Y$, a controlled derivation may involve supports of unbounded
cardinality. A paired-factor swap still makes sense on each local observable,
but the nilpotence bound in the algebraic homotopy need no longer be uniform
over all terms of a derivation. Integrating a pointwise defined path does not
automatically give a chain in an algebraic exterior power. The proof therefore
does not settle stable vanishing for the full $\operatorname{Der}_c$ without
the finite-body restriction. The map on degree-zero homology is always the
identity on $\mathbb C$.

See {ref}`Controlled derivation <article-controlled-derivation>` for the
definitions and related stabilized calculations, and
{ref}`Spin system and local nets <article-spin-system>` for the point-factor
description and conditional expectations.
