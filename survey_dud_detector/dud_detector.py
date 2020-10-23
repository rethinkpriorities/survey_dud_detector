import pandas as pd

from collections import Counter


def detect_straightlining(df):
    return df.apply(lambda xs: max(Counter([str(x) for x in xs.values]).values()), axis=1) / df.shape[1]


def detect_low_incidence(df, low_incidence_threshold=0.04, adjust=False):
    counts = None

    for c in df.columns:
        count_ = df[c].fillna('na').replace(dict((df[c].fillna('na').value_counts(normalize=True) <= low_incidence_threshold).astype(int)))
        if counts is None:
            counts = count_
        else:
            counts += count_

    if adjust:
        counts = pd.Series([low_incidence_threshold ** c * len(df) for c in counts])
        return pd.Series([1 if c >= 1 else c for c in counts]) 
    else:
        return counts.astype(int)

