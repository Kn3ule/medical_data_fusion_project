import base64

import dash
import numpy as np
from dash import html, callback, Output, Input, dcc
import plotly.graph_objs as go

#from pages.patient_details.details_model import load_recordings, load_ecg
from pages.patient_details.details_controller import view_ecg
from pages.patient_details.details_model import load_patient_data

dash.register_page(__name__, path_template='/details-view/<id>')

#Read the local image file and encode it to Base64
with open("./images/EkgViewPage.png", "rb") as img_file:
    encoded_image = base64.b64encode(img_file.read()).decode('utf-8')

def layout(id=None):
    # Safe id of patient in global variables
    global patient_id
    patient_id = id

    patient_data = load_patient_data(id)

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

                html.Div(style={'maxWidth': '800px', 'padding': '20px', 'border': '2px solid #ccc',
                                'borderRadius': '10px', 'background-color': 'rgba(255, 255, 255, 0.9)',
                                'margin': 'auto', 'position': 'absolute', 'top': '35%', 'left': '50%',
                                'transform': 'translate(-50%, -50%)'},
                         children=[
                        html.Div(id="alert-output-edit-patient"),
                        html.H1("Edit Patient Details", className="display-4 text-center mb-4",
                                style={'font-size': '3em', 'font-weight': 'bold'}),

                        html.Div(
                            style={'marginBottom': '20px'},
                            children=[
                                html.Strong('Age:', style={'fontWeight': 'bold'}),
                                # Input field for visual features
                                dcc.Input(
                                    value=patient_data['age'][0],
                                    style={'marginLeft': '10px'},
                                    disabled=False,
                                    id='age-edit-input'
                                ),
                            ]
                        ),

                        html.Div(
                            style={'marginBottom': '20px'},
                            children=[
                                html.Strong('Sex:', style={'fontWeight': 'bold'}),
                                # Dropdown for gender
                                dcc.Dropdown(
                                    id='sex-edit-dropdown',
                                    options=[
                                        {'label': 'Male', 'value': '0'},
                                        {'label': 'Female', 'value': '1'},
                                        {'label': 'Diverse', 'value': '-1'},
                                    ],
                                    value=patient_data['sex'][0],
                                    placeholder='Select Sex'
                                ),
                            ]),

                             html.Div(
                                 style={'marginBottom': '20px'},
                                 children=[
                                     html.Strong('Height:', style={'fontWeight': 'bold'}),
                                     # Input field for visual features
                                     dcc.Input(
                                         value=patient_data['height'][0],
                                         style={'marginLeft': '10px'},
                                         disabled=False,
                                         id='height-edit-input'
                                     ),
                                 ]
                             ),

                             html.Div(
                                 style={'marginBottom': '20px'},
                                 children=[
                                     html.Strong('Weight:', style={'fontWeight': 'bold'}),
                                     # Input field for visual features
                                     dcc.Input(
                                         value=patient_data['weight'][0],
                                         style={'marginLeft': '10px'},
                                         disabled=False,
                                         id='weight-edit-input'
                                     ),
                                 ]
                             ),

                             html.Div(
                                 style={'display': 'flex', 'justifyContent': 'space-between', 'margintop': '20px'},
                                 children=[
                                     html.A(
                                         # Cancel button
                                         html.Button('Cancel', id='cancel-button', n_clicks=0,
                                                     className='btn btn-secondary',
                                                     style={'padding': '10px 20px', 'margin': '10px'}),
                                         href='/'
                                     ),
                                     html.A(
                                         # Delete button
                                         html.Button('Delete ECG', id='delete-button-edit-patient', n_clicks=0,
                                                     className='btn btn-secondary', value=patient_id,
                                                     style={'padding': '10px 20px', 'margin': '10px'})),
                                     html.A(
                                         # Save button
                                         html.Button('Save Changes', id='save-button-edit-patient', n_clicks=0,
                                                     className='btn btn-secondary', value=patient_id,
                                                     style={'padding': '10px 20px', 'margin': '10px'})
                                     ),

                                     html.A(
                                         # Save button
                                         html.Button('View ECG', id='view-ecg-button', n_clicks=0,
                                                     className='btn btn-secondary', value=patient_id,
                                                     style={'padding': '10px 20px', 'margin': '10px'})
                                     ),
                                 ]
                             ),
                             dcc.Location(id='url-edit-ecg'),
                         ]
                         )
            ]
        )
    else:
        return html.Div("No patient ID was provided.")



