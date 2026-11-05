(ref-coarse-space)=
# Coarse space

This page fixes the terminology used throughout the wiki. For motivation and
metric examples, see [Coarse spaces: the idea](../geometry/coarse-spaces.md).

## Coarse structure

```{prf:definition} Coarse structure
:label: def-coarse-structure

A **coarse structure** on a set $X$ is a collection
$\mathcal E\subseteq\mathcal P(X\times X)$ containing the diagonal $\Delta_X$
and closed under subsets, finite unions, inverses, and compositions. Its members
are called **entourages** or **controlled sets**. We use

$$
E^{-1}=\{(y,x):(x,y)\in E\},\qquad
E\circ F=\{(x,z):\exists y,\ (x,y)\in E,\ (y,z)\in F\}.
$$
```

## Bornology and compatibility

```{prf:definition} Bornology
:label: def-bornology

A **bornology** on $X$ is a collection $\mathcal B\subseteq\mathcal P(X)$
containing every finite subset of $X$ and closed under subsets and finite unions.
Its members are called **bounded subsets**.
```

````{prf:definition} Coarse space
:label: def-coarse-space

```{include} ../_snippets/coarse-space.inc.md
```
````

The bornology is part of the data. In particular, the coarse structure and the
choice of bounded sets should both be specified when constructing an example.
The more general literature also uses *coarse space* for just $(X,\mathcal E)$;
our abbreviated terminology always retains $\mathcal B$.

## Next steps

[Coarse maps and equivalences](coarse-maps.md) describes maps between these
objects. [Roe algebras](../algebras/roe-algebras.md) explains how controlled sets
constrain operator propagation. See {ref}`bib-bunke-engel` for the bornological
framework, especially §2.1.
