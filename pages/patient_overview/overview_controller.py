import dash
import pandas as pd
from dash import html, callback, Output, Input, State, dash_table
import dash_ag_grid as dag
from pages.patient_overview.overview_model import load_patients, load_patient_numbers, load_patient_with_id

'''
# Callback executed when page is loaded
@callback(Output('patients-table', 'children'),
          [Input('url', 'pathname')])
def patient_overview(pathname):
    # If the page is the start page, the table is loaded
    if pathname == '/':
        df = load_patients()

        return dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns])
    
'''
# Callback executed when page is loaded
@callback(Output('patients-table', 'children'),
          [Input('url', 'pathname')])
def patient_overview(pathname):
    # If the page is the start page, the table is loaded
    if pathname == '/':
        df = load_patients()

        return dag.AgGrid(
            rowData=df.to_dict("records"),
            columnDefs=[
                {"field": "ID", "filter": "agNumberColumnFilter", "cellRenderer": "Details"},
                {"field": "Date", "filter": "agNumberColumnFilter"},
                {"field": "Patient", "filter": "agNumberColumnFilter"},
                {"field": "Age", "filter": "agNumberColumnFilter"},
                {"field": "Sex", "filter": "agNumberColumnFilter"},
                {"field": "Height", "filter": "agNumberColumnFilter"},
                {"field": "Weight", "filter": "agNumberColumnFilter"}
                ],
            dashGridOptions={"pagination": True, "paginationAutoPage": True},
            columnSize="sizeToFit"
        )
    
'''
# Callback executed when page is loaded
@callback(Output('patients-table', 'children'),
          [Input('url', 'pathname')])
def patient_overview(pathname):
    # If the page is the start page, the table is loaded
    if pathname == '/':
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
                            ] + [html.Th("ECG", style={'padding': '12px', 'margin': '0', 'text-align': 'center',
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
                                        html.Img(src="/assets/lupe.png", style={'height': '25px', 'width': '25px'}),
                                        href=f"/details-view/{row['ID']}"),
                                    style={'text-align': 'center', 'padding': '12px'}
                                ),
                            ]) for row in load_patients().to_dict('records')
                ], style={'background-color': 'black'})
            ],
        )
        '''