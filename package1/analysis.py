import numpy as np
import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt
from fbprophet import Prophet
from fbprophet.diagnostics import cross_validation
from fbprophet.plot import add_changepoints_to_plot


def get_df(market, mm, timeframe):
    try:
        series = mm.loc[timeframe[market][0]:timeframe[market][1],
                 market].iloc[:-1].fillna(0)
        df_output = series.reset_index().rename({'index': 'ds', market: 'y'},
                                                axis=1)

        return df_output
    except:
        return print(f"There isn't enough historic data to predict {market} volumes or {market} is not a valid market.")


def get_test_val(market, grid, mm, timeframe):
    return round(len(get_df(market,
                            mm,
                            timeframe)) * grid[market]['initial'])


def get_test_val_2(market, mm, timeframe, units):
    if units == 'D':
        return len(get_df(market, mm, timeframe)) - 360
    elif units == 'W':
        return len(get_df(market, mm, timeframe)) - 53
    elif units == 'M':
        return len(get_df(market, mm, timeframe)) - 12


def fit_model_kwargs(market, grid, mm, timeframe):
    X = get_df(market, mm, timeframe)
    if market in ['GBP', 'EUR', 'CAD', 'USD', 'AUD']:
        X.loc[X['ds'] > '2020-03-02', 'y'] = None
    print(f"-----------------Training {market} model------------------")
    model = Prophet(**grid[market]['params'])
    return model.fit(X)


def create_forecast_df(market, period, frequency, grid, mm, timeframe):
    model = fit_model_kwargs(market, grid, mm, timeframe)

    future = model.make_future_dataframe(periods=period, freq=frequency)
    forecast = model.predict(future)
    forecast = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
    forecast[['yhat', 'yhat_lower']] = forecast[['yhat', 'yhat_lower']].clip(0, )
    forecast_df = pd.merge(forecast, get_df(market, mm, timeframe),
                           how='left', on='ds')

    return forecast_df


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


def model_error_kwargs(market, cutoff, fcst, units, grid, mm, timeframe):
    model = fit_model_kwargs(market, grid, mm, timeframe)
    print(f"-----------------Cross validating {market} model------------------")
    cv_results = cross_validation(model=model,
                                  initial=pd.to_timedelta(get_test_val_2(market,
                                                                       mm,
                                                                       timeframe,
                                                                       units),
                                                          unit=units),
                                  period=pd.to_timedelta(cutoff, unit=units),
                                  horizon=pd.to_timedelta(fcst, unit=units))
    cv_results[['yhat', 'yhat_lower']] = cv_results[['yhat', 'yhat_lower']].clip(0, )

    mape = mean_absolute_percentage_error(cv_results.y, cv_results.yhat)

    return mape


def model_score(grid, mm, timeframe, args):
    freq = args.units
    x_cutoff = args.x_cutoff
    x_fcst = args.x_forecast
    scores = {i: model_error_kwargs(i, x_cutoff, x_fcst, freq, grid, mm, timeframe)
              for i in grid.keys()}
    return scores


def get_threshold(x):
    value = x
    print(f"-----------------Threshold {value} set------------------")
    return float(value)


def export_df(test_passed_scores, grid, mm, timeframe, args):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_df = pd.DataFrame()
    for i in test_passed_scores:
        market_df = create_forecast_df(i,
                                       period=args.horizon,
                                       frequency=args.units,
                                       grid=grid,
                                       mm=mm,
                                       timeframe=timeframe).assign(market=i,
                                                                   mape=test_passed_scores[i])
        output_df = output_df.append(market_df)

    output_df.to_csv(f'data/processed/output{timestamp}.csv', index=False)
    print(f"-----------------Output Dataset exported at {timestamp}------------------")
    return output_df


def analysis(mm, timeframe, grid, args):
    dict_scores = model_score(grid, mm, timeframe, args)
    markets_passed_threshold = {i: dict_scores[i] for i in dict_scores if dict_scores[i] < args.threshold}
    return export_df(markets_passed_threshold, grid, mm, timeframe, args)
