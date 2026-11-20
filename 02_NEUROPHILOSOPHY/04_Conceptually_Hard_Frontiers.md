# Neurophilosophy: Tier 4 — Conceptually Hard & Frontier Questions
## Markov Blankets, Free Energy Formalisms, and Action Theory Critiques

---

### Question 1: Markov Blankets and the "Self-Evidencing" Brain
**Format**: Conceptual Multiple-Choice (Format A)  
**Difficulty Tier**: Conceptually Hard / Frontiers  
**Primary Thinkers**: Karl Friston (2013, 2019), Jakob Hohwy (2016), Michael Kirchhoff et al. (2018)

In the formal mathematical architecture of Karl Friston’s **Free Energy Principle (FEP)**, any biological organism that maintains its structural integrity and resists entropic dissolution is partitioned into four classes of states via a **Markov Blanket**:
1. *External States* ($\eta$): Environmental variables hidden beyond the blanket.
2. *Sensory States* ($s$): Surface variables influenced by external states, affecting internal states.
3. *Active States* ($a$): Surface variables influenced by internal states, affecting external states.
4. *Internal States* ($\mu$): Systemic variables insulated from external states by the sensory-active blanket.

Jakob Hohwy (2016) and Karl Friston formulate the concept of the brain as a **"Self-Evidencing System"**. What is the precise epistemological consequence of the Markov Blanket boundary for the internal states of the brain?

- (A) The internal states $\mu$ have no direct, unmediated access to external states $\eta$; they can interact with the cosmos *only* through the statistical mediation of sensory and active states, meaning that maintaining internal homeostasis is mathematically equivalent to maximizing the Bayesian marginal likelihood of the agent's own existence ($p(s|m)$), rendering the organism a model of its own phenotypic niche.
- (B) The Markov Blanket allows the brain to instantly teleport quantum states across cell membranes without passing through sensory receptors.
- (C) The Markov Blanket proves that external physical reality does not exist and that reality is an illusion projected by the hippocampus.
- (D) The internal states $\mu$ are causally disconnected from active states, proving that voluntary action is physically impossible.

**Correct Answer**: **(A)**

#### Philosophical Grounding & Demonstration:
In probability theory, a **Markov Blanket** of a node or set of states isolates those states from the rest of the network: conditioned on the blanket states, the internal states are conditionally independent of the external states:
$$P(\mu, \eta | s, a) = P(\mu | s, a) P(\eta | s, a)$$
In the Free Energy Principle applied to neurobiology:
1. *Epistemological Boundary*: The brain ($\mu$) is physically locked inside the darkness of the cranium. It never directly touches, sees, or contacts external worldly objects ($\eta$). All it receives are fluctuations in sensory blanket states ($s$), and all it can emit are changes in active blanket states ($a$, motor signals).
2. *Variational Free Energy as Self-Evidencing*: Any living organism that avoids entropy and maintains its phenotypic viability must minimize **variational free energy** ($F$). Mathematically:
   $$F \ge -\ln p(s|m)$$
   where $-\ln p(s|m)$ is the **surprise** (the negative log-evidence of the organism's model of its existence).
3. Minimizing free energy is mathematically equivalent to **maximizing Bayesian model evidence** (marginal likelihood). In Hohwy’s and Friston’s phrase, the organism is **"self-evidencing"**:
   > "By acting on the world to fulfill its sensory expectations (active inference) and updating its internal states to match sensory inputs (perceptual inference), the organism continually gathers evidence for its own continued existence as an embodied system."

This formulation provides a unified biological grounding for epistemology, perception, and action: perception updates internal beliefs to match the world, while action changes the world to match internal expectations.

#### Distractor Analysis:
- **(B) is incorrect**: The Markov Blanket is a classical statistical separation boundary in dynamical systems theory; it does not involve quantum teleportation.
- **(C) is incorrect**: The Free Energy Principle is a robust physicalist and realist framework; external states $\eta$ exist objectively, but the organism must infer them probabilistically.
- **(D) is incorrect**: Internal states $\mu$ are directly coupled to active states $a$; action is central to the Free Energy Principle through *active inference*.

**Primary Textual Reference**: Karl Friston, "Life as We Know It", *Journal of the Royal Society Interface* 10(86) (2013): 20130475; Jakob Hohwy, "The Self-Evidencing Brain", *Noûs* 50(2) (2016): 259–285; Michael Kirchhoff et al., "The Markov Blankets of Life: Autonomy, Active Inference and the Extended Mind", *Royal Society Open Science* 5(1) (2018): 171825.

---

### Question 2: Alfred Mele's Critique of Benjamin Libet: Intention vs. Urge
**Format**: Conceptual Multiple-Choice (Format A)  
**Difficulty Tier**: Conceptually Hard / Frontiers  
**Primary Thinkers**: Alfred R. Mele (2009)

In *Effective Intentions: The Power of Conscious Will* (2009), philosopher of action Alfred Mele levels a devastating conceptual and empirical critique against Benjamin Libet’s claim to have disproven conscious free will. What is Mele’s primary conceptual distinction that dismantles Libet’s interpretation of the Readiness Potential ($RP$)?

- (A) Libet systematically equivocated between a passive, non-committal **urge / desire** to act and an executive **decision / proximal intention** to act, and because the readiness potential occurs prior to genuine commitment, an $RP$ merely reflects the non-conscious preliminary emergence of an urge, not an unfree decision.
- (B) Libet used an analog oscilloscope rather than a digital clock, rendering all timing measurements invalid by a factor of 10 seconds.
- (C) Libet failed to recognize that the human soul is non-physical, so EEG electrodes only record the metabolic decay of glial cells.
- (D) Libet’s subjects were under hypnosis and therefore lacked ordinary legal consciousness.

**Correct Answer**: **(A)**

#### Philosophical Grounding & Demonstration:
In action theory and the philosophy of mind, Alfred Mele exposes the cardinal flaw in Libet’s experimental paradigm: **the conceptual conflation of urges with decisions**.

Mele differentiates between three distinct mental phases:
1. *Urge / Inclination / Desire*: A feeling of being prompted toward an action (e.g., feeling the urge to scratch an itch or reach for a biscuit). Having an urge does *not* constitute deciding or intending to act; one frequently experiences urges and consciously dismisses them without a second thought.
2. *Decision*: The momentary mental action of forming an intention to act in response to uncertainty or competing inclinations.
3. *Intention (Proximal vs. Distal)*: An executive commitment to execute an action (proximal: "flick the wrist *now*"; distal: "go to the gym tomorrow").

Mele analyzes Libet’s instructions to subjects:
Libet instructed participants to *"wait for the urge to act to arise spontaneously, and do not plan the action in advance."*
Mele demonstrates:
- The onset of the Readiness Potential ($RP$) at $-550\text{ ms}$ represents the brain’s unconscious preparation corresponding to the **emergence of the urge**, or the general background readiness to flex.
- The conscious awareness reported by subjects at $-200\text{ ms}$ ($W$ time) is the subject’s **first awareness of that urge**.
- The actual **decision / proximal intention** to execute occurs *after* the urge is recognized (between $-200\text{ ms}$ and $-50\text{ ms}$).

Mele concludes:
> "Libet’s data show that conscious awareness of an urge to act arises after unconscious neural preparation for that urge. But an urge is not a decision! It is perfectly compatible with free will that our urges arise from unconscious neural processes, so long as conscious deliberation and executive intentions have the power to endorse, guide, or reject those urges."

Subsequent empirical studies by Judy Trevena and Jeff Miller (2010), as well as Aaron Schurger et al. (2012), verified Mele’s philosophical critique: the readiness potential occurs even when subjects ultimately decide *not* to move, proving that the $RP$ is merely ongoing stochastic neural fluctuations, not an irrevocable decision to act.

#### Distractor Analysis:
- **(B) is incorrect**: Libet’s cathode-ray clock was carefully calibrated and accurate to within tens of milliseconds; the flaw was conceptual, not an equipment calibration error of 10 seconds.
- **(C) is incorrect**: Mele is an empirical, naturalistic philosopher who fully embraces neuroscience; he never appeals to Cartesian soul-substances or glial cell decay.
- **(D) is incorrect**: Libet’s subjects were ordinary, alert, non-hypnotized human volunteers.

**Primary Textual Reference**: Alfred R. Mele, *Effective Intentions: The Power of Conscious Will* (Oxford University Press, 2009), Chapter 3: "Libet's Challenge", pp. 47–78; Aaron Schurger, Jacobo D. Sitt, and Stanislas Dehaene, "An Accumulator Model for Spontaneous Neural Activity Prior to Self-Initiated Movement", *Proceedings of the National Academy of Sciences* 109(42) (2012): E2904–E2913.
