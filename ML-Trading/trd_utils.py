import pandas as pd
import matplotlib.pyplot as plt

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