(theorem-ample-modules)=
# Controlled unitary equivalence of ample modules

```{warning}
Agent-generated, not reviewed yet
```

The equivalence below is controlled in the coarse sense.
It need not be an isomorphism of $C_0(X)$-representations.

## Statement

```{prf:theorem} Comparison of ample modules
:nonumber:
:label: thm-ample-modules

Let $X$ be a separable proper metric space, and let $\rho_i:C_0(X)\to\mathcal B(H_i)$, $i=1,2$, be nondegenerate ample representations on separable complex Hilbert spaces.
There exists a finite-propagation unitary $U:H_1\to H_2$.
Conjugation by $U$ gives an isomorphism
$$
C^*(X;H_1)\xrightarrow{\cong}C^*(X;H_2).
$$
```

## A uniformly bounded Borel partition

Fix $r>0$ and choose a maximal $r$-separated subset $\Lambda\subseteq X$.
Properness makes it locally finite, and separability makes it countable.
Every point is within distance at most $r$ of $\Lambda$.
Assign each point to a nearest center, resolving ties by a fixed enumeration.
This gives a Borel partition $(B_\lambda)_{\lambda\in\Lambda}$ with diameter at most $2r$.
Each cell contains the open ball of radius $r/2$ about its center.
Every bounded set meets only finitely many cells: their centers lie in a bounded $r$-thickening of that set and are $r$-separated.

## Construction of the unitary

Borel functional calculus gives orthogonal decompositions
$$
H_i=\bigoplus_{\lambda\in\Lambda}H_{i,\lambda},\qquad
H_{i,\lambda}=\rho_i(\mathbf1_{B_\lambda})H_i.
$$
Choose a nonzero compactly supported continuous function in the interior of $B_\lambda$.
Its action has range in $H_{i,\lambda}$ and is noncompact by ampleness.
Therefore every $H_{i,\lambda}$ is infinite-dimensional.
Since these Hilbert spaces are separable, choose a unitary $U_\lambda:H_{1,\lambda}\to H_{2,\lambda}$.

The orthogonal direct sum $U=\bigoplus_\lambda U_\lambda$ is unitary.
It moves vectors only within the same cell, so its propagation is at most $2r$.
This proves the controlled equivalence.

## Conjugation of Roe algebras

If $T$ has propagation at most $R$, then $UTU^*$ has propagation at most $R+4r$.
To check local compactness, fix a bounded Borel set $B$.
The finitely many cells meeting $B$ have bounded union $C$, and
$$
\chi_B^{(2)}U=\chi_B^{(2)}U\chi_C^{(1)}.
$$
Thus $\chi_B^{(2)}UTU^*$ is compact if $T$ is locally compact; the analogous argument works on the other side.
Applying the same reasoning to $U^*$ gives the converse.
Conjugation therefore identifies the finite-propagation locally compact algebras and, by norm continuity, their completions.

## Related articles

See {ref}`Geometric module <article-geometric-module>` for ampleness and {ref}`Roe algebra <article-roe-algebra>` for the completion.
