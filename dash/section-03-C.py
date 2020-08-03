import pandas as pd 
import plotly.offline as pyo 
import plotly.graph_objs as go 

df = pd.read_csv('Data/2010YumaAZ.csv')
days = ['TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY','MONDAY']

data = []

# for day in days:
#     cur_day = df[df['DAY']==day]
#     trace = go.Scatter(
#         x=cur_day['LST_TIME'],
#         y=cur_day['T_HR_AVG'],
#         mode='lines',
#         name=day)
    
#     data.append(trace)


data = [
    {
        'x' : df['LST_TIME'],
        'y' : df[df['DAY']==day]['T_HR_AVG'],
        'name' : day
    } for day in df['DAY'].unique()
]

layout = go.Layout(title='Daily Temp')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)