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

Let $(B_i)_{i \in I}$ be a {prf:ref}`uniformly bounded <def-uniformly-bounded-collection>`, {prf:ref}`locally finite <def-locally-finite-collection>` and pairwise disjoint collection of subsets of $X$.
A *partitioned unitary* subordinate to this collection is a collection $(u_i)_{i \in I}$ of unitaries $u_i \in \cA_{B_i}$.
```

A partitioned unitary as above gives rise to a QCA $\beta$ by setting
$$
\beta(a) := \left(\prod_{\substack{i \in I \\ B_i \cap B \neq \emptyset}} u_i\right) a \left(\prod_{\substack{i \in I \\ B_i \cap B \neq \emptyset}}u_i^*\right), \qquad a \in \cA_B.
$$
Here each product is finite by local finiteness of the supporting collection $(B_i)_{i \in I}$.

```{prf:definition} Quantum circuit
:nonumber:
:label: def-quantum-circuit

A *(finite depth) quantum circuit* is a QCA that is a composition of finitely many QCA given by partitioned unitaries.
```

It was noticed in [Ludewig, Remark 2.41(2)](https://arxiv.org/abs/2603.10501) ({ref}`bibliographic details <bib-qca>`) that finite depth quantum circuits do not give a coarsely invariant notion, as images of pairwise disjoint collections of subsets may no longer be pairwise disjoint, and it may not even be possible to divide them into finitely many subcollections each of which is pairwise disjoint.
The following notion slightly generalizes that of a quantum circuit while being coarsely invariant.

```{prf:definition} Coarsely local automorphism
:nonumber:
:label: def-coarsely-local-automorphism

An automorphism $\alpha$ of $\cA_X$ is *elementary coarsely local* if there exists a collection $(\cA^{(i)})_{i \in I}$ of pairwise commuting subalgebras generating $\cA_X$ such that $\alpha$ preserves each $\cA^{(i)}$ and such that $\cA^{(i)} \subseteq \cA_{B_i}$ for some {prf:ref}`uniformly bounded <def-uniformly-bounded-collection>` and {prf:ref}`locally finite <def-locally-finite-collection>` collection $(B_i)_{i \in I}$ of subsets of $X$.
An automorphism is *coarsely local* if it is a finite product of elementary coarsely local automorphisms.
```

Coarsely local automorphisms form a normal subgroup of the group of controlled automorphisms; see [Ludewig, Lemma 2.32](https://arxiv.org/abs/2603.10501) ({ref}`bibliographic details <bib-qca>`).
