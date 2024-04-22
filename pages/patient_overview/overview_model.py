import pandas as pd
from models import engine
import sys

# Load locations from database
def load_patients():
    #print(sys.path)
    return pd.read_sql("""SELECT DISTINCT CAST(patient_id AS INT) as "ID", age as "Age", sex as "Sex", height as "Height", weight as "Weight" FROM metadata LIMIT 100
;""", engine)