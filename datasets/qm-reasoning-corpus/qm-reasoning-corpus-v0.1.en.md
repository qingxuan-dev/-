# Quantum Mechanics Reasoning Corpus v0.1 (English)

**Source:** Ruolin's questions (2026-11-03) and the notes "Quantum mechanics notes: starting from your questions", expanded into corpus format by Claude, with key facts checked by web search; translated from the Chinese original by Claude.
**Entries:** 22, plus 10 correction records
**Verification status:** `[checked]` verified by search in this session, with link / `[common]` textbook or well-known, not re-checked / `[to verify]` check before use
**Credibility:** established / frontier / speculative / advice

---

## QM-01 What is antimatter?

- **Domains:** Particle physics, Antimatter
- **Level:** 1
- **Type:** correction
- **Credibility:** established
- **User's original claim:** Antimatter is another kind of matter, like positive and negative electrons.
- **Verdict:** Correct

**Question:** Is antimatter something different from ordinary matter, like the positron versus the electron?

**Reasoning chain:**
1. Definition first: every particle has a corresponding antiparticle with the same mass and spin, and opposite charge and other conserved quantum numbers such as baryon and lepton number.
2. The most familiar pair: the electron carries −e, its antiparticle the positron carries +e, and both have a mass of about 0.511 MeV/c².
3. Atoms made of antiparticles are antimatter. For example, an antiproton plus a positron makes antihydrogen, which CERN can now produce and trap in quantity.
4. So antimatter is not "matter of a different nature"; it is matter under the same physical laws with charge and related quantum numbers reversed.

**Answer:** Correct. Antimatter is made of antiparticles, which have the same mass and spin as their partners and opposite charge and related quantum numbers; the electron's antiparticle is the positron.

**Key facts:**
- Electron rest energy mₑc² ≈ 0.511 MeV, the same for the positron `[common]` Source: CODATA recommended values
- Antihydrogen has been produced and trapped at CERN's Antiproton Decelerator (ALPHA, ATRAP and other experiments) `[common]` Source: CERN

**Common errors:**
- Thinking antimatter has negative mass or energy.
- Thinking antimatter is a kind of "dark matter". The two are unrelated.

---

## QM-02 Annihilation: why two 511 keV photons

- **Domains:** Particle physics, Antimatter
- **Level:** 2
- **Type:** calculation
- **Credibility:** established
- **User's original claim:** Annihilation happens because it reacts with ordinary matter.
- **Verdict:** Mostly correct

**Question:** When a positron meets an electron they annihilate. Is that a chemical reaction? Why does light come out?

**Reasoning chain:**
1. Annihilation is not a chemical reaction but an interaction between elementary particles: the entire rest mass of the particle and antiparticle can be converted into other particles.
2. Simplest case: an electron and a positron nearly at rest. Total energy = 2mₑc² ≈ 1.022 MeV, total momentum ≈ 0.
3. A single photon always carries momentum E/c, so it cannot have zero total momentum; at least two photons must be produced.
4. The two photons have opposite momenta and equal energies, each mₑc² ≈ 511 keV, emitted back to back.
5. Detail: the electron and positron first form positronium. The spin singlet (para-positronium) decays into 2 photons with a lifetime of about 0.125 ns; the spin triplet (ortho-positronium) can only decay into 3 photons, with a lifetime of about 142 ns.
6. Application: hospital PET scans locate tissue by detecting this back-to-back pair of 511 keV photons in coincidence.

**Answer:** Mostly correct, but it is an interaction between elementary particles, not a chemical reaction. An electron–positron pair at rest turns its full 1.022 MeV of rest energy into photons; momentum conservation requires at least two, so the most common outcome is two back-to-back 511 keV photons (triplet positronium decays into three).

**Key facts:**
- Para-positronium → 2γ, lifetime about 125 ps; ortho-positronium → 3γ, lifetime about 142 ns `[common]` Source: Standard atomic physics textbooks
- PET imaging uses coincidence detection of 511 keV photon pairs `[common]` Source: Medical physics textbooks

**Common errors:**
- Saying annihilation always produces two photons, ignoring that triplet positronium produces three.
- Thinking annihilation can produce a single photon (violates momentum conservation).
- Treating annihilation as a chemical reaction (chemical reactions don't change particle species and involve energies of order eV).

**Check:** Electron–positron pair at rest: Σp = 0. With one photon, p_γ = E/c = 2mₑc ≠ 0, a contradiction; with two photons p₁ = −p₂ and E₁ = E₂ = mₑc² = 511 keV.

---

## QM-03 Does gravity pull antimatter down or push it up?

- **Domains:** Antimatter, Gravity
- **Level:** 2
- **Type:** fact
- **Credibility:** established
- **User's original claim:** Antimatter must have mass.
- **Verdict:** Correct

**Question:** Does antimatter have mass? Could gravity push it upwards?

**Reasoning chain:**
1. Inertial mass: CERN's BASE experiment compared the charge-to-mass ratios of the antiproton and proton in a Penning trap; they agree to 16 parts per trillion.
2. Gravitational mass: theory (general relativity plus CPT) expects antimatter to be attracted in the same way, but there was no direct measurement until 2023.
3. ALPHA-g slowly released antihydrogen atoms from a magnetic trap and counted how many escaped upwards versus downwards, finding an acceleration of about (0.75 ± 0.13 ± 0.16) g.
4. That precision, about 25%, is enough to rule out "antigravity" (upward acceleration) but not yet enough to test small differences from g.

**Answer:** Yes, and the mass is positive. Inertially, the antiproton and proton charge-to-mass ratios agree to 16 ppt; gravitationally, ALPHA-g directly observed antihydrogen falling in 2023, with an acceleration of about 0.75 g and an uncertainty of about ±25%, consistent with ordinary matter and ruling out antigravity.

**Key facts:**
- ALPHA-g: antihydrogen gravitational acceleration (0.75 ± 0.13 (stat + syst) ± 0.16 (simulation)) g; Anderson et al., Nature 621, 716–722 (2023) `[checked]` Source: Berkeley News 2023-09-27; APS DNP 2024 abstract <https://news.berkeley.edu/2023/09/27/antimatter-embraces-earth-falling-downward-like-normal-matter/>
- BASE: antiproton/proton charge-to-mass ratio = 1.000000000003(16), equal within 16 ppt; Borchert et al., Nature 601, 53–57 (2022) `[checked]` Source: CERN Courier; GSI news <https://cerncourier.com/a/base-breaks-new-ground-in-matter-antimatter-tests/>

**Common errors:**
- Describing the ALPHA-g result as "exactly g". The current uncertainty is about 25%.
- Thinking antimatter is repelled by gravity.

---

## QM-04 The phrase "anti-energy"

- **Domains:** Antimatter, Concept check
- **Level:** 2
- **Type:** correction
- **Credibility:** established
- **User's original claim:** Anti-energy has mass.
- **Verdict:** Needs correction

**Question:** Does antimatter correspond to "anti-energy"? Does anti-energy have mass?

**Reasoning chain:**
1. Physics has no object called "anti-energy". Antimatter is made of antiparticles that carry ordinary positive energy; the photons released in annihilation also have positive energy.
2. The phrase probably comes from the history of the Dirac equation: his 1928 equation had "negative-energy solutions", which Dirac later used to predict the anti-electron.
3. In modern quantum field theory these negative-energy solutions are reinterpreted as positive-energy antiparticles; there are no negative-energy particles.
4. Another concept that is easy to confuse is "negative energy density": in the Casimir effect between two metal plates, the local vacuum energy density is lower than outside. This is a property of how field energy is distributed and has nothing to do with antimatter.

**Answer:** Needs correction: there is no "anti-energy". Antimatter carries positive energy and has positive mass. The Dirac equation's negative-energy solutions are interpreted in quantum field theory as positive-energy antiparticles; "negative energy density" (as in the Casimir effect) is a separate concept unrelated to antimatter.

**Key facts:**
- The Dirac equation (1928) has negative-energy solutions; in 1931 Dirac proposed the anti-electron `[common]` Source: Dirac, Proc. R. Soc. A 117, 610 (1928); Proc. R. Soc. A 133, 60 (1931)
- Casimir effect (predicted 1948, measured precisely by Lamoreaux in 1997) `[common]` Source: History of physics

**Common errors:**
- Treating "antimatter" and "negative energy" as the same thing.
- Thinking Dirac's negative-energy solutions are still interpreted today as negative-energy particles.

---

## QM-05 Why the universe has more matter than antimatter

- **Domains:** Cosmology, Antimatter
- **Level:** 3
- **Type:** frontier
- **Credibility:** established + frontier
- **User's original claim:** The universe must be asymmetric; otherwise matter and antimatter would annihilate into pure energy and reality could hardly form.
- **Verdict:** The factual part is right; "must" is unexplained

**Question:** If the Big Bang made equal amounts of matter and antimatter, wouldn't they all have annihilated? Why are we here?

**Reasoning chain:**
1. Observed fact: the observable universe is almost entirely matter, with no large antimatter regions found (their boundaries would emit strong annihilation gamma rays).
2. Quantitatively: the ratio of baryons to photons is η ≈ 6.1 × 10⁻¹⁰, about 6 baryons for every 10 billion photons. Most of today's photons are left over from early matter–antimatter annihilation.
3. Interpretation: in the early universe matter outnumbered antimatter by a tiny fraction; almost every pair annihilated, and the small remainder became all the galaxies.
4. Sakharov (1967) showed that producing net matter from a symmetric start requires three conditions at once: baryon number can change; C and CP symmetry are violated; the universe departs from thermal equilibrium at some stage.
5. The Standard Model has a source for each condition in principle, but its known CP violation is too weak, giving an asymmetry many orders of magnitude smaller than observed. Physics beyond the Standard Model is widely thought necessary (candidates: leptogenesis, electroweak baryogenesis); none is confirmed.
6. On "must": physics can say "in fact it is asymmetric, or there would be no galaxies or people", but cannot yet explain why it had to be so.

**Answer:** Your intuition matches cosmology: with perfect symmetry, almost nothing but radiation would remain today. The observed η ≈ 6.1 × 10⁻¹⁰ (about 6 baryons per 10 billion photons). Producing this asymmetry requires the Sakharov conditions, and the Standard Model's CP violation is not enough; the actual mechanism is an open problem.

**Key facts:**
- η = n_b/n_γ = (6.104 ± 0.058) × 10⁻¹⁰ (Planck 2018 CMB) `[checked]` Source: Fields et al., Big-Bang Nucleosynthesis after Planck (2020) <https://arxiv.org/abs/1912.01132>
- Sakharov conditions: A. D. Sakharov, JETP Lett. 5, 24 (1967) `[common]` Source: Original paper

**Common errors:**
- Saying "a few baryons per billion photons" (it is about 0.6, off by about a factor of 10; the original notes made this error).
- Thinking the Standard Model already explains the asymmetry.
- Treating "we exist" as a physical explanation of the asymmetry (it is observational selection, not a mechanism).

**Check:** η ≈ 6.1×10⁻¹⁰ ⇒ about 6.1 baryons per 10¹⁰ photons ⇒ about 0.61 baryons per 10⁹ photons.

---

## QM-06 CP violation: from kaons to baryons

- **Domains:** Particle physics, Symmetry
- **Level:** 3
- **Type:** fact
- **Credibility:** established + frontier

**Question:** Do matter and antimatter follow exactly the same rules? Has any experiment seen a difference?

**Reasoning chain:**
1. C swaps particles for antiparticles; P is a spatial reflection. If CP were conserved, a process and its "mirror-image antimatter version" would occur with the same probability.
2. In 1964 Christenson, Cronin, Fitch and Turlay first observed CP violation in neutral kaon decays; Cronin and Fitch received the 1980 Nobel Prize for it.
3. CP violation was later seen in B and D mesons too, but all of these are mesons (quark + antiquark).
4. In 2025 LHCb measured a difference of about 2.45% between the decay rates of Λb⁰ → p K⁻ π⁺ π⁻ and its antibaryon counterpart, at 5.2σ: the first observation of CP violation in baryons.
5. All of these are described by the Standard Model's CKM mechanism, so on their own they cannot explain the matter left over in the universe (see QM-05).

**Answer:** Not exactly. CP symmetry is violated in the weak interaction: first discovered in kaons in 1964, and observed in baryon decays for the first time by LHCb in 2025 (about 2.45%, 5.2σ). But all known CP violation is within Standard Model expectations and too weak to explain the matter left in the universe.

**Key facts:**
- Christenson, Cronin, Fitch, Turlay, PRL 13, 138 (1964) `[common]` Source: Original paper
- LHCb: CP asymmetry in Λb⁰ → pK⁻π⁺π⁻ of (2.45 ± 0.46 ± 0.10)%, 5.2σ; Nature 643, 1223–1228 (2025) `[checked]` Source: CERN news; LHCb outreach <https://home.cern/news/news/physics/new-piece-matter-antimatter-puzzle>

**Common errors:**
- Thinking the discovery of CP violation solved the matter–antimatter asymmetry.
- Confusing CP violation with CPT violation (no CPT violation has been found).

---

## QM-07 Is time an observable in quantum mechanics?

- **Domains:** Quantum foundations, Time
- **Level:** 3
- **Type:** concept
- **Credibility:** established

**Question:** Position and momentum have operators. Why doesn't time?

**Reasoning chain:**
1. In the Schrödinger equation iħ ∂ψ/∂t = Ĥψ, t is an externally given parameter, not an operator acting on states.
2. Pauli's argument: if a self-adjoint time operator T canonically conjugate to the Hamiltonian existed ([T, Ĥ] = iħ), then e^{iaT} would shift the energy by any amount a, so the spectrum of Ĥ would fill the whole real line.
3. But physical energies are bounded below (there is a ground state), a contradiction. So in general no such time operator exists.
4. That is why the energy–time "uncertainty relation" is different in kind from position–momentum: Δt usually means the time the system takes to change appreciably, not the standard deviation of an operator.

**Answer:** Because in standard quantum mechanics time is an external parameter. Pauli argued that a self-adjoint time operator conjugate to Ĥ would force the energy spectrum to be unbounded below, contradicting the existence of a ground state. So the energy–time relation cannot be derived from operator commutators the way position–momentum is.

**Key facts:**
- Pauli's theorem (1933, Handbuch der Physik) `[common]` Source: Pauli, Handbuch der Physik 24 (1933)

**Common errors:**
- Treating ΔE·Δt ≥ ħ/2 as an operator relation of exactly the same kind as Δx·Δp ≥ ħ/2.

---

## QM-08 Can time emerge from entanglement? The Page–Wootters mechanism

- **Domains:** Quantum foundations, Time, Quantum gravity
- **Level:** 4
- **Type:** frontier
- **Credibility:** frontier
- **User's original claim:** Time is produced by the change and motion of reality.
- **Verdict:** There are serious theories about this

**Question:** If the quantum state of the whole universe doesn't change in time, how do we come to feel time flowing?

**Reasoning chain:**
1. In the Wheeler–DeWitt equation of quantum gravity, Ĥ|Ψ⟩ = 0, the universe's total state satisfies a "zero energy" constraint with no external time parameter. This is the "problem of time".
2. Page and Wootters (1983) proposed splitting the universe into a "clock" C and "everything else" S. The total state is static, but C and S are entangled.
3. Conditioning on the clock reading (asking "what state is S in when the clock shows t?"), the conditional state |ψ_S(t)⟩ obeys the Schrödinger equation and appears to evolve.
4. So "evolution" is a correlation between subsystems; for the whole there is no change. Hence the paper's title, "Evolution without evolution".
5. In 2014 Moreva et al. made a toy demonstration with the polarisation of two photons: an internal observer (correlated with the clock photon) sees the other photon change; an external observer measuring only global properties confirms the total state is static.
6. This is a proof of principle; it does not show that time in the real universe arises this way.

**Answer:** The Page–Wootters mechanism offers one possibility: the universe's total state is static, but a "clock" is entangled with "everything else", and conditioned on the clock reading the rest appears to evolve. A toy version was demonstrated with photons in 2014. It is a frontier idea, not settled.

**Key facts:**
- Page & Wootters, "Evolution without evolution", Phys. Rev. D 27, 2885 (1983) `[common]` Source: Original paper
- Moreva et al., "Time from quantum entanglement: an experimental illustration", Phys. Rev. A 89, 052122 (2014) `[checked]` Source: arXiv:1310.4691 <https://arxiv.org/abs/1310.4691>

**Common errors:**
- Saying "experiments proved that time is produced by entanglement". The experiment only showed the mechanism is self-consistent in a toy system.
- Treating the Page–Wootters mechanism as the mainstream consensus of quantum mechanics.

---

## QM-09 Relational time and thermal time

- **Domains:** Quantum foundations, Time, Philosophy
- **Level:** 4
- **Type:** frontier
- **Credibility:** frontier + speculative
- **User's original claim:** Underlying changes in time are determined by changes in physical reality.
- **Verdict:** Close to relational time and the thermal time hypothesis

**Question:** Can we say that time itself is produced by things changing?

**Reasoning chain:**
1. Relational time: time is not an independent background container but the relation between changes in physical quantities (how one quantity changes relative to another). Rovelli and others developed this view within loop quantum gravity.
2. Thermal time hypothesis (Connes & Rovelli, 1994): in a theory with no preferred time, the system's statistical (thermodynamic) state can itself define a "flow of time", called thermal time.
3. Both are very close to the intuition that "time is produced by change": the first matches "relations of change", the second "the statistical state sets the direction".
4. But neither currently has an experimental test that distinguishes it from standard theory, so thermal time remains speculative and relational time is more a choice of theoretical framework.

**Answer:** There are corresponding theories: relational time holds that time is the relation between changes in physical quantities; the thermal time hypothesis holds that a system's statistical state determines the flow of time. They are close to your intuition, but neither has distinguishing experimental evidence yet.

**Key facts:**
- Connes & Rovelli, Class. Quantum Grav. 11, 2899 (1994) `[common]` Source: Original paper

**Common errors:**
- Treating a philosophical possibility as a confirmed physical result.

---

## QM-10 The arrow of time

- **Domains:** Thermodynamics, Time, Cosmology
- **Level:** 3
- **Type:** concept
- **Credibility:** established + frontier

**Question:** Most equations of physics are symmetric in time. Why can we remember the past but not the future?

**Reasoning chain:**
1. The microscopic equations (Newton, Schrödinger) are essentially symmetric under time reversal (the tiny T violation in the weak interaction is not the source of the everyday arrow of time).
2. The second law of thermodynamics: the entropy of an isolated system almost always increases, which gives a direction.
3. But entropy increase needs a premise: the past had lower entropy than now. Traced back, the universe must have begun in an extremely low-entropy state (the "Past Hypothesis").
4. Memory, causation, ageing and other directional phenomena can all be traced to this entropy gradient.
5. Why the initial entropy was so low has no accepted explanation.

**Answer:** The mainstream explanation is entropy: the direction of time is the direction in which entropy increases. Entropy can keep increasing because the universe began in an extremely low-entropy state, and the origin of that initial condition is unresolved.

**Key facts:**
- The "Past Hypothesis", see David Albert, Time and Chance (2000) `[common]` Source: Philosophy of science literature

**Common errors:**
- Saying "the law of entropy increase explains everything", ignoring its dependence on a low-entropy initial condition.

---

## QM-11 Is the speed of light the "lowest render"?

- **Domains:** Relativity, Concept check
- **Level:** 2
- **Type:** correction
- **Credibility:** established + speculative
- **User's original claim:** Light is the lowest render and the universe's speed limit.
- **Verdict:** Second half right; first half is a metaphor

**Question:** Is the speed of light the universe's "render speed", which is why nothing can go faster?

**Reasoning chain:**
1. The speed of light c is the same in all inertial frames; this is the starting point of special relativity. Since 1983, c = 299 792 458 m/s is exact by definition.
2. A more precise view: c is the maximum speed at which causal influence can propagate. Light moves at it because photons have no rest mass; anything massless moves at c.
3. Evidence: in 2017 the gravitational waves of GW170817 and a gamma-ray burst arrived about 1.7 s apart after a journey of about 130 million light-years, limiting any difference in speed to about 10⁻¹⁵; gravity also propagates at c.
4. "Rendering" comes from computing: the universe as a frame-by-frame simulation. To become a physical claim, it would have to predict a measurable phenomenon that current theory doesn't (for example, dispersion caused by discrete spacetime).
5. No such prediction has been confirmed, so it remains a metaphor or philosophy.

**Answer:** The second half is right: c is the speed limit for causal propagation, and both light and gravitational waves travel at it; GW170817 limits any difference between the speed of gravity and light to about 10⁻¹⁵. The first half, "rendering", is a metaphor with no testable prediction or experimental support so far.

**Key facts:**
- GW170817 / GRB 170817A: (v_gw − c)/c between −3×10⁻¹⁵ and +7×10⁻¹⁶; ApJL 848, L13 (2017) `[checked]` Source: LIGO/Virgo/Fermi/INTEGRAL, arXiv:1710.05834 <https://arxiv.org/abs/1710.05834>
- In 1983 the 17th General Conference on Weights and Measures defined the metre as the distance light travels in 1/299 792 458 s `[common]` Source: BIPM

**Common errors:**
- Saying "the speed of light is a property of light". More precisely, c is a property of spacetime, and light just happens to move at it.
- Treating the "simulated universe" as an established result of physics.

---

## QM-12 Does a photon experience time?

- **Domains:** Relativity, Concept check
- **Level:** 3
- **Type:** concept
- **Credibility:** established

**Question:** I've heard that photons "don't experience time". Is that true?

**Reasoning chain:**
1. A massive object moves along a timelike worldline; its proper time τ is the time elapsed on its own clock.
2. A photon moves along a lightlike worldline with interval ds² = 0, so the proper time accumulated along it is zero.
3. But a photon has no rest frame: the Lorentz transformation diverges as v → c, so "the world as seen by a photon" cannot be defined.
4. So "a photon experiences zero time" is a popular paraphrase of ds² = 0; strictly, "the time a photon experiences" is not well defined in relativity.

**Answer:** It's a popular paraphrase. The proper time along a photon's worldline is zero, but a photon has no rest frame, so "how much time the photon itself experiences" is not well defined in relativity.

**Common errors:**
- Saying "from the photon's point of view the universe is instantaneous", as if a photon reference frame existed.

---

## QM-13 Superposition is not "not knowing"

- **Domains:** Quantum foundations
- **Level:** 1
- **Type:** concept
- **Credibility:** established

**Question:** Does quantum superposition mean the particle is really in one definite place and we just don't know which?

**Reasoning chain:**
1. If the particle "really went through one slit and we just don't know which", the double-slit pattern would be the plain sum of the two single-slit patterns.
2. Experiments show interference fringes: at some positions the probability is lower than with only one slit open.
3. Firing electrons one at a time still builds up fringes (Tonomura et al., 1989), so the interference is not an interaction between many particles.
4. So a superposition is a real state, and the amplitudes of the two paths add and cancel.
5. Once you arrange to detect which slit the particle went through, the interference disappears.

**Answer:** No. Superposition is a real physical state whose amplitudes interfere: in the single-electron double-slit experiment, some positions have a lower probability than with one slit open, which "just not knowing" cannot explain.

**Key facts:**
- Tonomura et al., Am. J. Phys. 57, 117 (1989): single-electron double-slit interference `[common]` Source: Original paper

**Common errors:**
- Reading superposition as a classical probabilistic mixture (ignorance).

---

## QM-14 The Born rule: amplitudes can cancel, probabilities can't

- **Domains:** Quantum foundations
- **Level:** 2
- **Type:** calculation
- **Credibility:** established

**Question:** What is the essential difference between quantum probability and the probability of rolling dice?

**Reasoning chain:**
1. Quantum mechanics assigns each possible outcome a complex amplitude a; the probability of getting that outcome is P = |a|² (the Born rule).
2. When an outcome can be reached by two indistinguishable paths, add the amplitudes first, then take the squared modulus: P = |a₁ + a₂|².
3. Let the two paths have equal-sized amplitudes a₁ = ½·e^{iφ₁}, a₂ = ½·e^{iφ₂}, with phase difference Δφ = φ₂ − φ₁.
4. Then P = ¼|1 + e^{iΔφ}|² = ½(1 + cos Δφ): Δφ = 0 gives P = 1 (constructive), Δφ = π gives P = 0 (destructive).
5. Classical probability can only add probabilities: P = ¼ + ¼ = ½, independent of phase, and never 0.

**Answer:** Classical probabilities only add; quantum mechanics adds amplitudes and then squares. Two paths' amplitudes can cancel completely when their phases are opposite, producing a dark fringe where "with both paths open, the particle can't arrive", which classical probability cannot do.

**Key facts:**
- The Born rule (Born, 1926) `[common]` Source: Z. Phys. 37, 863 (1926)

**Common errors:**
- Adding the probabilities of each path first and then discussing interference.
- Thinking amplitudes are square roots of probabilities and therefore always positive.

**Check:** P(Δφ) = ½(1 + cos Δφ); at Δφ = π/2, P = ½, exactly the classical value; at Δφ = π, P = 0.

---

## QM-15 Observables are Hermitian operators

- **Domains:** Quantum foundations, Linear algebra
- **Level:** 2
- **Type:** concept
- **Credibility:** established

**Question:** Why is linear algebra called "the native language of quantum mechanics"?

**Reasoning chain:**
1. A quantum state is a unit vector in a complex vector space (Hilbert space).
2. Each observable corresponds to a Hermitian operator A = A†. Hermiticity guarantees real eigenvalues (measurement readings are real) and orthogonal eigenvectors for different eigenvalues.
3. A measurement can only return an eigenvalue λ of A, with probability equal to the squared modulus of the state's projection onto the corresponding eigenvector.
4. In finite-dimensional cases such as spin, operators are just finite matrices, e.g. σ_z = diag(1, −1) with eigenvalues ±1 (times ħ/2).
5. Position and momentum are unbounded operators on an infinite-dimensional space with continuous spectra and no normalisable eigenvectors; they need more functional analysis, but the idea is the same.

**Answer:** Because states are vectors, observables are Hermitian matrices (operators), measurement results are eigenvalues and probabilities are squared projection lengths. The finite-dimensional case (e.g. spin) is entirely matrices; position and momentum are the infinite-dimensional, continuous-spectrum generalisation.

**Key facts:**
- Von Neumann, Mathematical Foundations of Quantum Mechanics (1932), established the Hilbert space formulation `[common]` Source: Standard literature

**Common errors:**
- Saying "observables are matrices" without mentioning that position and momentum are infinite-dimensional with continuous spectra.
- Thinking any matrix can be an observable (it must be Hermitian).

**Check:** σ_z has eigenvectors |↑⟩ = (1,0)ᵀ and |↓⟩ = (0,1)ᵀ with eigenvalues +1 and −1; their inner product is 0.

---

## QM-16 The uncertainty principle is not instrument error

- **Domains:** Quantum foundations
- **Level:** 3
- **Type:** concept
- **Credibility:** established

**Question:** Is position and momentum uncertainty caused by imprecise instruments?

**Reasoning chain:**
1. Robertson's inequality: for any two observables A and B, σ_A σ_B ≥ ½|⟨[A, B]⟩|, where [A, B] = AB − BA.
2. Position and momentum satisfy [x̂, p̂] = iħ; substituting gives σ_x σ_p ≥ ħ/2.
3. This constrains the widths of two distributions for the same state: no state has both arbitrarily narrow position and momentum distributions.
4. It does not limit the precision of a single measurement: you can measure position very precisely, at the cost of a very wide momentum distribution afterwards.
5. The root is mathematical structure: the position and momentum representations are Fourier transforms of each other, so the narrower one is, the wider the other.

**Answer:** No. It comes from the non-commuting position and momentum operators ([x, p] = iħ), equivalent to a property of the Fourier transform: no quantum state has both an arbitrarily narrow position distribution and an arbitrarily narrow momentum distribution. It has nothing to do with instrument quality.

**Key facts:**
- Heisenberg (1927); rigorous forms by Kennard (1927) and Robertson (1929) `[common]` Source: Standard literature

**Common errors:**
- Saying "uncertainty comes from the measurement disturbing the particle" (that is the heuristic Heisenberg microscope picture, not the principle itself).
- Saying "position cannot be measured precisely".

**Check:** Gaussian wave packet ψ(x) ∝ e^{−x²/4σ²}: σ_x = σ, σ_p = ħ/(2σ), and the product equals ħ/2, attaining the bound.

---

## QM-17 Self-test: measurement probabilities for spin 1/2

- **Domains:** Quantum foundations, Linear algebra
- **Level:** 2
- **Type:** calculation
- **Credibility:** established

**Question:** A spin is in an equal superposition of "up" and "down". Measuring along z and along x, what are the probabilities? And along an arbitrary direction?

**Reasoning chain:**
1. Write the state: the equal superposition |ψ⟩ = (|↑⟩ + |↓⟩)/√2 = (1, 1)ᵀ/√2.
2. Measure along z: eigenstates |↑⟩ = (1,0)ᵀ, |↓⟩ = (0,1)ᵀ. P(↑) = |⟨↑|ψ⟩|² = |1/√2|² = ½, P(↓) = ½.
3. Measure along x: σ_x = [[0,1],[1,0]] with eigenstates |±x⟩ = (1, ±1)ᵀ/√2. ⟨+x|ψ⟩ = 1, so P(+x) = 1 and P(−x) = 0: this state is "up" along x.
4. Arbitrary direction: measure along a direction n in the xz plane at angle θ from the z axis, with eigenstate |+n⟩ = (cos θ/2, sin θ/2)ᵀ.
5. ⟨+n|ψ⟩ = (cos θ/2 + sin θ/2)/√2, so P(+n) = ½(1 + sin θ). Check: θ = 0 gives ½, θ = 90° gives 1.
6. General formula: with Bloch vector s for the state and measurement direction n, P(+n) = ½(1 + s·n).

**Answer:** Along z: up and down each ½. Along x: +x with probability 1. This "equal superposition" is in fact a definite state along x. Along a direction at angle θ from z: P(+) = ½(1 + sin θ); in general P = ½(1 + s·n).

**Common errors:**
- Thinking an equal superposition gives 50/50 in every direction.
- Forgetting to square, taking the amplitude 1/√2 as the probability.

**Check:** θ = 30°: P(+) = ½(1 + 0.5) = 0.75; θ = 180° (the −z direction): P(+) = ½.

---

## QM-18 The measurement problem and the main interpretations

- **Domains:** Quantum foundations, Philosophy
- **Level:** 4
- **Type:** contested
- **Credibility:** frontier

**Question:** The Schrödinger equation is continuous, so why do we see only one result when we measure? Which interpretation is right?

**Reasoning chain:**
1. Schrödinger evolution is linear and deterministic and would put the apparatus into superposition too; yet each time we see one reading. This is the measurement problem.
2. Copenhagen: measurement causes collapse; it does not ask about the mechanism of collapse.
3. Many-worlds (Everett, 1957): no collapse; every outcome is realised in a different branch, and decoherence explains why branches don't interfere.
4. Bohmian mechanics: particles always have definite positions, guided by the wave function; a nonlocal deterministic theory.
5. Spontaneous collapse: GRW (1986) lets each particle localise at random with a tiny fixed rate and has nothing to do with gravity; it is the Diósi–Penrose model that ties collapse to gravity. In 2020 an underground experiment at Gran Sasso ruled out the parameter-free version of the Diósi–Penrose model.
6. QBism: the wave function represents an agent's beliefs.
7. Apart from spontaneous-collapse models, the interpretations make the same predictions for current experiments, so the choice depends more on philosophical preference.

**Answer:** There is no consensus. The main interpretations (Copenhagen, many-worlds, Bohmian, QBism) predict the same results for current experiments; spontaneous-collapse models are the exception, predicting measurable deviations (such as faint radiation) that experiments are testing, and the simplest gravity-related collapse model was ruled out in 2020.

**Key facts:**
- Ghirardi, Rimini, Weber, Phys. Rev. D 34, 470 (1986) `[common]` Source: Original paper
- Donadi et al. (2020, Nature Physics): a germanium detector at Gran Sasso saw 576 photons against about 506 expected from background, ruling out the parameter-free Diósi–Penrose model `[checked]` Source: Physics World 2020-09 <https://physicsworld.com/a/physicists-place-fresh-limits-on-gravitys-role-in-wavefunction-collapse/>

**Common errors:**
- Saying GRW is a gravity-related collapse model (the original notes made this mix-up).
- Claiming some interpretation has been experimentally confirmed.
- Saying "consciousness causes collapse" is the mainstream view.

---

## QM-19 Bell's theorem and the CHSH calculation

- **Domains:** Quantum foundations, Entanglement
- **Level:** 4
- **Type:** calculation
- **Credibility:** established

**Question:** Einstein thought particles' results were fixed in advance. How did Bell show that this is wrong?

**Reasoning chain:**
1. Suppose Alice chooses to measure along a or a′ and Bob along b or b′, with results ±1.
2. If results are fixed in advance and unaffected by the other side's choice (local hidden variables), then S = E(a,b) − E(a,b′) + E(a′,b) + E(a′,b′) satisfies |S| ≤ 2 (the CHSH inequality, 1969).
3. Quantum mechanics: for the spin singlet, E(a,b) = −cos(θ_a − θ_b).
4. Take a = 0°, a′ = 90°, b = 45°, b′ = 135°: the four correlations are −0.707, +0.707, −0.707, −0.707, giving S = −2√2 ≈ −2.83 and |S| = 2√2 > 2.
5. 2√2 is also the largest value quantum mechanics can reach (the Tsirelson bound).
6. Experiments: Clauser (1972), Aspect (1982) and others closed in step by step; in 2015 three experiments simultaneously closed the main loopholes; the 2022 Nobel Prize in Physics went to Aspect, Clauser and Zeilinger.

**Answer:** Bell showed that any local theory with predetermined results satisfies |S| ≤ 2, while quantum mechanics predicts that the singlet can reach 2√2 ≈ 2.83. Experiments have repeatedly measured values above 2, and loophole-free tests were achieved in 2015, so local hidden-variable theories are ruled out.

**Key facts:**
- Bell, Physics 1, 195 (1964); Clauser, Horne, Shimony, Holt, PRL 23, 880 (1969) `[common]` Source: Original papers
- Loophole-free Bell tests in 2015: Hensen et al. (Delft), Giustina et al. (Vienna), Shalm et al. (NIST) `[common]` Source: Nature / PRL 2015
- 2022 Nobel Prize in Physics: Aspect, Clauser, Zeilinger `[common]` Source: nobelprize.org

**Common errors:**
- Saying Bell's theorem proves "quantum mechanics is nonlocal". Strictly, it rules out the combination "local + predetermined results".
- Remembering |S| ≤ 2 as |S| ≤ 1.

**Check:** cos 45° = 0.7071. S = −cos45° − (−cos135°) − cos45° − cos(−45°) = −4 × 0.7071 = −2.828.

---

## QM-20 Can entanglement send signals faster than light?

- **Domains:** Quantum foundations, Entanglement, Relativity
- **Level:** 3
- **Type:** concept
- **Credibility:** established

**Question:** Since entangled particles are correlated instantly, could we use them to send messages faster than light?

**Reasoning chain:**
1. Alice measures her particle; the result is random and she cannot choose which result she gets.
2. Looking only at his own results, Bob's statistics are unchanged no matter which direction Alice measures, or whether she measures at all (no-communication theorem: Bob's reduced density matrix is unaffected by Alice's operations).
3. The correlation only shows up after the two compare records over an ordinary channel (no faster than light).
4. So entanglement produces very strong correlations but cannot carry information, and it does not conflict with relativity.

**Answer:** No. Bob's own measurement statistics are unaffected by anything Alice does (the no-communication theorem); the correlation appears only after results are compared over an ordinary channel, so no faster-than-light signalling is possible.

**Key facts:**
- No-communication theorem: Ghirardi, Rimini, Weber (1980) and others `[common]` Source: Standard literature

**Common errors:**
- Saying "quantum teleportation achieves faster-than-light transmission". Teleportation needs two classical bits sent over a classical channel.

**Check:** In the singlet, Bob measuring along any direction gets P(+) = P(−) = ½, independent of Alice's measurement direction.

---

## QM-21 Why antiparticles are necessary

- **Domains:** Quantum field theory, Antimatter
- **Level:** 4
- **Type:** concept
- **Credibility:** established

**Question:** Is antimatter an extra assumption added to the theory, or is it unavoidable?

**Reasoning chain:**
1. Combining quantum mechanics with special relativity: particle number is no longer conserved (enough energy can create new particles), single-particle wave functions stop being self-consistent, and quantum field theory is needed.
2. In quantum field theory particles are excitations of fields. Requiring the field to be Lorentz invariant and measurements at spacelike separation not to affect each other (microcausality), the expansion of a charged field must contain both particle and antiparticle parts.
3. So for charged particles, antiparticles are not an extra assumption but a consequence of the theory's consistency.
4. Addendum: neutral particles can be their own antiparticles, e.g. the photon and the π⁰ meson. Whether neutrinos are their own antiparticles (Majorana particles) is not yet known; neutrinoless double beta decay experiments are searching.

**Answer:** For charged particles it is unavoidable: relativity + quantum mechanics + causality require charged fields to describe both particles and antiparticles. Neutral particles can be their own antiparticles (e.g. the photon); whether neutrinos are is still open.

**Key facts:**
- Weinberg, The Quantum Theory of Fields, Vol. 1 (1995), Chapter 5 `[common]` Source: Standard textbook

**Common errors:**
- Saying "every particle has a distinct antiparticle", ignoring that the photon and others are their own antiparticles.

---

## QM-22 What to learn first for quantum mechanics

- **Domains:** Learning path
- **Level:** 1
- **Type:** learning
- **Credibility:** advice

**Question:** I want to teach myself quantum mechanics. Where should I start with the maths?

**Reasoning chain:**
1. Quantum states are vectors and observables are matrices, so linear algebra comes first: vector spaces, inner products, eigenvalues, Hermitian matrices.
2. Amplitudes are complex numbers: complex arithmetic and Euler's formula e^{iφ} = cos φ + i sin φ.
3. Probability: expectation and variance, which describe the statistics of measurement results.
4. Calculus and differential equations: the Schrödinger equation is a partial differential equation; start with one dimension.
5. Fourier analysis: position and momentum are related by the Fourier transform, which is also the root of the uncertainty principle.
6. Physics order: two-level systems (spin 1/2, only 2×2 matrices) → one-dimensional problems (infinite well, harmonic oscillator, tunnelling) → the hydrogen atom and angular momentum → the Dirac equation and an introduction to quantum field theory.
7. A test: if you can do the QM-17 calculation on your own, you are over the threshold.

**Answer:** Start with linear algebra and complex numbers, beginning with 2×2 matrix problems like spin 1/2; then the one-dimensional Schrödinger equation and the hydrogen atom; finally the Dirac equation and quantum field theory. Griffiths, Introduction to Quantum Mechanics, is a good first textbook; Sakurai, Modern Quantum Mechanics, is more mathematical.

**Common errors:**
- Starting from wave functions and partial differential equations and skipping linear algebra, which hides the structure of measurement and superposition.

---

## Appendix: corrections (usable as negatives)

| Origin | Original claim | Problem | Correction | Entry |
|---|---|---|---|---|
| User intuition | Anti-energy has mass | Physics has no object called "anti-energy" | Antimatter carries ordinary positive energy and positive mass; Dirac's negative-energy solutions are interpreted in QFT as positive-energy antiparticles; negative energy density (Casimir effect) is a different concept | QM-04 |
| User intuition | Light is the lowest render | A metaphor with no testable prediction | c is the speed limit of causal propagation; "rendering" would need a new measurable prediction to become a physical claim | QM-11 |
| User intuition | The universe must be asymmetric | "In fact asymmetric" holds; "must" is unexplained | η ≈ 6.1×10⁻¹⁰ is an observed fact; the mechanism of the asymmetry is an open problem | QM-05 |
| User intuition | Annihilation happens because it reacts with ordinary matter | Worded like a chemical reaction | An interaction between elementary particles in which all rest mass is converted into other particles | QM-02 |
| Original notes | A few baryons for every billion photons | Too large by about a factor of 10 | About 6 baryons per 10 billion photons (about 0.6 per billion) | QM-05 |
| Original notes | Objective collapse (e.g. GRW) … possibly related to gravity | Conflates GRW with gravitational collapse | GRW is unrelated to gravity; the gravity-related one is the Diósi–Penrose model | QM-18 |
| Original notes | Electron–positron annihilation produces two photons of 511 keV each | Missing conditions | A near-rest spin singlet gives two photons; spin-triplet positronium gives three | QM-02 |
| Original notes | In 1928 Dirac … eventually interpreted it as a new particle of opposite charge | Compressed timeline | His 1930 hole theory first identified holes with protons; he proposed the anti-electron in 1931, and Anderson found the positron in 1932 | QM-04 |
| Original notes | Each observable corresponds to an operator (think of it as a matrix) | Not strict for position and momentum | Finite-dimensional observables are Hermitian matrices; position and momentum are unbounded operators on an infinite-dimensional space with continuous spectra | QM-15 |
| Original notes | The mathematical structure of fields naturally requires antiparticles | Needs a qualification | True for charged fields; neutral particles can be their own antiparticles (photon, π⁰) | QM-21 |
