import dash
import dash_core_components as dcc
import dash_html_components as html
from olympics_package.queries import *

from olympics_package import app
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

import json
from dash.dependencies import Input, Output

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style = {'fontFamily': 'Sans-Serif'}, children=[
    html.H1(
        children = 'Summer Olympics',
        style = {
            'margin': '48px 0',
            'textAlign': 'center',
            'color': colors['text'],
            'fontFamily': 'Sans-Serif'
        }
    ),
    html.Div(children = 'Dash: ', style = {
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id = 'Graph1',
        figure = {
            'data': country_medal_totals(),
            'layout': go.layout(
                xaxis={'title': 'Country'},
                yaxis={'title': 'Medal'})})

                })
            }
        }
    )
])
