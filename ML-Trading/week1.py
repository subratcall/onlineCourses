import pandas as pd
from trd_utils import *

def test_run():
    #defining data range
    start_date = '2018-06-25'
    end_date = '2018-06-30'
    dates = pd.date_range(start_date,end_date)

    #creating an empty dataframe
    df1 = pd.DataFrame(index=dates)
    
    #reading spy
    # dfIBM = pd.read_csv("data/IBM.csv", 
    #     index_col="Date", 
    #     parse_dates=True,
    #     usecols=['Date','Adj Close'],
    #     na_values=['nan'])
    #print(dfIBM)
    # joining the tow dataframes
    #df1= df1.join(dfIBM, how = 'inner')
    #df1 = df1.dropna()

    symbols = ['AAPL','IBM','SP5']
    for symbol in symbols:
        df_temp = pd.read_csv("data/{}.csv".format(symbol), index_col="Date", parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df1=df1.join(df_temp)

    print(df1)
test_run()