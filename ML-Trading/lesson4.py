import pandas as pd
import os
from trd_utils import *

def test_run_rolling():
    start_date = "2018-07-01"
    end_date = "2019-03-01"
    dates = pd.date_range(start_date,end_date)
   
    symbols = ["SPY"]
    df = get_data(symbols, dates)
    ax = df["SPY"].plot(title="SPY rolling mean", label="SPY")

    window =30

    rm_SPY = get_rolling_mean(df["SPY"], window = window)
    rstd_SPY = get_rolling_std(df["SPY"], window = window)

    upper_band, lower_band = get_bollinger_bands(rm_SPY, rstd_SPY)
        
    rm_SPY.plot(label="Rolling mean", ax=ax)

    upper_band.plot(label="upper band", ax=ax)
    lower_band.plot(label="lower band", ax=ax)
    

    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc="upper left")
    plt.show()
    #print(df["2018-06-26":"2018-06-27",["AAPL","IBM"]])
    
    #plot_data(df)

    #print(df.std())

def test_run_daily_return():
    start_date = "2018-07-01"
    end_date = "2019-03-01"
    dates = pd.date_range(start_date,end_date)
   
    symbols = ["SPY","AAPL"]
    df = get_data(symbols, dates) 
    plot_data(df)

    daily_returns = compute_daily_return(df)
    plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")

if __name__ == "__main__":
    test_run_daily_return()    