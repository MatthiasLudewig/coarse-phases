(article-topological-phases)=
# From locality to topological phases

Coarse geometry provides a language for locality without requiring translation
symmetry. The basic route is to choose a space, encode controlled operators in
an algebra, and study invariants of suitable Hamiltonians in that algebra.
See {ref}`bib-ewert-meyer` for a Roe-algebra approach to disordered systems.

## A simple gapped setting

For orientation, let $A\subseteq\mathcal B(H)$ be a **unital** complex
$C^*$-algebra and $h=h^*\in A$ a bounded Hamiltonian. Suppose the Fermi energy
$\mu$ is outside the spectrum of $h$. Functional calculus gives the projection

```{math}
:label: eq-fermi-projection

p=\mathbf 1_{(-\infty,\mu)}(h)\in A.
```

Although the characteristic function is discontinuous on $\mathbb R$, its
restriction to the gapped spectrum is continuous. The projection defines a
class $[p]\in K_0(A)$. Here $K_0(A)$ is formed from stable equivalence classes
of projections in matrix algebras over $A$, followed by group completion.

If $h_t$ is a norm-continuous path with a common open gap around $\mu$, choose
one continuous function that is one below the gap and zero above it. Applying
it to each $h_t$ gives a norm-continuous path of projections. Consequently the
$K_0$ class is unchanged along this path.

## Where geometry enters

The choice of $A$ determines which locality conditions and deformations are
allowed. [Roe algebras](../algebras/roe-algebras.md) use the controlled sets of
the underlying {prf:ref}`coarse space <def-coarse-space>` to encode propagation.
The Roe algebra in that article is generally nonunital. Applying the simple
picture above to it requires specifying the Hamiltonian's algebra or multiplier
algebra and checking where the spectral projection, or its difference from a
reference projection, belongs. This is an additional step in a physical model.

## Scope of this introduction

The paragraph above concerns bounded one-particle Hamiltonians without added
symmetry constraints. Real structures, symmetries, interacting systems, and
quantum cellular automata require further definitions. This draft does not
assert a classification theorem for those settings.

For the geometric foundations, start with
[Coarse spaces: the idea](../geometry/coarse-spaces.md). For source material,
see the [reading list](../bibliography/index.md).
