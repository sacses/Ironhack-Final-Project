import pandas as pd

covid = pd.DataFrame({
  'holiday': 'covid',
  'ds': pd.to_datetime(['2020-03-23', '2020-03-16', '2020-03-09',
                        '2020-03-02']),
  'lower_window': 0,
  'upper_window': 0,
})


grid = {'GBP': {'params': {'daily_seasonality': False, 'weekly_seasonality': False,
                           'holidays': None, 'n_changepoints': 25, 'changepoint_range': 0.8,
                           'seasonality_mode': 'multiplicative', 'holidays_prior_scale': 10.0,
                           'changepoint_prior_scale': 0.5},
                'initial': 0.8},

        'AUD': {'params': {'daily_seasonality': False, 'weekly_seasonality': False,
                           'holidays': None, 'n_changepoints': 35,
                           'changepoint_range': 0.7, 'seasonality_mode': 'multiplicative',
                           'holidays_prior_scale': 10, 'seasonality_prior_scale': 40,
                           'changepoint_prior_scale': 40},
                'initial': 0.8},

        'CAD': {'params': {'daily_seasonality': False, 'weekly_seasonality': False,
                           'holidays': None, 'n_changepoints': 34, 'changepoint_range': 0.85,
                           'seasonality_mode': 'multiplicative', 'seasonality_prior_scale': 0.05,
                           'holidays_prior_scale': 10.0, 'changepoint_prior_scale': 0.5},
                'initial': 0.8},

        'EUR': {'params': {'daily_seasonality': False, 'weekly_seasonality': False,
                           'holidays': None, 'n_changepoints': 34, 'changepoint_range': 0.8,
                           'seasonality_mode': 'multiplicative', 'holidays_prior_scale': 10.0,
                           'changepoint_prior_scale': 0.5},
                'initial': 0.8},

        'JPY': {'params': {'daily_seasonality': False, 'weekly_seasonality': False,
                           'holidays': covid, 'n_changepoints': 34, 'changepoint_range': 0.8,
                           'seasonality_mode': 'multiplicative', 'holidays_prior_scale': 10.0,
                           'changepoint_prior_scale': 0.05},
                'initial': 0.71},

        'SGD': {'params': {'daily_seasonality': False, 'weekly_seasonality': False,
                           'holidays': covid, 'n_changepoints': 34, 'changepoint_range': 0.8,
                           'seasonality_mode': 'multiplicative', 'holidays_prior_scale': 10.0,
                           'changepoint_prior_scale': 5},
                'initial': 0.63},

        'HKD': {'params': {'daily_seasonality': False, 'weekly_seasonality': False,
                           'holidays': covid, 'n_changepoints': 25, 'changepoint_range': 0.6,
                           'seasonality_mode': 'multiplicative', 'holidays_prior_scale': 0.1,
                           'changepoint_prior_scale': 20},
                'initial': 0.76},

        'USD': {'params': {'daily_seasonality': False, 'weekly_seasonality': False,
                           'holidays': None, 'n_changepoints': 34, 'changepoint_range': 0.8,
                           'seasonality_mode': 'multiplicative', 'holidays_prior_scale': 10.0,
                           'changepoint_prior_scale': 5},
                'initial': 0.86}}

