(ref-coarse-maps)=
# Coarse maps and equivalences

Let $X=(X,\mathcal E_X,\mathcal B_X)$ and
$Y=(Y,\mathcal E_Y,\mathcal B_Y)$ be {prf:ref}`coarse spaces <def-coarse-space>`.

## Maps

```{prf:definition} Controlled and coarse maps
:label: def-coarse-map

A map $f:X\to Y$ is **controlled** if $(f\times f)(E)\in\mathcal E_Y$
for every $E\in\mathcal E_X$. It is **proper** if
$f^{-1}(B)\in\mathcal B_X$ for every $B\in\mathcal B_Y$.
A **coarse map** is a map satisfying both conditions.
```

Here *proper* refers to inverse images of bornologically bounded sets. No
topology is implicit. Controlled maps alone need not be coarse maps: the
constant map from $\mathbb Z$ to a point is controlled but is not proper for
the usual metric bornology on $\mathbb Z$.

## Equivalences

```{prf:definition} Closeness and coarse equivalence
:label: def-coarse-equivalence

Two maps $f,g:X\to Y$ are **close** if
$\{(f(x),g(x)):x\in X\}\in\mathcal E_Y$.
A coarse map $f:X\to Y$ is a **coarse equivalence** if there is a coarse map
$g:Y\to X$ such that $gf$ and $fg$ are close to the respective identity maps.
```

The inverse is allowed to recover a point only up to a controlled displacement.
For metric spaces, closeness means a uniform bound on pointwise distance.

```{prf:theorem} The integer lattice and the real line
:label: thm-lattice-line

Equip $\mathbb Z$ and $\mathbb R$ with their usual metric coarse structures and
metric bornologies. The inclusion $i:\mathbb Z\hookrightarrow\mathbb R$ is a
coarse equivalence.
```

````{dropdown} Proof
:class-container: proof-dropdown

```{prf:proof}
Set $r(t)=\lfloor t\rfloor$. The inclusion is controlled, and
$|r(s)-r(t)|\leq |s-t|+1$ shows that $r$ is controlled.
Both maps have bounded inverse images of bounded sets, so they are proper.
Moreover, $ri$ is the identity on $\mathbb Z$, while $|ir(t)-t|<1$ for all
$t\in\mathbb R$. Thus $ir$ is close to the identity on $\mathbb R$.
```
````

## Interpretation

The theorem makes precise one sense in which a lattice and a continuum have
the same large-scale geometry. Additional hypotheses and constructions are
needed when transporting operator algebras or physical models; coarse
equivalence of spaces alone is not a classification of phases.

Return to [the geometric introduction](../geometry/coarse-spaces.md), or continue
to [Roe algebras](../algebras/roe-algebras.md). For the general definitions see
{ref}`bib-bunke-engel`, §2.1 and §3.2.
