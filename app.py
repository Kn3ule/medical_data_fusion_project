import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], use_pages=True, suppress_callback_exceptions=True)


nav = dbc.NavbarSimple(
    [


    ],
    brand="ECG Data",
    brand_href="/",
    color="#333333",
    dark=True,
)

app.layout = html.Div(
    [
        dcc.Location(id='url', refresh=False),
        nav,
        # content of each page
        dash.page_container
    ]
)

if __name__ == "__main__":
    app.run(debug=True)