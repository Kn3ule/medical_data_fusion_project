import os

import numpy as np
import pandas as pd
import wfdb
from sqlalchemy import text

from models import engine

# Load locations from database
def load_patient_data(id):
    return pd.read_sql(f"""SELECT * FROM metadata where ecg_id = {id}
;""", engine)

def save_patient_data(id, age, sex, height, weight):
    # Construct the SQL UPDATE statement
    query = text(f"""
        UPDATE metadata
        SET age = :new_age, sex = :new_sex, height = :new_height, weight = :new_weight
        WHERE ecg_id = :id;
    """)

    # Execute the UPDATE statement
    with engine.connect() as connection:
        connection.execute(query,
                           {"new_age": age, "new_sex": sex, "new_height": height, "new_weight": weight,
                            "id": id})
        connection.commit()
