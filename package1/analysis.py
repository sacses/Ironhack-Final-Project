import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from fbprophet import Prophet
from fbprophet.diagnostics import cross_validation
from fbprophet.plot import add_changepoints_to_plot


def get_df(x):
    try:
        series = MM.loc[dict_series_end_start[x][0]:dict_series_end_start[x][1], x].iloc[:-1].fillna(0)
        df_output = series.reset_index().rename({'index': 'ds', x: 'y'}, axis=1)

        return df_output
    except:
        return print(f"There isn't enough historic data to predict {x} volumes or {x} is not a valid market.")


def get_test_val(x):
    return round(len(get_df(x)) * grid[x]['initial'])


def fit_model_kwargs(market):
    X = get_df(market)
    if market in ['GBP', 'EUR', 'CAD', 'USD', 'AUD']:
        X.loc[X['ds'] > '2020-03-02', 'y'] = None
    model = Prophet(**grid[market]['params'])
    return model.fit(X)


def create_forecast(market, period, frequency):
    model = fit_model_kwargs(market)

    future = model.make_future_dataframe(periods=period, freq=frequency)
    forecast = model.predict(future)
    forecast[['yhat', 'yhat_lower']] = forecast[['yhat', 'yhat_lower']].clip(0, )

    return forecast


def plot_forecast(market, period, frequency):
    model = fit_model_kwargs(market)

    future = model.make_future_dataframe(periods=period, freq=frequency)
    forecast = model.predict(future)
    forecast[['yhat', 'yhat_lower']] = forecast[['yhat', 'yhat_lower']].clip(0, )

    fig = model.plot_components(forecast)
    fig = model.plot(forecast)
    a = add_changepoints_to_plot(fig.gca(), model, forecast)


def mean_absolute_percentage_error(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return round(np.mean(np.abs((y_true - y_pred) / y_true)) * 100, 1)


def model_error_kwargs(market, cutoff, fcst, units):
    model = fit_model_kwargs(market)

    cv_results = cross_validation(model=model, initial=pd.to_timedelta(get_test_val(market), unit=units),
                                  period=pd.to_timedelta(cutoff, unit=units),
                                  horizon=pd.to_timedelta(fcst, unit=units))
    cv_results[['yhat', 'yhat_lower']] = cv_results[['yhat', 'yhat_lower']].clip(0, )

    mape = mean_absolute_percentage_error(cv_results.y, cv_results.yhat)

    return mape


def model_score(grid):
    scores = {i: model_error_kwargs(i, 4, 13, 'W') for i in grid.keys()}
    return scores



def analysis(mm, timeframe):
    MM = mm
    dict_series_end_start = timeframe


