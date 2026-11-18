(article-gapped-ground-state)=
# Gapped ground state

```{warning}
Agent-generated, not reviewed yet
```

A gapped ground state strengthens the {prf:ref}`algebraic ground-state inequality <def-ground-state-derivation>` by a positive lower bound on the energy of centered observables.
When the derivation generates dynamics, the condition used here expresses both a spectral gap and nondegeneracy of the ground space in the state's GNS representation.

## Definition

Let $A$ be a unital $C^*$-algebra and let $D$ be a {prf:ref}`derivation <def-derivation>` on $A$.

```{prf:definition} Nondegenerate gapped ground state
:nonumber:
:label: def-gapped-ground-state

A {prf:ref}`state <def-state>` $\omega$ is a *(nondegenerate) gapped ground state with gap at least $\gamma>0$* for $D$ if
$$
-i\omega(a^*D(a))\geq\gamma\bigl(\omega(a^*a)-|\omega(a)|^2\bigr)
\qquad(a\in\dom(D)).
$$
```

The right-hand side is nonnegative by the Cauchy–Schwarz inequality, so this condition implies the ground-state condition.
The gapped ground state condition is equivalent to the condition
$$
-i\omega(a^*D(a))\geq\gamma\omega(a^*a)
\qquad\text{whenever }a\in\dom(D)\text{ and }\omega(a)=0.
$$

## Implementing Hamiltonian

Let $\omega$ be a gapped ground state for a derivation $D$ on a $C^*$-algebra $A$ and assume that $D$ generates a strongly continuous group of $*$-automorphisms of $A$.
As explained {ref}`here <article-ground-state-energy-of-hamiltonian>`, $D$ is implemented in the {prf:ref}`GNS-representation <def-gns-representation>` $(\cH, \pi, \Omega)$ of $\omega$ by a positive self-adjoint operator $H$ annihilating the vacuum vector.

```{prf:theorem} Nondegenerate gap and the GNS Hamiltonian
:nonumber:
:label: thm-gapped-ground-state-hamiltonian

If $\omega$ has gap at least $\gamma$, then the implementing Hamiltonian $H$ for $D$ satisfies
$$
\ker H =\C\Omega,
\qquad
\spec(H) \subseteq \{0\} \cup [\gamma, \infty).
$$
```

(gapped-ground-state-purity)=
## Purity and degeneracy

If $D$ generates a strongly continuous semigroup of $*$-automorphisms, then any gapped ground state for $D$ is necessarily pure, see {ref}`here <theorem-nondegenerate-ground-state-pure>`.
The {ref}`weighted ferromagnetic counterexample <theorem-mixed-gapped-ground-state>` shows that without this assumption on $D$, a gapped ground state for $D$ need not be pure, even for {prf:ref}`spin systems <def-quantum-spin-system>`.

Purity also does not ensure uniqueness of dynamics extending an algebraic derivation.
The {ref}`pure spin-chain counterexample <theorem-pure-gapped-ground-state-nonunique-dynamics>` has two distinct generating extensions of the same controlled derivation on the full local algebra, with the same pure gapped ground state for both.
