from dash import callback, Output, Input

from pages.patient_details.details_model import load_ecg

def register_callbacks():
    @callback(Output('ecg-plot', 'children'),
              [Input('recordings-dropdown', 'value')])
    def update_genus_options(filename_lr):
            values = load_ecg(filename_lr)
            print(values)

            return []

