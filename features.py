import numpy as np
import pandas as pd

EPS = 1e-8

def robust_z(s, window=23):
    s = s.astype(float)
    med = s.rolling(window, min_periods=3).median()
    mad = (s-med).abs().rolling(window, min_periods=3).median()
    return ((s-med)/(1.4826*mad+EPS)).replace([np.inf,-np.inf], np.nan).fillna(0.0)

def build_crab_features(df, source_columns, horizons=(3,7,23)):
    x = df[source_columns].astype(float).copy()
    out = pd.DataFrame(index=df.index)

    zcols = []
    for c in source_columns:
        zc = f"{c}__z"
        out[zc] = robust_z(x[c], max(horizons))
        zcols.append(zc)

    # Simple ensemble properties.
    out["source_mean"] = x.mean(axis=1)
    out["source_variance"] = x.var(axis=1).fillna(0.0)
    out["source_range"] = (x.max(axis=1) - x.min(axis=1)).fillna(0.0)

    # Pairwise contradiction relative to each pair's own historical relation.
    contradiction_cols = []
    for i, a in enumerate(source_columns):
        for b in source_columns[i+1:]:
            rel = x[a] - x[b]
            expected = rel.rolling(max(horizons), min_periods=3).median()
            residual = rel - expected
            mad = residual.abs().rolling(max(horizons), min_periods=3).median()
            contradiction = residual.abs() / (1.4826*mad + EPS)
            name = f"contradiction__{a}__{b}"
            out[name] = contradiction.replace([np.inf,-np.inf], np.nan).fillna(0.0)
            contradiction_cols.append(name)

    if contradiction_cols:
        out["contradiction_mean"] = out[contradiction_cols].mean(axis=1)
        out["contradiction_max"] = out[contradiction_cols].max(axis=1)
        out["contradiction_variance"] = out[contradiction_cols].var(axis=1).fillna(0.0)
    else:
        out["contradiction_mean"] = 0.0
        out["contradiction_max"] = 0.0
        out["contradiction_variance"] = 0.0

    out["contradiction_velocity"] = out["contradiction_mean"].diff().fillna(0.0)
    out["contradiction_acceleration"] = out["contradiction_velocity"].diff().fillna(0.0)

    # Consensus instability: the ensemble center may remain stable while internal agreement collapses.
    out["consensus_instability"] = (
        out["source_variance"].rank(pct=True)
        + out["source_range"].rank(pct=True)
        + out["contradiction_mean"].rank(pct=True)
    ) / 3.0

    for h in horizons:
        out[f"contradiction_mean_{h}"] = out["contradiction_mean"].rolling(h, min_periods=1).mean()
        out[f"contradiction_max_{h}"] = out["contradiction_max"].rolling(h, min_periods=1).mean()
        out[f"consensus_instability_{h}"] = out["consensus_instability"].rolling(h, min_periods=1).mean()
        out[f"contradiction_velocity_{h}"] = out["contradiction_velocity"].rolling(h, min_periods=1).mean()

    components = [
        out["contradiction_mean"],
        out["contradiction_max"],
        out["contradiction_variance"],
        out["contradiction_velocity"].clip(lower=0),
        out["contradiction_acceleration"].clip(lower=0),
        out["consensus_instability"],
    ]
    for h in horizons:
        components.extend([
            out[f"contradiction_mean_{h}"],
            out[f"contradiction_max_{h}"],
            out[f"consensus_instability_{h}"],
            out[f"contradiction_velocity_{h}"].clip(lower=0),
        ])

    ranked = pd.concat(components, axis=1).rank(pct=True)
    out["crab_contradiction_score"] = ranked.mean(axis=1).fillna(0.0)

    return out.replace([np.inf,-np.inf], np.nan).fillna(0.0)
