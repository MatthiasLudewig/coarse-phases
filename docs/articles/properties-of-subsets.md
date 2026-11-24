(article-properties-of-subsets)=
(article-collections-of-bounded-subsets)=
# Properties of subsets

Let $(X, \cB, \cC)$ be a {prf:ref}`bornological coarse space <def-bornological-coarse-space>`.

(def-uniformly-dense)=
```{prf:definition} Coarsely dense
:nonumber:
:label: def-coarsely-dense

A subset $Y \subseteq X$ is *coarsely dense* if there exists an entourage $E$ such that $Y_E = X$.
```

Here $Y_E$ denotes the {ref}`fattening <def-fattening>` of $Y$ by $E$.

```{prf:definition} Locally finite subset
:nonumber:
:label: def-locally-finite-subset

A subset $Y \subseteq X$ is *locally finite* if $Y \cap B$ is finite for each bounded set $B \subseteq X$.
```

```{prf:definition} Uniformly locally finite subset
:nonumber:
:label: def-uniformly-locally-finite-subset

A subset $Y \subseteq X$ is *uniformly locally finite* if for each entourage $E$, there exists a number $n$ such that for all subsets $B \subseteq X$ with $B \times B \subseteq E$, we have
$$
\#(B \cap Y) \leq n.
$$
```

```{prf:definition} Bounded geometry
:nonumber:
:label: def-bounded-geometry

$X$ is said to have *bounded geometry* if it admits a {prf:ref}`coarsely dense <def-coarsely-dense>` and {prf:ref}`uniformly locally finite <def-uniformly-locally-finite-subset>` subset $Y \subseteq X$.
```

```{prf:definition} $E$-separated
:nonumber:
:label: def-E-separated

For an entourage $E$, a subset $Y \subseteq X$ is *$E$-separated* if, whenever $x, y \in Y$ with $x \neq y$, we have $(x, y) \notin E$.
```

```{prf:definition} Uniformly bounded collections
:nonumber:
:label: def-uniformly-bounded-collection

A collection $(B_i)_{i \in I}$ of bounded subsets of $X$ is called *uniformly bounded* if $\bigcup_{i \in I} (B_i \times B_i)$ is an entourage.
```

```{prf:definition} Locally finite collections
:nonumber:
:label: def-locally-finite-collection

A collection $(B_i)_{i \in I}$ of bounded subsets of $X$ is called *locally finite* if for any bounded set $B \subseteq X$, we have $B \cap B_i = \emptyset$ for all but finitely many indices $i \in I$.
```
