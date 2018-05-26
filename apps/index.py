import dash
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = html.Div([
    dcc.Link('Navigate to "/"', href='/'),
    html.Br(),
    dcc.Link('Demo Instagram', href='/apps/demo1'),
    html.Br()
])