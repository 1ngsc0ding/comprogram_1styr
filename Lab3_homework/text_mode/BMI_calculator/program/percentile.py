from pathlib import Path

import pandas as pd
from scipy.stats import norm


def load_cdc_chart(gender):
    if gender.lower() == "male":
        pass
    elif gender.lower() == "female":
        pass
    else:
        raise ValueError("Gender must be male or female")

    data_dir = Path(__file__).resolve().parent.parent / "data"
    df1 = pd.read_csv(data_dir / "wtage.csv")
    df2 = pd.read_csv(data_dir / "statage.csv")
    df3 = pd.read_csv(data_dir / "bmiagerev.csv")

    for df in (df1, df2, df3):
        for column in ["Agemos", "L", "M", "S"]:
            if column in df.columns:
                df[column] = pd.to_numeric(df[column], errors="coerce")

    df = pd.concat([df1, df2, df3], ignore_index=True)
    return df

def calculate_z_score(bmi, L, M, S):

    if L == 0:
        z = ((bmi / M) - 1) / S
    else:
        z = (((bmi / M) ** L) - 1) / (L * S)
    return z

def calculate_percentile(gender, age_month, bmi):
    chart = load_cdc_chart(gender)

    # Find closest age in CDC table
    closest = chart.iloc[(chart["Agemos"] - age_month).abs().argsort()[:1]]

    L = closest["L"].values[0]
    M = closest["M"].values[0]
    S = closest["S"].values[0]

    z_score = calculate_z_score(bmi, L, M, S)
    percentile = norm.cdf(z_score)* 100

    return round(percentile, 2)