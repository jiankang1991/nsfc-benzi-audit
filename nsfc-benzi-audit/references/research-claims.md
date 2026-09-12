# Claim-Specific Evidence Boundaries

Read only cards matching a claim actually made in the draft. These cards are diagnostic criteria, not NSFC official requirements. Apply the countercheck in [benzi-logic.md](benzi-logic.md#check-before-issuing-a-finding) before issuing a strong opinion. Card IDs identify maintained rule families; findings have their own IDs.

## PRED — Association, Prediction And Statistical Methods

- **Applies to:** prediction, estimation, calibration, uncertainty, generalization or statistical evaluation claims.
- **Inspect:** target quantity/population, information available when the prediction is made, assumptions, evaluation unit, comparison, metrics and evidence appropriate to the stated scope. Inspect data splitting/tuning only when data are part of the claim; theoretical work may rely on proofs and counterexamples.
- **Substantive failure:** validation uses information unavailable in the claimed setting, reported evidence supports a different population/quantity, or a claimed guarantee is evaluated by a measure that cannot test it.
- **Exceptions:** prediction or association does not promise causality. An uncertainty or method-validity contribution need not add a mechanistic experiment. Random splits may be appropriate for a within-source claim; regional, temporal or patient-independent claims need corresponding evidence. Planned tests are not completed results.
- **Basis:** inference must stay within the information, assumptions and evaluation scope stated by the applicant. For actual model mathematics, verify the provided derivation rather than treating this card as proof.
- **Routing:** clinical endpoints/cohorts use the medical reference; spatial units and acquisitions use the geospatial reference. Do not import either domain solely because the draft uses ML.

## CAUSAL — Mechanisms And Causal Explanations

- **Applies to:** a claim that a factor causes, mediates or explains a process, rather than merely predicts it.
- **Inspect:** proposed causal relation, competing explanations, relevant biological/physical components, and how the planned evidence distinguishes those explanations. Existing literature may support a premise if its identity and scope are checked.
- **Substantive failure:** the conclusion attributes a cause or mechanism that the stated observations/design cannot distinguish, or depends on a component absent from the declared model without complementary evidence.
- **Exceptions:** no universal 内因×外因×孕育/发展/终止 structure, molecular experiment or particular intervention is required. The applicable evidence can be experimental, observational with justified identification assumptions, theoretical or complementary. A planned mechanism study need not have completed its decisive result before applying.
- **Basis:** the evidence must distinguish the causal claim from relevant alternatives. Concrete medical model facts require model-specific sources; see [medical-biomedical.md](medical-biomedical.md#models-and-experiments).

## MODEL — Mathematical, Statistical And Computational Models

- **Applies to:** a model or solver whose properties support a scientific claim.
- **Inspect:** variables, assumptions, formulation, proposed analysis/solver and how the claimed property will be tested. Track whether an approximation changes the property being claimed.
- **Substantive failure:** the formulation cannot represent the stated object/condition, an essential assumption is contradicted elsewhere, or the proposed analysis never reaches the promised result.
- **Exceptions:** governing equations, initial/boundary conditions, extrema and transition criteria matter only for models that use them. Statistical, discrete and learning models do not all need PDE-style completeness. Feasibility needs a credible route and supporting capacity, not a finished theorem.
- **Basis:** internal consistency between model, assumptions and claimed property; inspect the applicant's actual mathematics before calling it false.

## INVERSE — Recovering Unknowns From Observations

- **Applies to:** retrieval, reconstruction, identification or inversion claims about unknown quantities.
- **Inspect:** observation-to-unknown relation, ambiguity and stability relevant to the promised recovery, constraints/priors and their influence, proposed solver, and validation against the claimed recovery target.
- **Substantive failure:** the argument treats an ambiguous recovery as uniquely determined without a supporting restriction, or validates observation fit while promising unsupported recovery accuracy.
- **Exceptions:** no mandatory theorem proving all of existence/uniqueness/stability, regularizer or causal perturbation applies to every inverse problem. A predictive inverse mapping may have a narrower empirical scope. Priors must be explained when used, not added just to satisfy a checklist.
- **Basis:** distinguish fitting observed data from support for the inferred unknown. Specialist mathematical claims require inspection of their source/derivation.

## MEASURE — New Observables And Precision Limits

- **Applies to:** a new measurement modality, sensitivity advantage or claimed improvement over a physical precision/resolution limit.
- **Inspect:** observation/noise model, parameters and nuisance quantities, sensitivity under named conditions, proposed or preliminary bound/error analysis, observability limits and a fair comparison with the incumbent modality.
- **Substantive failure:** the asserted advantage has neither supporting evidence nor a credible way to test its magnitude or limits, or comparisons change operating conditions without explaining their effect.
- **Exceptions:** CRLB/Fisher information is one possible tool, not a mandatory formula; state its assumptions if used. A bound proposed as a project result is not a missing completed prerequisite. Qualitative discovery claims need evidence appropriate to their actual strength.
- **Basis:** a claim about a measurable advantage needs a comparable measurement model and evidence; this card does not certify any physical-limit derivation.

## TRANSFER — Proxies, Analogy And Generalization

- **Applies to:** inference from a proxy, simulation, borrowed law, population, scale or domain to another target.
- **Inspect:** which relationship/property is transferred, why relevant assumptions survive, what changes, and what theoretical or empirical check supports the target scope.
- **Substantive failure:** validity in the source setting is presented as target validity without addressing a material difference, or validation supports only a narrower scope than the conclusion.
- **Exceptions:** inspiration or routine use of an established algorithm does not assert that a source-domain law is universally valid. Tables, named bridging quantities, real-world deployments and a fixed collection of validation scenes are not universal prerequisites. A study explicitly limited to a proxy may be coherent within that limit.
- **Basis:** the burden follows the claimed inference across conditions, not the presence of interdisciplinary vocabulary.

## NOVEL — Novelty, Priority And Knowledge Increment

- **Applies to:** a claimed knowledge/method increment or broad priority statement such as 首次/空白/国际领先.
- **Inspect:** the stated comparison set, actual prior result and assumptions, proposed increment, and search/source scope. Keep topic similarity separate from method equivalence.
- **Substantive failure:** supplied comparable evidence already establishes the specific claim described as new, or the draft's own argument does not identify what its claimed increment is.
- **Exceptions:** absent accessible references leave novelty unverified; they do not prove novelty or lack of it. Originality need not overturn a published impossibility, escape a universally dead-end route or already have third-party adoption. Technical improvements can embody a scientific-method contribution when the new property and evidence are specified.
- **Basis:** comparisons must support the exact scope of the claim. Literature evidence levels live in [representative-works.md](representative-works.md); kd records alone cannot establish the full research frontier.

## Maintaining These Cards

Each high-impact card states applicability, evidence, exceptions and basis in one place. Domain references specialize the evidence; writing examples cannot strengthen the verdict threshold. When changing a card, inspect its callers, record any superseded rule in the maintenance record, and test a matching substantive failure plus a plausible non-failure. Follow [exemplar-learning.md](exemplar-learning.md#improving-this-skill-from-examples) for source admission; do not promote an observed successful style directly into a requirement.
