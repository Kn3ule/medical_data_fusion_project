import base64

import dash
import numpy as np
from dash import html, callback, Output, Input, dcc
import plotly.graph_objs as go

from pages.patient_details.details_model import load_recordings, load_ecg
from pages.patient_details.details_controller import update_ecg_plot


dash.register_page(__name__, path_template='/details-view/<id>')

#Read the local image file and encode it to Base64
with open("./images/EkgViewPage.png", "rb") as img_file:
    encoded_image = base64.b64encode(img_file.read()).decode('utf-8')

def layout(id=None):
    # Safe id of patient in global variables
    global patient_id
    patient_id = id

    if patient_id is not None:
        options = [{'label': row['recording_date'], 'value': row['filename_lr']} for index, row in load_recordings(patient_id).iterrows()]

        return html.Div(
            style={
                'position': 'fixed',
                'top': '10',
                'left': '0',
                'width': '100%',
                'height': '100vh',
                'z-index': '-1',
                'backgroundPosition': 'center',
                'backgroundSize': 'cover',
                'backgroundImage': f'url("data:image/jpeg;base64,{encoded_image}")'
            },
            children=[
                html.Div(
                    dcc.Dropdown(
                        id='recordings-dropdown',
                        options=options,
                        value=options[0]['value'],
                        placeholder='Select Recording',
                        style={'width': '50%', 'position': 'absolute', 'top': '10px', 'left': '50px',
                               'backgroundColor': 'rgba(240, 240, 240, 0.5)', 'zIndex': '1','maxWidth': '500px'},

                    ),
                    style={'position': 'absolute', 'top': '30px', 'left': '0', 'width': '100%', 'zIndex': '1'}
                ),
                dcc.Graph(id='ecg-plot', style={'width': '100%', 'height': '95vh', 'opacity': 0.9}, responsive=True),
            ]
        )