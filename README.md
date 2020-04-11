# Ironhack-Final-Project

Nowadays most commpanies rely on demand planning forecasts to avoid surplus shorthages, so that they are able to capture all the available demand and transform it into revenue, as well as prevent any impact on their customer base due to infraestructure capacity.

The main motivation of this project lies heavily on the second reason, that is, allocate the appropiate resources at the necessary time periods that will allow the company to operate business as usual.


## Goal

The aim of this project is to train a time series forecasting model to predict the dollar amount that is going to be disbursed in each market over a certain time period.


## Deliverable
The pipeline provides with a **CSV** file in which the prediction (`yhat`),  the actual historic (`y`), as well as its upper and lower bounderies (`yhat_upper` & `yhat_lower`) are reflected. This is then used to feed a **Tableau dashboard** where the user can evaluate the market forecast for a given time period and its reliability meassured by the [MAPE](https://en.wikipedia.org/wiki/Mean_absolute_percentage_error).

## Stack
* The original dataset contains disbursed dollar amounts of a fintech company in each currency over several years.
* The model is trained using the recently publicly released [Prophet library from Facebook](https://facebook.github.io/prophet/docs/quick_start.html).
* Other Python libraries used to model the dataset are `pandas`, `numpy`, `glob` and `matplotlib`.



