import plotly.offline as pyo
import plotly.graph_objs as go 
go
import pandas as pd 

df=pd.read_csv('Data/2018WinterOlympics.csv')

trace1 = go.Bar(
    x=df['NOC'],
    y=df['Gold'],
    name='Gold',
    marker={'color':'#ffd700'}
)

trace2 = go.Bar(
    x=df['NOC'],
    y=df['Silver'],
    name='Silver',
    marker={'color':'#9ea0a1'}
)

trace3 = go.Bar(
    x=df['NOC'],
    y=df['Bronze'],
    name='Bronze',
    marker={'color':'#cd7f32'}
)

data = [trace1, trace2, trace3]

layout = go.Layout(title='Medals', barmode='stack')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)