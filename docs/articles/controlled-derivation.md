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

The real vector space of controlled $*$-derivations is a real Lie algebra under the commutator of linear maps. 

```{prf:definition} Locally generated derivation
:nonumber:
:label: def-locally-generated-derivation

A derivation is *locally generated* if there are self-adjoint
$h_i\in\mathcal A_{B_i}$ with the family $(B_i)$ locally finite and uniformly
bounded, such that

$$
D(a)=i\sum_i[h_i,a].
$$

```

Here *local finiteness* means that each bounded subset meets only finitely many $B_i$, and *uniform boundedness* means that
$\bigcup_i(B_i\times B_i)$ is an entourage.

For local matrix nets, controlled and locally generated derivations coincide.
The full statement and proof can be found
{ref}`here <theorem-controlled-derivations>`.
