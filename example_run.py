import json
import pandas as pd
from crab import CRABExperiment

df = pd.read_csv("example_data.csv")

exp = CRABExperiment(
    time_column="time",
    target_column="failure",
    source_columns=["source_a","source_b","source_c","source_d"],
    horizons=(3,7,23),
    random_state=23,
)

result = exp.run(df)
print(json.dumps(result, indent=2))
