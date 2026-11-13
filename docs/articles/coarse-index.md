(article-coarse-index)=
# Coarse index

```{warning}
Agent-generated, not reviewed yet
```

The coarse index is the large-scale index class of an elliptic operator.
For a complete Riemannian manifold it takes values in the $K$-theory of the Roe algebra, without requiring the operator to be Fredholm on the whole $L^2$-space.

## Construction

Let $D$ be a self-adjoint Dirac-type operator on a Hermitian Clifford module over a complete Riemannian manifold $M$, with the usual finite propagation speed for $e^{itD}$.
Work on its $L^2$-module, enlarged to an ample module when necessary.
Let $D^*(M)$ be the norm closure of finite-propagation pseudolocal operators, where *pseudolocal* means $[T,f]$ is compact for all $f\in C_0(M)$.
Then $C^*(M)$ is an ideal in $D^*(M)$.

Choose an odd continuous normalizing function $\chi$ with $\chi(t)\to\pm1$ as $t\to\pm\infty$.
Functional calculus gives $F=\chi(D)\in D^*(M)$ and $F^2-1\in C^*(M)$.
The latter is a local compactness statement, not in general global compactness.

```{prf:definition} Coarse index
:nonumber:
:label: def-coarse-index

In the ungraded case, $p=(F+1)/2$ is a projection modulo $C^*(M)$.
The *coarse index* is
$$
\ind_{\mathrm c}(D)
 =\partial[p]\in K_1(C^*(M)),
$$
where $\partial$ is the boundary map of $0\to C^*(M)\to D^*(M)\to D^*(M)/C^*(M)\to0$.

In the graded case, write $F$ as an odd operator.
Its off-diagonal part is invertible modulo the Roe ideal, and its boundary class is $\ind_{\mathrm c}(D)\in K_0(C^*(M))$.
```

These are the odd and even complex index classes.
Changing $\chi$ does not change the class.
For a compact manifold the construction reduces to the ordinary Fredholm index.
If $D$ is uniformly invertible, one may use its sign modulo the functional calculus comparison, and the coarse index vanishes.

## Finite propagation representatives

The index also admits representatives with strict finite propagation.
Choose an odd smooth chopping function $\chi$ whose Fourier transform is compactly supported as a distribution and for which $\chi^2-1$ is rapidly decreasing.
Finite propagation speed then gives finite propagation of $F=\chi(D)$.
Under the local elliptic summability hypothesis, $(1+D^2)^{-N}$ is locally trace-class for some $N$, so $F^2-1$ is locally trace-class as well.

In even degree, write
$$
F=\begin{pmatrix}0&Q\\P&0\end{pmatrix},\qquad
S=1-QP,\quad T=1-PQ.
$$
The remainders $S,T$ are locally trace-class and have finite propagation.
An index idempotent is
$$
e_F=
\begin{pmatrix}
S^2&S(1+S)Q\\
TP&1-T^2
\end{pmatrix},\qquad
 e_0=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
$$
The identities $SQ=QT$ and $TP=PS$ imply $e_F^2=e_F$, and every entry of $e_F-e_0$ is locally trace-class with finite propagation.
Thus $[e_F]-[e_0]$ represents the even index.
This is the algebraic boundary construction applied before taking the norm closure.
The idempotent need not be self-adjoint; replacing it by an orthogonal projection can lose strict finite propagation.

In odd degree, the boundary is represented in the completed Roe algebra by $\exp(2\pi i(F+1)/2)$.
Exponentiation generally loses finite propagation.
Put $A=(F+1)/2$ and choose a polynomial $q$ satisfying $q(0)=q(1)=1$ which approximates $e^{2\pi it}$ closely enough on an interval containing $\spec(A)$ to remain nonzero there.
Then $q(A)$ is invertible, has finite propagation, and represents the same $K_1$-class by a straight-line homotopy through invertibles.
Moreover,
$$
q(A)-1=A(A-1)r(A)=\tfrac14(F^2-1)r(A)
$$
for a polynomial $r$, so the difference is locally trace-class.
The resulting representative is invertible in the completed algebra; it need not be unitary, and its inverse need not have finite propagation.
These are separate conditions from strict finite propagation of the representative.

The trace-class assertion throughout is **local**.
On a noncompact manifold it does not say that the index representative differs from a scalar operator by a globally trace-class operator.

## Relation to coarse K-theory

The index lies in {ref}`coarse K-theory <article-coarse-k-theory>` and can be paired, through suitable Chern character constructions, with {ref}`partition cohomology classes <article-coarse-transversality>`.
The {ref}`cone construction <article-coarse-homology-theory>` provides a homological formulation of the passage from local symbol data to the coarse index.
Positivity away from a {prf:ref}`big family <def-big-family>` leads to localized index classes, as developed in [Bunke–Ludewig, Coronas and Callias type operators in coarse geometry](https://arxiv.org/abs/2411.01646).
