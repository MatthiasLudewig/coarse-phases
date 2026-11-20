(article-quantum-cellular-automaton)=
# Quantum cellular automaton

A quantum cellular automaton is an automorphism of a spin system which moves local observables only a controlled distance.

## Definition

Let $(X, \cB, \cC)$ be a bornological coarse space and let $\cA$ be a spin system on $X$.

```{prf:definition} Quantum cellular automaton
:nonumber:
:label: def-qca

A *quantum cellular automaton* (QCA) is a controlled $*$-automorphism $\alpha$ of $\cA_X$.
Explicitly, there exists an entourage $E$ such that for each bounded set $B \subseteq X$, we have
$$
\alpha(\cA_B) \subseteq \cA_{B_E}.
$$
```

If $\alpha$ is a QCA, then also the inverse automorphism $\alpha^{-1}$ is controlled, hence a QCA.

## Quantum circuits and coarsely local automorphisms

Typically, some QCA, called *quantum circuits*, are considered to be trivial.
As above, let $(X, \cB, \cC)$ be a bornological coarse space and let $\cA$ be a spin system on $X$.

```{prf:definition} Partitioned unitary
:nonumber:
:label: def-partitioned-unitary

Let $(B_i)_{i \in I}$ be a {prf:ref}`uniformly bounded <def-uniformly-bounded-collection>` and pairwise disjoint collection of subsets of $X$.
A *partitioned unitary* subordinate to this collection is a collection $(u_i)_{i \in I}$ of unitaries $u_i \in \cA_{B_i}$.
```

A partitioned unitary as above gives rise to a QCA $\beta$ by setting
$$
\beta(a) := \left(\prod_{\substack{i \in I}{B_i \cap B}} u_i\right) a \left(\prod_{\substack{i \in I}{B_i \cap B}}u_i^*\right), \qquad a \in \cA_B.
$$

```{prf:definition} Quantum circuit
:nonumber:
:label: def-quantum-circuit

A *finite depth quantum circuit* is a QCA that is a composition of finitely many QCA given by partitioned unitaries.
```
