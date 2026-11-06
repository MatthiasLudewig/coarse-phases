(article-roe-algebra)=
# Roe algebra

```{warning}
Agent-generated, not reviewed yet
```

The Roe algebra combines control of propagation with local compactness.
It is an operator-algebraic invariant of large-scale geometry and supplies
the target for the coarse index.

Let $X$ be a separable proper metric space and $H$ a separable nondegenerate
{ref}`geometric module <article-geometric-module>`. Use the spectral measure
to let bounded Borel functions act on $H$.

## Locally compact finite propagation operators

```{prf:definition} Finite propagation and local compactness
:label: def-roe-operators

A bounded operator $T$ has propagation at most $R$ if
$\chi_AT\chi_B=0$ whenever $A,B$ are Borel subsets with $d(A,B)>R$.
It has finite propagation if such a finite $R$ exists. It is locally compact
if $fT$ and $Tf$ are compact for every $f\in C_0(X)$.
```

For proper metric spaces, local compactness is equivalent to compactness of
$\chi_BT$ and $T\chi_B$ for every bounded Borel $B$. One direction uses a
compactly supported continuous function equal to one on $B$; the other uses
uniform approximation of a function in $C_0(X)$ by compactly supported ones.

```{prf:definition} Roe algebra
:label: def-roe-algebra

Let $\mathbb C[X;H]$ be the $*$-algebra of locally compact, finite propagation
operators on $H$. The Roe algebra is its operator-norm closure:

$$
C^*(X;H)=\overline{\mathbb C[X;H]}^{\|\cdot\|}\subseteq\mathcal B(H).
$$

```

Propagation bounds add under composition. Local compactness is preserved under
composition with a finite propagation operator: a cutoff on one side can be
replaced by a cutoff on a bounded thickening on the other side. These facts
verify the $*$-algebra assertion.

If $H$ is ample, its choice can be suppressed up to a noncanonical algebra
isomorphism; see {ref}`the ample-module theorem <theorem-ample-modules>`.
For bounded $X$, the ample Roe algebra is $\mathcal K(H)$. On an unbounded
space an element of $C^*(X;H)$ need not be compact or have finite propagation;
it is a norm limit of operators with these local and controlled properties.

For a discrete proper metric space and $H=\ell^2(X)$, every bounded operator
is locally compact, since bounded subsets are finite. Its finite-propagation
closure is the uniform Roe algebra in this scalar-fiber model. This is not
by definition the ample Roe algebra, which uses infinite-dimensional fibers.

## Locally trace-class variant

```{prf:definition} Finite propagation locally trace-class algebra
:label: def-trace-roe-algebra

A bounded operator is locally trace-class if $fT$ and $Tf$ are trace-class
for every bounded Borel function $f$ with bounded support. Let

$$
\mathcal B_{\mathrm{tr}}(X;H)
 =\{T:T\text{ has finite propagation and is locally trace-class}\}.
$$

```

This is a $*$-algebra contained in $\mathbb C[X;H]$. For a bounded Borel set
$B$, a trace-class localization $\chi_BT$ can be moved past another
finite-propagation operator after enlarging $B$ by its propagation bound.
This proves closure under products by the ideal property of trace-class
operators.

Under the proper metric hypotheses above, the norm closure of
$\mathcal B_{\mathrm{tr}}(X;H)$ is again $C^*(X;H)$. Here is the approximation
argument. Partition $X$ into locally finitely many uniformly bounded Borel
cells $(B_j)$. For a locally compact finite-propagation $T$, choose finite-rank
projections $P_j$ on $\chi_{B_j}H$ so that both
$\|(1-P_j)\chi_{B_j}T\|$ and $\|T\chi_{B_j}(1-P_j)\|$ are less than
$\varepsilon 2^{-j}$. Put $P=\bigoplus_jP_j$. Then
$\|T-PTP\|\leq2\varepsilon$, while $PTP$ still has finite propagation.
Its localization to a bounded set has finite rank, because that set meets
only finitely many cells. Thus $PTP\in\mathcal B_{\mathrm{tr}}(X;H)$.

Nevertheless, the uncompleted algebra is important. Trace pairings use local
trace norms and strict propagation; these conditions are not retained merely
by taking the operator-norm closure. For example, coarse transversality can
force a product of localized finite-propagation operators to be globally
trace-class even when no individual operator is globally trace-class.

## Sources

See {ref}`Roe <bib-roe-cohomology>`, §§4.1–4.3, and
{ref}`Ludewig–Thiang <bib-large-scale-trace>`, §2.2.
The comparison of module choices is discussed in
{ref}`Ewert–Meyer <bib-ewert-meyer>`, §2.
