import pandas as pd
import glob


def acquire():
    data = [i for i in glob.glob('../data/raw/data2*.csv')]

    MM = pd.read_csv(data[0], skiprows=[1, 483], header=0,
                     na_values=0, parse_dates=['Payouts Payout Currency'],
                     index_col='Payouts Payout Currency').rename_axis(None)
    return MM
