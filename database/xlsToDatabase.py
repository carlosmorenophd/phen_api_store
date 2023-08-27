import os.path
import pandas as pd


def save_all_files(path):
    # Save file location
    save_file_xls(os.path.join(path, '51ST IDYN_Loc_data.xls'))


def save_file_xls(file_name):
    if os.path.isfile(file_name):
        print(file_name)
        df_sheet_index = pd.read_csv(file_name)
        print(df_sheet_index)
    else:
        raise FileNotFoundError('File to save into database do not exist')
