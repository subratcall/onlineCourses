import plotly.offline as pyo 
import plotly.graph_objs as go 
import pandas as pd 

df = pd.read_csv('Data/mpg.csv', index_col=0)
print(df.head())
data = [go.Scatter(
    x = df['horsepower']
)]