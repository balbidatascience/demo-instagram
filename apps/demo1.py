from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go

import InstragramAPI


# Get data
df = InstragramAPI.getRecentMedia()
df = df[['countLikes', 'photoId']].groupby(['photoId']).sum().sort_values(by='countLikes', ascending=True)

data = {'x': df['countLikes'], 'y': df.index, 'type': 'bar', 'orientation': 'h', 'name': 'SF'}

layout = {
    'margin': {'l': '220',
               'pad': '2'},
    'title': 'Ranking de Post'
}

fig = dict(data=[data], layout=layout)

appPage = html.Div(
    [
        html.Div(className='col-8',
                 children=[
                     dcc.Graph(id='demo1insta-graph',
                               animate=True,
                               style={'margin-top': '20'},
                               figure=fig)
                 ]
                 )])
