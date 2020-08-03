import plotly.offline as pyo 
import plotly.graph_objs as go 
import pandas as pd 

df = pd.read_csv('Data/mpg.csv')

data = [go.Scatter(
    x=df['horsepower'], 
    y=df['mpg'], 
    text=df['name'], 
    mode='marker',
    marker=dict(size=2*df['cylinders']))]