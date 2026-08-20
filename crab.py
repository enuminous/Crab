from dataclasses import dataclass
import pandas as pd

from features import build_crab_features
from baselines import LogisticModel, BaseRateModel, variance_score, mean_anomaly_score
from metrics import binary_metrics, contradiction_strata

@dataclass
class CRABExperiment:
    time_column: str
    target_column: str
    source_columns: list
    horizons: tuple = (3,7,23)
    train_fraction: float = 0.65
    random_state: int = 23

    def run(self, df):
        df = df.sort_values(self.time_column).reset_index(drop=True).copy()
        cut = max(20, int(len(df)*self.train_fraction))
        y = df[self.target_column].astype(int).to_numpy()

        cf = build_crab_features(df, self.source_columns, self.horizons)
        raw = df[self.source_columns].astype(float).ffill().fillna(0.0)
        crab_X = pd.concat([raw, cf], axis=1).fillna(0.0)

        # Score-only baselines converted into single-feature probabilistic models
        var_df = pd.DataFrame({"variance_score": variance_score(df, self.source_columns)})
        anom_df = pd.DataFrame({"mean_anomaly_score": mean_anomaly_score(df, self.source_columns)})

        models = {
            "crab": (LogisticModel(self.random_state), crab_X),
            "raw_sources": (LogisticModel(self.random_state), raw),
            "variance_only": (LogisticModel(self.random_state), var_df),
            "mean_anomaly": (LogisticModel(self.random_state), anom_df),
            "base_rate": (BaseRateModel(), raw),
        }

        results = {}
        for name, (model, X) in models.items():
            model.fit(X.iloc[:cut], y[:cut])
            p = model.predict_proba(X.iloc[cut:])
            results[name] = {
                "overall": binary_metrics(y[cut:], p),
                "by_contradiction": contradiction_strata(
                    y[cut:], p, cf["contradiction_mean"].to_numpy()[cut:]
                )
            }

        return {
            "n_total": len(df),
            "train_n": cut,
            "test_n": len(df)-cut,
            "results": results,
            "primary_delta_brier_raw_minus_crab": (
                results["raw_sources"]["overall"]["brier"]
                - results["crab"]["overall"]["brier"]
            ),
            "interpretation": (
                "Positive delta favors CRAB over the matched raw-source model. "
                "Check whether any gain is concentrated in high-contradiction cases."
            )
        }
