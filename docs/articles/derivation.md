---
stub: true
---

(article-derivation)=
# Derivation

```{warning}
Agent-generated, not reviewed yet
```

## Definition

Let $A$ be a unital $C^*$-algebra.

```{prf:definition} Derivation
:nonumber:
:label: def-derivation

A *derivation* of $A$ is a densely defined linear map $D:A \supseteq \dom(D)\to A$ satisfying
$$
D(ab)=D(a)b+aD(b),\qquad D(a^*)=D(a)^*.
$$
```

The first condition is the algebraic condition of being a derivation, which makes sense on any algebra; the second condition is the compatibility with the star operation.

Derivations on a $C^*$-algebra $A$ arise, as infinitesimal generators of strongly continuous 1-parameter groups of $*$-automorphisms $(\alpha_t)_{t \in \R}$ (meaning that $\alpha_t(a)$ is norm-continuous in $t$ for all fixed $a \in A$).
Concretely, for any such 1-parameter group, the operator
$$
D(a) := \lim_{t \to 0} \frac{1}{t} (\alpha_t(a) - a)
$$
is a derivation on $A$ with domain $\dom(D)$ the set of all $a \in A$ for which the limit exists.
Such a derivation is necessarily a closed operator, possibly unbounded; conversely, however, not every closed derivation generates a 1-parameter group of $*$-automorphisms.

## Bounded derivations on simple unital algebras

Let $A$ be a unital $C^*$-algebra.
A derivation $D:A\to A$ is *inner* if there is an element $b\in A$ such that 
$$
D(a)=[b,a]=ba-ab, \qquad a \in A.
$$
The identity $D(a^*) = D(a)^*$ implies that the element $b$ is necessarily skew-adjoint.
Typically, it is written as $b =ih$ with $h \in A$ self-adjoint.

The following gives a motivation to consider unbounded derivations.

```{prf:theorem} Sakai's innerness theorem
:nonumber:
:label: thm-sakai-simple-unital-derivations

If $A$ is simple, then any bounded derivation on $A$ is inner.
```

The proof is omitted here; see [Sakai, *Derivations of simple $C^*$-algebras, II*, p. 259 and the theorem in Section 2](https://www.numdam.org/article/BSMF_1971__99__259_0.pdf) ({ref}`bibliographic details <bib-sakai-simple-derivations>`).

