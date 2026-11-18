(article-controlled-state)=
# Controlled states

```{warning}
Agent-generated, not reviewed yet
```

A controlled state has no correlations between observables supported sufficiently far apart.


## Definition

Let $\cA$ be a {prf:ref}`quantum spin system <def-quantum-spin-system>` on a {prf:ref}`bornological coarse space <def-bornological-coarse-space>` $(X,\cB,\cC)$.
Write $\cA_Y$ for its algebra of observables supported in $Y\subseteq X$.

```{prf:definition} Controlled state
:nonumber:
:label: def-controlled-state

Let $E$ be an entourage.
A {prf:ref}`state <def-state>` $\omega$ on $\cA_X$ is *$E$-controlled* if
$$
\omega(ab)=\omega(a)\omega(b)
$$
for every pair of subsets $Y,Z\subseteq X$ with $(Y\times Z)\cap E=\varnothing$ and all $a\in\cA_Y$, $b\in\cA_Z$.
It is *controlled* if it is $E$-controlled for some entourage $E\in\cC$.
```

Supposing that $E$ is a symmetric entourage, the condition $(Y\times Z)\cap E=\varnothing$ is equivalent to
$$
Y_E \cap Z = \emptyset, \qquad Y \cap Z_E = \emptyset,
$$
where we used the {ref}`fattening notation <def-fattening>`.
It is enough to test bounded supports, because local observables are norm dense in the corresponding subset algebras.
In other words, the sets $Y$ and $Z$ are required to be $E$-separated.

For a coarse structure obtained from a metric, choosing $E=\{(x,y):d(x,y)\leq R\}$ says that the factorization holds whenever every point of $Y$ is at distance greater than $R$ from every point of $Z$.

