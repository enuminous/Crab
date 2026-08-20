import pandas as pd
from features import build_crab_features
from crab import CRABExperiment

SOURCES = ["source_a","source_b","source_c","source_d"]

def test_features():
    df = pd.read_csv("example_data.csv")
    cf = build_crab_features(df, SOURCES)
    assert len(cf) == len(df)
    assert "crab_contradiction_score" in cf.columns
    assert cf["crab_contradiction_score"].between(0,1).all()

def test_experiment_runs():
    df = pd.read_csv("example_data.csv")
    exp = CRABExperiment(
        time_column="time",
        target_column="failure",
        source_columns=SOURCES,
    )
    out = exp.run(df)
    assert "results" in out
    assert "crab" in out["results"]
    assert "raw_sources" in out["results"]
