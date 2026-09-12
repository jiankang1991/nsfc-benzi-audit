# Geospatial And Remote-Sensing Applications

Use this reference when a draft or example involves remote sensing, GIS, geospatial intelligence, DEM/terrain/geomorphology, spatial databases, point clouds, SAR/optical/hyperspectral imagery, video GIS, camera networks, POI/trajectory/location data, city 3D modeling, or geospatial knowledge graphs.

Use these domain questions within [benzi-logic.md](benzi-logic.md). Prediction, inversion, measurement and transfer burdens are defined in [research-claims.md](research-claims.md); specialize them to the stated spatial object and claim. Read only relevant sections.

## Context Calibration

Geospatial drafts often carry strong application language: mapping, classification, monitoring, 3D modeling, emergency response, smart cities, public safety, ecological monitoring, or resource management. This is acceptable when the proposal exposes:

- the spatial object, scene, scale, and sensor/data boundary;
- the concrete bottleneck caused by geometry, physics, spectrum, topology, time, scale, annotation, uncertainty, or cross-source mismatch;
- the model, representation, mechanism, taxonomy, optimization, or evaluation question behind the bottleneck;
- the data, benchmark, field site, ground truth, simulation, prototype, or downstream task that can verify the claim.

Do not reject a draft merely because it mentions maps, systems, algorithms, platforms, databases, or applications. Flag it when "make a better map/model/system" is the only scientific answer.

## Geospatial Demand-To-Question Conversion

Strong geospatial drafts commonly use this chain:

`spatial scenario -> data/geometry/physical constraint -> representation or knowledge model -> method/optimization -> multi-scale or real-scene validation`

Audit questions:

- Does the draft name the spatial object and scale: pixel/point/object/region/network/city/terrain unit/global grid?
- Are the relevant data modalities and constraints visible: SAR-optical mismatch, hyperspectral bands, DEM resolution, point-cloud density, camera pose, occlusion, cloud cover, temporal revisit, label noise, or map-data incompleteness?
- Is the bottleneck framed as a relation, mechanism, representation, taxonomy, or optimization problem rather than only a processing task?
- Does the method preserve or explain spatial, spectral, temporal, topological, semantic, or physical consistency?
- Are validation scenes diverse enough to test scale, region, sensor, time, and boundary-condition generalization?

Weak signs:

- The proposal promises "intelligent interpretation", "automatic mapping", or "3D modeling" without naming the scientific obstacle.
- Data construction, model design, and application demonstration are listed, but the representation or knowledge problem connecting them is unclear.
- The key scientific question is "how to build a high-precision platform/database/system".
- The draft treats ground truth, annotation, registration, field validation, or map accuracy as implementation details rather than evidence for the scientific claim.

## Content Architecture Patterns

Common strong chains include:

- `dataset/benchmark/metadata -> representation or feature learning -> transfer/fusion/generalization -> real-scene validation`
- `physical/geometric mechanism -> model or regularizer -> solver/algorithm -> field or downstream-task evaluation`
- `taxonomy/knowledge graph -> knowledge computation -> AI-assisted classification -> database/map/atlas validation`
- `spatiotemporal unification -> coverage/topology model -> fusion/map generation -> cooperative control or scenario validation`
- `small-scale Euclidean approximation -> large-scale non-Euclidean representation -> physical constraint -> prediction/forecast validation`

Audit questions:

- Can each content item be assigned a scientific role, whether in a dependency chain or a set of complementary studies?
- Does the final map, database, platform, or prototype validate the scientific model's boundary and generality?
- Are data resources, annotation rules, registration methods, metrics, and uncertainty tied to the relevant research contents?
- For key projects, do subteams contribute to one shared framework rather than parallel deliverables?

The examples do not prescribe task counts. Check the coherence of contributions, actual dependencies and feasible scope for the target category.

## Scientific Questions

Good geospatial scientific questions often ask about:

- cross-source or cross-modal representation under spectral, spatial, geometric, or temporal mismatch;
- reconstruction, restoration, or detection under cloud, occlusion, missing data, sparse labels, or no-reference evaluation;
- coupling among spatial geometry, topology, semantics, physics, and temporal dynamics;
- taxonomy, knowledge graph, or rule-system construction for objects whose categories have both morphology and genesis/process;
- transfer and generalization across regions, sensors, scales, seasons, cities, or terrain units;
- non-Euclidean, spherical, graph, or manifold representations for large-scale spatial data;
- camera/sensor network coverage, topology, synchronization, pose, and cooperative observation under quality constraints;
- evaluation validity when ground truth is expensive, missing, delayed, or only partially observable.

Both compact noun phrases (e.g. "散射机理约束") and interrogatives can express a question. Use the shape below to inspect the underlying proposition, not to prescribe its title form:

`Under [spatial scene/data modality/scale], how do [geometry/physics/topology/semantics/time/annotation constraints] affect [representation/model/knowledge/optimization/evaluation], and how can this relation be described, computed, or validated?`

Flag questions whose body sentence can only be answered by "we will process data and compare accuracy" — the "tasks restated as problems" antipattern (a set of noun-phrase SQs that are really just the research contents relabeled, with the only real science buried elsewhere).

## Modality-Specific Physical Consistency

"Physical consistency" is often asserted generically. Check whether the physics actually enters the scientific question, the method, AND the evaluation — not just the introduction.

- SAR: 散射机理 / 属性散射中心 (ASC) / 成像几何与多角度一致性 / 极化 (HH·HV·VV)、入射角、分辨率、波段 (as controllable conditions or shift-inducing factors) / 复值与相位 / 散斑. A strong SAR draft threads these through the SQ (e.g. "生成的多条件解耦与散射机理约束"), uses a physical quantity (ASC + feature matching) as an evaluation metric, and defines its open-world along physical axes (目标观测受限 / 场景散射变化 / 载荷配置多样). "SAR" merely name-dropped in the intro is the weak case. Add the frequency/aperture axis when the draft works in the signal domain: 距离频域子带 / 多普勒(方位)频域 / 彩色子孔径图像 (CSI) / 时频谱 — bandwidth and synthetic-aperture length decide what frequency selectivity is observable at all, so 带宽、PRF、多普勒带宽 act simultaneously as the method's resource and as its 可观测性 constraint (which orders, periods, or target scales simply cannot enter the processed band). A draft that uses this axis only to display colour or texture, with no quantitative link from the frequency-domain feature back to a physical or geometric parameter, is still at the qualitative stage.
- InSAR (historical exemplar evidence is `样本不足`; this is domain guidance): 相干性 / 干涉相位 / 形变-大气-地形相位分解 / 时空基线. Use the INVERSE card in [research-claims.md](research-claims.md#inverse--recovering-unknowns-from-observations) for parameter-recovery claims; this does not mandate a causal experiment.
- Optical/hyperspectral (`样本不足`): 成像光谱 / 混合像元-端元-丰度 / 空谱联合 / 大气校正 / 降维. Term trap: real hyperspectral method vocabulary often appears in English (unmixing / endmember / abundance / low-rank / super-resolution) while 混合像元/降维/空谱 are rarely written literally — do not key domain detection only on Chinese surface terms.

## Literature And Rationale

For geospatial drafts, literature review is persuasive when it is organized by bottleneck and spatial condition:

- what existing work solves for a given sensor, scale, region, object, or data condition;
- where it fails under this project's condition, such as cross-source mismatch, cloud/occlusion, sparse labels, topology, physical consistency, or map generality;
- why that gap leads to one proposed content;
- what data, metric, field site, or downstream task will test the gap.

Avoid treating national strategy, public safety, smart-city demand, or map/database construction as a substitute for scientific rationale.

## Validation And Feasibility

Choose validation layers that test the actual claim; these are alternatives or complementary evidence, not three mandatory stages:

- controlled validation: simulation, benchmark, ablation, uncertainty analysis, theoretical property, convergence, or complexity;
- geospatial validation: multi-region, multi-sensor, multi-season, field-site, UAV/ground truth, map comparison, or physical/geometric consistency;
- application validation: downstream classification, retrieval, forecasting, monitoring, planning, emergency response, or prototype operation that tests the model rather than merely displays it.

Check whether the draft explains data source, scale, representativeness, preprocessing, registration, annotation quality, permissions, security sensitivity, and continuity. For no-reference or hard-to-observe tasks, look for proxy ground truth, downstream-task metrics, field measurements, or uncertainty bounds.

For learned models, check split independence at the unit of the generalization claim: adjacent/overlapping patches, repeated views of the same target and shared acquisitions can leak across random splits. A claimed cross-region, cross-time or cross-sensor result needs a corresponding held-out design; random splits can remain appropriate for a narrower within-source claim. Verify preprocessing and tuning use only allowed training/validation information.

## Research Basis Mapping

Strong geospatial basis sections usually map:

`previous result -> data/model/platform capability gained -> proposed content supported -> remaining gap`

For large projects, map both individual expertise and shared resources:

- sensors/data/platforms;
- prior algorithms/models;
- field sites or application partners;
- software/database/map production capability;
- theory or domain knowledge needed for taxonomy, physics, geometry, or topology.

Flag basis sections that list papers, projects, equipment, or platforms without showing which content they support.

## Innovation

Innovation should not be only a technology stack or a new dataset. Ask whether each innovation states:

- the existing limitation under the project's geospatial condition;
- the new representation, model, knowledge system, physical/geometric constraint, or evaluation principle;
- what capability or understanding becomes possible;
- what data or validation will demonstrate the claim.

Datasets, maps, knowledge bases, or systems can support innovation, but they are usually not the innovation alone unless the scientific contribution is the taxonomy, annotation principle, measurement framework, uncertainty model, or generalizable construction method.

For 一体化 / 协同 / 融合 claims, inspect the stated coupling: a mutual prior, joint objective, shared representation, common evaluation or explicit inter-model connection. Report an integration gap only when the promised relation has no support anywhere in the design. Parallel tasks can share a coherent framework; their scheduling alone does not refute integration.

## Figure Conventions

Use figures to expose spatial relations, data provenance, model structure or validation when they materially improve understanding. A shared overview, a schema or selected method diagrams may help; choose them against the applicable page limit. Do not require a framework figure or a historical figure-count norm from every draft.

## Report Add-On

Record relevant domain coverage concisely. Expand the following only when useful; reference existing finding IDs instead of repeating their explanation:

```markdown
### 遥感/GIS/地理空间专项检查
- 空间对象、尺度、数据模态是否明确：
- 数据/几何/物理/拓扑/语义约束是否转成科学问题：
- 研究内容是否形成数据/知识/模型/验证依赖链：
- 标注、配准、真值、评价指标和不确定性是否支撑核心问题：
- 地图/数据库/平台/示范是否用于验证科学主张，而非单纯交付：
- 研究基础是否映射到数据、模型、平台和场景任务：
```
