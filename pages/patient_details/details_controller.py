from dash import callback, Output, Input, State

#from pages.patient_details import details_view
#from pages.patient_details.details_model import load_ecg
import numpy as np
import plotly.graph_objs as go

from pages.patient_details.details_model import save_patient_data


@callback(
    Output('url-edit-ecg', 'href',
           allow_duplicate=True),
    #Output('url-view-ecg', 'refresh'),
    [Input('view-ecg-button', 'n_clicks'),
     Input('view-ecg-button', 'value')],
prevent_initial_call=True
)
def view_ecg(n_clicks, id):
    if n_clicks > 0:
        return f'/ecg-view/{str(id)}'


# Callback executed when cancel button is clicked
@callback(
    Output('alert-output-edit-patient', 'children'),
    Output('url-edit-ecg', 'href'),
    Output('url-edit-ecg', 'refresh'),
    [Input('save-button-edit-patient', 'n_clicks'),
     Input('save-button-edit-patient', 'value')],
    [State('age-edit-input', 'value'),
     State('sex-edit-dropdown', 'value'),
     State('height-edit-input', 'value'),
     State('weight-edit-input', 'value')],
    prevent_initial_call=True
)
def save_changes(n_clicks, id, age, sex, height, weight):
    if n_clicks is not None:


        save_patient_data(id, age, sex, height, weight)


        return '', '/', True

    return '', '', False