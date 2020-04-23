from typing import Tuple

import pandas as pd


def scheduling(df: pd.DataFrame) -> Tuple[int, int]:
    """
    Schedules jobs in decreasing order of the difference (weight - length) and
                   in decreasing order of the ratio (weight/length)
    Parameters
    ----------
    df : pandas DF
        dataframe with job weight and job length
    Returns
    -------
    diff_weight_length
        sum of the of weighted completion times based on difference of weight and length
    ratio_weight_length
        sum of the of weighted completion times based on ratio of weight and length
    """
    df["diff"] = df["weights"] - df["lenghts"]
    df.sort_values(["diff", "weights"], ascending=[False, False], inplace=True)

    df["cum_len_diff"] = df["lenghts"].cumsum()
    df["sum_diff"] = df["weights"] * df["cum_len_diff"]

    df["ratio"] = df["weights"] / df["lenghts"]
    df.sort_values(["ratio", "weights"], ascending=[False, False], inplace=True)

    df["cum_len_ratio"] = df["lenghts"].cumsum()
    df["sum_ratio"] = df["weights"] * df["cum_len_ratio"]

    diff_weight_length = df["sum_diff"].sum()
    ratio_weight_length = df["sum_ratio"].sum()

    return diff_weight_length, ratio_weight_length
