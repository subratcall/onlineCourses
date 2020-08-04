import plotly.offline as pyo 
import plotly.graph_objs as go 
import pandas as pd 

df = pd.read_csv('Data/mpg.csv')

data = [go.Scatter(
    x=df['horsepower'], 
    y=df['mpg'], 
    text=df['name'], 
    mode='markers',
    marker=dict(
        size=0.01*df['weight'], 
        color=df['cylinders'],
        showscale=True))]

layout = go.Layout(title='Bubble Chart', hovermode='x')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)