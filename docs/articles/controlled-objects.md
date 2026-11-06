(article-controlled-objects)=
# Controlled objects

```{warning}
Agent-generated, not reviewed yet
```

Controlled objects provide a common language for geometric modules and local
operator algebras. The bornology specifies the regions on which an object is
defined, and the coarse structure controls how far a morphism can move it.

## Controlled objects in a symmetric monoidal category

Let $X$ be a coarse space with bornology $\mathcal B_X$. Let $\mathcal C$ be
a category with an initial object $\mathbf1$, and suppose the directed colimits
used below exist, either in $\mathcal C$ or in a specified ambient category.
We regard the bornology as a category under inclusion.

```{prf:definition} Controlled object
:label: def-controlled-object

A controlled object over $X$ with values in $\mathcal C$ is a functor
$V:\mathcal B_X\to\mathcal C$ such that its structure morphisms are
monomorphisms, $V(\varnothing)=\mathbf1$, and for every directed collection
of bounded subsets $(B_i)$ with union a bounded set $B$, the canonical map
$$
\operatorname*{colim}_iV(B_i)\longrightarrow V(B)
$$
is an isomorphism.
```

When $\mathcal C$ is symmetric monoidal, we assume its monoidal unit is the
initial object. This is the convention of the supplied notes: it holds for
Hilbert spaces under direct sum and for unital complex algebras under tensor
product. It is an additional hypothesis, not a property of every symmetric
monoidal category.

If tensor products preserve the relevant directed colimits and take pairs of
monomorphisms to monomorphisms, the pointwise formula
$(V\otimes W)(B)=V(B)\otimes W(B)$ again defines a controlled object.

## Controlled morphisms

```{prf:definition} Controlled morphism
:label: def-controlled-morphism

An $E$-controlled presentation of a morphism $V\to W$ is a natural collection
of maps $\varphi_B:V(B)\to W(E[B])$, with $E$ a fixed entourage containing
the diagonal. Two presentations define the same controlled morphism if their
maps agree after passage to $W(G[B])$ for a common larger entourage $G$.
```

Composing an $E$-controlled presentation with an $F$-controlled one gives an
$F\circ E$-controlled presentation. The diagonal controls identity morphisms.
This defines the category $\mathrm{Con}_{\mathcal C}(X)$. A controlled
isomorphism requires a controlled inverse. A morphism of propagation zero
has a presentation controlled by $\Delta_X$.

In concrete categories one can often form a global object
$V_X=\operatorname*{colim}_{B\in\mathcal B_X}V(B)$. Then a controlled
morphism is a morphism of global objects sending $V(B)$ into $W(E[B])$.
For Hilbert spaces we additionally require global operators to be bounded;
boundedness is not implied merely by boundedness on each local piece.

## Local and semilocal objects

The initial-unit assumption gives canonical maps from each factor into a
tensor product.

```{prf:definition} Local controlled object
:label: def-local-controlled-object

A semilocal object is a controlled object with natural tensor-extension maps
$$
\tau_{B,C}:V(B)\otimes V(C)\longrightarrow V(B\sqcup C)
\qquad(B\cap C=\varnothing),
$$
restricting to the structure maps on each factor. They satisfy the unit,
symmetry, and associativity compatibilities. The object is local if all
$\tau_{B,C}$ are isomorphisms.
```

For unital algebras, the tensor-extension map is multiplication and its
existence expresses commutativity of disjoint local algebras. For Hilbert
spaces with direct sum and isometric embeddings, it expresses orthogonality
of the two local subspaces.

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
$\mathcal C\subseteq\widehat{\mathcal C}$ with the same initial unit.

```{prf:definition} Azumaya controlled object
:label: def-azumaya-controlled-object

A semilocal $\widehat{\mathcal C}$-valued object $V$ is Azumaya relative to
$\mathcal C$ if there is a semilocal object $W$ such that $V\otimes W$ is
controlled-isomorphic to a local $\mathcal C$-valued object.
```

For matrix nets, take $\mathcal C$ to be full matrix algebras and
$\widehat{\mathcal C}$ finite-dimensional unital $C^*$-algebras. The tensor
complement and the controlled isomorphism are essential: Azumaya does not
mean that the given local pieces already split pointwise as a matrix net.
The definition depends on the chosen pair of coefficient categories.

## Categories of controlled, local, and Azumaya objects

We use $\mathrm{Con}_{\mathcal C}(X)$ for all controlled morphisms.
The notation $\mathrm{Loc}_{\mathcal C}(X)$ and
$\mathrm{sLoc}_{\mathcal C}(X)$ denotes the groupoids of local and semilocal
objects and controlled isomorphisms preserving the tensor-extension data.
The corresponding Azumaya groupoid is $\mathrm{Az}_{\mathcal C}(X)$.
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

## Sources

This formulation follows the author's {ref}`Controlled objects
<bib-controlled-notes>`, §§1–3 and the Azumaya construction, with the
colimit and tensor-product hypotheses made explicit.
