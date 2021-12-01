# 11. Growth Analysis on MercadoLibre, the most popular e-commerce site
Analyzing MercadoLibre's financial and user traffic data to make the company grow 
by translating predicted search traffic into stock price impact and revenue forecast.
* Step 1: Find unusual patterns in hourly Google search traffic
* Step 2: Mine the search traffic data for seasonality
* Step 3: Relate the search traffic to stock price patterns
* Step 4: Create a time series model with Prophet
* Step 5 (optional): Forecast revenue by using time series models

# Technologies
* Prophet forecast model - user search traffic and revenue prediction
* Panda, hvPlot to Chart data visualization 
* Colaboratory(Colab) notebook with Google Drive - Google Cloud 


# Installation Guide
For this project modeule: we need the following dependencies:
  pip install pystan
  pip install fbprophet
  pip install hvplot
  pip install holoviews
** strongly recommended to use Colab with Google Drive rather than installing and running fbprophet on your local window machine
Colab allows you to write and execute Python in your browser from cloud, with
* Zero configuration required
* Free access to GPUs
* Easy sharing


# Usage
To run this project load the jupyter notebook forecasting_net_prophet.ipynb and run.
Required libaray: 
    import pandas as pd
    import holoviews as hv
    from fbprophet import Prophet
    import hvplot.pandas
    import datetime as dt
    import numpy as np
    import io
    %matplotlib inline
 
# Contributers
Ken Lee
Columbia FinTech BootCamp
# Licence
Open source project, made for educational purposes only
