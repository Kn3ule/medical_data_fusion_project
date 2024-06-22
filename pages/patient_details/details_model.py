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

def validate_input(value, expected_type):
    try:
        return expected_type(value)
    except ValueError:
        raise ValueError(f"Invalid value: {value} for type: {expected_type}")
    

def save_patient_data(id, age, sex, height, weight):

    try:
        # Validating inputs
        id = validate_input(id, int)
        age = validate_input(age, int)
        sex = validate_input(sex, str)  # Assuming sex is a string, adjust as needed
        height = validate_input(height, float)
        weight = validate_input(weight, float)
    except:
        return False

    # Construct the SQL UPDATE statement
    query = text(f"""
        UPDATE metadata
        SET age = :new_age, sex = :new_sex, height = :new_height, weight = :new_weight
        WHERE ecg_id = :id;
    """)

    # Execute the UPDATE statement
    with engine.connect() as connection:
        try:
            connection.execute(query,
                            {"new_age": age, "new_sex": sex, "new_height": height, "new_weight": weight,
                                "id": id})
        except:
            connection.rollback()
            print("Exception")
            return False
        else:
            print("Läuft durch")
            connection.commit()

def delete_patient_data(id):
    query = text(f"""DELETE FROM metadata where ecg_id = {id}
    ;""")

    # Execute the UPDATE statement
    with engine.connect() as connection:
        connection.execute(query)
        connection.commit()
