(theorem-nondegenerate-ground-state-pure)=
# Nondegenerate ground states are pure

```{warning}
Agent-generated, not reviewed yet
```

This page proves the purity assertion used in the {ref}`Ground state article <article-ground-state>` for a general $C^*$-dynamical system.
Nondegeneracy of the GNS ground space is sufficient; a spectral gap is not needed for this result.
A gap above a degenerate ground space is insufficient, as the {ref}`matrix example in the Gapped ground state article <gapped-ground-state-purity>` shows.

```{prf:theorem} Purity of a nondegenerate ground state
:nonumber:
:label: thm-nondegenerate-ground-state-pure

Let $A$ be a $C^*$-algebra, let $(\alpha_t)_{t\in\R}$ be a strongly continuous group of $*$-automorphisms, and let $\omega$ be an $\alpha$-invariant state.
Suppose that the canonical implementing group $U_t=e^{itH}$ in its GNS representation $(\cH,\pi,\Omega)$ satisfies
$$
H\geq0,\qquad\ker H=\C\Omega.
$$
Then $\omega$ is pure.
Consequently, a {prf:ref}`nondegenerate gapped ground state <def-gapped-ground-state>` for a derivation whose closure generates $\alpha$, with the given domain as a core, is pure.
```

The generator and core assumptions in the last sentence are the ones in the {prf:ref}`Hamiltonian characterization <thm-gapped-ground-state-hamiltonian>`.
The theorem is not an assertion about arbitrary densely defined derivations without those analytic hypotheses.

## Positive-energy states form a face

We first show that if $\omega$ is a ground state for $\alpha$ and $\varphi$ is a state satisfying $\varphi\leq c\omega$ for some $c>0$, then $\varphi$ is also an invariant positive-energy ground state.
This is the face property of the ground-state set.
We supply the argument to make the purity proof independent of a separate structure theorem for ground states.

For an integrable function $f$ and $a\in A$, write
$$
a_f=\int_\R f(t)\alpha_t(a)\,dt,
\qquad\widehat f(s)=\int_\R f(t)e^{its}\,dt.
$$
If $f$ is a Schwartz function with $\widehat f$ compactly supported in $(-\infty,0)$, positive energy gives
$$
\pi(a_f)\Omega=\widehat f(H)\pi(a)\Omega=0.
$$
Domination implies $\varphi(a_f^*a_f)\leq c\omega(a_f^*a_f)=0$.
Consequently, in the GNS representation of $\varphi$ one has $\pi_\varphi(a_f)\Omega_\varphi=0$, and in particular $\varphi(a_f)=0$.

For $a=a^*$, the function $t\mapsto\varphi(\alpha_t(a))$ is bounded, continuous, and real-valued.
The preceding vanishing says that its distributional Fourier transform has no support on one open half-line.
Reality excludes the other half-line as well, so that transform is supported at zero.
A distribution supported at a single point is a finite sum of derivatives of the point mass; its inverse Fourier transform is a polynomial.
Boundedness makes that polynomial constant.
Thus $\varphi(\alpha_t(a))=\varphi(a)$, first for self-adjoint $a$ and then for all $a$ by linearity.

Invariance now supplies a canonical implementing group $e^{itH_\varphi}$.
The already established vector identity becomes
$$
\widehat f(H_\varphi)\pi_\varphi(a)\Omega_\varphi=0.
$$
The vectors $\pi_\varphi(a)\Omega_\varphi$ are dense, so all smooth spectral cutoffs supported in $(-\infty,0)$ vanish.
The spectral theorem yields $H_\varphi\geq0$, proving the face property.

## Proof of purity

Suppose that $\omega=t\varphi+(1-t)\psi$ for states $\varphi,\psi$ and $0<t<1$.
By the face property, $\varphi$ is invariant.
The positive-functional correspondence proved with the {prf:ref}`GNS purity criterion <thm-pure-state-gns>` supplies a positive operator $T\in\pi(A)'$ such that
$$
\varphi(a)=\langle\Omega,T\pi(a)\Omega\rangle,
\qquad0\leq T\leq t^{-1}1.
$$
Invariance and uniqueness of this operator imply $U_s^*TU_s=T$ for every $s\in\R$.
Indeed, the operator $U_s^*TU_s$ represents $\varphi\circ\alpha_s$, which is $\varphi$.
Functional calculus then gives
$$
U_sT^{1/2}\Omega=T^{1/2}U_s\Omega=T^{1/2}\Omega.
$$
Hence $T^{1/2}\Omega\in\ker H=\C\Omega$.
It has norm one because $\varphi$ is a state, so its vector state on $A$ equals $\omega$.
But that vector state is exactly $\varphi$, since $T$ commutes with $\pi(A)$.
Therefore $\varphi=\omega$, and the convex decomposition also gives $\psi=\omega$.
This proves purity.

For nonunital $A$, the same argument uses the nondegenerate GNS representation, or equivalently the state and dynamics extended to the minimal unitization.
The norm of $T^{1/2}\Omega$ is still one, as follows by evaluating $\varphi$ on an approximate identity.
