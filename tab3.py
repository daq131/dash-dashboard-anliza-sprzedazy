from calendar import day_name

from click import style
from dash import dcc
from dash import html
import dash
import plotly.graph_objects as go
import plotly.express as px

def render_tab(df):

    fig = px.bar(df, x='Store_type', y='total_amt',
                 color='Gender',
                 height=400,
                 barmode='group',
                 labels={'Gender': 'Sales results for gender'})

    layout = html.Div([
                html.H1('Kanały', style={'text-align': 'center'}),
                html.Div([
                    html.Div(
                        [dcc.Graph(id='pie', figure=fig)], style={'width': '50%'}),
                        # html.P("Select store type:"),
                        # dcc.Dropdown(
                        #                 id="ticker1",
                        #                 options=[{'label': Gender, 'value': Gender} for Gender in
                        #                 df['Gender'].unique()],
                        #                 value='M',
                        #                 clearable=False)], style={'width': '50%'}),
                    html.Div([
                        dcc.Graph(id="days"),
                        html.P("Select store type:"),
                        dcc.Dropdown(
                            id="ticker",
                            options=[{'label': Store_type, 'value': Store_type} for Store_type in
                                     df['Store_type'].unique()],
                            value=df['Store_type'][1],
                            clearable=False,
                        ),
                    ],style={'width': '50%'})
                ,],style={'display': 'flex'})
    ])

    ## podstawowy
    # layout = html.Div([
    #     html.H1('Kanały', style={'text-align': 'center'}),
    #     dcc.Graph(id="days"),
    #     html.P("Select store type:"),
    #     dcc.Dropdown(
    #         id="ticker",
    #         options=[{'label': Store_type, 'value': Store_type} for Store_type in df['Store_type'].unique()],
    #         value=df['Store_type'][1],
    #         clearable=False,
    #     ),
    # ])

    return layout