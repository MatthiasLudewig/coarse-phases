(article-state)=
# State

States are certain linear functionals on a $C^*$-algebra.
In the Heisenberg model of quantum mechanics where the $C^*$-algebra is viewed as the observable algebra of a quantum system, a state describes the state of the quantum system.

## States and their topology

Let $A$ be a not necessarily unital complex $C^*$-algebra.

```{prf:definition} State
:nonumber:
:label: def-state

A *state* on $A$ is a positive linear functional $\omega:A\to\C$ of norm one.
Here *positivity* means that $\omega(a^*a)\geq0$ for every $a\in A$.
The set of states is denoted by $S(A)$.
```

Positive linear functionals on a $C^*$-algebra are automatically bounded.
If $A$ is unital, positivity gives $\|\omega\|=\omega(1)$, so the normalization is equivalently $\omega(1)=1$.

```{prf:definition} Weak-* topology on the state space
:nonumber:
:label: def-state-space

The *state space* $S(A)$ carries the subspace topology inherited from the weak-* topology $\sigma(A^*,A)$ on the Banach dual.
```

Concretely, a net $(\omega_i)_{i \in I}$ in $S(A)$ converges to $\omega$ precisely when
$$
\lim_{i \in I} \omega_i(a)=\omega(a)\qquad\text{for every }a\in A.
$$
$S(A)$ is a convex subset of the dual space $A^*$.
For unital $A$, it is weak-* compact.
If $A$ is also separable, this topology is metrizable.

## Examples

For $A=\Mat_n(\C)$, every state has the form
$$
\omega(a)=\Tr(\rho a),\qquad\rho\geq0,\quad\Tr(\rho)=1.
$$
The positive matrix $\rho$ of trace one is called the *density matrix* of the state.
For $A=C(K)$ with $K$ compact Hausdorff, states correspond to probability measures on $K$, with expectation
$$
\omega(f)=\int_K f\,d\mu.
$$
The {ref}`Pure state article <article-pure-state>` describes the extreme points in these examples.

## The GNS representation

```{prf:definition} GNS representation
:nonumber:
:label: def-gns-representation

The *Gelfand–Naimark–Segal representation* of a state $\omega$ is a triple $(\cH,\pi,\Omega)$ consisting of a Hilbert space, a nondegenerate $*$-representation $\pi:A\to\mathbf{B}(\cH)$, and a cyclic unit vector $\Omega$ such that
$$
\omega(a)=\langle\Omega,\pi(a)\Omega\rangle.
$$
```

Inner products here are linear in the second variable.
Cyclicity of $\Omega$ means that the set $\{\pi(a)\Omega \mid a\in A\}$ is dense in $\cH$.
The triple $(\cH,\pi,\Omega)$ is unique up to a unitary intertwiner preserving cyclic vectors.

For unital $A$, $\cH$ is obtained by forming the quotient of $A$ by the left ideal $\{a\in A \mid \omega(a^*a)=0\}$ and then completing it with respect to the inner product $\langle[a],[b]\rangle=\omega(a^*b)$.
Then $\pi$ is given by left multiplication and $\Omega=[1]$.
