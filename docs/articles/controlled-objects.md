(article-controlled-objects)=
# Controlled objects

Controlled objects provide a common language for geometric modules and local operator algebras.

Throughout, we fix a category $C$.


## Controlled objects in a symmetric monoidal category

Let $(X, \mathcal{B}, \mathcal{C})$ be a {prf:ref}`bornological coarse space <def-bornological-coarse-space>` and let $C$ be a category.
We regard the bornology as a category under inclusion.

```{prf:definition} Controlled object
:nonumber:
:label: def-controlled-object

An *$X$-controlled object* in $C$ is a functor $V:\mathcal{B}\to C$ such that its structure morphisms are monomorphisms and which satisfies the following continuity property: for every directed subcollection $\mathcal{B}' \subseteq \mathcal{B}$ whose union $B = \bigcup \mathcal{B}'$ is bounded, the canonical map
$$
\operatorname*{colim}_{B' \in \mathcal{B}'}V(B')\longrightarrow V(B)
$$
is an isomorphism.
In particular, we require these colimits to exist in $C$.
```

Here a *directed subcollection* is a possibly empty subset $\mathcal{B}' \subseteq \mathcal{B}$ such that, for any $B_1,B_2\in\mathcal{B}'$, some $D\in\mathcal{B}'$ contains $B_1\cup B_2$.
In particular, taking $\mathcal{B}'$ to be the empty cover of the empty set, we obtain that $V(\emptyset)$ is an initial object of $C$.
So having an initial object is a necessary requirement for controlled objects valued in $C$ to exist.

This condition is weaker than the cosheaf condition for the Grothendieck topology whose covers are jointly surjective families of inclusions of bounded sets.
For disjoint bounded $B_1, B_2$, that cosheaf condition would require $V(B_1\sqcup B_2)$ to be the coproduct of $V(B_1)$ and $V(B_2)$ in $C$, which is usually not satisfied by the relevant examples if $C$ is not an abelian category.
The relaxation present in the {prf:ref}`definition above <def-controlled-object>` is akin to that used for factorization algebras, which are required to satisfy the cosheaf condition for Weiss covers.

If $C$ has a monoidal structure, we may define the tensor product $V \otimes W$ of two $X$-controlled objects $V$ and $W$ by
$$
(V \otimes W)(B) = V(B) \otimes W(B).
$$

## Controlled morphisms

The notion of controlled morphism depends on the choice of a larger category $\widehat{C}$ containing $C$ as a full subcategory.
We assume that $\widehat{C}$ is closed under filtered colimits and that the inclusion $C \hookrightarrow \widehat{C}$ preserves filtered colimits that already exist in $C$.
Then for any subset $Y\subseteq X$, we may define an object of $\widehat C$ by
$$
V(Y):=\operatorname*{colim}_{\substack{B\in\mathcal{B}\\B\subseteq Y}}V(B).
$$


````{prf:definition} Controlled morphism
:nonumber:
:label: def-controlled-morphism

Let $V$ and $W$ be $X$-controlled objects in $C$.
For an entourage $E$, an *$E$-controlled morphism* $V \to W$ is a morphism $f:V(X)\to W(X)$ in $\widehat C$ such that for each bounded $B\subseteq X$ there is a morphism $f_B:V(B)\to W(B_E)$ in $C$ making the diagram

```{tikz}
:libs: cd
:alt: The local map f_B from V(B) to W(B_E) agrees with f after the canonical maps to V(X) and W(X).

\begin{tikzcd}
V(B) \arrow[r, "f_B", dashed] \arrow[d]
  & W(B_E) \arrow[d] \\
V(X) \arrow[r, "f"'] & W(X)
\end{tikzcd}
```

commute.
A *controlled morphism* is a morphism that is $E$-controlled for some entourage $E$.

A morphism is called *of propagation zero* if it is controlled by the diagonal $\Delta \subseteq X \times X$.
````

Here $B_E$ denotes the {ref}`fattening <def-fattening>` of $B$, which is bounded by compatibility of the bornology and coarse structure.

The identity morphism is always of propagation zero, hence in particular controlled.
If $f:V\to W$ is $E$-controlled and $g:W\to U$ is $F$-controlled, then $g\circ f$ is $(F\circ E)$-controlled: its local maps are $g_{B_E}\circ f_B$, and $(B_E)_F=B_{F\circ E}$.
This defines the *category of $X$-controlled objects in $C$*, denoted $\mathrm{Con}_C(X)$.
The dependence on the category $\widehat{C}$ will usually be suppressed.

## Local and semilocal objects

````{prf:definition} Local controlled object
:nonumber:
:label: def-local-controlled-object

A *semilocal object* is a controlled object with tensor-extension maps
$$
\tau_{B, B'}:V(B)\otimes V(B')\longrightarrow V(B \sqcup B')
$$
for disjoint bounded $B,B'$ for which the maps
$$
V(B) \cong V(B) \otimes \mathbf{1} \to V(B) \otimes V(B') \xrightarrow{\tau_{B, B'}} V(B \sqcup B'),
\qquad
V(B') \cong \mathbf{1} \otimes V(B') \to V(B) \otimes V(B') \xrightarrow{\tau_{B, B'}} V(B \sqcup B'),
$$
are the canonical structure maps of $V$.
Moreover, they are also required to satisfy obvious compatibility conditions with respect to unitors, associators and the symmetry of the tensor product.

The object is *local* if all $\tau_{B,B'}$ are isomorphisms.
````

The full subcategory of $\mathrm{Con}_C(X)$ consisting of local objects is denoted by $\mathrm{Loc}_C(X)$.


Given objects $V_x$ of $C$ for each $x\in X$, consider the formula
$$
V(B)=\operatorname*{colim}_{F\subseteq B,\ F\text{ finite}}
                       \bigotimes_{x\in F}V_x.
$$
The transition maps insert the unique maps from the unit.
This gives a local controlled object provided the colimits exist in $C$, tensor products preserve them in each variable, and the induced maps $V(B)\to V(B')$ for $B\subseteq B'$ are monomorphisms.
Conversely, every local controlled object has the displayed point-object description; see the proof of {ref}`Local objects are determined by their point objects <theorem-local-objects-points>`.

## Examples

1. Taking $C$ to be the category of separable Hilbert spaces with morphisms isometric embeddings and monoidal structure direct sum, local $X$-controlled objects in $C$ are precisely {prf:ref}`geometric modules <def-geometric-module>`.
Tensor-extension maps are unique in this case.
The category $\widehat{C}$ can be taken to be the category of all Hilbert spaces.
Notice, however, that the category $\mathrm{Hilb}(X)$ described in the article {ref}`geometric module <article-geometric-module>` has more morphisms than $\mathrm{Loc}_C(X)$: It contains arbitrary controlled operators, while $\mathrm{Loc}_C(X)$ only contains isometric embeddings.

2. Taking $C$ to be the category of matrix algebras over $\mathbb{C}$ with $*$-homomorphisms and $\widehat{C}$ the category of all $C^*$-algebras, one obtains the notion of a {prf:ref}`quantum spin system <def-quantum-spin-system>`.
