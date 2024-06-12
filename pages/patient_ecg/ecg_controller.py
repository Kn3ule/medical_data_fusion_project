import matplotlib.pyplot as plt
from dash import callback, Output, Input, html

from pages.patient_ecg.ecg_model import load_ecg100, load_ecg500, load_ecg, load_details_for_ecg
import numpy as np
import plotly.graph_objs as go


import neurokit2


def register_callbacks():
    @callback(Output('ecg-plot', 'children'),
              [Input('recordings-dropdown', 'value')])
    def update_genus_options(filename_lr):
            values = load_ecg(filename_lr)
            print(values)

            return []

def calculate_hr_from_ecg(ecg_signals, sampling_rate):
    hr_list = []
    duration = 10  # Aufnahmezeitraum in Sekunden

    for ecg in ecg_signals:
        # Peaks finden
        _, results = neurokit2.ecg_process(ecg, sampling_rate=sampling_rate)
        peaks = results["ECG_R_Peaks"]  # Abstand mindestens 0.6s für menschliche Herzfrequenz
        num_beats = len(peaks)

        print(results)


        # Herzfrequenz in Hz berechnen
        hr_hz = (num_beats / duration) * 60
        hr_list.append(hr_hz)

    # Durchschnittliche Herzfrequenz berechnen
    average_hr_hz = np.mean(hr_list)

    return average_hr_hz

@callback(Output('ecg-plot', 'figure'),
Output('average-heart-rate', 'children'),
          [Input('recordings-dropdown', 'value')])
def update_ecg_plot(filename):
    # Überprüfe die letzten beiden Buchstaben
    if filename[-2:] == "lr":
        ecg_data=load_ecg100(filename)
        sampling_rate = 100
    else:
        ecg_data=load_ecg500(filename)
        sampling_rate = 500

    ecg_data_transposed = np.array(ecg_data).T


    average_hr = calculate_hr_from_ecg(ecg_data_transposed, sampling_rate)

    average_hr_html = html.P(average_hr)

    print(average_hr)


    y_axis_names = ['V6', 'V5', 'V4', 'V3', 'V2', 'V1', 'AVF', 'AVL', 'AVR', 'III', 'II', 'I']

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
                            title={'text': '', 'font': {'size': 17}},#Time (sec)
                            #tickvals=np.arange(0, 1000, 100),
                            #ticktext=x_axis_names
                        ),
                    yaxis=dict(
                            title={'text': 'ECG', 'font': {'size': 17}},
                            tickvals=np.arange(1,13,1),
                            ticktext=y_axis_names,
                    ),
                    showlegend=True,

                )
    }

    return figure, average_hr_html

'''
@callback(Output('detail-information', 'children'),
          [Input('url', 'href')])
def update_ecg_plot(url):
    print(url)

'''
