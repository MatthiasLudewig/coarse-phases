(article-flasque-coarse-space)=
# Flasque coarse space

```{warning}
Agent-generated, not reviewed yet
```

A flasque space admits a controlled motion which eventually moves the entire
space away from each bounded set. Such a motion implements the coarse version
of the Eilenberg swindle.

## Definition

```{prf:definition} Flasque space
:label: def-flasque-space

A coarse space $X$ is flasque if there is a coarse map $f:X\to X$ such that:

1. $f$ is close to $\mathrm{id}_X$;
2. for every entourage $E$, the union $\bigcup_{n\geq0}(f^n\times f^n)(E)$
   is an entourage;
3. for every bounded $B\subseteq X$, there is an $N$ with $f^N(X)\cap B=\varnothing$.
```

The images $f^n(X)$ decrease with $n$, so the last condition holds for all
$n\geq N$. The shift $n\mapsto n+1$ makes $\mathbb N$ flasque. More generally,
$(x,n)\mapsto(x,n+1)$ makes $X\otimes\mathbb N$ flasque for every $X$.
Translation on $\mathbb Z$ does not witness flasqueness: it is surjective, so
no iterate moves the whole space away from a nonempty bounded set.

## Factorization of the identity through a ray

There are two closely related conventions. In Bunke–Engel the factorization
criterion characterizes **generalized flasqueness**. Ordinary flasqueness as
above supplies such a factorization, but the converse is not asserted without
an additional condition on the motion.

```{prf:definition} Generalized flasqueness
:label: def-generalized-flasqueness

A coarse space is flasque in the generalized sense if there are coarse maps
$f_n:X\to X$, $n\geq0$, with $f_0=\mathrm{id}_X$, such that
$$
\bigcup_{n\geq0}\{(f_n(x),f_{n+1}(x)):x\in X\}\in\mathcal C_X,
\qquad
\bigcup_{n\geq0}(f_n\times f_n)(E)\in\mathcal C_X
$$
for every entourage $E$, and for every bounded $B$ there is an $N$ such that
$f_n(X)\cap B=\varnothing$ for all $n\geq N$.
```

```{prf:proposition} Ray factorization criterion
:label: prop-flasque-ray-factorization

Generalized flasqueness is equivalent to the existence of a coarse map
$F:X\otimes\mathbb N\to X$ such that $F(x,0)=x$. Equivalently,
$$
\mathrm{id}_X=F\circ i_0,\qquad i_0(x)=(x,0).
$$
```

```{prf:proof}
Given the family $(f_n)$, set $F(x,n)=f_n(x)$. The first uniform control
condition controls consecutive levels, and the second controls pairs at the
same level. These generate the product coarse structure, so $F$ is controlled.
For bounded $B$, the escape condition gives
$$
F^{-1}(B)\subseteq\bigcup_{n<N} f_n^{-1}(B)\times\{n\},
$$
a bounded set. Thus $F$ is proper.

Conversely, restrict a coarse $F$ to each level to obtain $f_n$. Images under
$F\times F$ of the two kinds of product entourages give the uniform control
conditions. Since $F^{-1}(B)$ is contained in $B'\times\{0,\ldots,N\}$ for
some bounded $B'$ and finite $N$, all higher levels miss $B$.
```

For an ordinary flasqueness map, take $F(x,n)=f^n(x)$. Conversely, if a
factorization satisfies the action identity
$F(F(x,n),m)=F(x,n+m)$, then $f(x)=F(x,1)$ witnesses ordinary flasqueness.
This is the precise additional condition recovering the iterated-map definition.

## Consequence for coarse homology

A {ref}`coarse homology theory <article-coarse-homology-theory>` vanishes on
flasque spaces by definition. It also vanishes on generalized flasque spaces:
the identity on $E(X)$ factors through $E(X\otimes\mathbb N)=0$, so $E(X)$
is zero. No choice of a homology theory is needed in the factorization criterion.

## Sources

See {ref}`Bunke–Engel <bib-bunke-engel>`, Definitions 3.21 and 3.27 and
Lemma 3.28 in the supplied preprint.
