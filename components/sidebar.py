import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app

from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd


# ========= Layout ========= #
layout = dbc.Col([
    html.H1("Finanças", className="tesxt-primary"),
    html.Hr(),

    # Perfil
    dbc.Button(id='botao-avatar',
               children=[html.Img(src='/assets/img_hom.png', id='avatar_change', alt='Avatar', className='perfil_avatar')
                         ], style={'backgroud-color': 'transparent', 'border-color': 'transparent'}),

    # New
    dbc.Row([
        dbc.Col([
            dbc.Button(color='success', id='new-recipe',
                       children=['Receita'])
        ], width=6),
        dbc.Col([
            dbc.Button(color='danger', id='new-expense', children=['Despesa'])
        ], width=6)
    ]),

    # Modal Recipe
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle('Add to Recipe')),
        dbc.ModalBody([

        ])
    ], id='modal-new-recipe'),

    # Modal Expense
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle('Add to Expense')),
        dbc.ModalBody([

        ])
    ], id='modal-new-expense'),

    # Navigation
    html.Hr(),

    dbc.Nav(
        [
            dbc.NavLink("Dashboard", href="/dashboards", active="exact"),
            dbc.NavLink("Extratos", href="/extratos", active="exact"),
        ], vertical=True, pills=True, id='nav_buttons', style={"margin-button": "50px"}
    )


], id='sidebar_completa')


# =========  Callbacks  =========== #
# Pop-up recipe
@app.callback(
    Output('modal-new-recipe', 'is_open'),
    Input('open-new-recipe', 'n_clicks'),
    State('modal-new-recipe', 'is_open')
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open


# Pop-up expense
@app.callback(
    Output('modal-new-expense', 'is_open'),
    Input('open-new-expense', 'n_clicks'),
    State('modal-new-expense', 'is_open')
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
