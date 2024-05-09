import os

import numpy as np
import pandas as pd
import wfdb

from models import engine


# Load recordings from database
def load_recordings(id):
    return pd.read_sql("""SELECT recording_date, filename_lr FROM metadata WHERE ecg_id = %s;""", engine, params=(int(id),))

def load_ecg(filename_lr):

    base_path = 'C:/Users/Delta.MSI/Downloads/ptb-xl-a-large-publicly-available-electrocardiography-dataset-1.0.3/ptb-xl-a-large-publicly-available-electrocardiography-dataset-1.0.3/'

    data = [wfdb.rdsamp(base_path + f) for f in [filename_lr]]

    data = np.squeeze(np.array([signal for signal, meta in data]))
    return data