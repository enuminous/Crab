# CRAB

<!-- ENUMINOUS-NETWORK:START -->
**eNuminous network:** [All repositories](https://enuminous.github.io/EFMW/repositories.html) · [EFMW](https://enuminous.github.io/EFMW/) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [165 triplets](https://enuminous.github.io/FieldSpace/) · [Zoo](https://enuminous.github.io/Tortoise/) · [Lean](https://enuminous.github.io/Aristotle-102-Monolithic-Lean/) · [Engine](https://enuminous.github.io/Archimedes-Engine/) · [Papers](https://enuminous.github.io/medium/papers-essays-index.html) · [Audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/portfolio/INTERLOCK_AUDIT.md)

[Repository](https://github.com/enuminous/Crab) · This repository is linked through its source; GitHub Pages is not enabled.

<details>
<summary>Recent repositories (9)</summary>

- [Oroboros](https://github.com/enuminous/Oroboros) · [README](https://github.com/enuminous/Oroboros/blob/main/README.md) · [Page](https://enuminous.github.io/Oroboros/)
- [P-NP](https://github.com/enuminous/P-NP) · [README](https://github.com/enuminous/P-NP/blob/main/README.md) · [Page](https://enuminous.github.io/P-NP/)
- [Research-Program](https://github.com/enuminous/Research-Program) · [README](https://github.com/enuminous/Research-Program/blob/main/README.md) · [Page](https://enuminous.github.io/Research-Program/)
- [I-Have-Guts](https://github.com/enuminous/I-Have-Guts) · [README](https://github.com/enuminous/I-Have-Guts/blob/main/README.md) · [Page](https://enuminous.github.io/I-Have-Guts/)
- [Wrights-Law](https://github.com/enuminous/Wrights-Law) · [README](https://github.com/enuminous/Wrights-Law/blob/main/README.md) · [Page](https://enuminous.github.io/Wrights-Law/)
- [Aristotle-eNuminous](https://github.com/enuminous/Aristotle-eNuminous) · [README](https://github.com/enuminous/Aristotle-eNuminous/blob/main/README.md) · [Page](https://enuminous.github.io/Aristotle-eNuminous/)
- [Multiverse-Simulator](https://github.com/enuminous/Multiverse-Simulator) · [README](https://github.com/enuminous/Multiverse-Simulator/blob/main/README.md) · [Page](https://enuminous.github.io/Multiverse-Simulator/)
- [accelerando-8192](https://github.com/enuminous/accelerando-8192) · [README](https://github.com/enuminous/accelerando-8192/blob/main/README.md) · [Page source](https://github.com/enuminous/accelerando-8192/blob/main/docs/index.html)
- [Codex-888](https://github.com/enuminous/Codex-888) · [README](https://github.com/enuminous/Codex-888/blob/main/README.md) · [Page](https://enuminous.github.io/Codex-888/)

</details>
<!-- ENUMINOUS-NETWORK:END -->

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
