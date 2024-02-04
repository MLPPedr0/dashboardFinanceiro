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
    html.H1("Finanças", className="text-primary"),
    html.Hr(),

    # Perfil
    dbc.Button(id='botao-avatar',
               children=[html.Img(src='/assets/img_hom.png', id='avatar_change', alt='Avatar', className='perfil_avatar')
                         ], style={'background-color': 'transparent', 'border-color': 'transparent'}),

    # New
    dbc.Row([
        dbc.Col([
            dbc.Button(color='success', id='new-recipe', children=['Recipe'])
        ], width=6),
        dbc.Col([
            dbc.Button(color='danger', id='new-expense', children=['Expense'])
        ], width=6)
    ]),

    # Modal Recipe
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle('Add to Recipe')),
        dbc.ModalBody([
            dbc.Row([
                dbc.Col([
                    dbc.Label('Description: '),
                    dbc.Input(
                        placeholder="Ex. : Salário, Prêmio... ", id="txt-recipe"),
                ], width=6),
                dbc.Col([
                    dbc.Label('Value: '),
                    dbc.Input(placeholder="R$100.00",
                              id="value-recipe", value="")
                ], width=6)
            ]),

            dbc.Row([
                dbc.Col([
                    dbc.Label("Date: "),
                    dcc.DatePickerSingle(id='date-recipes',
                                         min_date_allowed=date(2020, 1, 1),
                                         max_date_allowed=date(2050, 12, 31),
                                         date=datetime.today(),
                                         style={"width": "100%"}
                                         )
                ], width=4),

                dbc.Col([
                    dbc.Label("Extras"),
                    dbc.Checklist(
                        options=[],
                        value=[],
                        id='switches-input-recipe',
                        switch=True
                    )
                ], width=4),

                dbc.Col([
                    html.Label('Recipe Category'),
                    dbc.Select(id='select_recipe', options=[], value=[])
                ], width=4)
            ], style={'margin-top': '25px'}),

            dbc.Row([
                dbc.Accordion([
                    dbc.AccordionItem(children=[
                        dbc.Row([
                            dbc.Col([
                                html.Legend("Add Category", style={
                                            'color': 'green'}),
                                dbc.Input(
                                    type="text", placeholder="New category...", id="input-add-recipe", value=""),
                                html.Br(),
                                dbc.Button("To Add", className="btn btn-success",
                                           id="add-category-recipe", style={"margin-top": "20px"}),
                                html.Br(),
                                html.Div(
                                    id="category-div-add-recipe", style={}),
                            ], width=6),

                            dbc.Col([
                                html.Legend("Remove Category",
                                            style={'color': 'red'}),
                                dbc.Checklist(
                                    id='checklist-selected-style-recipe',
                                    options=[],
                                    value=[],
                                    label_checked_style={'color': 'red'},
                                    input_checked_style={
                                        'backgroundColor': 'blue', 'borderColor': 'orange'},
                                ),
                                dbc.Button(
                                    'Remove', color='warning', id='remove-category-recipe', style={'margin-top': '20px'})
                            ], width=6)
                        ])
                    ], title='Add/Remove Categories')
                ], flush=True, start_collapsed=True, id='accordion-recipe'),

                html.Div(id='id_test_recipe', style={'padding-top': '20px'}),
                dbc.ModalFooter([
                    dbc.Button("Add Recipe", id="save_recipe",
                               color='success'),
                    dbc.Popover(dbc.PopoverBody(
                        "Recipe Saved"), target="save_recipe", placement="left", trigger="click"),
                ])
            ], style={'margin-top': '25px'})
        ])
    ], style={"background-color": "rgba(17, 140, 79, 0.05)"},
        id="modal-new-recipe",
        size="lg",
        is_open=False,
        centered=True,
        backdrop=True),

    # Modal Expense
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle('Add to Expense')),
        dbc.ModalBody([
            dbc.Row([
                dbc.Col([
                    dbc.Label('Description: '),
                    dbc.Input(
                        placeholder="Ex. : Mercado, Diversos, Energia...", id="txt-expense"),
                ], width=6),
                dbc.Col([
                    dbc.Label('Value: '),
                    dbc.Input(placeholder="R$100.00",
                                          id="value-expense", value="")
                ], width=6)
            ]),

            dbc.Row([
                dbc.Col([
                    dbc.Label("Date: "),
                    dcc.DatePickerSingle(id='date-expense',
                                         min_date_allowed=date(2020, 1, 1),
                                         max_date_allowed=date(2050, 12, 31),
                                         date=datetime.today(),
                                         style={"width": "100%"}
                                         )
                ], width=4),

                dbc.Col([
                    dbc.Label("Extras"),
                    dbc.Checklist(
                        options=[],
                        value=[],
                        id='switches-input-expense',
                        switch=True
                    )
                ], width=4),

                dbc.Col([
                    html.Label('Recipe Category'),
                    dbc.Select(id='select_expense', options=[], value=[])
                ], width=4)
            ], style={'margin-top': '25px'}),

            dbc.Row([
                dbc.Accordion([
                    dbc.AccordionItem(children=[
                        dbc.Row([
                            dbc.Col([
                                html.Legend("Add Category", style={
                                            'color': 'green'}),
                                dbc.Input(
                                    type="text", placeholder="New category...", id="input-add-expense", value=""),
                                html.Br(),
                                dbc.Button("To Add", className="btn btn-success",
                                           id="add-category-expense", style={"margin-top": "20px"}),
                                html.Br(),
                                html.Div(
                                    id="category-div-add-expense", style={}),
                            ], width=6),

                            dbc.Col([
                                html.Legend("Remove Category",
                                            style={'color': 'red'}),
                                dbc.Checklist(
                                    id='checklist-selected-style-expense',
                                    options=[],
                                    value=[],
                                    label_checked_style={'color': 'red'},
                                    input_checked_style={
                                        'backgroundColor': 'blue', 'borderColor': 'orange'},
                                ),
                                dbc.Button(
                                    'Remove', color='warning', id='remove-category-expense', style={'margin-top': '20px'})
                            ], width=6)
                        ])
                    ], title='Add/Remove Categories')
                ], flush=True, start_collapsed=True, id='accordion-expense'),

                html.Div(id='id_test_expense', style={'padding-top': '20px'}),
                dbc.ModalFooter([
                    dbc.Button("Add expense", id="save_expense",
                               color='success'),
                    dbc.Popover(dbc.PopoverBody(
                        "Expense Saved"), target="save_expense", placement="left", trigger="click"),
                ])
            ], style={'margin-top': '25px'})
        ])
    ], style={"background-color": "rgba(17, 140, 79, 0.05)"},
        id="modal-new-expense",
        size="lg",
        is_open=False,
        centered=True,
        backdrop=True),


    # Navigation
    html.Hr(),

    dbc.Nav(
        [
            dbc.NavLink("Dashboard", href="/dashboards", active="exact"),
            dbc.NavLink("Extratos", href="/extratos", active="exact"),
        ], vertical=True, pills=True, id='nav_buttons', style={"margin-bottom": "50px"}
    )

], id='sidebar_completa')


# =========  Callbacks  =========== #
# Pop-up recipe
@app.callback(
    Output('modal-new-recipe', 'is_open'),
    Input('new-recipe', 'n_clicks'),
    State('modal-new-recipe', 'is_open')
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open


# Pop-up expense
@app.callback(
    Output('modal-new-expense', 'is_open'),
    Input('new-expense', 'n_clicks'),
    State('modal-new-expense', 'is_open')
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
