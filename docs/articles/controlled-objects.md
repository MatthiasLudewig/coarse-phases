(article-controlled-objects)=
# Controlled objects

```{warning}
Agent-generated, not reviewed yet
```

Controlled objects provide a common language for geometric modules and local operator algebras. 

## Controlled objects in a symmetric monoidal category

Let $(X, \mathcal{B}, \mathcal{C})$ be a bornological coarse space. 
Let $C$ be a category with an initial object $\mathbf1$, and suppose the directed colimits used below exist, either in $C$ or in a specified ambient category.
We regard the bornology as a category under inclusion.

```{prf:definition} Controlled object
:nonumber:
:label: def-controlled-object

A *controlled object* over $X$ with values in $C$ is a functor
$V:\mathcal B\to C$ such that its structure morphisms are
monomorphisms, $V(\varnothing)=\mathbf1$, and for every directed collection
$\mathcal{B}'\subseteq\mathcal{B}$ whose union $B$ is bounded, the canonical map

$$
\operatorname*{colim}_{B' \in \mathcal{B}'}V(B')\longrightarrow V(B)
$$

is an isomorphism.
```

When $C$ is symmetric monoidal, we assume its monoidal unit is the
initial object. 
This holds for Hilbert spaces under direct sum and for unital complex algebras under tensor product. 

If tensor products preserve the relevant directed colimits and take pairs of monomorphisms to monomorphisms, the pointwise formula $(V\otimes W)(B)=V(B)\otimes W(B)$ again defines a controlled object.

## Controlled morphisms

```{prf:definition} Controlled morphism
:nonumber:
:label: def-controlled-morphism

An *$E$-controlled presentation* of a morphism $V\to W$ is a natural collection of maps $\varphi_B:V(B)\to W(B_E)$, with $E$ a fixed entourage containing the diagonal. 
Two presentations define the same *controlled morphism* if their
maps agree after passage to $W(B_F)$ for a common larger entourage $F$.
```

Composing an $E$-controlled presentation with an $F$-controlled one gives an $F\circ E$-controlled presentation, hence the composition of controlled morphisms defines a controlled morphism again.
This defines the category $\mathrm{Con}_{C}(X)$.
A morphism is called *of propagation zero* if it has a presentation controlled by $\Delta_X$.

In concrete categories one can often form a global object $V_X=\operatorname*{colim}_{B\in\mathcal B}V(B)$.
Then a controlled morphism is a morphism of global objects sending $V(B)$ into $W(B_E)$.
For Hilbert spaces we additionally require global operators to be bounded;
boundedness is not implied merely by boundedness on each local piece.

## Local and semilocal objects

The initial-unit assumption gives canonical maps from each factor into a tensor product.

```{prf:definition} Local controlled object
:nonumber:
:label: def-local-controlled-object

A *semilocal object* is a controlled object with natural tensor-extension maps

$$
\tau_{B,C}:V(B)\otimes V(C)\longrightarrow V(B\sqcup C)
\qquad(B\cap C=\varnothing),
$$

restricting to the structure maps on each factor. They satisfy the unit,
symmetry, and associativity compatibilities. The object is *local* if all
$\tau_{B,C}$ are isomorphisms.
```

For unital algebras, the tensor-extension map is multiplication and its
existence expresses commutativity of disjoint local algebras. For Hilbert
spaces with direct sum and isometric embeddings, it expresses orthogonality of the two local subspaces.

Assigning an object $V_x$ to each point gives a local object by

$$
V(B)=\operatorname*{colim}_{F\subseteq B,\ F\text{ finite}}
                       \bigotimes_{x\in F}V_x,
$$

provided these colimits exist in the chosen category. The converse, including
the finite-dimensional cases where only locally finitely many $V_x$ are
nontrivial, is proved on the separate page
{ref}`Local objects are determined by their point objects <theorem-local-objects-points>`.

## Local nets and Azumaya objects

For finite-dimensional unital $C^*$-algebras, semilocal controlled objects
are semilocal nets. A local **matrix** net additionally requires every $V(B)$
to be a full matrix algebra. These are the {ref}`spin systems
<article-spin-system>` considered here. In the Hilbert-space example, local
objects give the point-determined version of {ref}`geometric modules
<article-geometric-module>`.

To define Azumaya objects, fix a full symmetric monoidal inclusion
$C\subseteq\widehat C$ with the same initial unit.

```{prf:definition} Azumaya controlled object
:nonumber:
:label: def-azumaya-controlled-object

A semilocal $\widehat C$-valued object $V$ is
*Azumaya relative to $C$* if there is a semilocal object $W$ such that
$V\otimes W$ is controlled-isomorphic to a local $C$-valued object.
```

For matrix nets, take $C$ to be full matrix algebras and
$\widehat C$ finite-dimensional unital $C^*$-algebras. The tensor
complement and the controlled isomorphism are essential: Azumaya does not
mean that the given local pieces already split pointwise as a matrix net.
The definition depends on the chosen pair of coefficient categories.

## Categories of controlled, local, and Azumaya objects

We use $\mathrm{Con}_{C}(X)$ for all controlled morphisms.
The notation $\mathrm{Loc}_{C}(X)$ and
$\mathrm{sLoc}_{C}(X)$ denotes the groupoids of local and semilocal
objects and controlled isomorphisms preserving the tensor-extension data.
The corresponding Azumaya groupoid is $\mathrm{Az}_{C}(X)$.
Compatibility is read in the ambient colimit object, after enlarging controls
where necessary. In coefficient categories where tensor extensions are unique,
this condition adds no further choices.

For local matrix nets, it is also useful to allow all controlled unital
$*$-homomorphisms. That larger category is specified explicitly in the spin
system article. Its maximal subgroupoid is the one used in the QCA
$K$-theory construction.

For a coarse map $f:X\to Y$, pushforward is given by
$(f_*V)(B)=V(f^{-1}(B))$. Properness ensures that this expression is defined
on bounded $B$, and controlledness sends a control $E$ to $(f\times f)(E)$.
This is the geometric origin of functoriality in $X$.
