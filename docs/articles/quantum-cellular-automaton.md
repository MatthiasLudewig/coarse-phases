(article-quantum-cellular-automaton)=
# Quantum cellular automaton

```{warning}
Agent-generated, not reviewed yet
```

A quantum cellular automaton is an automorphism of a spin system which moves local observables only a controlled distance.

## Controlled automorphisms of local nets

Let $(X, \cB, \cC)$ be a bornological coarse space.

```{prf:definition} Quantum cellular automaton
:nonumber:
:label: def-qca

Let $\cA$ be a local matrix net on $X$.
A *quantum cellular automaton* (QCA) is a controlled $*$-automorphism $\alpha$ of $\cA_X$.
Explicitly, there exists an entourage $E$ such that for each bounded set $B \subseteq X$, we have
$$
\alpha(\cA_B) \subseteq \cA_{B_E}.
$$
```

If $\alpha$ is a QCA, then also the inverse automorphism $\alpha^{-1}$ is controlled, hence a QCA.
