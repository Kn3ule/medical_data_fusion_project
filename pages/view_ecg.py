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

# Create traces for each signal
traces = []
for i in range(ecg_sample.shape[1]):
    trace = go.Scatter(
        x=list(range(len(ecg_sample))),
        y=ecg_sample[:, i],
        mode='lines',
        name=f'Signal {i+1}'
    )
    traces.append(trace)


# Read the local image file and encode it to Base64
#with open("./images/Rivers_Forests_Mountains_American_bison_Grass.jpg", "rb") as img_file:
#    encoded_image = base64.b64encode(img_file.read()).decode('utf-8')

# Show animals in a table
layout = html.Div(
    children=[
        html.H1("ECG Data", className="display-4 text-center mb-4",
                style={'font-size': '3em', 'font-weight': 'bold', 'padding-top': '40px'}),
        dcc.Graph(
            id='ecg-plot',
            figure={
                'data': traces,
                'layout': go.Layout(
                    title='ECG Signals',
                    xaxis={'title': 'Sample'},
                    yaxis={'title': 'Amplitude'},
                    showlegend=True,
                    height=800,
                    width=1000
                )
            }
        )
    ] + [dcc.Graph(
        id=f'ecg-plot-{i}',
        figure={
            'data': [go.Scatter(
                x=list(range(len(ecg_sample))),
                y=ecg_sample[:, i],
                mode='lines',
                name=f'Signal {i + 1}'
            )],
            'layout': go.Layout(
                title=f'Signal {i + 1}',
                xaxis={'title': 'Sample'},
                yaxis={'title': 'Amplitude'},
                showlegend=True,
                height=400,
                width=800
            )
        }
    ) for i in range(ecg_sample.shape[1])]
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