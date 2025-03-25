from calendar import day_name

from click import style
from dash import dcc
from dash import html
import dash
import plotly.graph_objects as go

def render_tab(df):

    # df['day_name'] = df['tran_date'].dt.strftime("%A")

    layout = html.Div([
        html.H1('Kanały', style={'text-align': 'center'}),
        dcc.Graph(id="days"),
        html.P("Select store type:"),
        dcc.Dropdown(
            id="ticker",
            options=[{'label': Store_type, 'value': Store_type} for Store_type in df['Store_type'].unique()],
            value=df['Store_type'][1],
            clearable=False,
        ),
    ])

    return layout