# CRAB

<!-- ENUMINOUS-UNIFIED-NAV:START -->
## Repository navigation

**eNuminous network:** [All public repositories](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md) · [EFMW](https://github.com/enuminous/EFMW) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [Frozen Lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Zoo](https://github.com/enuminous/Tortoise) · [Papers](https://github.com/enuminous/papers) · [Quantum geometry](https://github.com/enuminous/Base888-Quantum-Geometry)

**This project:** [Repository home](https://github.com/enuminous/Crab) · [Subject index](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md#zoo-index-and-agents)

<details open>
<summary><strong>On this page</strong></summary>

- [Intended uses](#intended-uses)
- [Core signal path](#core-signal-path)
- [Flat-stack repository](#flat-stack-repository)
- [Scientific hypothesis](#scientific-hypothesis)
- [Baselines](#baselines)
- [Primary endpoint](#primary-endpoint)
- [Installation](#installation)
- [Run](#run)
- [Tests](#tests)
- [Minimal use](#minimal-use)
- [Freeze discipline](#freeze-discipline)
- [Negative results](#negative-results)
- [Status](#status)


</details>

**Related repositories:** [Tortoise](https://github.com/enuminous/Tortoise) · [Monolithic-Zoo-Lean4](https://github.com/enuminous/Monolithic-Zoo-Lean4) · [Monolithic-102-Zoo-Lean4](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Shepherd](https://github.com/enuminous/Shepherd) · [Eagle](https://github.com/enuminous/Eagle) · [Pulse](https://github.com/enuminous/Pulse) · [Hive](https://github.com/enuminous/Hive)

> **Evidence boundary:** A link between projects is navigation, not an assertion of proven equivalence, experimental validation, or shared authorship. See each repository’s own status and review notes.
<!-- ENUMINOUS-UNIFIED-NAV:END -->


**Contradiction Resolution and Anomaly Benchmark**

CRAB is an EFMW-derived framework for systems where the important signal may be disagreement among individually plausible sources.

Its narrow question is:

> Does contradiction across sensors, models, reviewers, forecasts, or subsystems provide predictive information beyond ordinary anomaly magnitude?

## Intended uses

- ensemble model monitoring
- multi-sensor systems
- clinician/reviewer disagreement
- financial forecast disagreement
- AI evaluator disagreement
- redundant control systems
- network observability
- organizational reporting
- multi-agent systems

## Core signal path

```text
source outputs
→ normalize each source
→ pairwise disagreement
→ expected relation
→ contradiction residual
→ persistence / acceleration
→ consensus instability
→ CRAB contradiction score
→ target prediction
```

## Flat-stack repository

```text
README.md
LICENSE
CITATION.cff
pyproject.toml
requirements.txt
crab.py
features.py
baselines.py
metrics.py
freeze.py
contradiction_schema.json
example_config.yaml
example_data.csv
example_run.py
test_crab.py
MANIFEST.sha256
```

## Scientific hypothesis

> In some systems, a failure precursor appears first as increasing inconsistency among sources rather than as a large error in any one source.

CRAB does not assume this is true.

## Baselines

Included:

- mean anomaly magnitude
- source variance
- majority/consensus confidence
- raw logistic model
- base-rate predictor

## Primary endpoint

Compare CRAB against the matched raw-source model on held-out data.

Primary metric:

- Brier score

Secondary metrics:

- log loss
- ROC-AUC
- average precision
- calibration
- contradiction-stratified performance

## Installation

```bash
python -m pip install -r requirements.txt
```

## Run

```bash
python example_run.py
```

## Tests

```bash
pytest -q
```

## Minimal use

```python
import pandas as pd
from crab import CRABExperiment

df = pd.read_csv("example_data.csv")

exp = CRABExperiment(
    time_column="time",
    target_column="failure",
    source_columns=["source_a","source_b","source_c","source_d"],
    horizons=(3,7,23),
)

print(exp.run(df))
```

## Freeze discipline

Freeze before prospective testing:

- source list
- source semantics
- normalization
- expected-relation rule
- contradiction equations
- temporal horizons
- target definition
- cutoff
- baselines
- metrics
- exclusions
- random seeds

Then run:

```bash
python freeze.py
```

## Negative results

If raw-source magnitude or simple variance performs equally well, CRAB has not demonstrated incremental contradiction value.

## Status

Research software. Experimental. Not validated for safety-critical use.
