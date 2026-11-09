(article-controlled-objects)=
# Controlled objects

```{warning}
Agent-generated, not reviewed yet
```

Controlled objects provide a common language for geometric modules and local operator algebras.

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
For disjoint bounded $B_1,B_2$, that cosheaf condition would require $V(B_1\sqcup B_2)$ to be the coproduct of $V(B_1)$ and $V(B_2)$ in $C$.
For example, a local matrix net on two sites with point algebras $M_2(\mathbb C)$ assigns $M_2(\mathbb C)\otimes M_2(\mathbb C)$ to their union.
This is not a coproduct: the two identity maps to $M_2(\mathbb C)$ agree on the scalars but do not extend to the tensor product, since their images do not commute.
In the category of unital $C^*$-algebras, the coproduct is instead the unital free product.
Thus tensor factorization does not imply ordinary cosheaf gluing.


## Controlled morphisms

To define morphisms between controlled objects, choose a category $\widehat C$ containing $C$ as a full subcategory and admitting all small filtered colimits.
We also require that for a directed diagram of monomorphisms in $C$, each canonical map from a diagram object to its colimit in $\widehat C$ is a monomorphism in $\widehat C$.
Existence of filtered colimits alone does not imply this additional condition.

For any subset $Y\subseteq X$, define an object of $\widehat C$ by
$$
V(Y):=\operatorname*{colim}_{\substack{B\in\mathcal B\\B\subseteq Y}}V(B).
$$
The indexing set is nonempty and directed.
If $Y$ is bounded, it has terminal object $Y$, so this agrees canonically with the original $V(Y)$.
Write $j_B^V:V(B)\to V(X)$ for the canonical maps.
The continuity axiom for bounded unions above is imposed in $C$; we do not assume that the inclusion $C\hookrightarrow\widehat C$ preserves those colimits.


````{prf:definition} Controlled morphism
:nonumber:
:label: def-controlled-morphism

Let $V$ and $W$ be $X$-controlled objects in $C$.
For an entourage $E$, an *$E$-controlled morphism* $V \to W$ is a morphism $f:V(X)\to W(X)$ in $\widehat C$ such that for each bounded $B\subseteq X$ there is a morphism $f_B:V(B)\to W(B_E)$ in $C$ making the diagram

```{tikz}
:libs: cd
:alt: The local map f_B from V(B) to W(B_E) agrees with f after the canonical maps to V(X) and W(X).

\begin{tikzcd}
V(B) \arrow[r, "f_B", dashed] \arrow[d, "j_B^V"']
  & W(B_E) \arrow[d, "j_{B_E}^W"] \\
V(X) \arrow[r, "f"'] & W(X)
\end{tikzcd}
```

commute.
A *controlled morphism* is a morphism that is $E$-controlled for some entourage $E$.

A morphism is called *of propagation zero* if it is controlled by $\Delta_X$.
````

Here $B_E$ denotes the {ref}`fattening <def-fattening>` of $B$, which is bounded by compatibility of the bornology and coarse structure.
Since $j_{B_E}^W$ is a monomorphism by the ambient-category assumption, $f_B$ is unique if it exists.
The same assumption implies that these local maps are natural under inclusions of bounded sets.
The identity morphism is always of propagation zero, hence in particular controlled.

If $f:V\to W$ is $E$-controlled and $g:W\to U$ is $F$-controlled, then $g\circ f$ is $(F\circ E)$-controlled: its local maps are $g_{B_E}\circ f_B$, and $(B_E)_F=B_{F\circ E}$.
This defines the *category of $X$-controlled objects in $C$*, denoted $\mathrm{Con}_C(X)$.
The global colimit objects depend on $\widehat C$, but the presentation description below identifies the controlled-morphism categories for ambient categories satisfying our assumptions.

For an essentially small category $C$, a universal choice is its *$\mathrm{Ind}$-completion*, $\widehat C=\mathrm{Ind}(C)$.
It is the full subcategory of set-valued presheaves on a small skeleton of $C$ consisting of small filtered colimits of representable presheaves.
The inclusion of $C$ is the Yoneda embedding.
It satisfies the monomorphism condition above: the Yoneda embedding sends monomorphisms to pointwise injections, and filtered colimits of presheaves are computed pointwise.

In this case, controlled morphisms can be described entirely in terms of $C$.
A *presentation* consists of an entourage $E$ and maps $f_B:V(B)\to W(B_E)$ compatible with inclusions, meaning that

```{tikz}
:libs: cd
:alt: The local maps f_B and f_B' commute with the structure maps for an inclusion B contained in B'.

\begin{tikzcd}
V(B) \arrow[d] \arrow[r, "f_B"] & W(B_E) \arrow[d] \\
V(B') \arrow[r, "f_{B'}"'] & W(B'_E)
\end{tikzcd}
```

commutes whenever $B\subseteq B'$.
These maps induce a morphism of global colimits.
Conversely, the local maps of a controlled global morphism give such a presentation.
Two presentations define the same controlled morphism if their maps agree after passage to $W(B_F)$ for a common larger entourage $F$.
Indeed, equality in $W(X)$ can be checked in $W(B_F)$ because its canonical map to $W(X)$ is monomorphic.
Thus controlled morphisms are equivalence classes of presentations.
This argument also applies to any other ambient category satisfying the assumptions above.

For Hilbert spaces, a formal colimit in $\mathrm{Ind}(C)$ should not be identified with a completed Hilbert space carrying arbitrary bounded operators.
The {ref}`geometric-module convention <article-geometric-module>` uses completed Hilbert spaces and requires controlled operators to be globally bounded; boundedness on each bounded region alone does not imply this.

## Local and semilocal objects

Keep the coefficient and ambient categories above, and assume additionally that $\widehat C$ has a symmetric monoidal structure restricting to $C$.
Require its tensor unit $\mathbf1$ to be initial in $C$.
We identify $V(\varnothing)$ with $\mathbf1$ by the unique isomorphism and write $u_B:\mathbf1\to V(B)$ for the unique map.
Write $s_{D,D'}:V(D)\to V(D')$ for a structure map when $D\subseteq D'$.

````{prf:definition} Local controlled object
:nonumber:
:label: def-local-controlled-object

A *semilocal object* is a controlled object with tensor-extension maps
$$
\tau_{B, B'}:V(B)\otimes V(B')\longrightarrow V(B \sqcup B')
$$
for disjoint bounded $B,B'$.
These maps are natural under inclusions of disjoint pairs and restrict to the structure maps on both factors, as expressed by the following diagrams.
Here $\lambda$ and $\rho$ are the left and right unit isomorphisms.

```{tikz}
:libs: cd
:alt: Inserting the unit into the second factor and then applying tau gives the structure map from V(B) to V(B disjoint union B').

\begin{tikzcd}
V(B)\otimes\mathbf1 \arrow[r, "\mathrm{id}\otimes u_{B'}"]
  \arrow[d, "\rho_{V(B)}"']
  & V(B)\otimes V(B') \arrow[d, "\tau_{B,B'}"] \\
V(B) \arrow[r, "s_{B,B\sqcup B'}"'] & V(B\sqcup B')
\end{tikzcd}
```

```{tikz}
:libs: cd
:alt: Inserting the unit into the first factor and then applying tau gives the structure map from V(B') to V(B disjoint union B').

\begin{tikzcd}
\mathbf1\otimes V(B') \arrow[r, "u_B\otimes\mathrm{id}"]
  \arrow[d, "\lambda_{V(B')}"']
  & V(B)\otimes V(B') \arrow[d, "\tau_{B,B'}"] \\
V(B') \arrow[r, "s_{B',B\sqcup B'}"'] & V(B\sqcup B')
\end{tikzcd}
```

They also satisfy the following unit, symmetry, and associativity conditions.
For the diagrams write $A=V(B)$, $A'=V(B')$, $A''=V(B'')$, and $A_{12}=V(B\sqcup B')$, $A_{23}=V(B'\sqcup B'')$, $A_{123}=V(B\sqcup B'\sqcup B'')$.
The unit condition is

```{tikz}
:libs: cd
:alt: Tensor extension with the empty region agrees with the left and right unit isomorphisms.

\begin{tikzcd}
\mathbf1\otimes A \arrow[r, "\tau_{\varnothing,B}"]
  \arrow[dr, "\lambda_A"'] & A
  & A\otimes\mathbf1 \arrow[l, "\tau_{B,\varnothing}"']
    \arrow[dl, "\rho_A"] \\
  & A \arrow[u, equal] &
\end{tikzcd}
```

For disjoint $B,B'$, symmetry requires the following square to commute, where $\beta$ is the symmetry isomorphism:

```{tikz}
:libs: cd
:alt: Swapping the two tensor factors before tensor extension gives the same map to the union.

\begin{tikzcd}
A\otimes A' \arrow[r, "\beta_{A,A'}"] \arrow[d, "\tau_{B,B'}"']
  & A'\otimes A \arrow[d, "\tau_{B',B}"] \\
A_{12} \arrow[r, equal] & A_{12}
\end{tikzcd}
```

For pairwise disjoint $B,B',B''$, associativity requires the following diagram to commute, where $\alpha$ is the associativity isomorphism:

```{tikz}
:libs: cd
:alt: Combining three disjoint regions in either order gives the same tensor-extension map, after the associativity isomorphism.

\begin{tikzcd}[row sep=large, column sep=large]
(A\otimes A')\otimes A'' \arrow[r, "\alpha_{A,A',A''}"]
  \arrow[d, "\tau_{B,B'}\otimes\mathrm{id}"']
  & A\otimes(A'\otimes A'') \arrow[d, "\mathrm{id}\otimes\tau_{B',B''}"] \\
A_{12}\otimes A'' \arrow[d, "\tau_{B\sqcup B',B''}"']
  & A\otimes A_{23} \arrow[d, "\tau_{B,B'\sqcup B''}"] \\
A_{123} \arrow[r, equal] & A_{123}
\end{tikzcd}
```

The object is *local* if all $\tau_{B,B'}$ are isomorphisms.
````

Given objects $V_x$ of $C$ for each $x\in X$, consider the formula
$$
V(B)=\operatorname*{colim}_{F\subseteq B,\ F\text{ finite}}
                       \bigotimes_{x\in F}V_x.
$$
The transition maps insert the unique maps from the unit.
This gives a local controlled object provided the colimits exist in $C$, tensor products preserve them in each variable, and the induced maps $V(B)\to V(D)$ for $B\subseteq D$ are monomorphisms.
Indeed, finite tensor products satisfy the disjoint-union identity, and every finite subset of a directed union lies in one member of that directed family.

If $\{x:V_x\not\cong\mathbf1\}$ meets each bounded set in finitely many points, the colimits stabilize at finite tensor products.
In this case it suffices that the maps inserting units into those tensor products are monomorphisms.
This holds for finite-dimensional Hilbert spaces with isometric embeddings and direct sum, and for full complex matrix algebras with unital $*$-homomorphisms and tensor product; it is not automatic in an arbitrary symmetric monoidal category with initial unit.

Conversely, every local controlled object has the displayed point-object description; see the proof of {ref}`Local objects are determined by their point objects <theorem-local-objects-points>`.

Whenever pointwise tensor products of controlled objects are used below, we assume tensor products preserve the relevant directed colimits and take pairs of monomorphisms to monomorphisms.
These hypotheses ensure that $(V\otimes W)(B)=V(B)\otimes W(B)$ is again controlled.

## Local nets and Azumaya objects


For finite-dimensional unital $C^*$-algebras, semilocal controlled objects are semilocal nets.
A local **matrix** net additionally requires every $V(B)$ to be a full matrix algebra.
These are the {ref}`spin systems <article-spin-system>` considered here.
In the Hilbert-space example, local objects give the point-determined version of {ref}`geometric modules <article-geometric-module>`.

To define Azumaya objects, fix a full symmetric monoidal inclusion $C\subseteq D$ with the same initial unit, and choose a common ambient category for controlled morphisms.
The larger coefficient category $D$ need not itself admit all filtered colimits.

```{prf:definition} Azumaya controlled object
:nonumber:
:label: def-azumaya-controlled-object

A semilocal $D$-valued object $V$ is *Azumaya relative to $C$* if there is a semilocal $D$-valued object $W$ such that $V\otimes W$ is controlled-isomorphic to a local $C$-valued object.
```

For matrix nets, take $C$ to be full matrix algebras and $D$ finite-dimensional unital $C^*$-algebras, with global colimits taken in unital $C^*$-algebras.
The tensor complement and the controlled isomorphism are essential: Azumaya does not mean that the given local pieces already split pointwise as a matrix net.
The definition depends on the chosen pair of coefficient categories.

## Categories of controlled, local, and Azumaya objects

We use $\mathrm{Con}_{C}(X)$ for all controlled morphisms.
The notation $\mathrm{Loc}_{C}(X)$ and $\mathrm{sLoc}_{C}(X)$ denotes the groupoids of local and semilocal objects and controlled isomorphisms preserving the tensor-extension data.
The corresponding Azumaya groupoid is $\mathrm{Az}_{C}(X)$.
Compatibility is read in the ambient colimit object, after enlarging controls where necessary.
In coefficient categories where tensor extensions are unique, this condition adds no further choices.

For local matrix nets, it is also useful to allow all controlled unital $*$-homomorphisms.
That larger category is specified explicitly in the spin system article.
Its maximal subgroupoid is the one used in the QCA $K$-theory construction.

For a coarse map $f:X\to Y$, pushforward is given by $(f_*V)(B)=V(f^{-1}(B))$.
Properness ensures that this expression is defined on bounded $B$, and controlledness sends a control $E$ to $(f\times f)(E)$.
This is the geometric origin of functoriality in $X$.
