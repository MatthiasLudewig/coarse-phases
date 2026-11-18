(article-ground-state)=
# Ground state

A physical system is in its ground state if it has the least amount of energy.
As the primitive mathematical formulation, we take one using the notions of {prf:ref}`state <def-state>` and {prf:ref}`derivation <def-state>` on a $C^*$-algebra.
A posteriori, this is related to the lowest spectral level of the Hamiltonian governing the physical system.

## Definition

Let $A$ be a unital $C^*$-algebra.

```{prf:definition} Ground state of a derivation
:nonumber:
:label: def-ground-state-derivation

Let $D$ be a {prf:ref}`derivation <def-derivation>` on $A$. 
A {prf:ref}`state <def-state>` $\omega$ is a *ground state* for $D$ if
$$
-i\omega(a^*D(a)) \geq 0, \qquad a \in \dom(D).
$$
In particular, the left hand side is required to be real.
```

Every ground state $\omega$ for a derivation $D$ is *stationary for the derivation*, meaning that 
$$
\omega(D(a))=0, \qquad  a \in \dom(D).
$$

````{dropdown} Proof
:class-container: proof-dropdown

Let $z \in \C$. 
We calculate
$$
\begin{aligned}
0 \leq - i \omega((a + z)^*D(a + z)) 
&= - i \omega((a^* + \overline{z})D(a)) 
\\
&= - i \omega(a^*D(a)) - i \overline{z} \omega(D(a)).
\end{aligned}
$$
Since $\omega$ is an algebraic ground state for $D$, the whole expression must be real and so is the first term on the right-hand-side. 
As this holds for any $z \in \C$, this forces $\omega(D(a))$ to vanish.
````

(article-ground-state-energy-of-hamiltonian)=
## Energy of Hamiltonian.

Let $A$ be a $C^*$-algebra with a {prf:ref}`derivation <def-derivation>` $D$ and let $\omega$ be a {prf:ref}`state <def-state>` for $D$ that annihilates $D$, that is
$$
\omega(D(a)) = 0, \qquad a \in A.
$$

Assume that $D$ generates a strongly continuous group $(\alpha_t)_{t \in \R}$ of $*$-automorphisms of $A$, a condition that may not be satisfied in general.  
Since $\omega$ annihilates $D$, $(\alpha_t)_{t \in \R}$ preserves $\omega$.

Let $(\cH, \pi, \Omega)$ be the GNS-representation of $\omega$. 
Then
$$
U_t \pi(b)\Omega := \pi(\alpha_t(b))\Omega, \qquad b \in A,
$$
defines a strongly continuous group of unitaries on $\cH$, which implements $\alpha_t$ on $\cH$ in the sense that
```{math}
label : eq-ground-state-implementation
U_t\pi(b)U_t^* = \pi(\alpha_t(b)), \qquad b \in A
```
Write $U_t = e^{itH}$ with a possibly unbounded self-adjoint operator $H$ on $\cH$.

```{prf:theorem} Ground state theorem
:nonumber:
:label: thm-ground-state-Hamilonian

$\omega$ is a ground state for $D$ if and only if the Hamiltonian $H$ is a positive operator,
$$
\langle \xi, H\xi\rangle \geq 0, \qquad \xi \in \cH.
$$
```

````{dropdown} Proof
:class-container: proof-dropdown

The derivation $D$ is implemented by $H$ in the sense that
$$
\pi(D(a)) = i [H, \pi(a)], \qquad a \in \dom(A).
$$
Here it is easy to see that $\pi(a)\Omega \in \dom(H)$ whenever $a \in \dom(D)$.
Putting $a = 1$ in {eq}`eq-ground-state-implementation` yields that $U_t\Omega = \Omega$, hence $\Omega \in \dom(H)$ with $H\Omega = 0$. 
For $a \in \dom(D)$, one now calculates
$$
\begin{aligned}
- i \omega(a^*D(a)) 
&= - i\langle \pi(a)\Omega, \pi(Da)\Omega \rangle
\\
&= - i\langle \pi(a)\Omega, i [H, \pi(a)]\Omega \rangle
\\
&= \langle \pi(a)\Omega, H \pi(a)\Omega \rangle - \langle \pi(a)\Omega, \pi(a)H\Omega \rangle
\\
&= \langle \pi(a)\Omega, H \pi(a)\Omega \rangle.
\end{aligned}
$$
Hence if $H$ is positive, then $D$ is a ground state.
Conversely, if $D$ is a ground state, then the left hand side in the equality above is non-negative, hence $H$ is positive on $\pi(a)$. 
[Finish proof]
````

A ground state need not be pure.
For example, when $D=0$, every state is a ground state.
However, if $\omega$ is a ground state for a derivation $D$ that generates a 1-parameter group of $*$-automorphisms such that the associated Hamiltonian $H$ has a one-dimensional ground state, then the {ref}`purity theorem <theorem-nondegenerate-ground-state-pure>` states that $\omega$ is necessarily pure. 
This is, for example, true for a {ref}`Gapped ground state article <gapped-ground-state-purity>`.