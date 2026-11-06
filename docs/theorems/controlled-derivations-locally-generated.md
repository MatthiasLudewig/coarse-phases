(theorem-controlled-derivations)=
# Controlled derivations are locally generated

```{warning}
Agent-generated, not reviewed yet
```

The statement concerns derivations on the algebraic local algebra of a
{prf:ref}`local matrix net <def-local-matrix-net>`. It makes no assertion about
existence of a dynamics on its norm completion.

## Statement

```{prf:theorem} Controlledness and local generation
:nonumber:
:label: thm-controlled-locally-generated

Let $\mathcal A$ be a local matrix net on a bornological coarse space $X$.
A $*$-derivation of $\mathcal A_X^{\mathrm{alg}}$ is
{prf:ref}`controlled <def-controlled-derivation>` if and only if it is
{prf:ref}`locally generated <def-locally-generated-derivation>`.
```

## Normalized local implementers

Use the {ref}`point-object description <theorem-local-objects-points>` to write
the net on a locally finite support $\Lambda$. Fix a symmetric control $E$
containing the diagonal. For bounded $B$, there is a unique self-adjoint
$h_B\in\mathcal A_{E[B]}$ such that

$$
D(a)=i[h_B,a]\quad(a\in\mathcal A_B),\qquad
\mathbb E_{X\setminus B}(h_B)=0.
$$

To see existence, regard $D|_{\mathcal A_B}$ as a derivation from the matrix
algebra $M_d(\mathbb C)=\mathcal A_B$ into the bimodule
$\mathcal A_{E[B]}$. For matrix units $e_{ij}$, set

$$
K=\sum_i D(e_{i1})e_{1i}.
$$

The identity $e_{kl}e_{i1}=\delta_{li}e_{k1}$, after applying $D$, gives
$[K,e_{kl}]=D(e_{kl})$. Thus $D(a)=[K,a]$. Since $D$ preserves the involution,
$K+K^*$ commutes with $\mathcal A_B$, so replacing $K$ by $(K-K^*)/2$ does
not change its commutator. Write this skew-adjoint implementer as $ih$ with
$h=h^*$, and subtract $\mathbb E_{X\setminus B}(h)$.
The subtracted term lies in the relative commutant and does not change $D$.

For uniqueness, two normalized implementers differ by an element of
$\mathcal A_B'\cap\mathcal A_{E[B]}=\mathcal A_{E[B]\setminus B}$.
Conditional expectation onto $X\setminus B$ fixes this difference and also
annihilates it, so it is zero.

## Construction of the interaction

Use the exact-support vector-space decomposition

$$
\mathcal A_X^{\mathrm{alg}}
 =\bigoplus_{F\subseteq\Lambda,\ F\text{ finite}}\mathcal A_F^\circ
$$

from the {ref}`conditional expectation construction <article-spin-system>`.
Let $p_F$ be projection onto the $F$-summand. These projections preserve
self-adjointness. Normalization of $h_B$ implies
$p_F(h_B)=0$ if $F\cap B=\varnothing$.

If $B\subseteq C$, then $h_C-h_B$ commutes with $\mathcal A_B$ and hence
has only components supported away from $B$. Consequently
$p_F(h_C)=p_F(h_B)$ whenever $F\cap B\neq\varnothing$.
Using $B\cup C$ gives the same comparison for arbitrary $B,C$ both meeting
$F$.

For each nonempty finite $F\subseteq\Lambda$, define

$$
h^F=p_F(h_F).
$$

For every $x\in F$ the compatibility just proved gives
$h^F=p_F(h_{\{x\}})$. Since $h_{\{x\}}\in\mathcal A_{E[\{x\}]}$,
a nonzero $h^F$ requires $F\subseteq E[\{x\}]$ for every $x\in F$.
In particular $F\times F\subseteq E$, so the nonzero interaction supports
are uniformly bounded.

They are locally finite as a family: if $F$ meets a bounded set $B$, then
$F\subseteq E[B]\cap\Lambda$, a finite set. There are only finitely many
possible nonempty subsets $F$ of that finite set.
Finally, for $a\in\mathcal A_B$,

$$
D(a)=i[h_B,a]
    =i\sum_{F\cap B\neq\varnothing}[h^F,a].
$$

Terms supported away from $B$ commute with $a$. This is the desired locally
finite, uniformly controlled interaction.

## The converse

Suppose $D(a)=i\sum_i[h_i,a]$ with the prescribed support conditions. If
$a\in\mathcal A_B$, only terms with $B_i\cap B\neq\varnothing$ contribute.
Choose a symmetric entourage $E$ containing the diagonal and every
$B_i\times B_i$. Each such $B_i$ lies in $E[B]$. Hence
$D(a)\in\mathcal A_{E[B]}$, proving controlledness. The sum is finite on
each local algebra and thus satisfies the Leibniz and $*$ identities there.

## Related articles

See {ref}`Controlled derivation <article-controlled-derivation>` for the
definitions and the Lie algebra homology of locally generated derivations.
