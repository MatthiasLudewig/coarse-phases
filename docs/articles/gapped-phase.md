(article-gapped-phase)=
# Gapped phases

A controlled gapped phase is a pair of a derivation on the global algebra of a spin system and a gapped ground state for the derivation.
The control condition in this article is imposed on the derivation, not on the state.

## Controlled gapped phases

Let $(X, \cB, \cC)$ be a {prf:ref}`bornological coarse space <def-bornological-coarse-space>` and let $\cA$ be a spin system over $X$.

```{prf:definition} Controlled gapped phase
:nonumber:
:label: def-controlled-gapped-phase

A *controlled gapped phase* on $\cA$ is a pair $(D,\omega)$ consisting of a {prf:ref}`controlled derivation <def-controlled-derivation>` $D$ and a {prf:ref}`gapped ground state <def-gapped-ground-state>` $\omega$ for $D$.
```


## Pure factor states and pointed systems

```{prf:definition} Pure factor state
:nonumber:
:label: def-pure-factor-state

A *pure factor state* on $\cA$ is a state $\omega_0$ whose restriction to $\cA_B$ is pure for every bounded $B\subseteq X$.
```

Equivalently, in the pointwise tensor-product description of a spin system, it is a product $\omega_0=\bigotimes_{x\in X}\omega_x$ of pure on-site states.
Indeed, the restriction to each point is pure, and {ref}`factorization over a pure restriction <pure-state-products>` forces product factorization on each finite tensor product.
Locality and norm density then determine the state on the whole algebra.
Conversely, a bounded subset contains only finitely many nontrivial matrix factors, so a product of pure on-site states restricts to a pure state there.

Every pure factor state is globally pure.
In a convex decomposition of $\omega_0$, purity of its bounded restrictions forces both summands to agree with $\omega_0$ on the dense local algebra.
It also factorizes over arbitrary disjoint subsets and is therefore $\Delta_X$-controlled.
The term *pure factor state* here means a pure product state relative to the spin-system decomposition.
It should not be confused with the more general operator-algebraic use of *factor state* for a state whose GNS von Neumann algebra has trivial center.

```{prf:definition} Pointed spin system
:nonumber:
:label: def-pointed-spin-system

A *pointed spin system*, also called a *pointed local matrix net*, is a pair $(\cA,\omega_0)$ consisting of a spin system and a chosen pure factor state.
A unital morphism $\varphi:(\cA,\omega_0)\to(\cB,\nu_0)$ is *pointed* if $\nu_0\circ\varphi=\omega_0$.
It has *propagation zero* if $\varphi(\cA_Y)\subseteq\cB_Y$ for every $Y\subseteq X$.
```

### A trivial gapped representative

Let $p_x\in\cA_x$ be the rank-one projection representing $\omega_x$, and put $h_x=1-p_x$.
For a scalar site $\cA_x=\C$, this means $p_x=1$ and $h_x=0$.
Define
$$
D_0(a)=i\sum_{x\in X}[h_x,a],\qquad a\in\cA_X^{\mathrm{alg}}.
$$
Only finitely many terms act nontrivially on any local observable.
Thus $D_0$ is a well-defined derivation of propagation zero.
The pair $(D_0,\omega_0)$ is called the *trivial gapped representative* of the pointed system.

To check its gap, let $a\in\cA_B$ for $B$ bounded and write $\Omega_B$ for the product ground vector.
On the finite tensor product for $B$, the operator $H_B=\sum_{x\in B}h_x$ annihilates $\Omega_B$ and is at least one on its orthogonal complement.
Consequently,
$$
-i\omega_0(a^*D_0(a))
=\langle a\Omega_B,H_Ba\Omega_B\rangle
\geq\omega_0(a^*a)-|\omega_0(a)|^2.
$$
The gap is therefore at least one, uniformly in $B$.
The sum of on-site terms is essential for compatibility under inclusion of bounded subsets: the alternative expressions $i[1-p_B,a]$ with $p_B=\bigotimes_{x\in B}p_x$ do not generally agree when $B$ is enlarged.
