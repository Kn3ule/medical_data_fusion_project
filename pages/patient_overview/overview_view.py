import base64

import dash
import pandas as pd
from dash import html, callback, Output, Input
from models import engine
from pages.patient_overview.overview_model import load_patients

dash.register_page(__name__, path="/")

# Read the local image file and encode it to Base64
#with open("./images/Woodpecker_Birds_Bokeh.jpg", "rb") as img_file:
#    encoded_image = base64.b64encode(img_file.read()).decode('utf-8')

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
#        'backgroundImage': f'url("data:image/jpeg;base64,{encoded_image}")',
    },
    children=[
        html.H1("Patient Overview", className="display-4 text-center mb-4",
                style={'font-size': '3em', 'font-weight': 'bold', 'padding-top': '30px'}),
        html.Div(id='patients-table',
                 style={'overflow-y': 'scroll', 'max-height': '600px', 'margin': 'auto', 'max-width': '800px'})

    ])

# Callback executed when page is loaded
@callback(Output('patients-table', 'children'),
          [Input('url', 'pathname')])
def update_recent_observations(pathname):
    print("test")
    print(pathname)
    print(load_patients().columns)
    # If the page is the start page, the table is loaded
    if pathname == '/':
        print("if")
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
                                for col in load_patients().columns
                                # Add additional column for details
                            ] + [html.Th("Details", style={'padding': '12px', 'margin': '0', 'text-align': 'center',
                                                           'font-weight': 'bold',
                                                           'background-color': '#343a40', 'color': 'white',
                                                           'position': 'sticky', 'top': '0'})])
                ),
                # Table body
                html.Tbody([
                    html.Tr([
                                html.Td(str(row[col]), style={'padding': '12px', 'text-align': 'center'}) for col in
                                load_patients().columns
                            ] + [
                                # Add link to the edit page of each row
                                html.Td(
                                    html.A(
                                        html.Img(src="/assets/edit-button.png", style={'height': '20px', 'width': '20px'}),
                                        href=f"/details-view/{row['ID']}"),
                                    style={'text-align': 'center', 'padding': '12px'}
                                ),
                            ]) for row in load_patients().to_dict('records')
                ], style={'background-color': 'black'})
            ],
        )