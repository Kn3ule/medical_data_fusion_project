import base64

import dash
import numpy as np
import pandas as pd
from dash import html, callback, Output, Input, dcc
import plotly.graph_objs as go

#from models import engine

dash.register_page(__name__)

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

# Show animals in a table
layout = html.Div(
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

# Callback executed when page is loaded
@callback(Output('all-animals-table', 'children'),
          [Input('url', 'pathname')])
def update_recent_observations(pathname):
    # If the page is view-animals, the table is loaded
    if pathname == '/view-animals':
        return html.Table(
            className="table",
            style={'opacity': '0.9'},
            children=[
                # Table header
                html.Thead(
                    html.Tr([
                                html.Th(col, style={'padding': '12px', 'text-align': 'center', 'font-weight': 'bold',
                                                    'background-color': '#343a40', 'color': 'white',
                                                    'position': 'sticky', 'top': '0'})
                                for col in load_animals().columns
                                # Add additional column for the details
                            ] + [html.Th("Details", style={'padding': '12px', 'margin': '0', 'text-align': 'center',
                                                           'font-weight': 'bold', 'background-color': '#343a40',
                                                           'color': 'white', 'position': 'sticky', 'top': '0', })])
                ),
                # Table body
                html.Tbody([
                    html.Tr([
                                html.Td(str(row[col]), style={'padding': '12px', 'text-align': 'center'}) for col in
                                load_animals().columns
                            ] + [
                                html.Td(
                                    html.A(
                                        html.Img(src="/assets/edit-button.png", style={'height': '20px', 'width': '20px'}),
                                        href=f"/edit-animal/{row['ID']}"),
                                    style={'text-align': 'center', 'padding': '12px'}
                                ),
                            ]) for row in load_animals().to_dict('records')
                ], style={'background-color': 'white'})
            ],
        )