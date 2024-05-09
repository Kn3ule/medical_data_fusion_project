import pandas as pd
from models import engine
import sys

# Load locations from database
def load_patients():
    #print(sys.path)
    return pd.read_sql("""SELECT CAST(ecg_id AS INT) as "ID", recording_date as "Date", patient_id as "Patient", age as "Age", sex as "Sex", height as "Height", weight as "Weight" FROM metadata
;""", engine)

def load_patient_numbers():
    return pd.read_sql("""SELECT count(DISTINCT CAST(patient_id AS INT)) FROM metadata
;""", engine)

def load_patient_with_id(id):
    return pd.read_sql(f"""SELECT DISTINCT CAST(patient_id AS INT) as "ID", age as "Age", sex as "Sex", height as "Height", weight as "Weight" FROM metadata where patient_id = {id};""", engine)

if __name__ == '__main__':
    print(load_patients())