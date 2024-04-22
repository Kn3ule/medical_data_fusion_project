import pandas as pd
from models import engine

import sys

# Load locations from database
def load_patients():
    return pd.read_sql("""SELECT * FROM metadata;""", engine)

if __name__ == '__main__':
    print(load_patients())