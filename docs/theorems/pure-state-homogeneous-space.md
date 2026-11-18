(theorem-pure-state-homogeneous-space)=
# The pure-state space as an automorphism quotient

```{warning}
Agent-generated, not reviewed yet
```

This page explains the homogeneous-space description discussed in the {ref}`Pure state article <article-pure-state>`.
The transitivity theorem is quoted from a public paper; the topological quotient assertion is proved below using the open mapping principle for Polish group actions.
The topologies are the weak-* topology on pure states and the point-norm topology on automorphisms.
The argument is due to Narutaka Ozawa.

## Transitivity

```{prf:theorem} Kishimoto–Ozawa–Sakai homogeneity theorem
:nonumber:
:label: thm-pure-state-homogeneity

Let $A$ be a separable $C^*$-algebra and let $\omega,\varphi$ be pure states with $\ker\pi_\omega=\ker\pi_\varphi$.
There is an automorphism $\alpha$ with $\varphi=\omega\circ\alpha$.
It can be chosen so that
$$
\alpha(a)=\lim_{t\to\infty}u_t a u_t^*\qquad(a\in A),
$$
where $(u_t)_{t\geq0}$ is a norm-continuous unitary path in $A$ or its unitization, with $u_0=1$.
In particular, if $A$ is nonzero, separable, and simple, $\Aut(A)$ acts transitively on $P(A)$.
```

No proof of this theorem is supplied here.
See [Kishimoto, Ozawa, and Sakai, Theorems 1.1 and 2.1](https://arxiv.org/abs/math/0110152), together with their verification of Properties 1.2 and 1.3.
The theorem uses asymptotically inner automorphisms; it does not say that inner automorphisms connect all pure states.
For simple $A$, every nonzero representation is faithful, which verifies the kernel hypothesis.

## The topological quotient

```{prf:theorem} Homogeneous-space description
:nonumber:
:label: thm-pure-state-quotient

Let $A$ be a nonzero unital separable simple $C^*$-algebra, and fix $\omega\in P(A)$.
Let
$$
G=\Aut(A),\qquad H=\Aut_\omega(A)=\{\alpha\in G \mid \omega\circ\alpha=\omega\}.
$$
Then $H$ is closed and the map
$$
G/H\longrightarrow P(A),\qquad\alpha H\longmapsto\omega\circ\alpha^{-1},
$$
is a homeomorphism, where $G/H$ has the quotient topology.
In particular, the orbit map is an open continuous surjection.
```

### Proof

We verify the hypotheses of the open mapping principle rather than infer openness from surjectivity.
A *Polish space* is a separable space with a compatible complete metric.
The principle says that a continuous transitive action of a Polish group on a Polish space has open orbit maps.
This is the global-action case of [Gómez, Pinedo, and Uzcátegui, Theorem 3.5](https://arxiv.org/abs/1709.01977), whose proof is not reproduced here.

First, $G$ is Polish.
Choose a dense sequence $(a_n)$ in the unit ball of $A$ and use the metric
$$
d_G(\alpha,\beta)=\sum_{n\geq1}2^{-n}
\left(\|\alpha(a_n)-\beta(a_n)\|+
\|\alpha^{-1}(a_n)-\beta^{-1}(a_n)\|\right).
$$
This induces point-norm convergence, since point-norm convergence of automorphisms to an automorphism also implies convergence of their inverses.
A Cauchy sequence has pointwise limits for both the automorphisms and their inverses.
These limits are mutually inverse $*$-homomorphisms, so the metric is complete.
Evaluation of automorphisms and their inverses on $(a_n)$ embeds $G$ into the second-countable space $A^{\N}\times A^{\N}$, proving separability.
Composition and inversion are continuous by the isometric property of automorphisms.

Second, $P(A)$ is Polish.
The {prf:ref}`state space <def-state-space>` $S(A)$ is compact metrizable; fix a compatible metric $d$.
For $n\geq1$, let
$$
C_n=\left\{\tfrac12(\varphi+\psi) \mid \varphi,\psi\in S(A),\ d(\varphi,\psi)\geq1/n\right\}.
$$
Each $C_n$ is compact.
Every nonextreme point is the midpoint of two distinct points on a segment through it, so
$$
S(A)\setminus P(A)=\bigcup_{n\geq1}C_n.
$$
Thus $P(A)$ is a $G_\delta$ subset of a compact metrizable space and is Polish.

Third, the action $\alpha\cdot\varphi=\varphi\circ\alpha^{-1}$ is jointly continuous.
If $\alpha_j\to\alpha$ point-norm and $\varphi_j\to\varphi$ weak-*, then for every $a\in A$,
$$
\left|\varphi_j(\alpha_j^{-1}(a))-\varphi(\alpha^{-1}(a))\right|
\leq\|\alpha_j^{-1}(a)-\alpha^{-1}(a)\|
+\left|(\varphi_j-\varphi)(\alpha^{-1}(a))\right|\longrightarrow0.
$$
The {prf:ref}`homogeneity theorem <thm-pure-state-homogeneity>` makes this action transitive, so the open mapping principle applies.
The stabilizer $H$ is closed as the inverse image of $\{\omega\}$ under the continuous orbit map.
Its fibers are exactly the left cosets $\alpha H$.
The induced bijection $G/H\to P(A)$ is continuous and open and is therefore a homeomorphism.

## Conventions and scope

The inverse in $\omega\circ\alpha^{-1}$ makes this a left action with quotient $G/H$.
If instead one uses the pullback orbit map $\alpha\mapsto\omega\circ\alpha$, its fibers are right cosets $H\alpha$, and the corresponding quotient is $H\backslash G$.
Inversion identifies the two descriptions.

The quotient is a homogeneous space, not generally a quotient group: the stabilizer need not be normal.
An open orbit map does not by itself provide continuous local sections, so no fiber-bundle assertion is made here.
Separability is part of both the transitivity theorem used here and the Polish-space argument.
The theorem therefore applies to a spin system with countably many nontrivial matrix sites, but its application to a more general spin system requires checking separability.
It also imposes no geometric control on the automorphisms, unlike the conditions used for {ref}`gapped phases <article-gapped-phase>`.
