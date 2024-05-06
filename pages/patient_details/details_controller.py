from dash import callback, Output, Input

#from pages.patient_details import details_view
#from pages.patient_details.details_model import load_ecg
import numpy as np
import plotly.graph_objs as go

@callback(
    Output('url-view-ecg', 'href'),
    #Output('url-view-ecg', 'refresh'),
    [Input('view-ecg-button', 'n_clicks'),
     Input('view-ecg-button', 'value')],
)
def view_ecg(n_clicks, id):
    if n_clicks > 0:
        return f'/ecg-view/{str(id)}'