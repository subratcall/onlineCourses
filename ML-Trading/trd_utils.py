import pandas as pd
import matplotlib.pyplot as plt
import os

def get_max_close(symbol, print_val=True):
    df = pd.read_csv("data/{}.csv".format(symbol))
    max_val =df['Close'].max()
    if print_val:
        print('max val :{}'.format(max_val))
    return max_val

def get_mean_volume(symbol, print_val=True):
    df = pd.read_csv("data/{}.csv".format(symbol)) 
    mean_val =df['Close'].mean()
    if print_val:
        print('mean :{}'.format(mean_val))
    return mean_val 

def symbol_to_path(symbol, base_dir="data"):
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    #if 'SPY' not in symbols:  # add SPY for reference, if absent
    #    symbols.insert(0, 'SPY')
    for symbol in symbols:
        # TODO: Read and join data for each symbol
        df_temp = pd.read_csv(symbol_to_path(symbol),index_col="Date", parse_dates=True,usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df=df.join(df_temp)

    return df.dropna()

def plot_data(df, title="Stock Prices",xlabel="Date", ylabel="Price"):
    'plotting stock prices'
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show()

def plot_selected(df, columns, start_index, end_index):
    """Plot the desired columns over index values in the given range."""
    plot_data(df.ix[start_index:end_index,columns])

def normalize_data(df):  
    return df/df.ix[0,:]

def get_rolling_mean(df, window):
    return df.rolling(window).mean()

def get_rolling_std(df, window):
    return df.rolling(window).std()

def get_bollinger_bands(rm, rstd):
    upper_band = rm + 2*rstd
    lower_band = rm -2*rstd
    return upper_band, lower_band    

def compute_daily_return(df):
    daily_returns = (df/df.shift(1))-1
    daily_returns.ix[0, :] = 0
    return daily_returns

def fill_missing_values(df_data):
    df_data = df_data.fillna(method="ffil")
