import base64

import dash
import numpy as np
from dash import html, callback, Output, Input, dcc
import plotly.graph_objs as go

#from pages.patient_details.details_model import load_recordings, load_ecg
from pages.patient_details.details_controller import view_ecg


dash.register_page(__name__, path_template='/details-view/<id>')

#Read the local image file and encode it to Base64
with open("./images/EkgViewPage.png", "rb") as img_file:
    encoded_image = base64.b64encode(img_file.read()).decode('utf-8')

def layout(id=None):
    # Safe id of patient in global variables
    global patient_id
    patient_id = id

    if patient_id is not None:
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
            },
            children=[
                html.H1("Patient Details", className="display-4 text-center mb-4",
                        style={'font-size': '2.5em', 'font-weight': 'bold', 'padding-top': '30px'}),

                html.Button('View ECG', id='view-ecg-button', n_clicks=0, value=patient_id),
                dcc.Location(id='url-view-ecg')

            ])

