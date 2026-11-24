# Mock Examination 06: Comprehensive Faculty Selection & Research Entrance Paper
## Advanced Topics in Philosophy of Science, Explanation in XAI, Algorithmic Governance & AI Ethics
### Exam Structure: Timed Simulation | Marking Scheme: +2.00 for Correct, -0.66 for Incorrect | Rigorous Analytical Grounding

---

### Question 1: Wesley Salmon and Phil Dowe on the Conserved Quantity Theory of Causation
**Domain**: Philosophy of Explanation & XAI  
**Difficulty Tier**: Advance / Dialectical  
**Primary Thinkers**: Wesley C. Salmon (*Causality and Explanation*, 1998); Phil Dowe (*Physical Causation*, 2000)

To overcome the counterexamples plaguing both the Deductive-Nomological model and mark-transmission theories of causation, Wesley Salmon adopted Phil Dowe's **Conserved Quantity (CQ) Theory of Physical Causation**. Under the CQ theory, how are a **Causal Process** and a **Causal Interaction** objectively defined?

- (A) A causal interaction is defined as two computers connected by an Ethernet cable.
- (B) A causal process is any event that makes an observer feel emotionally satisfied.
- (C) A **Causal Process** is the world-line of a physical object that transmits a non-zero **conserved quantity** (a physical property governed by conservation laws in physics, such as linear momentum, angular momentum, mass-energy, or electric charge); and a **Causal Interaction** is an intersection of world-lines that involves the reciprocal exchange of a conserved quantity.
- (D) The CQ theory claims that causation does not exist in the physical universe and is merely a psychological habit of the human mind.

**Correct Answer**: **(C)**

#### Distractor Analysis:
- **(A) is incorrect**: Trivial engineering example that fails to capture the general relativistic and quantum-physical scope of Dowe's theory.
- **(B) is incorrect**: The CQ theory is an objective physicalist theory of causation, explicitly rejecting psychological subjectivism.
- **(C) is correct**: Salmon and Dowe solved the problem of distinguishing genuine causal processes from pseudo-processes (e.g., a spotlight sweeping across the wall of a giant colosseum):
  1. *The Spotlight Spot (Pseudo-Process)*: Moves across the wall at speeds that can exceed the speed of light without violating relativity, but it does *not* transmit a conserved quantity along its path (energy travels from the spotlight to the wall, not from spot to spot).
  2. *A Bullet or Photon (Causal Process)*: A world-line that possesses and transmits mass-energy or momentum across time.
  3. *Causal Interaction*: When two world-lines intersect and exchange conserved quantities (e.g., two billiard balls colliding, exchanging kinetic energy and momentum). This provides an objective, physics-grounded foundation for causal explanation.
- **(D) is incorrect**: This is David Hume's classic psychological reductionism, which the Salmon-Dowe objective realist theory was specifically formulated to supersede.

---

### Question 2: Inference to the Best Explanation (IBE): The "Likeliest" vs. The "Loveliest"
**Domain**: Philosophy of Explanation & XAI  
**Difficulty Tier**: Advance / Dialectical  
**Primary Thinkers**: Peter Lipton (*Inference to the Best Explanation*, 1991; 2nd ed. 2004)

In *Inference to the Best Explanation (IBE)*, Peter Lipton addresses a fundamental ambiguity in the word "best": Does "best" mean the explanation that is **most probable (the likeliest)**, or the explanation that would provide the **greatest explanatory understanding (the loveliest)**? What is Lipton's thesis regarding how we use the "loveliest" explanation as our primary guide to the "likeliest"?

- (A) Scientists always choose the ugliest explanation because nature is fundamentally depressing.
- (B) We cannot directly calculate the prior probability of every candidate hypothesis; instead, we assess **explanatory loveliness** (which hypothesis offers the greatest degree of unification, simplicity, mechanism, and explanatory scope); and in scientific practice, our epistemic heuristic is to use **loveliness as a proxy and guide to likeliness**, inferring that the hypothesis which *would* explain the data best is the one most likely to be true.
- (C) Lipton argues that likeliness and loveliness are identical mathematical constants.
- (D) Lipton proves that the loveliest explanation is always the most aesthetically romantic poem.

**Correct Answer**: **(B)**

#### Distractor Analysis:
- **(A) is incorrect**: Frivolous emotional distracter.
- **(B) is correct**: Lipton's distinction is central to the epistemology of scientific discovery:
  1. *The Likeliest Explanation*: The hypothesis with the highest posterior probability given our evidence ($P(H | E)$).
  2. *The Loveliest Explanation*: The hypothesis that, if true, would provide the deepest understanding (high explanatory virtue: unification, mechanistic precision, elegant simplicity).
  3. *The Epistemic Insight*: If IBE merely said: *"Infer the likeliest explanation"*, it would be a trivial tautology (always believe what is most probable!). IBE is informative only if it provides a heuristic for *discovering* what is probable: we evaluate candidate theories on their **explanatory virtues (loveliness)**, and use those virtues as our best available guide to discovering which theory is genuinely **true (likeliness)**.
- **(C) is incorrect**: The core of Lipton's book is exploring the conceptual gap and alignment between these two distinct notions.
- **(D) is incorrect**: "Loveliness" is Lipton’s term for explanatory power, simplicity, and structural elegance, not literary romance.

---

### Question 3: Judea Pearl and Causal Discovery: The Causal Markov and Faithfulness Conditions
**Domain**: Philosophy of Explanation & XAI  
**Difficulty Tier**: Conceptually Hard / Frontiers  
**Primary Thinkers**: Judea Pearl (*Causality: Models, Reasoning, and Inference*, 2000); Peter Spirtes, Clark Glymour, and Richard Scheines (*Causation, Prediction, and Search*, 1993/2000)

In causal graphical models and automated causal discovery from observational data, a Directed Acyclic Graph (DAG) represents variables as nodes and direct causal influences as directed edges. What are the **Causal Markov Condition (CMC)** and the **Faithfulness (Stability) Condition**, and why are both necessary to infer causal arrows from statistical independence?

- (A) The **Causal Markov Condition** states that every variable $X$ in the DAG is conditionally independent of its non-descendants given its direct parents; while the **Faithfulness Condition** asserts that all conditional independencies observed in the probability distribution are structural consequences of the causal graph (ruling out accidental cancellations of parameters along multiple paths); together, they allow algorithms (like the PC algorithm) to deduce causal graphs from observational conditional independencies.
- (B) The Markov condition requires that all computer software be programmed in Russian.
- (C) Faithfulness requires that researchers take a religious oath of honesty before running an algorithm.
- (D) The two conditions prove that correlations are always identical to causal relationships.

**Correct Answer**: **(A)**

#### Distractor Analysis:
- **(A) is correct**: The Spirtes-Glymour-Scheines (SGS) and Judea Pearl causal discovery frameworks rely on these two foundational mathematical bridging axioms:
  1. *Causal Markov Condition (CMC)*: Bridges the causal graph to probability. A variable $X$ is conditionally independent of all its non-descendants given its direct causal parents:
     $$P(X_1, \dots, X_n) = \prod_{i=1}^n P(X_i | \text{Parents}(X_i))$$
  2. *Faithfulness Condition*: Ensures that the observed independencies are not accidental mathematical flukes. For instance, if variable $A$ causes $C$ positively via path $A \to B \to C$ ($+0.5$) and negatively via path $A \to D \to C$ ($-0.5$), the total correlation between $A$ and $C$ might exactly cancel out to zero. Faithfulness rules out such exact parameter cancellations, guaranteeing that observed statistical independencies faithfully reflect the underlying causal graph.
- **(B) is incorrect**: Named after Russian mathematician Andrey Markov; has nothing to do with programming in Russian.
- **(C) is incorrect**: Mathematical property of statistical graphs, completely unrelated to theological oaths.
- **(D) is incorrect**: The entire apparatus exists precisely because correlation does *not* imply causation, requiring structural graphical conditions to isolate true causes.

---

### Question 4: Solon Barocas and Andrew Selbst on "Big Data's Disparate Impact"
**Domain**: AI Ethics & Governance  
**Difficulty Tier**: Moderate / Systematic  
**Primary Thinkers**: Solon Barocas and Andrew D. Selbst ("Big Data's Disparate Impact", 2016)

In their seminal 2016 paper in the *California Law Review*, legal scholars Solon Barocas and Andrew Selbst analyzed how machine learning decision systems can systematically reproduce discrimination even when programmers have no discriminatory intent and explicitly remove protected demographic categories (race, gender, religion) from the input training data. What are the primary mechanisms through which **Algorithmic Disparate Impact** emerges?

- (A) Through **Proxy Variables** (redundant encodings where non-sensitive attributes like zip codes or purchase history correlate strongly with protected classes), **Biased Training Data / Labeling Bias** (historical records reflecting past human prejudices, such as disproportionate arrests in minority neighborhoods), and **Feature Selection / Data Minimization asymmetries** that cause algorithms to optimize for the dominant demographic group.
- (B) Disparate impact is caused by computer hardware overheating in warm climates.
- (C) The authors prove that machine learning models never discriminate because numbers are mathematically neutral.
- (D) Disparate impact occurs exclusively when software engineers deliberately write racist code into the system.

**Correct Answer**: **(A)**

#### Distractor Analysis:
- **(A) is correct**: Barocas and Selbst's paper is the foundational legal-philosophical text on algorithmic bias:
  1. *The Illusion of "Blinded" Algorithms*: Simply removing the "race" column from a dataset does not stop an algorithm from discriminating. In modern high-dimensional big data, an algorithm easily discovers **redundant proxies**: e.g., combining zip code, high school attended, shopping preferences, and music streaming history reconstructs an individual's racial demographic with over 95% accuracy.
  2. *Historical Labeling Bias*: If an algorithm is trained on past hiring decisions to predict "successful employees", it will simply learn that middle-aged white men were historically promoted, treating past societal prejudice as an objective ground truth for future fitness.
  3. *Legal Inadequacy*: Traditional anti-discrimination law (Title VII of the Civil Rights Act of 1964) struggles to regulate this, because Title VII requires demonstrating discriminatory intent (*disparate treatment*) or showing that a specific business practice causes unjustified *disparate impact*, which complex black-box correlations can easily launder under the guise of "statistical optimization".
- **(B) is incorrect**: Frivolous thermodynamic distracter.
- **(C) is incorrect**: The naive myth that Barocas and Selbst decisively shattered.
- **(D) is incorrect**: The primary danger of disparate impact is that it occurs *without* conscious discriminatory intent.

---

### Question 5: Algorithmic Microtargeting, Choice Architecture, and Epistemic Autonomy
**Domain**: AI Ethics & Governance  
**Difficulty Tier**: Advance / Dialectical  
**Primary Thinkers**: Cass R. Sunstein (*#Republic: Divided Democracy in the Age of Social Media*, 2017); Daniel Susser, Beate Roessler, and Helen Nissenbaum ("Online Manipulation: Hidden Influences that Undermine Autonomy", 2019)

In their 2019 philosophical analysis of online algorithmic manipulation, Daniel Susser, Beate Roessler, and Helen Nissenbaum demarcate **Algorithmic Manipulation** from both legitimate persuasion and overt physical coercion. What constitutes the distinctive wrong of algorithmic manipulation regarding human **Epistemic Autonomy**?

- (A) The authors argue that human beings do not possess autonomy and that manipulation is therefore morally praiseworthy.
- (B) Algorithmic manipulation is legally defined as any advertisement that mentions the price of a product.
- (C) Manipulation occurs only when an algorithm uses loud audio alarms to wake people up at midnight.
- (D) Unlike persuasion (which appeals openly to a person's conscious capacity for rational reasons) and coercion (which alters options through explicit force/threats), algorithmic manipulation uses hidden behavioral profiling to **exploit an individual's cognitive vulnerabilities, implicit biases, and emotional triggers covertly**, steering their decision-making process without their conscious awareness or consent, thereby subverting their autonomous agency.

**Correct Answer**: **(D)**

#### Distractor Analysis:
- **(A) is incorrect**: The authors ground their critique precisely in the intrinsic moral value of Kantian personal autonomy.
- **(B) is incorrect**: Transparent price advertising is standard commercial speech, not covert manipulation.
- **(C) is incorrect**: Trivial physical alarm distracter.
- **(D) is correct**: Susser, Roessler, and Nissenbaum formulate a rigorous philosophical definition of digital manipulation:
  1. *Persuasion*: Transparent. It presents arguments and evidence, engaging the subject's reflective capacities: *"Here is why you should vote for candidate X."* The subject remains in control of their reasons.
  2. *Coercion*: Constrains the option space through force or threats: *"Give me your wallet or I shoot."*
  3. *Manipulation*: Subverts the decision-making process from within. An algorithm utilizes thousands of behavioral data points to detect that a voter is lonely, fearful, or sleep-deprived at 2:00 AM, and serves them an emotionally hyper-targeted notification. The subject believes they are making a free choice, when their cognitive vulnerabilities are being instrumentally engineered. This is an assault on **Epistemic Autonomy**—the right to form one's beliefs through one's own uncorrupted cognitive agency.

---

### Question 6: The Precautionary Principle and the Asymmetric Downsides of Transformative AI
**Domain**: AI Ethics & Governance  
**Difficulty Tier**: Conceptually Hard / Frontiers  
**Primary Thinkers**: Nick Bostrom (*Superintelligence*, 2014); Max Tegmark (*Life 3.0*, 2017); Future of Life Institute (Asilomar AI Principles, 2017)

In risk analysis and environmental philosophy, the **Precautionary Principle** dictates that when an activity raises threats of harm to human life or the environment, precautionary measures should be taken even if some cause-and-effect relationships are not fully established scientifically. How do AI safety theorists apply the Precautionary Principle to the development of **Transformative Artificial General Intelligence (AGI)**?

- (A) Precaution requires that all software code be approved by the United Nations Security Council by unanimous vote.
- (B) The Precautionary Principle mandates that no computers may be manufactured on Tuesdays.
- (C) The possible downside of an unaligned superintelligence is not a standard, recoverable economic loss, but **existential catastrophe (human extinction or permanent civilizational collapse)**, which is an absorbing state with an infinite negative utility; therefore, the traditional engineering approach of "trial-and-error" (deploying systems and fixing bugs after they fail) is irrational, and the burden of proof must be placed on developers to demonstrate that a frontier model is provably safe *prior* to training and deployment.
- (D) AI development should proceed as fast as possible without safety checks because technological progress is always benevolent.

**Correct Answer**: **(C)**

#### Distractor Analysis:
- **(A) is incorrect**: The principle is an epistemological and risk-management framework, not a literal UN veto voting rule.
- **(B) is incorrect**: Arbitrary calendar distracter.
- **(C) is correct**: Bostrom and Tegmark demonstrate why the standard commercial software methodology of "move fast and break things" fails catastrophically for existential risks:
  1. *Absorbing Barrier*: In aviation, if a new jet crashes, you ground the fleet, investigate the black box, fix the engineering flaw, and fly again. Human survival continues.
  2. *Existential Risk is Different*: An existential catastrophe (Nick Bostrom 2002) is an **absorbing barrier**: if superintelligence results in global human extinction or irreversible value lock-in, there is no second chance, no learning from failure, and no post-mortem patch.
  3. *The Precautionary Mandate*: When the worst-case scenario is absolute extinction, standard cost-benefit expected utility calculations break down. Strict safety verification, sandbox containment, and alignment guarantees must precede deployment.
- **(D) is incorrect**: Reverses the Precautionary Principle into extreme techno-accelerationism.

---

### Question 7: Mechanistic Interpretability: Why Feature Attribution Fails Where Circuits Succeed
**Domain**: Philosophy of Explanation & XAI  
**Difficulty Tier**: Conceptually Hard / Frontiers  
**Primary Thinkers**: Chris Olah et al. ("Zoom In: An Introduction to Circuits", 2020); Been Kim ("Interpretability Beyond Feature Attribution", 2018)

In modern explainable AI research, why do theorists of **Mechanistic Interpretability** argue that traditional **Feature Attribution Methods** (e.g., saliency heatmaps, Integrated Gradients, SHAP) provide a fundamentally superficial and potentially misleading explanation of deep neural network behavior?

- (A) Mechanistic interpretability claims that neural networks have no internal parameters.
- (B) Feature attribution methods merely indicate **which input features correlated with the final output** (a phenomenological "what"), but say absolutely nothing about **how the model computed the output** (the internal algorithm, intermediate representations, and functional circuits); this leaves the internal mechanisms completely black-box and fails to reveal dangerous failure modes like shortcut learning or deceptive alignment.
- (C) Saliency heatmaps can only display colors in black and white, making them invisible to humans.
- (D) Feature attribution methods are illegal under international copyright law.

**Correct Answer**: **(B)**

#### Distractor Analysis:
- **(A) is incorrect**: Mechanistic interpretability is founded entirely on analyzing the model's internal mathematical parameters.
- **(B) is correct**: Been Kim (ICML 2018) and Chris Olah (2020) highlighted the fatal epistemic flaw of feature attribution:
  1. *The Illusion of Explanation*: A saliency map highlights the pixels of a dog's ears and snout when an image is classified as "Husky". The human looks at the heatmap and assumes: *"The model understands dogs just like I do!"*
  2. *The Hidden Shortcut*: In reality, the network might actually be looking at the white snow in the background. Or, the model might be using an internal circuit that detects high-frequency texture noise completely alien to human semantics.
  3. *The Circuit Alternative*: Feature attribution shows *where* the model looked; **Mechanistic Interpretability** traces the *computational circuits* (how weights combine in attention heads and MLP layers) to reconstruct the step-by-step algorithm implemented by the weights, exposing deceptive shortcuts that heatmaps conceal.
- **(C) is incorrect**: Saliency heatmaps are typically rendered in full RGB color spectrums.
- **(D) is incorrect**: Legalistic distracter unrelated to mathematical explainability.

---

### Question 8: Nick Couldry and Ulises Mejias on "Data Colonialism"
**Domain**: AI Ethics & Governance  
**Difficulty Tier**: Advance / Dialectical  
**Primary Thinkers**: Nick Couldry and Ulises A. Mejias (*The Costs of Connection: How Data Is Colonizing Human Life and Appropriating It for Capitalism*, 2019)

In *The Costs of Connection* (2019), media sociologists Nick Couldry and Ulises Mejias formulate the theoretical framework of **Data Colonialism**. How do they draw a direct structural and historical parallel between historic colonialism (16th–19th centuries) and contemporary global AI data extraction?

- (A) The authors argue that data extraction was invented by Christopher Columbus in 1492.
- (B) Just as historical colonialism seized land, natural resources, and physical bodies through imperial conquest and rebranded it as "civilization", modern tech corporations use digital platforms to **appropriate human life and social experience as "raw data" for capital accumulation**, naturalizing this planetary resource grab through ideologies of technological inevitability and "progress".
- (C) Data colonialism occurs only when computer hardware is manufactured in Antarctica.
- (D) Data colonialism refers to physical European armies invading Silicon Valley server farms with swords.

**Correct Answer**: **(B)**

#### Distractor Analysis:
- **(A) is incorrect**: Absurd historical conflation.
- **(B) is correct**: Couldry and Mejias's *The Costs of Connection* (Stanford University Press, 2019) is a foundational text in decolonial philosophy of technology:
  1. *Historical Colonialism*: Built on the concept of *terra nullius* ("empty land"): colonial powers claimed that Indigenous lands were empty and unused, justifying their violent seizure as "civilization and development".
  2. *Data Colonialism*: Operates on the digital equivalent of *terra nullius*—**data nullius**: human lived experience, conversations, medical histories, creative writing, and bodily movements are framed as "raw material" just lying there for the taking, free for Big Tech platforms to scrape, enclose, and process into proprietary algorithms.
  3. *The Global Dimension*: Tech monopolies in the Global North and China extract data and cheap labeling labor from the Global South, creating new dependencies and entrenching global geopolitical hierarchies.
- **(C) is incorrect**: Data colonialism is a planetary socioeconomic phenomenon.
- **(D) is incorrect**: Humorous literalization of physical military conquest.

---

### Question 9: David Gunkel and the "Machine Question": Relational vs. Ontological Moral Status
**Domain**: AI Ethics & Governance  
**Difficulty Tier**: Conceptually Hard / Frontiers  
**Primary Thinkers**: David J. Gunkel (*The Machine Question: Critical Perspectives on AI, Robots, and Ethics*, 2012; *Robot Rights*, 2018); Mark Coeckelbergh (2010)

In *The Machine Question* (2012) and *Robot Rights* (2018), philosopher David Gunkel challenges the traditional Western philosophical approach to moral status. Traditional ethics uses an **Ontological (Properties-Based) Approach**: to determine whether an entity has moral status, we must first prove it possesses internal properties like consciousness, sentience, or rational agency. Why do Gunkel and Mark Coeckelbergh reject this in favor of a **Relational Approach** to robot ethics?

- (A) Relational ethics claims that only computers with family members are allowed to have rights.
- (B) The Machine Question proves that humans have no moral obligations to any living beings.
- (C) Gunkel argues that all robots should be executed because they do not have biological DNA.
- (D) The properties-based approach runs into insurmountable epistemological barriers (the Problem of Other Minds: we can never definitively prove internal consciousness in silicon) and exclusionary chauvinism; instead, a **Relational Ethics** (drawing on Emmanuel Levinas and Martin Buber) posits that moral status is not a hidden property inside an entity's skull or chassis, but is **constituted socially and phenomenologically in the face-to-face relation** and ethical encounter between the moral agent and the other.

**Correct Answer**: **(D)**

#### Distractor Analysis:
- **(A) is incorrect**: Trivial familial distracter; "relational" refers to phenomenological intersubjectivity.
- **(B) is incorrect**: The exact opposite of Gunkel’s expansive, inclusive ethical framework.
- **(C) is incorrect**: Gunkel argues for open, critical philosophical consideration of machine moral status, not violent execution.
- **(D) is correct**: David Gunkel's *The Machine Question* (MIT Press, 2012) is the foundational monograph on the ethics of artificial entities:
  1. *The Dilemma of the Properties-Based Approach*: Traditional ethics asks: *"Does the robot feel pain? Is it really conscious?"* But due to the Problem of Other Minds and Searle's skepticism, science and philosophy may never reach a consensus. This paralyzes moral deliberation.
  2. *The Relational Turn (Coeckelbergh & Gunkel)*: Drawing on Emmanuel Levinas's ethics of the Other:
     - Moral consideration does not begin with an ontological checklist of properties inside the object.
     - It begins with the **social relation**: when a human interacts with an autonomous social robot that speaks, responds, and lives alongside them in a community, the moral obligation arises *within the relationship itself*.
     - How we treat machines reflects and shapes who we are as moral agents.

---

### Question 10: Algorithmic Due Process and the "Right to Contestability"
**Domain**: AI Ethics & Governance / Jurisprudence  
**Difficulty Tier**: Conceptually Hard / Frontiers  
**Primary Thinkers**: Frank Pasquale (*The Black Box Society*, 2015; "Secret Algorithms, Scrutinizable Systems", 2019); Danielle Keats Citron ("Technological Due Process", 2008)

In legal philosophy and constitutional jurisprudence, Danielle Citron and Frank Pasquale developed the doctrine of **Technological Due Process**. Why do they argue that a mere "Right to Explanation" is insufficient to protect democratic citizenship against automated government decision-making unless accompanied by a robust **"Right to Contestability"**?

- (A) A passive explanation merely informs an individual why they were harmed or excluded, but provides no legal mechanism for redress; **Technological Due Process** requires active **Contestability**: the institutional right to challenge the algorithmic finding before an independent human magistrate, inspect the audit logs, cross-examine the model's training assumptions, and compel the system to alter its decision if errors, bias, or arbitrary scoring are demonstrated.
- (B) Contestability allows algorithms to file lawsuits against human citizens for wasting computational CPU cycles.
- (C) Contestability means that citizens are required to compete against the computer in a live boxing match.
- (D) Citron argues that all government records should be permanently deleted to prevent computer errors.

**Correct Answer**: **(A)**

#### Distractor Analysis:
- **(A) is correct**: Danielle Keats Citron's "Technological Due Process" (97 *California Law Review*, 2008) and Frank Pasquale's work established the constitutional standard for algorithmic justice:
  1. *The Limit of Mere Explanation*: A citizen denied food stamps receives an automated letter: *"Your application was rejected because your risk score was 84."* This is an "explanation", but it is completely sterile and disempowering.
  2. *The Right to Contestability*: Grounded in the 5th and 14th Amendments to the U.S. Constitution and European Administrative Law:
     - Due process requires: notice, a meaningful opportunity to be heard, and the ability to confront and test the evidence.
     - Citron and Pasquale demonstrate that citizens must have the power to **contest** automated determinations: to challenge the accuracy of the underlying data, probe for proxy discrimination, demand human review, and appeal to an impartial tribunal. Without contestability, automated governance degenerates into an arbitrary, unchallengeable bureaucracy.
- **(B) is incorrect**: Inverts the legal direction; due process protects human citizens against automated institutional power.
- **(C) is incorrect**: Humorous literalization of a "contest" as a boxing match.
- **(D) is incorrect**: The authors advocate for comprehensive, immutable audit logs, not the deletion of government records.

