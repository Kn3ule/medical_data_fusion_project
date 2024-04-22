import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], use_pages=True, suppress_callback_exceptions=True)


nav = dbc.NavbarSimple(
    [

        # dropdown for editing entries
        dbc.DropdownMenu(
                    children=[
                        dbc.DropdownMenuItem(page['name'], href=page['path'])
                        for page in dash.page_registry.values() if "View" in page['name'] and "observation" not in page['name']
                    ],
                    nav=True,
                    in_navbar=True,
                    label="Edit Data",
                ),
    ],
    brand="ECG Data",
    brand_href="/",
    color="dark",
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