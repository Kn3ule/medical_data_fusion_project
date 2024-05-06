import base64

import dash
import numpy as np
from dash import html, callback, Output, Input, dcc
import plotly.graph_objs as go

from pages.patient_details.details_model import load_recordings, load_ecg
from pages.patient_details.details_controller import update_ecg_plot


dash.register_page(__name__, path_template='/details-view/<id>')

#Read the local image file and encode it to Base64
with open("./images/EkgViewPage.png", "rb") as img_file:
    encoded_image = base64.b64encode(img_file.read()).decode('utf-8')

