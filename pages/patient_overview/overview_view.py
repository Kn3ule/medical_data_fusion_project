import base64

import dash
import pandas as pd
from dash import html, callback, Output, Input, dcc
from models import engine
from pages.patient_overview.overview_model import load_patients

from pages.patient_overview.overview_controller import patient_overview

dash.register_page(__name__, path="/")

#Read the local image file and encode it to Base64
with open("./images/PatientOverview.png", "rb") as img_file:
    encoded_image = base64.b64encode(img_file.read()).decode('utf-8')

# Show observations in a table
layout = html.Div(
    style={
        'position': 'fixed',
        'top': '10',
        'left': '0',
        'width': '100%',
        'height': '100vh',
        'z-index': '-1',
        'backgroundPosition': 'center',
        'backgroundSize': 'cover',
        'backgroundImage': f'url("data:image/jpeg;base64,{encoded_image}")',
    },
    children=[
        html.H1("Patient Overview", className="display-4 text-center mb-4",
                style={'font-size': '2.5em', 'font-weight': 'bold', 'padding-top': '30px'}),
        # Search input and button
        html.Div([
            html.Label('Enter Patient ID:'),
            html.Div([
                dcc.Input(id='search-input', type='text', value='', debounce=True),
                html.Button('Search', id='search-button', n_clicks=0),
            ]),
        ]),
        html.Div(id='patients-table',
                 style={'overflow-y': 'scroll', 'max-height': '600px', 'margin': 'auto', 'max-width': '800px'})

    ])