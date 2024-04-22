import base64

import dash
import numpy as np
import pandas as pd
from dash import html, callback, Output, Input, dcc
import plotly.graph_objs as go

from pages.patient_details.details_model import load_recordings, load_ecg

#from models import engine

dash.register_page(__name__, path_template='/details-view/<id>')

print("load data")

ecg_sample = np.loadtxt('ecg_sample.csv', delimiter=',')

y_axis_names = ['V6', 'V5', 'V4', 'V3', 'V2', 'V1', 'AVF', 'AVL', 'AVR', 'III', 'II', 'I']
x_axis_names = ['', '1', '2', '3', '4', '5',
                '6', '7', '8', '9', '10']

traces = []
for i in range(11, -1, -1):
    trace = go.Scatter(
        x=list(range(len(ecg_sample))),
        y=ecg_sample[:, i] + 12-i,  # Verschiebe jede Linie vertikal, um Überlappungen zu vermeiden
        mode='lines',
        name=f'{y_axis_names[-(i + 1)]}'
    )
    traces.append(trace)

#Read the local image file and encode it to Base64
with open("./images/EkgEditPage.png", "rb") as img_file:
    encoded_image = base64.b64encode(img_file.read()).decode('utf-8')

def layout(id=None):
    # Safe id and data of animal in global variables
    global patient_id
    patient_id = id

    if patient_id is not None:
        # Load animal and genus data from database

        return html.Div(
    style={'position': 'fixed',
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
    dcc.Dropdown(
                                                         id='recordings-dropdown',
                                                         options = [{'label': row['recording_date'], 'value': row['filename_lr']} for index, row in load_recordings(patient_id).iterrows()],

                                                         #value=load_recordings(patient_id),
                                                         placeholder='Select Recording'
                                                     ),
        dcc.Graph(
            id='ecg-plot',
            figure={
                'data': traces,
                'layout': go.Layout(
                    title='ECG Signals',
                    xaxis=dict(
                            title='Time (sec)',
                            tickvals=np.arange(0, 1000, 100),
                            ticktext=x_axis_names
                        ),
                    yaxis=dict(
                            title='ECG',
                            tickvals=np.arange(1,13,1),
                            ticktext=y_axis_names,
                    ),
                    showlegend=True,
                    height=1000
                )
            },
            style={'opacity': 0.9}

        )
    ]
)



@callback(Output('ecg-plot', 'children'),
          [Input('recordings-dropdown', 'value')])
def update_genus_options(filename_lr):
        values = load_ecg(filename_lr)
        print(values)

        return []