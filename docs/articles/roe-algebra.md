(article-roe-algebra)=
# Roe algebra

```{warning}
Agent-generated, not reviewed yet
```

The Roe algebra combines control of propagation with local compactness.
The coarse structure specifies which pairs of regions an operator may connect, while the bornology specifies where its localizations must be compact.
This construction works without a metric or a topology, once a geometric module has been chosen.

Let $X=(X,\mathcal C,\mathcal B)$ be any {prf:ref}`bornological coarse space <def-bornological-coarse-space>`.
Choose a complex {prf:ref}`point-determined geometric module <def-geometric-module>` $H$ over $X$, and write $\chi_A$ for its support projection for $A\subseteq X$.
Neither $X$ nor $H$ is assumed countable or separable, and the module need not be locally finite.
The topological model used for proper metric spaces is discussed below.

(locally-compact-finite-propagation-operators)=
## Locally compact controlled operators

```{prf:definition} Controlled propagation and local compactness
:nonumber:
:label: def-roe-operators

A bounded operator $T\in\mathcal B(H)$ is *$E$-controlled*, for $E\in\mathcal C$, if
$$
\chi_AT\chi_B=0\qquad\text{whenever }(A\times B)\cap E=\varnothing,
\quad A,B\subseteq X.
$$
It has *controlled propagation* if it is $E$-controlled for some entourage $E$.
It is *locally compact* if $\chi_BT$ and $T\chi_B$ are compact for every $B\in\mathcal B$.
```

The control condition says that $T$ sends vectors supported in $B$ to vectors supported in the {ref}`fattening <def-fattening>` $B_E$.
Equivalently, its matrix entries $T_{xy}:H_y\to H_x$ vanish whenever $(x,y)\notin E$.
Indeed, singleton compressions give one implication, and finite sums of point-supported vectors are dense in each support subspace, giving the converse.
For a metric coarse structure, controlled propagation is the usual *finite propagation*: the nonzero matrix entries have a common finite bound on $d(x,y)$.
On a general coarse space the bound is an entourage, not a real number.

```{prf:definition} Roe algebra
:nonumber:
:label: def-roe-algebra

Let $\mathbb C[X;H]$ be the $*$-algebra of locally compact operators of controlled propagation on $H$.
The *Roe algebra* of $X$ on $H$ is its operator-norm closure:
$$
C^*(X;H)=\overline{\mathbb C[X;H]}^{\|\cdot\|}\subseteq\mathcal B(H).
$$
```

Here is a verification of the algebra assertion.
If $T$ is $E$-controlled and $S$ is $F$-controlled, then $T+S$ is $(E\cup F)$-controlled, $T^*$ is $E^{-1}$-controlled, and $TS$ is $(E\circ F)$-controlled.
For the product, apply the support condition successively: $S$ sends $\chi_BH$ into $\chi_{B_F}H$, and $T$ sends this subspace into $\chi_{(B_F)_E}H$.
Local compactness is preserved under sums and adjoints, and under products since
$$
\chi_BTS=(\chi_BT)S,\qquad TS\chi_B=T(S\chi_B).
$$
Each right-hand side is compact if $T$ and $S$ are locally compact.

Compatibility of the coarse structure and bornology gives a useful stronger statement.
For an $E$-controlled $T$ and bounded $B$,
$$
T\chi_B=\chi_{B_E}T\chi_B,\qquad
\chi_BT=\chi_BT\chi_{B_{E^{-1}}},
$$
and both fattenings are bounded.
Consequently, if $S$ is locally compact, then $TS$ and $ST$ are locally compact even when $T$ is not: insert these bounded cutoffs whenever the compact localization is on the other side of $T$.
In particular, $\mathbb C[X;H]$ is a two-sided $*$-ideal in the algebra of all bounded controlled operators.

Every element of $C^*(X;H)$ is still locally compact, since compact operators form a norm-closed ideal.
It need not itself have controlled propagation, and it need not be globally compact.
The algebra depends on the bornology as well as the coarse structure and the module.
Enlarging the bornology, while keeping it compatible with the same coarse structure, imposes more local compactness conditions and therefore gives a subalgebra on the same module.

## Examples and the choice of module

If $H$ is locally finite, all its bounded-set projections have finite rank, so every bounded operator on $H$ is locally compact.
For example, if the bornology consists of the finite subsets of $X$, this applies to $H=\ell^2(X)$.
The closure of the controlled operators in this scalar-fiber model is the *uniform Roe algebra* $C_u^*(X)$.
In particular, it recovers the usual uniform Roe algebra of a discrete proper metric space.
The module $\ell^2(X)\otimes\ell^2(\mathbb N)$ is also available for every coarse space, but its infinite-dimensional point fibers impose a different local compactness condition.
Already at a point these two choices give $\mathbb C$ and $\mathcal K(\ell^2(\mathbb N))$, respectively.

For an example with no metric specified, give any set $X$ the minimal coarse structure $\mathcal C=\mathcal P(\Delta_X)$ and the finite-set bornology.
These structures are compatible because fattening a set by a subset of the diagonal cannot enlarge it.
On $\ell^2(X)$, the controlled operators are precisely the diagonal multiplication operators, and hence $C^*(X;\ell^2(X))=\ell^\infty(X)$.
For infinite $X$ this contains the noncompact identity.

If $X$ is bounded, taking $B=X$ in the definition shows that $C^*(X;H)\subseteq\mathcal K(H)$.
If also $X\times X\in\mathcal C$, every operator is controlled and therefore $C^*(X;H)=\mathcal K(H)$.
The extra control hypothesis cannot simply be dropped for arbitrary bornological coarse spaces.
For instance, on a two-point set with the minimal coarse structure and the full bornology, the scalar-fiber Roe algebra is $\mathbb C\oplus\mathbb C$, whereas $\mathcal K(\mathbb C^2)=M_2(\mathbb C)$.

The module is kept in the notation because no independence assertion is being made for arbitrary choices of $H$.
A controlled unitary $U:H\to H'$ does give an isomorphism $T\mapsto UTU^*$ of Roe algebras.
To see this, if $U$ is $E$-controlled and $T$ is $F$-controlled, then $UTU^*$ is $(E\circ F\circ E^{-1})$-controlled.
For bounded $B$, the identity $\chi'_BU=\chi'_BU\chi_{B_{E^{-1}}}$ proves local compactness on the left, and its adjoint proves it on the right.
Apply the same argument to $U^*$ to obtain the inverse isomorphism.
The comparison of separable ample modules on proper metric spaces is a particular case with additional hypotheses, described below.
For the categorical construction on arbitrary coarse spaces, see the {prf:ref}`locally finite Roe category <def-roe-category>`.

## Coarse maps

For a {prf:ref}`coarse map <def-coarse-map>` $f:X\to Y$, push the module forward to $f_*H$, whose support projections are $\chi_A^{f_*H}=\chi_{f^{-1}(A)}^H$.
If $T$ is $E$-controlled over $X$, it is $(f\times f)(E)$-controlled over $Y$.
Properness of $f$ makes $f^{-1}(B)$ bounded whenever $B$ is bounded in $Y$, so it also preserves local compactness.
Thus the identity on underlying operators gives an injective $*$-homomorphism
$$
C^*(X;H)\longrightarrow C^*(Y;f_*H).
$$
This construction uses the pushed-forward module; comparison with a separately chosen module over $Y$ requires additional data.

## The proper metric formulation

Let $X$ now be a separable proper metric space, with its metric coarse structure and the bornology of finite-diameter subsets.
One may use a separable nondegenerate topological {ref}`geometric module <article-geometric-module>`, namely a representation of $C_0(X)$ on $H$.
Its spectral measure supplies support projections for Borel subsets.
In this formulation all sets in the control and localization conditions are taken to be Borel, and *finite propagation* means that, for some $R<\infty$,
$$
\chi_AT\chi_B=0\qquad\text{whenever }d(A,B)>R.
$$
The same norm-closure construction gives the classical Roe algebra on this topological module.

Here local compactness is equivalent to compactness of $fT$ and $Tf$ for every $f\in C_0(X)$.
One direction uses a compactly supported continuous function equal to one on the closure of a bounded set, which is compact by properness.
The other first writes $fT=f\chi_BT$ and $Tf=T\chi_Bf$ for compactly supported $f$ and a bounded Borel set $B$ containing its support, and then uses uniform approximation in $C_0(X)$.

(sec-roe-metric-partition)=

The relation to the point-determined model can be made explicit without assigning spectral projections to non-Borel sets.
Choose a countable maximal $1$-separated set of centers $(x_j)$, and assign each point to a nearest center, resolving ties by the enumeration.
Properness ensures that nearest centers exist and that bounded sets contain only finitely many centers.
The resulting Borel partition $(D_j)$ has cells of diameter at most $2$, each containing the open ball of radius $1/2$ about its center.
Every bounded set meets only finitely many cells, since their centers lie in its bounded $1$-neighborhood.
Regard $\chi_{D_j}H$ as the fiber at $x_j$, with zero fibers elsewhere.
If every cell has diameter at most $D$, this replacement changes propagation bounds by at most $2D$.
Each bounded-set projection for either model is dominated by a bounded-set projection for the other: take the union of cells meeting the set, or the set of their chosen points.
Thus both models give exactly the same locally compact controlled operators, and the same Roe algebra on $H$.

For separable ample topological modules, every cell subspace is infinite-dimensional: a nonzero compactly supported continuous function in the cell's interior acts noncompactly and has range in that subspace.
Discretization followed by [Bunke–Engel, Lemma 8.21](https://arxiv.org/abs/1607.03657) therefore supplies a controlled unitary comparison.
Under these hypotheses their Roe algebras are noncanonically isomorphic, and the notation $C^*(X)$ can suppress the module.
For a discrete proper metric space, ampleness requires infinite-dimensional point fibers, so the scalar-fiber uniform Roe algebra is a different module choice.

## Locally trace-class variant

Return to an arbitrary bornological coarse space with a point-determined module.

```{prf:definition} Controlled locally trace-class algebra
:nonumber:
:label: def-trace-roe-algebra

A bounded operator is *locally trace-class* if $\chi_BT$ and $T\chi_B$ are trace-class for every bounded subset $B$.
The *controlled locally trace-class algebra* is
$$
\mathcal B_{\mathrm{tr}}(X;H)
 =\{T\in\mathcal B(H):T\text{ has controlled propagation and is locally trace-class}\}.
$$
```

Equivalently, $fT$ and $Tf$ must be trace-class for every bounded function $f$ supported in a bounded subset, acting by multiplication on the point fibers.
For topological modules in the proper metric formulation, use bounded Borel sets and bounded Borel functions instead.
This recovers the *finite propagation locally trace-class algebra* in the metric setting.
The ideal property of trace-class operators and the bounded-cutoff argument above show that $\mathcal B_{\mathrm{tr}}(X;H)$ is a two-sided $*$-ideal in the algebra of bounded controlled operators.
It is contained in $\mathbb C[X;H]$.

### A sufficient condition for density

The definitions above require no metric or partition hypothesis.
The following approximation statement uses an additional assumption, which holds in the proper metric setting.

```{prf:proposition} Density under a controlled partition
:nonumber:
:label: prop-trace-roe-density

Suppose $X$ admits a finite or countable partition $(D_j)$ into bounded subsets such that every bounded set meets only finitely many cells and
$$
F:=\bigcup_j(D_j\times D_j)\in\mathcal C.
$$
Then the operator-norm closure of $\mathcal B_{\mathrm{tr}}(X;H)$ is $C^*(X;H)$.
The conclusion also holds for a topological module over a separable proper metric space, using a Borel partition with these properties.
```

````{dropdown} Proof
:class-container: proof-dropdown

```{prf:proof}
Let $T\in\mathbb C[X;H]$ be $E$-controlled and fix $\varepsilon>0$.
Enumerate the cells starting at $j=1$.
Since $\chi_{D_j}T$ and $T\chi_{D_j}$ are compact, choose a finite-rank orthogonal projection $P_j$ on $\chi_{D_j}H$ such that
$$
\|(\chi_{D_j}-P_j)T\|<\varepsilon 2^{-j},\qquad
\|T(\chi_{D_j}-P_j)\|<\varepsilon 2^{-j}.
$$
Put $P=\bigoplus_jP_j$.
Summing these estimates gives $\|(1-P)T\|\leq\varepsilon$ and $\|T(1-P)\|\leq\varepsilon$, so
$$
\|T-PTP\|\leq2\varepsilon.
$$
The operator $P$ is $F$-controlled, because it only moves vectors within a cell, and hence $PTP$ is $(F\circ E\circ F)$-controlled.
For bounded $B$, the operators $\chi_BP$ and $P\chi_B$ have finite rank: only finitely many cells meet $B$.
Thus $\chi_BPTP$ and $PTP\chi_B$ have finite rank, so $PTP$ is locally trace-class.
This proves the density assertion.
For a topological module the same argument uses Borel projections; a partition with these properties is provided by the {ref}`proper metric partition construction above <sec-roe-metric-partition>`.
```
````

The uncompleted algebra retains information useful for trace pairings: operator-norm completion does not in general preserve local trace norms or strict control by a single entourage.
Even at a point, a compact operator can fail to be trace-class, for example the diagonal operator with eigenvalues $1/n$ on $\ell^2(\mathbb N)$.
