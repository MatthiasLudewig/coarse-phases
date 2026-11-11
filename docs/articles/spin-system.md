(article-spin-system)=
(article-local-net)=
# Quantum spin system

A quantum spin system on a {prf:ref}`coarse space <def-bornological-coarse-space>` is a {prf:ref}`local controlled object <def-local-controlled-object>` valued in matrix algebras.
They are relevant for {ref}`quantum cellular automata <article-quantum-cellular-automaton>` and {ref}`gapped phases <article-gapped-phase>`.

## Definition

Let $(X, \mathcal{C}, \mathcal{B})$ be a bornological coarse space.
A quantum spin system is a {prf:ref}`local controlled object <def-local-controlled-object>` valued in the symmetric monoidal category of matrix algebras.
Spelling out the details leads to the following definition.

```{prf:definition} Quantum spin system
:nonumber:
:label: def-quantum-spin-system

A *quantum spin system* $\mathcal{A}$ on $X$ consists of a $C^*$-algebra $\mathcal{A}_X$ over $X$ together with an assignment of $C^*$-subalgebras $\mathcal{A}_Y$ for each subset $Y \subseteq X$ such that the following holds:

1. If $Y_1 \subseteq Y_2$, then $\mathcal{A}_{Y_1} \subseteq \mathcal{A}_{Y_2}$;
2. For disjoint subsets $Y,Y'$, the subalgebras $\mathcal{A}_Y$ and $\mathcal{A}_{Y'}$ commute;
3. Whenever $(Y_i)_{i \in I}$ is a collection of disjoint subsets with union $Y$, then linear combinations of finite products of elements in the subalgebras $\mathcal{A}_{Y_i}$ form a dense subset of $\mathcal{A}_Y$.
4. If $B \subseteq X$ is bounded, then $\mathcal{A}_B$ is isomorphic to a full matrix algebra.

The union $\mathcal{A}_X^{\mathrm{alg}}$ of all subalgebras $\mathcal{A}_B$ for bounded subsets $B \subseteq X$ is called the *local algebra* of the spin system.
Its $C^*$-closure $\mathcal{A}_X$ is the *quasi-local algebra*.
```

In particular, whenever $Y, Y' \subseteq X$ are disjoint subsets, we have an isomorphism
$$
\mathcal{A}_Y \otimes \mathcal{A}_{Y'} \cong \mathcal{A}_{Y \sqcup Y'},
$$
given by multiplication in $\mathcal{A}_X$.


A function $q : X \to \mathbb{N}$ with locally finite support (meaning that each $B \subseteq X$ bounded contains only finitely many points $x$ with $q(x) \neq 1$) determines a spin system by setting
$$
\mathcal A_Y=\bigotimes_{x \in Y} M_{q_x}(\mathbb C).
$$
If $Y$ is bounded, only finitely many factors are not equal to $\mathbb{C}$, so the tensor product is finite.
Otherwise, the right-hand-side is to be understood as the $C^*$-algebraic infinite tensor product.
Every spin system is isomorphic to one of this form, as proved in {ref}`the point-object proposition <theorem-local-objects-points>`.

## Conditional expectations for subsets

Each matrix algebra has a unique normalized trace.
Their tensor product determines a tracial state $\tau_Y$ on $\mathcal A_Y$ for every subset $Y$.
Locality gives a canonical identification
$$
\mathcal A_X\cong\mathcal A_Y \otimes \mathcal A_{X\setminus Y}.
$$

```{prf:definition} Conditional expectation onto a subset
:nonumber:
:label: def-subset-conditional-expectation

The *conditional expectation onto $\mathcal A_Y$* is
$$
\mathbb E_Y = \mathrm{id}_{\mathcal A_Y}\otimes\tau_{X\setminus Y}:
\mathcal A_X\longrightarrow\mathcal A_Y.
$$
```

It is a unital completely positive contraction, fixes $\mathcal A_Y$, and satisfies $\mathbb E_Y(bac)=b\mathbb E_Y(a)c$ for $b,c\in\mathcal A_Y$.
Furthermore, $\mathbb E_Y\mathbb E_Z=\mathbb E_{Y\cap Z}$ and $\mathbb E_Y(\mathcal A_B)\subseteq\mathcal A_{B\cap Y}$.
All these statements follow first on finite tensor products by partial trace and then on the completion by continuity.

Write $\mathcal A_x^\circ=\ker\tau_x$ for $x\in X$, and set $\mathcal A_F^\circ=\bigotimes_{x\in F}\mathcal A_x^\circ$, with $\mathcal A_\varnothing^\circ=\mathbb C\mathbf1$.
Then
$$
\mathcal A_X^{\mathrm{alg}}
 =\bigoplus_{F\subseteq\Lambda,\ F\text{ finite}}\mathcal A_F^\circ.
$$
This is a direct sum of vector spaces, not a decomposition into subalgebras.
On its $F$-summand, $\mathbb E_Y$ is the identity if $F\subseteq Y$ and zero otherwise.
This exact-support decomposition is used in the proof that {ref}`controlled derivations are locally generated <theorem-controlled-derivations>`.
