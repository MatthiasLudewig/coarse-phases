(article-pure-state)=
# Pure state

A pure state is a {ref}`state <article-state>` that cannot be expressed as a convex combination of other states.

## Definition

Let $A$ be a nonzero complex $C^*$-algebra, which need not be unital, and let $S(A)$ be its {prf:ref}`state space <def-state-space>`.

```{prf:definition} Pure state
:nonumber:
:label: def-pure-state

A state $\omega$ is *pure* if whenever 
$$
\omega=t\varphi+(1-t)\psi,
$$
for $t \in [0, 1]$ and states $\varphi, \psi \in S(A)$, we have $\varphi=\psi=\omega$.

The space of pure states, with its weak-* subspace topology, is denoted by $P(A)$.
```

Recall that an *extreme point* of a convex set is a point that lies in no nontrivial open line segment in that set.
Consequently, the pure states are exactly the extreme points of $S(A)$.
For unital $A$, the Krein–Milman theorem says that every state is a weak-* limit of finite convex combinations of pure states.
The pure-state space itself need not be closed or compact.

## Examples

For $A=\Mat_n(\C)$, a state $\omega(a)=\Tr(\rho a)$ is pure precisely when its density matrix $\rho$ is a rank-one projection.
In that case $\omega(a)=\langle\xi,a\xi\rangle$ for a unit vector $\xi$.
Thus $P(\Mat_n(\C))$ is complex projective space $\C P^{n-1}$.
For $A=C(K)$ with $K$ compact Hausdorff, the pure states are point evaluations, corresponding to point-mass probability measures.

## Purity and the GNS representation

```{prf:theorem} Purity and irreducibility
:nonumber:
:label: thm-pure-state-gns

A state $\omega$ on a $C^*$-algebra $A$ is pure if and only if its {prf:ref}`GNS representation <def-gns-representation>` is irreducible.
```

If $(\cH, \omega, \Omega)$ is the GNS representation, the theorem states equivalently that the commutant of $\pi(A)$ in $\mathbf{B}(\cH)$ is trivial, 
$$
\pi(A)'=\C1.
$$

````{dropdown} Proof
:class-container: proof-dropdown

```{prf:proof}
Write $(\cH,\pi,\Omega)$ for the GNS triple.
Every positive functional $\varphi\leq\omega$ determines a unique positive contraction $T\in\pi(A)'$ with
$$
\varphi(a)=\langle\Omega,T\pi(a)\Omega\rangle.
$$
Indeed, the form $([a],[b])\mapsto\varphi(a^*b)$ is positive and bounded by the GNS inner product, so it is represented by a positive contraction $T$.
The identity $\varphi(a^*cb)=\varphi((c^*a)^*b)$ shows that $T$ commutes with $\pi(c)$.
The formula and uniqueness follow by cyclicity, using the unitization when necessary.

If $\pi(A)'=\C1$, this correspondence makes every positive $\varphi\leq\omega$ a scalar multiple of $\omega$.
Apply this to $t\varphi\leq\omega$ in a convex decomposition to obtain purity.

Conversely, if $\pi(A)'\neq\C1$, its spectral projections include a projection $P$ different from $0$ and $1$.
Cyclicity implies $0<\|P\Omega\|^2<1$.
The vectors $P\Omega$ and $(1-P)\Omega$ give a convex decomposition of $\omega$ into two states.
It is nontrivial, since otherwise uniqueness of the representing contraction would force $P=\|P\Omega\|^2 1$.
Thus $\omega$ is not pure.
```
````

(pure-state-products)=
## Products and pure restrictions

If $\omega$ and $\nu$ are states on $C^*$-algebras $A$ and $B$, then $\omega \otimes \nu$ are states on the spatial tensor product of $A$ and $B$. 

```{prf:theorem} Purity of product states
:nonumber:
:label: thm-product-state-purity

Let $\omega$ and $\nu$ be states on $C^*$-algebras $A$ and $B$.
The product state $\omega\otimes\nu$ on the spatial tensor product $A\otimes B$ is pure if and only if both factors are pure.
```

````{dropdown} Proof
:class-container: proof-dropdown

```{prf:proof}
In one direction, a nontrivial convex decomposition of either factor gives one of the product.
The other direction follows from the {prf:ref}`GNS characterization <thm-pure-state-gns>`, as the tensor product of two irreducible representations is irreducible.
```
````

```{prf:theorem} Factorization from a pure restriction
:nonumber:
:label: thm-pure-restriction-factorization

Let $A$ and $B$ be unital $C^*$-algebras, and let $\rho$ be a state on their spatial tensor product $A\otimes B$ whose restriction to $A\otimes1$ is pure.
Then $\rho$ factorizes as
$$
\rho=\rho|_A\otimes\rho|_B.
$$
If $\rho$ itself is pure, its restriction to $1\otimes B$ is pure as well.
```

````{dropdown} Proof
:class-container: proof-dropdown

```{prf:proof}
For $b\geq0$ the functional $a\mapsto\rho(a\otimes b)$ is positive and bounded above by $\|b\|\rho|_A$.
Purity makes it a scalar multiple of $\rho|_A$, and evaluating at $1$ identifies that scalar as $\rho(1\otimes b)$.
Linearity and continuity give the assertion for all $b$.
If $\rho$ is pure, the {prf:ref}`product-state criterion <thm-product-state-purity>` implies that $\rho|_B$ is pure.
```
````

This is useful for {prf:ref}`pure factor states <def-pure-factor-state>` of spin systems.

## Automorphisms and pure states

An automorphism acts on the space of states by pullback and preserves purity.
We use the left action $\alpha\cdot\omega=\omega\circ\alpha^{-1}$ and the point-norm topology on $\Aut(A)$.
For separable simple $C^*$-algebras, this action is transitive by [Kishimoto–Ozawa–Sakai, Theorem 1.1](https://arxiv.org/abs/math/0110152).
The automorphism can even be chosen asymptotically inner, with its implementing unitary path starting at the identity.
These are automorphisms of the entire algebra; they are not required to respect supports in a spin system.

For unital separable simple $A$, the weak-* pure-state space is homeomorphic to the homogeneous space $\Aut(A)/\Aut_\omega(A)$, where $\Aut_\omega(A)$ fixes $\omega$,
$$
P(A) \approx \Aut(A)/\Aut_\omega(A).
$$
The {ref}`standalone theorem page <theorem-pure-state-homogeneous-space>` gives the precise statements and proves the topological quotient assertion using an open mapping theorem.