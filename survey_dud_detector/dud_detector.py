import pandas as pd

from collections import Counter


def detect_straightlining(df, adjust=True):
    """Detect straightlining

    :param df pandas.DataFrame.
    :param adjust bool. If True, the function will return the percentage of answers on which a user
        was straightlining. Otherwise, if False, the function returns the number of answers the user
        was straightlining.
    """
    straightlining = df.apply(lambda xs: max(Counter([str(x) for x in xs.values]).values()), axis=1)
    if adjust:
        return straightlining / df.shape[1]
    else:
        return straightlining


def detect_low_incidence(df, low_incidence_threshold=0.04, adjust=True):
    """
    Detect multiple low incidence values.

    :param df pandas.DataFrame.
    :param low_incidence_threshold float. The likelihood at which below defines low incidence.
    :param adjust bool. If True, the function will return the expected number of people to have that likelihood value.
        Otherwise, if False, the function returns the number of low incidence columns.
    """
    counts = None

    for c in df.columns:
        is_low_incidence_ = df[c].fillna('na').value_counts(normalize=True) <= low_incidence_threshold
        count_ = df[c].fillna('na').replace(dict(is_low_incidence_)).astype(int)
        if adjust:
            odds_ = count_.sum() / len(count_)
            count_ = count_.replace({True: odds_, False: 1 - odds_}).astype(float)
        if counts is None:
            counts = count_
        elif adjust:
            counts = pd.Series(counts) * pd.Series(count_)
        else:
            counts = pd.Series(counts) + pd.Series(count_)

    if adjust:
        return pd.Series([c * df.shape[0] for c in counts])
    else:
        return counts.astype(int)

