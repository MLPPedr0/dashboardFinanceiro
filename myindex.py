from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from app import *
from components import sidebar, dashboards, extratos


# =========  Layout  =========== #
content = html.Div(id="page-content")


app.layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col([
            dcc.Location(id='url'),
            sidebar.layout
        ], md=2, style={'background-color': 'grey', 'height': '1080px'}),
        dbc.Col([
            content
        ], md=10, style={'background-color': 'darkgrey', 'height': '1080px'})
    ])

], fluid=True,)


@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def render_page(pathname):
    if pathname == '/' or pathname == '/dashboard':
        return dashboards.layout

    if pathname == '/extratos':
        return extratos.layout


if __name__ == '__main__':
    app.run_server(port=8050, debug=True)
