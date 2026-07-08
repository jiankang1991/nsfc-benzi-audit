# Geospatial And Remote-Sensing Applications

Use this reference when a draft or example involves remote sensing, GIS, geospatial intelligence, DEM/terrain/geomorphology, spatial databases, point clouds, SAR/optical/hyperspectral imagery, video GIS, camera networks, POI/trajectory/location data, city 3D modeling, or geospatial knowledge graphs.

The goal is to decide whether a geospatial application has converted a data-processing, mapping, monitoring, or platform demand into a reviewable basic-research problem.

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

- Can each content item be assigned a role in one chain rather than treated as an independent technical module?
- Does the final map, database, platform, or prototype validate the scientific model's boundary and generality?
- Are data resources, annotation rules, registration methods, metrics, and uncertainty tied to the relevant research contents?
- For key projects, do subteams contribute to one shared framework rather than parallel deliverables?

For youth projects, three contents are usually enough: focused representation/model, method, validation. For general projects, three or four contents can work. For key projects, four or five contents may be justified when the first content establishes shared data/knowledge or a unified spatial-temporal frame, and later contents depend on it.

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

Real funded geospatial SQs are written as compact noun phrases (e.g. "散射机理约束", "地貌全信息知识图谱体系构建", "跨源表征的联合测度机理"), not as interrogatives. Use the shape below only as an internal test of the *body sentence* beneath the noun-phrase title, and do not flag a normal noun-phrase question as task-like for being non-interrogative:

`Under [spatial scene/data modality/scale], how do [geometry/physics/topology/semantics/time/annotation constraints] affect [representation/model/knowledge/optimization/evaluation], and how can this relation be described, computed, or validated?`

Flag questions whose body sentence can only be answered by "we will process data and compare accuracy" — the "tasks restated as problems" antipattern (a set of noun-phrase SQs that are really just the research contents relabeled, with the only real science buried elsewhere).

## Modality-Specific Physical Consistency

"Physical consistency" is often asserted generically. Check whether the physics actually enters the scientific question, the method, AND the evaluation — not just the introduction.

- SAR: 散射机理 / 属性散射中心 (ASC) / 成像几何与多角度一致性 / 极化 (HH·HV·VV)、入射角、分辨率、波段 (as controllable conditions or shift-inducing factors) / 复值与相位 / 散斑. A strong SAR draft threads these through the SQ (e.g. "生成的多条件解耦与散射机理约束"), uses a physical quantity (ASC + feature matching) as an evaluation metric, and defines its open-world along physical axes (目标观测受限 / 场景散射变化 / 载荷配置多样). "SAR" merely name-dropped in the intro is the weak case.
- InSAR (flag `样本不足` — add only by analogy, not as a sample-derived rule): 相干性 / 干涉相位 / 形变-大气-地形相位分解 / 时空基线. Treat parameter estimation as an inverse problem (see benzi-logic Research-Type Tests).
- Optical/hyperspectral (`样本不足`): 成像光谱 / 混合像元-端元-丰度 / 空谱联合 / 大气校正 / 降维. Term trap: real hyperspectral method vocabulary often appears in English (unmixing / endmember / abundance / low-rank / super-resolution) while 混合像元/降维/空谱 are rarely written literally — do not key domain detection only on Chinese surface terms.

## Literature And Rationale

For geospatial drafts, literature review is persuasive when it is organized by bottleneck and spatial condition:

- what existing work solves for a given sensor, scale, region, object, or data condition;
- where it fails under this project's condition, such as cross-source mismatch, cloud/occlusion, sparse labels, topology, physical consistency, or map generality;
- why that gap leads to one proposed content;
- what data, metric, field site, or downstream task will test the gap.

Avoid treating national strategy, public safety, smart-city demand, or map/database construction as a substitute for scientific rationale.

## Validation And Feasibility

Credible validation should make three layers visible:

- controlled validation: simulation, benchmark, ablation, uncertainty analysis, theoretical property, convergence, or complexity;
- geospatial validation: multi-region, multi-sensor, multi-season, field-site, UAV/ground truth, map comparison, or physical/geometric consistency;
- application validation: downstream classification, retrieval, forecasting, monitoring, planning, emergency response, or prototype operation that tests the model rather than merely displays it.

Check whether the draft explains data source, scale, representativeness, preprocessing, registration, annotation quality, permissions, security sensitivity, and continuity. For no-reference or hard-to-observe tasks, look for proxy ground truth, downstream-task metrics, field measurements, or uncertainty bounds.

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

Integration must be cashed out as a mechanism. When a draft's spine is 一体化 / 协同 / 融合, verify the word resolves to a concrete mechanism — a mutual prior between two tasks (e.g. segmentation ↔ reconstruction), a joint/unified mathematical framework or objective, a shared representation/latent space, or explicit inter-model 连接点 — not a bundling slogan. Strong drafts *earn* the integration word (e.g. "geometry-semantics mutual prior", a bidirectional generate↔perceive optimization loop with named stages); a title that claims 一体化 while the contents run in parallel is a flag.

## Figure Conventions

Funded geospatial/RS drafts front-load figures heavily (often 15+). Expect the framework/technical-route figures from `audit-surfaces.md`, plus field-specific ones: a 数据源 → 技术方法 → 研究内容 → 结果 → 效应 multi-lane master figure; a knowledge-graph schema figure (e.g. 形态类型 | 成因类型) for taxonomy/KG drafts; per-technique method flowcharts. Flag a geospatial draft that argues a data/knowledge/model/validation chain in prose with no framework figure.

## Report Add-On

When diagnosing a geospatial or remote-sensing draft, add:

```markdown
### 遥感/GIS/地理空间专项检查
- 空间对象、尺度、数据模态是否明确：
- 数据/几何/物理/拓扑/语义约束是否转成科学问题：
- 研究内容是否形成数据/知识/模型/验证依赖链：
- 标注、配准、真值、评价指标和不确定性是否支撑核心问题：
- 地图/数据库/平台/示范是否用于验证科学主张，而非单纯交付：
- 研究基础是否映射到数据、模型、平台和场景任务：
```
