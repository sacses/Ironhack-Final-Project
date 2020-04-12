import pandas as pd
import numpy as np


def series_end_start(x):
    end_start = [0, 0]
    notnan_index = x.index[x.notna()]
    for i in range(0, len(notnan_index)):
        notnan_upper = i + 1
        notnan_difference = notnan_index[i] - notnan_index[notnan_upper]
        if notnan_difference.days == 7:
            end_start[0] = notnan_index[i]
            nan_index = x.loc[end_start[0]:].index[x.loc[end_start[0]:].isnull()]
            for i in range(0, len(nan_index)):
                upper = i + 2
                difference = nan_index[i] - nan_index[upper]
                if difference.days == 14:
                    end_start[1] = nan_index[i]
                    return end_start


def wrangle(MM):
    dict_series_end_start = {i: series_end_start(MM[i]) for i in MM.columns}
    return dict_series_end_start
