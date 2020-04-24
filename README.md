# Ironhack-Final-Project

Nowadays most commpanies rely on demand planning forecasts to avoid surplus shorthages, so that they are able to capture all the available demand and transform it into revenue, as well as prevent any impact on their customer base due to infraestructure capacity.

The main motivation of this project lies heavily on the second reason, that is, allocate the appropiate resources at the necessary time periods that will allow the company to operate business as usual.


## Goal

The aim of this project is to train a time series forecasting model to predict the dollar amount that is going to be disbursed in each market over a certain time period. This will help the Operations Analyst to determine the optimum collateral amount in each payout account to deliver the eligible-to-be-advanced payments in 2-3 business days, in a given time period. The collateral figure to be allocated is defined by the below:


## Deliverable
The pipeline provides with a **.csv** file where the prediction (`yhat`),  the actual historic (`y`), as well as its upper and lower bounderies of the 95% confidence interval (`yhat_upper` & `yhat_lower`) are reflected. This is then used to feed a **Tableau dashboard** where the user can evaluate the market forecast for a given time period and its reliability meassured by the [MAPE](https://en.wikipedia.org/wiki/Mean_absolute_percentage_error).


## Model explanation
Interpreting the results of the trained model using Prophet is quite intuitive. The three major components of a timeseries model using Prophet are:
* Trend
* Holidays or special events
* Seasonality

The library provides with built-in methods that provide with simple visualizations of the model components as seen below:

![Model Components](https://github.com/sacses/Ironhack-Final-Project/blob/master/images/forecast_components.png)

Below there is a graph containing the previous model components, the actual historic of the time series and the trend changepoints observed:

![Model Forecast](https://github.com/sacses/Ironhack-Final-Project/blob/master/images/forecast_changepoint.png)


## Stack
* The model is trained using the Python library `fbprophet`.
* Other Python libraries used to model the dataset are `pandas`, `numpy`, `glob`, `argparse`, `pygsheets` and `matplotlib`.
* Tableau is the visualization tool used to show the results of the model.

## Next iteration
* Add [consumer confidence index](https://www.oecd-ilibrary.org/economics/consumer-confidence-index-cci/indicator/english_46434d78-en)
as regression variable to the model.
* Train new model using ARIMA and show Prophet vs. ARIMA forecast results in Tableau visualizations.
* Automate the data extraction directly using a database


## References

Below Facebook Prophet references:
* https://facebook.github.io/prophet/docs/quick_start.html
* https://towardsdatascience.com/predicting-the-future-with-facebook-s-prophet-bdfe11af10ff
* https://xang1234.github.io/prophet/
* https://towardsdatascience.com/implementing-facebook-prophet-efficiently-c241305405a3
* https://medium.com/@christopher.shayan/experimenting-on-facebook-prophet-eb44818278da
* https://medium.com/future-vision/the-math-of-prophet-46864fa9c55a
* https://towardsdatascience.com/forecasting-with-prophet-d50bbfe95f91

Below ARIMA references:
* https://machinelearningmastery.com/power-transform-time-series-forecast-data-python/
* https://www.machinelearningplus.com/time-series/arima-model-time-series-forecasting-python/
* https://machinelearningmastery.com/time-series-data-visualization-with-python/

Below Tableau references:
* https://towardsdatascience.com/python-pandas-dataframe-to-google-sheets-for-tableau-desktop-live-cc1f86982bca
* https://towardsdatascience.com/automated-etl-for-live-tableau-public-visualizations-54f2b8652224
