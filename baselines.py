import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import RobustScaler

class LogisticModel:
    def __init__(self, random_state=23):
        self.scaler = RobustScaler()
        self.model = LogisticRegression(max_iter=4000, random_state=random_state)
        self.constant_ = None

    def fit(self, X, y):
        y = np.asarray(y, dtype=int)
        if len(np.unique(y)) < 2:
            self.constant_ = float(y.mean()) if len(y) else 0.0
            return self
        self.scaler.fit(X)
        self.model.fit(self.scaler.transform(X), y)
        return self

    def predict_proba(self, X):
        if self.constant_ is not None:
            return np.full(len(X), self.constant_)
        return self.model.predict_proba(self.scaler.transform(X))[:,1]

class BaseRateModel:
    def fit(self, X, y):
        self.p_ = float(np.mean(y))
        return self
    def predict_proba(self, X):
        return np.full(len(X), self.p_, dtype=float)

def variance_score(df, source_columns):
    return df[source_columns].astype(float).var(axis=1).fillna(0.0).rank(pct=True).to_numpy()

def mean_anomaly_score(df, source_columns):
    x = df[source_columns].astype(float)
    centered = (x - x.rolling(23, min_periods=3).median()).abs()
    return centered.mean(axis=1).fillna(0.0).rank(pct=True).to_numpy()
