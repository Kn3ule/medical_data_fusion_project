import os

import numpy as np
import pandas as pd
import wfdb

from models import engine

# Load locations from database
def load_patient_data(id):
    return pd.read_sql(f"""SELECT * FROM metadata where patient_id = {id}
;""", engine)
