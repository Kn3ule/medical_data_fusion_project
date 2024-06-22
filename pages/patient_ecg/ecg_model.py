import os

import numpy as np
import pandas as pd
import wfdb

from models import engine


# Load recordings from database
def load_recordings(id):
    return pd.read_sql("""SELECT recording_date, filename_lr, filename_hr FROM metadata WHERE ecg_id = %s;""", engine,
                       params=(int(id),))
    #return pd.read_sql("""SELECT recording_date, filename_lr FROM metadata WHERE ecg_id = %s;""", engine, params=(int(id),))

def load_ecg100(filename_lr):

    base_path = 'ptb-xl-a-large-publicly-available-electrocardiography-dataset-1.0.3/'

    #data = [wfdb.rdsamp(base_path + f) for f in [filename_lr]]

    #data = np.squeeze(np.array([signal for signal, meta in data]))
    #return data

    lr_data = [wfdb.rdsamp(base_path + f) for f in [filename_lr]]


    lr_data = np.squeeze(np.array([signal for signal, meta in lr_data]))

    return lr_data


def load_ecg(filename_lr, filename_hr):

    base_path = 'ptb-xl-a-large-publicly-available-electrocardiography-dataset-1.0.3/'

    #data = [wfdb.rdsamp(base_path + f) for f in [filename_lr]]

    #data = np.squeeze(np.array([signal for signal, meta in data]))
    #return data

    lr_data = [wfdb.rdsamp(base_path + f) for f in [filename_lr]]
    hr_data = [wfdb.rdsamp(base_path + f) for f in [filename_hr]]


    lr_data = np.squeeze(np.array([signal for signal, meta in lr_data]))
    hr_data = np.squeeze(np.array([signal for signal, meta in hr_data]))

    return lr_data, hr_data


def load_ecg500(filename_hr):

    base_path = 'ptb-xl-a-large-publicly-available-electrocardiography-dataset-1.0.3/'

    #data = [wfdb.rdsamp(base_path + f) for f in [filename_lr]]

    #data = np.squeeze(np.array([signal for signal, meta in data]))
    #return data


    hr_data = [wfdb.rdsamp(base_path + f) for f in [filename_hr]]


    hr_data = np.squeeze(np.array([signal for signal, meta in hr_data]))

    return hr_data

def load_details_for_ecg(id):
    return pd.read_sql("""SELECT recording_date, device, report FROM metadata WHERE ecg_id = %s;""", engine,
                       params=(int(id),))

def load_scp_information(scp_code):
    return pd.read_sql("""SELECT recording_date, device, report FROM metadata WHERE ecg_id = %s;""", engine,
                       params=(int(id),))