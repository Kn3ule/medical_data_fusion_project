import numpy as np
import pandas as pd
import wfdb

from models import engine


# Load locations from database
def load_recordings(id):
    return pd.read_sql("""SELECT recording_date, filename_lr FROM metadata WHERE patient_id = %s;""", engine, params=(int(id),))

def load_ecg(filename_lr):

    base_path = 'C:/Users/Delta.MSI/Downloads/ptb-xl-a-large-publicly-available-electrocardiography-dataset-1.0.3/ptb-xl-a-large-publicly-available-electrocardiography-dataset-1.0.3/'

    path = base_path + filename_lr

    print(path)

    for f in filename_lr:
        print(f)

    data = wfdb.rdsamp(path)
    data = np.array([signal for signal, meta in data])

    return data

if __name__ == '__main__':
    print(load_ecg("records100/00000/00001_lr"))