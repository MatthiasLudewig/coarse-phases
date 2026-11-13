(theorem-local-objects-points)=
# Local objects are determined by their point objects

```{warning}
Agent-generated, not reviewed yet
```

This proposition describes the pointwise data underlying {prf:ref}`local controlled objects <def-local-controlled-object>`.
The local finiteness conclusion requires a finiteness hypothesis on the coefficient objects.

## Statement

```{prf:proposition} Point-object description
:nonumber:
:label: prop-local-objects-points

Let $V$ be a local controlled object over a bornological coarse space $X$, with values in a symmetric monoidal category whose unit $\mathbf1$ is initial.
The directed colimits in the definition of a controlled object are taken in this coefficient category.
Set $V_x=V(\{x\})$.
Then, naturally in bounded $B$,
$$
V(B)\cong\mathop{\colim}_{F\subseteq B,\ F\text{ finite}}
                      \bigotimes_{x\in F}V_x.
$$
If the coefficient category consists of finite-dimensional Hilbert spaces with isometric embeddings and direct sum, or full finite-dimensional complex matrix algebras with unital $*$-homomorphisms and tensor product, then $\Lambda=\{x:V_x\not\cong\mathbf1\}$ meets each bounded set in finitely many points.
In these cases the formula reduces to
$$
V(B)\cong\bigotimes_{x\in B\cap\Lambda}V_x,
$$
with direct sum in the Hilbert-space case.
Conversely, any such locally finite point assignment gives a local controlled object.
```

## Proof

For a finite subset $F$, repeated application of the locality isomorphism gives $V(F)\cong\bigotimes_{x\in F}V_x$.
Associativity makes this independent of parenthesization, and symmetry makes it independent of an ordering of $F$.
Naturality of the tensor-extension maps makes these isomorphisms compatible with inclusions of finite subsets.
The directed union of all finite subsets of $B$ is $B$; the continuity axiom now proves the colimit formula.

For finite-dimensional Hilbert spaces, the mutually orthogonal nonzero subspaces $V_x$ for $x\in B$ lie in the finite-dimensional space $V(B)$.
There can therefore be only finitely many of them.
For a matrix net write $V_x=M_{q_x}(\C)$.
For every finite $F\subseteq B$, the tensor product $\bigotimes_{x\in F}M_{q_x}(\C)$ embeds into $V(B)$.
If there were arbitrarily many points with $q_x\geq2$, its dimension would be unbounded, contradicting finite dimensionality of $V(B)$.
Thus $B\cap\Lambda$ is finite.

Conversely, a locally finite point assignment gives finite tensor products on bounded subsets.
Inclusions insert the unique unit maps, and disjoint unions give the locality isomorphisms.
For a nonempty directed cover of $B$, one member contains the finite set $B\cap\Lambda$, so the colimit axiom holds.
For the empty cover of the empty set, the colimit is the initial unit, which is also the empty tensor product.

## Why the qualification matters

For arbitrary Hilbert spaces the same point-object formula holds, but support need not be locally finite.
Take an infinite bounded set $X$ and $V(B)=\ell^2(B)$.
This is local for direct sum and is continuous under directed unions in the category of Hilbert spaces and isometries, yet every point of $X$ has nonzero fiber.
Thus the pointwise description is general; local finiteness follows from the finite-dimensional coefficient condition.

## Related articles

See {ref}`Quantum spin system <article-spin-system>` and {ref}`Geometric module <article-geometric-module>` for the two principal cases.
