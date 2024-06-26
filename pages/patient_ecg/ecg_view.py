import base64

import dash
import numpy as np
from dash import html, callback, Output, Input, dcc
import plotly.graph_objs as go

from pages.patient_ecg.ecg_model import load_recordings, load_ecg, load_details_for_ecg
from pages.patient_ecg.ecg_controller import update_ecg_plot


dash.register_page(__name__, path_template='/ecg-view/<id>')

# Read the local image file and encode it to Base64
with open("./images/EkgViewPage.png", "rb") as img_file:
    encoded_image = base64.b64encode(img_file.read()).decode('utf-8')

def layout(id=None):
    global patient_id
    patient_id = id

    if patient_id is not None:
        options = [{'label': '100 Hz', 'value': row['filename_lr']} for index, row in
                   load_recordings(patient_id).iterrows()]
        options += [{'label': '500 Hz', 'value': row['filename_hr']} for index, row in
                    load_recordings(patient_id).iterrows()]
        details = load_details_for_ecg(id)
        details_list = [f"{header}: {value}" for _, row in details.iterrows() for header, value in zip(details.columns, row)]

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
            'backgroundImage': f'url("data:image/jpeg;base64,{encoded_image}")',
            'overflow-y': 'scroll'
        },
        children=[
            html.Div(
                dcc.Dropdown(
                    id='recordings-dropdown',
                    options=options,
                    value=options[0]['value'],
                    placeholder='Select Recording',
                    style={'width': '50%', 'position': 'absolute', 'top': '10px', 'left': '50px',
                           'backgroundColor': 'rgba(240, 240, 240, 0.5)', 'zIndex': '1', 'maxWidth': '500px'}
                ),
                style={'position': 'absolute', 'top': '10px', 'left': '0', 'width': '50%', 'zIndex': '1'}
            ),
            dcc.Graph(id='ecg-plot', style={'width': '100%', 'height': '95vh', 'opacity': 0.9}, responsive=True),
            html.Div(
                children=[
                    html.Span("Average Heart Rate: ",
                              style={'fontWeight': 'bold', 'marginLeft': '15px', 'display': 'inline-block'}),
                    html.Span(id='average-heart-rate', style={'marginLeft': '5px', 'display': 'inline-block'}),
                    html.Span("bpm", style={'marginLeft': '5px', 'display': 'inline-block'})
                ],
                style={'position': 'absolute', 'fontWeight': 'bold', 'top': '35px', 'left': '50%',
                       'transform': 'translateX(-50%)', 'width': '50%', 'zIndex': '1'}
            ),
            html.Div(
                children=[
                    html.Div([
                        html.P([html.Strong(f'{header}: '), value],
                               style={'color': 'black', 'display': 'block', 'margin-bottom': '5px'})
                        for header, value in zip(details.columns, row)
                    ], style={'background-color': 'rgba(240, 240, 240, 0.5)'})
                    for _, row in details.iterrows()
                ],
                style={'position': 'absolute', 'top': '10px', 'right': '150px',
                       'backgroundColor': 'rgba(270, 270, 270, 0.0)', 'zIndex': '2', 'padding': '0px',
                       'width': '400px', 'max-height': '12vh', 'overflow-y': 'auto'}
            )
        ]
    )


