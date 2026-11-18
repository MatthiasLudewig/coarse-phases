(theorem-mixed-gapped-ground-state)=
# A mixed gapped ground state for a controlled spin derivation

```{warning}
Agent-generated, not reviewed yet
```

This page constructs a mixed state satisfying the {prf:ref}`nondegenerate gap inequality <def-gapped-ground-state>` for a {prf:ref}`controlled derivation <def-controlled-derivation>` on the full local algebra of a {prf:ref}`quantum spin system <def-quantum-spin-system>`.
The interactions are between adjacent sites, but their norms grow without bound.
The proof below includes the construction of the couplings, the uniform gap estimate, and the failure of the derivation's closure to generate dynamics.

## Statement

```{prf:theorem} A mixed algebraic gapped ground state on a qubit chain
:nonumber:
:label: thm-mixed-gapped-ground-state

Let $X=\{1,2,\ldots\}$, equipped with the bornology $\cB$ of finite subsets and the metric coarse structure $\cC$ associated to $d(m,n)=|m-n|$.
Consider the qubit spin system on $(X,\cB,\cC)$ with
$$
\begin{aligned}
\cA_{[1,n]}&=\bigotimes_{j=1}^n\Mat_2(\C),\\
\cA_{\mathrm{loc}}:=\cA_X^{\mathrm{alg}}&=\bigcup_{n\geq1}\cA_{[1,n]},
\qquad \cA_X=\overline{\cA_{\mathrm{loc}}}.
\end{aligned}
$$
Let $S_n$ exchange the tensor factors at sites $n$ and $n+1$, and set $h_n=1-S_n$.
For a unit vector $v\in\C^2$, let $\omega_v$ be the product state with every site in $v$, and let $\mu$ be normalized unitary-invariant measure on the unit sphere $S^3\subset\C^2$.

There are finite positive real numbers $J_n$, with $J_n\to\infty$, such that
$$
D(a)=i\sum_{n\geq1}J_n[h_n,a],
\qquad \dom(D)=\cA_{\mathrm{loc}},
$$
is a controlled $*$-derivation and the state
$$
\omega(a)=\int_{S^3}\omega_v(a)\,d\mu(v)
$$
is mixed and satisfies
$$
-i\omega(a^*D(a))\geq\omega(a^*a)-|\omega(a)|^2
\qquad(a\in\cA_{\mathrm{loc}}).
$$
The derivation is controlled by $E=\{(m,n)\in X\times X\mid |m-n|\leq1\}$, is closable in norm, and its closure does not generate a strongly continuous group of $*$-automorphisms of $\cA_X$.
```

The gap in this statement is the algebraic inequality with constant $1$ on every local observable.
The proof does not assume a time evolution, and the inequality is not restricted to self-adjoint observables.

## The state and the local energy

For $a\in\cA_{[1,n]}$, the state in the statement is given concretely by
$$
\omega(a)=\int_{S^3}\langle v^{\otimes n},a v^{\otimes n}\rangle\,d\mu(v).
$$
These positive normalized functionals are compatible with $a\mapsto a\otimes1$, so they define a state on the local algebra and extend continuously to $\cA_X$.

To see that $\omega$ is not {prf:ref}`pure <def-pure-state>`, write $v=(z,w)$ and split the sphere into the sets $U_\pm=\{(z,w)\in S^3\mid\pm(|z|^2-|w|^2)>0\}$.
They have equal measure, and their complement has measure zero.
The normalized conditional averages
$$
\omega_\pm(a)=2\int_{U_\pm}\omega_v(a)\,d\mu(v)
$$
give $\omega=\tfrac12\omega_++\tfrac12\omega_-$.
For the first-site observable $Z_1=\operatorname{diag}(1,-1)\otimes1\otimes\cdots$, one has
$$
\omega_+(Z_1)>0>\omega_-(Z_1),
$$
because $\omega_v(Z_1)=|z|^2-|w|^2$.
Thus this is a nontrivial convex decomposition into states on the whole quasi-local algebra.

For any choice of finite positive couplings, $D$ is well-defined on the entire local algebra: only bonds meeting the support of $a$ contribute to $D(a)$.
The Leibniz rule and $D(a^*)=D(a)^*$ follow from the corresponding identities for each commutator, with only finitely many terms involved for any fixed pair of local observables.
For every finite $B\subseteq X$,
$$
D(\cA_B)\subseteq\cA_{B_E}.
$$
In particular, $D$ maps the local algebra into itself.
The family of bond supports $\{n,n+1\}$ is locally finite and uniformly bounded in the coarse sense, irrespective of the sizes of the coefficients $J_n$.

The swap is a self-adjoint unitary, so $h_n\geq0$ and $\|h_n\|=2$.
Moreover, $h_n$ annihilates every constant product vector on a finite interval containing its support.
It follows that $\omega(h_n a)=\omega(a h_n)=0$ for every local $a$, and hence $\omega(D(a))=0$.
For $a\in\cA_{[1,n]}$, expanding the commutators gives
$$
q(a):=-i\omega(a^*D(a))
=\sum_{j=1}^nJ_j\omega(a^*h_j a)\geq0.
$$
All terms with $j>n$ vanish.
The remaining task is to bound this energy uniformly below by the variance.

## Finite local GNS spaces

Let $(\cH,\pi,\Omega)$ be the {prf:ref}`GNS representation <def-gns-representation>` of $\omega$, and put
$$
\cK_n=\pi(\cA_{[1,n]})\Omega,
\qquad \cK_0=\C\Omega.
$$
Each $\cK_n$ is finite-dimensional, and their union is dense in $\cH$.
For $a\in\cA_{[1,n]}$, the vector $\pi(a)\Omega$ can be represented by the homogeneous vector-valued polynomial
$$
F_a(v)=a v^{\otimes n}\in V_n,
\qquad V_n=(\C^2)^{\otimes n},\quad V_0=\C,
$$
with inner product
$$
\langle F_a,F_b\rangle
=\int_{S^3}\langle F_a(v),F_b(v)\rangle\,d\mu(v)
=\omega(a^*b).
$$
Thus this description identifies precisely the vectors that are identified in the GNS construction.
Every $V_n$-valued homogeneous polynomial of degree $n$ in $z,w$ occurs: its coefficients specify a linear map from the symmetric tensor subspace of $V_n$ to $V_n$, and that map extends to an operator on $V_n$.
A polynomial with zero norm vanishes everywhere on $S^3$, by continuity and the full support of $\mu$, and then vanishes identically by homogeneity.

Under this identification the inclusion $\cK_{n-1}\subseteq\cK_n$ is the isometry
$$
G(v)\longmapsto G(v)\otimes v.
$$
The cyclic vector is represented by $\Omega_n(v)=v^{\otimes n}$.
Writing $P_\Omega$ for the orthogonal projection onto its span, we have
$$
\omega(a^*a)-|\omega(a)|^2
=\|(1-P_\Omega)F_a\|^2.
$$
The desired gap is therefore a lower bound on the energy of these centered local vectors.

## The boundary energy detects the new local directions

Let $B_n$ be the positive operator on $\cK_n$ determined by the quadratic form
$$
\langle F,B_nF\rangle
=\int_{S^3}\langle F(v)\otimes v,
h_n(F(v)\otimes v)\rangle\,d\mu(v).
$$
Equivalently, $B_n$ is the compression of $\pi(h_n)$ to $\cK_n$.
It is independent of the couplings $J_j$.

```{prf:lemma} Kernel of the boundary energy
:nonumber:
:label: lem-ferromagnet-boundary-kernel

For every $n\geq1$, the kernel of $B_n$ is the embedded subspace $\cK_{n-1}\subseteq\cK_n$.
```

```{prf:proof}
Let $e_0,e_1$ be the standard basis of $\C^2$ and write
$$
F(z,w)=F_0(z,w)\otimes e_0+F_1(z,w)\otimes e_1,
$$
where $F_0,F_1$ take values in $V_{n-1}$ and are homogeneous of degree $n$.
Since $1-S_n$ is twice the projection onto the antisymmetric part of the last two tensor factors, direct expansion gives
$$
\langle F,B_nF\rangle
=\int_{S^3}\|wF_0(z,w)-zF_1(z,w)\|^2\,d\mu(v).
$$
If this integral vanishes, its continuous nonnegative integrand vanishes on the whole sphere.
Homogeneity then gives the polynomial identity $wF_0=zF_1$ on $\C^2$.
Applying divisibility in $\C[z,w]$ to each component, the fact that $z$ and $w$ are relatively prime implies
$$
F_0=zG,\qquad F_1=wG
$$
for a $V_{n-1}$-valued homogeneous polynomial $G$ of degree $n-1$.
Hence $F(v)=G(v)\otimes v$, which is exactly a vector from $\cK_{n-1}$.
Conversely, every vector of this form has zero boundary energy.
```

The kernel is a proper subspace, so the smallest positive eigenvalue
$$
b_n=\min\spec\bigl(B_n|_{\cK_{n-1}^{\perp}}\bigr)
$$
is well-defined and strictly positive, where the orthogonal complement is taken inside $\cK_n$.
For example, $\dim\cK_n=2^n(n+1)$, whereas $\dim\cK_{n-1}=2^{n-1}n$.
No lower bound uniform in $n$ is needed for the construction.

## Choosing the couplings

We use the following elementary finite-dimensional estimate to control the interaction between the old local space and its orthogonal complement.

```{prf:lemma} A positive penalty preserves a smaller gap
:nonumber:
:label: lem-ferromagnet-penalty

Let $\cK$ be a finite-dimensional Hilbert space, let $\Omega\in\cK$ be a unit vector, and let $V\subseteq\cK$ contain $\Omega$.
Suppose that $L,B\geq0$, $L\Omega=0$, $\ker B=V$, and $B\geq b$ on $V^\perp$ for some $b>0$.
Suppose also that $\|L\|\leq M$ and
$$
\langle x,Lx\rangle\geq\gamma_{\mathrm{old}}\|x\|^2
\qquad(x\in V\cap\Omega^\perp).
$$
For $0<\gamma<\gamma_{\mathrm{old}}$, the inequality
$$
Jb\geq\gamma+\frac{M^2}{\gamma_{\mathrm{old}}-\gamma}
$$
implies $L+JB\geq\gamma(1-P_\Omega)$ on $\cK$.
```

```{prf:proof}
For a centered vector write $F=x+y$, with $x\in V\cap\Omega^\perp$ and $y\in V^\perp$.
Positivity of $L$ and the norm bound give
$$
\langle F,(L+JB)F\rangle
\geq\gamma_{\mathrm{old}}\|x\|^2-2M\|x\|\|y\|+Jb\|y\|^2.
$$
Put $\varepsilon=\gamma_{\mathrm{old}}-\gamma$ and use
$$
2M\|x\|\|y\|\leq\varepsilon\|x\|^2+\frac{M^2}{\varepsilon}\|y\|^2.
$$
The assumed bound on $J$ makes the resulting expression at least $\gamma(\|x\|^2+\|y\|^2)$.
Both $L$ and $B$ annihilate $\Omega$, so the same operator inequality holds on all of $\cK$.
```

Set
$$
\gamma_n=1+2^{-n},
\qquad J_1=\frac{\gamma_1}{b_1}.
$$
Since $\ker B_1=\cK_0=\C\Omega$, this gives the required gap $\gamma_1$ on $\cK_1$.
Having chosen $J_1,\ldots,J_{n-1}$ for $n\geq2$, put
$$
\begin{aligned}
M_n&=2\sum_{j=1}^{n-1}J_j,
\qquad \varepsilon_n=\gamma_{n-1}-\gamma_n=2^{-n},\\
J_n&=\max\left\{n,\frac{\gamma_n+M_n^2/\varepsilon_n}{b_n}\right\}.
\end{aligned}
$$
This is a recursive prescription involving only finite-dimensional matrices and previously chosen numbers.
Every $J_n$ is finite and positive, and $J_n\geq n$ for $n\geq2$.

To verify the induction, the energy from the earlier bonds on $\cK_n$ is represented by
$$
L_n=\left.\sum_{j=1}^{n-1}J_j\pi(h_j)\right|_{\cK_n}.
$$
These bonds lie inside $[1,n]$, so each $\pi(h_j)$ preserves $\cK_n$.
Consequently $L_n\geq0$, $L_n\Omega=0$, and $\|L_n\|\leq M_n$.
For $a\in\cA_{[1,n]}$,
$$
q(a)=\langle F_a,(L_n+J_nB_n)F_a\rangle.
$$
The compression of $L_n$ to $\cK_{n-1}$ is exactly the energy operator constructed at the preceding stage.
Indeed, for $a\in\cA_{[1,n-1]}$, the same sum over $j\leq n-1$ computes its energy, with the bond $j=n-1$ serving as the previous boundary bond.
The new bond $j=n$ has zero energy on these vectors by the boundary-kernel lemma.

Assuming the gap $\gamma_{n-1}$ at the preceding stage, apply the {prf:ref}`penalty estimate <lem-ferromagnet-penalty>` with $V=\cK_{n-1}$, $B=B_n$, and $L=L_n$.
Our choice of $J_n$ gives
$$
q(a)\geq\gamma_n\|(1-P_\Omega)F_a\|^2
\geq\omega(a^*a)-|\omega(a)|^2
\qquad(a\in\cA_{[1,n]}).
$$
Every local observable belongs to one of these finite matrix algebras, so this proves the claimed uniform gap on the full local algebra.
In particular, the argument includes arbitrary nonnormal local observables.

## Closability and the absence of generated dynamics

We first check closability, so that the obstruction concerns the closure of the derivation as well as its initial domain.
Stationarity and the $*$-derivation rule imply, for local $a,b$,
$$
\langle\pi(b)\Omega,-i\pi(D(a))\Omega\rangle
=\langle-i\pi(D(b))\Omega,\pi(a)\Omega\rangle.
$$
If $\pi(a)\Omega=0$, the right-hand side vanishes for every local $b$; density therefore gives $\pi(D(a))\Omega=0$.
Thus
$$
H_0\pi(a)\Omega=-i\pi(D(a))\Omega,
\qquad \dom(H_0)=\pi(\cA_{\mathrm{loc}})\Omega,
$$
defines a densely defined symmetric operator.
It is nonnegative by the energy calculation and is closable because it is symmetric.

Suppose that $a_k\in\cA_{\mathrm{loc}}$, $a_k\to0$, and $D(a_k)\to b$ in the $C^*$-norm.
For each fixed local $c$, one has $\pi(a_kc)\Omega\to0$ and
$$
H_0\pi(a_kc)\Omega
=-i\pi\bigl(D(a_k)c+a_kD(c)\bigr)\Omega
\longrightarrow-i\pi(bc)\Omega.
$$
Closability of $H_0$ implies $\pi(bc)\Omega=0$ for every local $c$, hence $\pi(b)=0$ by density.
The representation $\pi$ is faithful: its unital restriction to each full matrix algebra $\cA_{[1,n]}$ is injective and therefore isometric, and the union of these algebras is norm-dense in $\cA_X$.
It follows that $b=0$, proving that $D$ is closable in norm.
The gap inequality passes to $\dom(\overline D)$ by approximation in the graph norm, since both sides are continuous under $a_k\to a$ and $D(a_k)\to\overline D(a)$.

If $\overline D$ generated a strongly continuous automorphism group, $\cA_{\mathrm{loc}}$ would be a core for its generator by the definition of graph closure.
The {prf:ref}`GNS gap characterization <thm-gapped-ground-state-hamiltonian>` and the {ref}`purity theorem <theorem-nondegenerate-ground-state-pure>` would then make $\omega$ pure, contradicting its explicit convex decomposition above.
Therefore $\overline D$ does not generate such a group.
This finishes the proof of the theorem.

## Role of the control condition

The support of each interaction $J_nh_n$ is the fixed-size bond $\{n,n+1\}$, while $\|J_nh_n\|=2J_n\to\infty$.
Thus support control permits the growing coefficients used in the induction.
At each stage the boundary term penalizes the new local GNS directions, and the previously chosen terms control the kernel of that boundary energy.
The decreasing target gaps remain above $1$, which makes the estimate uniform over all finite supports.

