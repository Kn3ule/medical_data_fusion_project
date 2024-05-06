from dash import callback, Output, Input

from pages.patient_details.details_model import load_ecg
import numpy as np
import plotly.graph_objs as go

def register_callbacks():
    @callback(Output('ecg-plot', 'children'),
              [Input('recordings-dropdown', 'value')])
    def update_genus_options(filename_lr):
            values = load_ecg(filename_lr)
            print(values)

            return []

@callback(Output('ecg-plot', 'figure'),
          [Input('recordings-dropdown', 'value')])
def update_ecg_plot(filename_lr):

    ecg_data = load_ecg(filename_lr)

    y_axis_names = ['V6', 'V5', 'V4', 'V3', 'V2', 'V1', 'AVF', 'AVL', 'AVR', 'III', 'II', 'I']
    x_axis_names = ['', '1', '2', '3', '4', '5',
                    '6', '7', '8', '9', '10']

    traces = []
    for i in range(11, -1, -1):
        trace = go.Scatter(
            x=list(range(len(ecg_data))),
            y=ecg_data[:, i] + 12 - i,  # Verschiebe jede Linie vertikal, um Überlappungen zu vermeiden
            mode='lines',
            name=f'{y_axis_names[-(i + 1)]}'
        )
        traces.append(trace)

    figure={
                'data': traces,
                'layout': go.Layout(
                    title={'text': 'ECG Signals', 'font': {'size': 30}},
                    xaxis=dict(
                            title={'text': 'Time (sec)', 'font': {'size': 17}},
                            tickvals=np.arange(0, 1000, 100),
                            ticktext=x_axis_names
                        ),
                    yaxis=dict(
                            title={'text': 'ECG', 'font': {'size': 17}},
                            tickvals=np.arange(1,13,1),
                            ticktext=y_axis_names,
                    ),
                    showlegend=True,

                )
    }

    return figure