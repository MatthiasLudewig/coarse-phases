(theorem-pure-gapped-ground-state-nonunique-dynamics)=
# A pure gapped spin ground state with nonunique dynamics

```{warning}
Agent-generated, not reviewed yet
```

A pure algebraic gapped ground state need not determine a unique extension of its derivation to the generator of dynamics.
This page gives an example on a qubit half-chain, with a {prf:ref}`controlled derivation <def-controlled-derivation>` defined on every local observable.
Two different closed extensions generate strongly continuous automorphism groups, and the same pure product state is a nondegenerate gapped ground state for both.
The proof is supplied below, using the cited Friedrichs–Krein extension theorem.

This complements the {ref}`mixed gapped ground-state example <theorem-mixed-gapped-ground-state>`: imposing purity still leaves an analytic extension problem.

## Statement

```{prf:theorem} A pure product ground state with two generating extensions
:nonumber:
:label: thm-pure-gapped-ground-state-nonunique-dynamics

Let $X=\{1,2,\ldots\}$ have the bornology $\cB$ of finite subsets and the metric coarse structure $\cC$ for $d(m,n)=|m-n|$.
Consider the qubit {prf:ref}`spin system <def-quantum-spin-system>` on $(X,\cB,\cC)$, with
$$
\cA_{\mathrm{loc}}=\bigcup_{m\geq1}\bigotimes_{n=1}^m\Mat_2(\C),
\qquad
\cA_X=\overline{\cA_{\mathrm{loc}}}.
$$
At site $n$, write $\sigma_n^+=|1\rangle\langle0|$, $\sigma_n^-=(\sigma_n^+)^*$, and $N_n=\sigma_n^+\sigma_n^-$.
Define
$$
\begin{aligned}
D(a)&=i\sum_{n\geq1}(1+4^n)[N_n,a]\\
&\quad+i\sum_{n\geq1}4^n
[\sigma_n^+\sigma_{n+1}^-+\sigma_n^-\sigma_{n+1}^+,a],\\
\dom(D)&=\cA_{\mathrm{loc}}.
\end{aligned}
$$
Both sums are finite for each local $a$.
Let $\omega$ be the product state with every site in $|0\rangle$.

Then $D$ is a norm-closable $*$-derivation controlled by
$$
E=\{(m,n)\in X\times X\mid |m-n|\leq1\},
$$
and $\omega$ is pure and satisfies the {prf:ref}`nondegenerate gap inequality <def-gapped-ground-state>`
$$
-i\omega(a^*D(a))
\geq\omega(a^*a)-|\omega(a)|^2
\qquad(a\in\cA_{\mathrm{loc}}).
$$
There are distinct closed $*$-derivations $\delta_F,\delta_K$ on $\cA_X$ with $D\subseteq\delta_F,\delta_K$, each generating a strongly continuous group of $*$-automorphisms.
The same state $\omega$ is invariant and satisfies the gap inequality with constant $1$ on the full domain of each generator.
The graph closure $\overline D$ does not itself generate an automorphism group, and $\cA_{\mathrm{loc}}$ is a core for neither $\delta_F$ nor $\delta_K$.
```

The coefficients are not uniformly bounded.
The control assertion concerns the supports of $D(a)$, as in the definition of a controlled derivation.

## A positive one-particle operator with two extensions

Put $\mathfrak h=\ell^2(X)$, and let $c_{00}(X)$ denote its finitely supported sequences.
On this dense domain define the symmetric operator
$$
(S_0u)_n=4^{n-1}u_{n-1}+4^nu_n+4^nu_{n+1},
\qquad u_0=0.
$$
The coefficients on opposite sides of each off-diagonal matrix entry agree, so symmetry follows by a finite summation.
The operator maps $c_{00}(X)$ into itself.

For $u\in c_{00}(X)$ set $v_n=(-2)^nu_n$ and $v_0=0$.
Expanding the squares gives
$$
\langle u,S_0u\rangle
=\frac12\sum_{n\geq0}|v_{n+1}-v_n|^2.
$$
In particular the term with $n=0$ is included; it supplies part of the diagonal coefficient at the first site.
Since $v_n=\sum_{k=0}^{n-1}(v_{k+1}-v_k)$, the Cauchy–Schwarz inequality gives
$$
\begin{aligned}
\|u\|^2
&=\sum_{n\geq1}4^{-n}|v_n|^2\\
&\leq\left(\sum_{n\geq1}n4^{-n}\right)
\sum_{k\geq0}|v_{k+1}-v_k|^2\\
&=\frac89\langle u,S_0u\rangle.
\end{aligned}
$$
Thus $S_0\geq9/8$, and the same lower bound holds for its closure $S=\overline{S_0}$.

Consider now the nonzero vector
$$
p_n=n(-2)^{-n}.
$$
It belongs to $\ell^2(X)$, and substitution in the difference expression gives zero at every site, including the first site with $p_0=0$.
For each finitely supported $u$, finite summation therefore gives $\langle S_0u,p\rangle=0$.
Consequently
$$
p\in\dom(S_0^*)=\dom(S^*),
\qquad S^*p=0.
$$
If $S$ were self-adjoint, its strictly positive lower bound would exclude this kernel vector.
Hence $S_0$ is not essentially self-adjoint.

We use the Friedrichs–Krein extension theorem for a densely defined closed symmetric operator $S\geq c>0$.
Its Friedrichs extension $S_F$ is self-adjoint with $S_F\geq c$, and its Krein extension $S_K$ is nonnegative and satisfies
$$
\dom(S_K)=\dom(S)\dotplus\ker(S^*),
\qquad S_K=S^*|_{\dom(S_K)}.
$$
This extension theorem is used without proof; see [Ananieva–Goloshchapova, Introduction, especially equation (2)](https://arxiv.org/pdf/1701.06371#page=1) ({ref}`bibliographic details <bib-extremal-jacobi-extensions>`).
Applied here, it gives
$$
S_F\geq\frac98,\qquad S_K\geq0,\qquad S_Kp=0.
$$
Thus the two extensions are distinct.
Set
$$
h_0=1+S_0,\qquad h_F=1+S_F,\qquad h_K=1+S_K.
$$
Both $h_F$ and $h_K$ extend $h_0$ and satisfy $h_\bullet\geq1$, but $h_F\neq h_K$.

## From the one-particle operator to the spin derivation

Put $Z_n=1-2N_n$ and introduce the Jordan–Wigner operators
$$
c_n=\left(\prod_{j<n}Z_j\right)\sigma_n^-.
$$
They satisfy the canonical anticommutation relations
$$
c_mc_n+c_nc_m=0,
\qquad
c_mc_n^*+c_n^*c_m=\delta_{mn}1.
$$
Indeed, $Z_n$ anticommutes with $\sigma_n^\pm$, while operators on different spin sites commute.
Also $c_n^*c_n=N_n$.
The inverse formulas $Z_n=1-2c_n^*c_n$ and $\sigma_n^-=(\prod_{j<n}Z_j)c_n$ show that $c_1,\ldots,c_m$ generate exactly $\cA_{[1,m]}$.
Thus the full spin algebra is the CAR algebra over $\mathfrak h$, and its entire local algebra consists of polynomials in finitely many $c_n,c_n^*$.

The adjacent hopping terms have no remaining strings:
$$
c_n^*c_{n+1}=\sigma_n^+\sigma_{n+1}^-,
\qquad
c_{n+1}^*c_n=\sigma_n^-\sigma_{n+1}^+.
$$
Accordingly, the formal quadratic expression associated to $h_0$ is
$$
\sum_{n\geq1}(1+4^n)c_n^*c_n
+\sum_{n\geq1}4^n(c_n^*c_{n+1}+c_{n+1}^*c_n),
$$
whose commutator on local observables is exactly the stated $D$.
No norm-convergent infinite Hamiltonian in $\cA_X$ is asserted or needed.

In spin coordinates, each term acts on either a single site or an adjacent pair.
Only finitely many such terms meet a fixed finite support, so $D$ is defined on every local observable and satisfies the Leibniz and $*$ rules.
For every finite $B\subseteq X$,
$$
D(\cA_B)\subseteq\cA_{B_E}.
$$
This proves the claimed support control, including for observables supported on nonconsecutive sites.

## Two strongly continuous automorphism groups

For finitely supported $f=\sum_n f_ne_n$, write $c^*(f)=\sum_n f_nc_n^*$ and $c(f)=c^*(f)^*$.
Represent these operators as creation and annihilation operators on the antisymmetric Fock space
$$
\cF=\bigoplus_{r\geq0}\bigwedge\nolimits^r\mathfrak h,
\qquad \Omega=1\in\bigwedge\nolimits^0\mathfrak h=\C.
$$
This is a faithful representation $\pi$ of the spin algebra: its unital restriction to each finite full matrix algebra is injective and isometric, and these algebras have norm-dense union.
The CAR give $\|c^*(f)\|\leq\|f\|$, and equality follows from $\|c^*(f)\Omega\|=\|f\|$.
Thus $c^*(f)$ and $c(f)$ extend by norm continuity to all $f\in\mathfrak h$.

For $\bullet\in\{F,K\}$, let $U_t^\bullet=e^{ith_\bullet}$ and let
$$
\Gamma(U_t^\bullet)=\bigoplus_{r\geq0}\bigwedge\nolimits^r U_t^\bullet.
$$
Strong continuity on finite wedge vectors extends to all of $\cF$ by density and the unitary norm bound.
On each wedge vector, conjugation by this unitary sends $c^*(f)$ to $c^*(U_t^\bullet f)$.
It therefore preserves the represented CAR algebra, and its inverse is conjugation by $\Gamma(U_{-t}^\bullet)$.
Faithfulness gives an automorphism $\alpha_t^\bullet$ of $\cA_X$ characterized by
$$
\alpha_t^\bullet(c^*(f))=c^*(e^{ith_\bullet}f).
$$
For each generator $c^*(f)$,
$$
\|\alpha_t^\bullet(c^*(f))-c^*(f)\|
=\|(e^{ith_\bullet}-1)f\|\longrightarrow0.
$$
The product rule for differences gives continuity on polynomials, and density together with the isometry of automorphisms gives continuity on every $a\in\cA_X$.
Thus $\alpha^\bullet$ is a strongly continuous automorphism group.

Let $\delta_\bullet$ denote its closed infinitesimal generator.
Because $e_n\in\dom(h_\bullet)$ and $h_\bullet e_n=h_0e_n$,
$$
\delta_\bullet(c_n^*)
=i c^*(h_0e_n)
=i\bigl(4^{n-1}c_{n-1}^*+(1+4^n)c_n^*+4^nc_{n+1}^*\bigr),
$$
where the first term is omitted when $n=1$.
The identity $[c_j^*c_k,c_n^*]=\delta_{kn}c_j^*$ shows that $D$ has exactly the same value on $c_n^*$.
The $*$ and Leibniz rules then give
$$
\cA_{\mathrm{loc}}\subseteq\dom(\delta_\bullet),
\qquad \delta_\bullet|_{\cA_{\mathrm{loc}}}=D.
$$
This agreement concerns all local spin observables, not only even fermionic polynomials.

The groups are different.
If they were equal, injectivity of $f\mapsto c^*(f)$ would give $e^{ith_F}=e^{ith_K}$ for every $t$, hence $h_F=h_K$ by uniqueness of the self-adjoint generator.
Their closed generators $\delta_F,\delta_K$ are therefore different as well.

## Purity and the gap on both generator domains

The Fock vacuum is annihilated by every $c_n$ and represents the product state with all spins in $|0\rangle$.
It is cyclic, since finite products of creation operators applied to it span a dense subspace of $\cF$.
To verify irreducibility, let $T$ be a bounded operator commuting with all $c_n,c_n^*$.
Then $c_nT\Omega=0$ for every $n$.
The common kernel of all annihilation operators on Fock space is $\C\Omega$, as follows by taking coefficients in the basis indexed by finite subsets of $X$.
Thus $T\Omega=\lambda\Omega$, and commutation with creation operators gives $T=\lambda1$ on their dense span.
The representation is irreducible, so $\omega$ is pure by the {prf:ref}`GNS purity criterion <thm-pure-state-gns>`.

The implementing group fixes $\Omega$ and has self-adjoint generator
$$
H_\bullet=d\Gamma(h_\bullet)
=\bigoplus_{r\geq0}
\left.\left(\sum_{j=1}^r
1\otimes\cdots\otimes h_\bullet\otimes\cdots\otimes1\right)
\right|_{\bigwedge^r\mathfrak h}.
$$
The summand for $r=0$ is zero.
For $r\geq1$, the tensor-factor operators strongly commute, and their sum is understood through the joint spectral calculus before restriction to the antisymmetric subspace.
Since $h_\bullet\geq1$, the $r$-particle summand is bounded below by $r$, and consequently
$$
H_\bullet\Omega=0,\qquad
H_\bullet\geq\cN\geq1-P_\Omega,
$$
where $\cN$ is the particle-number operator and $P_\Omega$ projects onto the vacuum.
In particular, the vacuum is the unique zero-energy vector, and $\omega$ is invariant under both groups.

For any $a\in\dom(\delta_\bullet)$, the identity
$$
e^{itH_\bullet}\pi(a)\Omega
=\pi(\alpha_t^\bullet(a))\Omega
$$
is differentiable at zero in Hilbert-space norm, since $\alpha_t^\bullet(a)$ is differentiable in the $C^*$-norm.
Hence
$$
\pi(a)\Omega\in\dom(H_\bullet),
\qquad H_\bullet\pi(a)\Omega=-i\pi(\delta_\bullet(a))\Omega.
$$
It follows that
$$
\begin{aligned}
-i\omega(a^*\delta_\bullet(a))
&=\langle\pi(a)\Omega,H_\bullet\pi(a)\Omega\rangle\\
&\geq\|(1-P_\Omega)\pi(a)\Omega\|^2\\
&=\omega(a^*a)-|\omega(a)|^2.
\end{aligned}
$$
This proves the gap on the full domain of each closed generator, and in particular proves the asserted algebraic gap for $D$ on $\cA_{\mathrm{loc}}$.
No core assumption on the local algebra was used in this argument.

## The graph closure and the core issue

Since $D$ has the closed extension $\delta_F$, it is closable.
Its unique graph closure satisfies
$$
\overline D\subseteq\delta_F,
\qquad \overline D\subseteq\delta_K.
$$
The existence of two extensions does not mean that graph closure itself is ambiguous.

We recall why a generator of an isometric group cannot have a proper extension that is also such a generator.
For such a generator $G$ and any $\lambda>0$, the bounded operator
$$
R_\lambda x=\int_0^\infty e^{-\lambda t}\alpha_t(x)\,dt
$$
is the inverse of $\lambda-G$.
The inverse identities follow by differentiation and integration by parts, first on $\dom(G)$ and then by density.
If $G\subseteq B$ and $B$ is another isometric-group generator, then for $x\in\dom(B)$ set $y=(\lambda-G)^{-1}(\lambda-B)x$.
One has $(\lambda-B)(x-y)=0$; injectivity of $\lambda-B$ gives $x=y\in\dom(G)$.
Thus $B=G$.

If $\overline D$ generated an automorphism group, this argument applied to both $\delta_F$ and $\delta_K$ would force $\delta_F=\overline D=\delta_K$, a contradiction.
If $\cA_{\mathrm{loc}}$ were a core for either generator, that generator would equal $\overline D$ and yield the same contradiction.
This completes the proof of the theorem.

The example therefore separates three properties: an algebraic gap, purity of the state, and uniqueness of a generating extension.
The first two hold, while uniqueness fails even though generating extensions exist and retain the same pure gapped ground state.
The fixed interaction supports give nearest-neighbor control, but the growing coefficients leave room for different self-adjoint extensions at infinity.
