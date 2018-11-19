import dash
import dash_core_components as dcc
import dash_html_components as html
from queries import *

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
        children = 'Summer Olympics Data From 1980-2016',
        style = {
            'margin': '20px 0',
            'textAlign': 'center',
            'color': colors['text'],
            'fontFamily': 'Sans-Serif'
        }
    ),
        dcc.Tabs(id="tabs", children=[
        dcc.Tab(label='Medal Scores by Event', children=[
            html.H1 (''),
            html.H1 (''),
            html.H3 ('See Scores for the Bronze, Silver and Gold Medals in Selected Events Over The Last 10 Olympics'),
            html.H4 ('Select a Sport and Then an Event:'),
                    html.Div([
                    dcc.Dropdown(
                        id='sport-dropdown',
                        options=[{'label':sport, 'value':sport} for sport in (total_sports)],
                        value='Athletics'
                        )
                        ],style={'width': '20%', 'display': 'inline-block'}),
                    html.Div([
                    dcc.Dropdown(
                        id='event-dropdown',
                        value ='400m men'
                        ),
                        ],style={'width': '20%', 'display': 'inline-block'}
                    ),
                    html.Hr(),
                    html.Div(id='display-selected-values'),

                    dcc.Graph(id='example-graph'),
                ]
            ),
        dcc.Tab(label='Country Medals', children=[
            html.H1("Compare Your Country's Total Medal Count Against the World Average"),
            html.Div([
                dcc.Dropdown(
                    id='country-dropdown',
                    options=[{'label':country, 'value':country} for country in (total_countries)],
                    style={'width': '50%', 'display': 'inline-block'}),
                # dcc.RadioItems(
                #     id='yaxis-type',
                #     options=[{'label': i, 'value': i} for i in ['Mean', 'Median']],
                #     value='Mean',
                #     labelStyle={'display': 'inline-block'}
                # ),
                dcc.Graph(id='countries-graph'),
                dcc.Markdown('*Note: average is referring to the mean. Filtered out countries with zero medal counts*')
                    ])
            # dcc.Graph(id='country-medals')
            ]
            ),
        dcc.Tab(label='Top 10', children=[
                html.H1("Top 10 Medal Getters"),
                html.Div([
                        dcc.Graph(
                        id='top10-graph',
                        figure={
                            'data':[
                            {
                                'x': get_10_countries(),
                                'y': get_10_counts(),
                                'type': 'bar'
                            }
                            ]
                        }
                        )])


        ])])
        ])

@app.callback(
    dash.dependencies.Output('countries-graph', 'figure'),
    [dash.dependencies.Input('country-dropdown', 'value')])

def update_graph_countries(value):
    print(value)
    figure = {
        'data': [
                {
                    'x': ordered_games,
                    'y': get_country_medal_count(value),
                    # 'text': text_gold(value),
                    # 'name': 'Gold Medals',
                    'type':'bar'
                },
                {
                    'x': ordered_games,
                    'y': [17.17511520737327, 6.350230414746544, 15.534562211981568, 8.774193548387096, 1.7649769585253456, 2.8847926267281108, 4.235023041474655, 4.211981566820277, 3.4516129032258065, 4.124423963133641],
                    'type': 'bar'
                }],
        'layout': {
            'title': 'Country Medal Count vs. Average',
            'xaxis' : dict(
                title='Olympic Game',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            )),
            'yaxis' : dict(
                title='Medal Count',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            ))
            }
    }
    return figure



@app.callback(
    dash.dependencies.Output('event-dropdown', 'options'),
    [dash.dependencies.Input('sport-dropdown', 'value')]
)
def update_event_dropdown(value):
    return [{'label': i, 'value': i} for i in sport_events(value)]

# @app.callback(
#     dash.dependencies.Output('example-graph', 'figure'),
#     [dash.dependencies.Input('event-dropdown', 'value')])

@app.callback(
    dash.dependencies.Output('example-graph', 'figure'),
    [dash.dependencies.Input('event-dropdown', 'value')])


def update_graph_src(value):
    figure = {
        'data': [
                {
                    'x': ordered_games,
                    'y': y_gold(value),
                    'text': text_gold(value),
                    'name': 'Gold Medals',
                    'mode': 'markers',
                    'marker':{'size': 12}
                },
                {
                    'x': ordered_games,
                    'y': y_silver(value),
                    'text': text_silver(value),
                    'name': 'Silver Medals',
                    'mode': 'markers',
                    'marker':{'size': 12}
                },
                {
                    'x': ordered_games,
                    'y': y_bronze(value),
                    'text': text_bronze(value),
                    'name': 'Bronze Medals',
                    'mode': 'markers',
                    'marker':{'size': 12}
                }],




        'layout': {
            'title': 'Medal Scores from Past 10 Summer Olympic Games',
            'xaxis' : dict(
                title='Olympic Game',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            )),
            'yaxis' : dict(
                title='Score',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            ))
        }
    }
    return figure
