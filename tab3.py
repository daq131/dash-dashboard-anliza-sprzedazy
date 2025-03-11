from dash import dcc
from dash import html
import dash
import plotly as go

def render_tab(df):


    layout = html.Div(children=[
        html.H1('Mój dashboard', style={'margin': 'auto'}),
        html.Div('Tu pojawi się content', style={'color': 'red'}),
        dcc.Graph(id='first-graph')
    ])

    return layout