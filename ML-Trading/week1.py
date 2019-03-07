import pandas as pd
from trd_utils import *

def test_run():
    #defining data range
    start_date = '2018-07-01'
    end_date = '2019-03-01'
    dates = pd.date_range(start_date,end_date)
   
    symbols = ['AAPL','IBM','SPY']

    df = normalize_data(get_data(symbols, dates))
    #print(df['2018-06-26':'2018-06-27',['AAPL','IBM']])
    plot_selected(df, ['SPY','IBM'],'2018-08-01','2019-02-01')
test_run()