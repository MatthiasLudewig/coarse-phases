(article-controlled-objects)=
# Controlled objects

Controlled objects provide a common language for geometric modules and local operator algebras.

Throughout, we fix a symmetric monoidal category $\widehat{C}$ together with a full symmetric monoidal subcategory $C$.
These are required to have the following properties:

1. $\widehat{C}$ admits all filtered colimits.
2. The tensor product functor preserves filtered colimits in each variable
3. The inclusion $C \hookrightarrow \widehat{C}$ preserves all filtered colimits already existing in $C$.
4. The tensor unit is an initial object of $\widehat{C}$.
5. If for a filtered diagram in $C$, all connecting morphisms are monomorphisms, then for each vertex of the diagram, the canonical map to the colimit is also a monomorphism.


## Controlled objects in a symmetric monoidal category

Let $(X, \mathcal{C}, \mathcal{B})$ be a bornological coarse space and let $C$ be a category.
We regard the bornology as a category under inclusion.

```{prf:definition} Controlled object
:nonumber:
:label: def-controlled-object

An *$X$-controlled object* in $C$ is a functor $V:\mathcal B\to C$ such that its structure morphisms are monomorphisms and which satisfies the following continuity property: for every directed subcollection $\mathcal{B}' \subseteq \mathcal{B}$ whose union $B = \bigcup \mathcal{B}'$ is bounded, the canonical map
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

The tensor product $V \otimes W$ of two $X$-controlled objects $V$ and $W$ is given by
$$
(V \otimes W)(B) = V(B) \otimes W(B).
$$

## Controlled morphisms

For any subset $Y\subseteq X$, we may define an object of $\widehat C$ by
$$
V(Y):=\operatorname*{colim}_{\substack{B\in\mathcal B\\B\subseteq Y}}V(B).
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
Since the map $W(B_E) \to W(X)$ is a monomorphism by the ambient-category assumption, $f_B$ is unique if it exists.
The same assumption implies that these local maps are natural under inclusions of bounded sets.

The identity morphism is always of propagation zero, hence in particular controlled.
If $f:V\to W$ is $E$-controlled and $g:W\to U$ is $F$-controlled, then $g\circ f$ is $(F\circ E)$-controlled: its local maps are $g_{B_E}\circ f_B$, and $(B_E)_F=B_{F\circ E}$.
This defines the *category of $X$-controlled objects in $C$*, denoted $\mathrm{Con}_C(X)$.
The global colimit objects depend on $\widehat C$, but the presentation description below identifies the controlled-morphism categories for ambient categories satisfying our assumptions.

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

Given objects $V_x$ of $C$ for each $x\in X$, consider the formula
$$
V(B)=\operatorname*{colim}_{F\subseteq B,\ F\text{ finite}}
                       \bigotimes_{x\in F}V_x.
$$
The transition maps insert the unique maps from the unit.
This gives a local controlled object provided the colimits exist in $C$, tensor products preserve them in each variable, and the induced maps $V(B)\to V(B')$ for $B\subseteq B'$ are monomorphisms.
Conversely, every local controlled object has the displayed point-object description; see the proof of {ref}`Local objects are determined by their point objects <theorem-local-objects-points>`.
