
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from trd_utils import *

def test_run():
    start_date = "2018-07-01"
    end_date = "2019-03-01"
    dates = pd.date_range(start_date,end_date)
    symbols = ["AAPL"]

    df = get_data(symbols, dates)

    daily_returns = compute_daily_return(df)
    daily_returns.hist(bins=50)

    mean = daily_returns["AAPL"].mean()
    std = daily_returns["AAPL"].std()
    kurtosis = daily_returns["AAPL"].kurtosis()

    print("kurtosis :{}".format(kurtosis))

    plt.axvline(mean,color="black",linestyle="dashed",linewidth=2)
    plt.axvline(std,color="red",linestyle="dashed",linewidth=2)
    plt.axvline(-std,color="red",linestyle="dashed",linewidth=2)
    plt.show()

def test_run2():
    start_date = "2018-07-01"
    end_date = "2019-03-01"
    dates = pd.date_range(start_date,end_date)
    symbols = ["AAPL","SPY"]

    df = get_data(symbols, dates)

    daily_returns = compute_daily_return(df)
    daily_returns["SPY"].hist(bins=50,label="SPY")
    daily_returns["AAPL"].hist(bins=50,label="AAPL")

    plt.legend(loc="upper right")
    plt.show()

def scatter_plot():
    start_date = "2018-07-01"
    end_date = "2019-03-01"
    dates = pd.date_range(start_date,end_date)
    symbols = ["AAPL","SPY"]

    df = get_data(symbols, dates)
possible to write a driver as part of your application, in practice most developers us
    daily_returns = compute_daily_return(df)

    daily_returns.plot(kind = "scatter", x="SPY",y="AAPL")

    beta_SPY, alpha_SPY = np.polyfit(daily_returns["SPY"], daily_returns["AAPL"],1)
    plt.plot(daily_returns["SPY"], beta_SPY*daily_returns["SPY"] + alpha_SPY,"-", color="red")
    plt.show()

    print(daily_returns.corr(method="pearson"))

if __name__ == "__main__":
    scatter_plot()