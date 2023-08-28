import os.path
import pandas as pd


def get_locations(path):
    csv_location = 'location.csv'
    os.rename(os.path.join(path, '51ST IDYN_Loc_data.xls'), os.path.join(path, csv_location))
    file_name = os.path.join(path, csv_location)
    if os.path.isfile(file_name):
        print(file_name)
        csv_data = pd.read_csv(file_name, delimiter='\t', engine='python', header=None, )
        csv_dictionary = csv_data.to_dict('index')
        head = csv_dictionary.pop(0)
        array_dictionary = []
        for key in csv_dictionary:
            dictio_to_save = {}
            for headKey in head:
                column = convert_head_csv_to_column(head_csv=head[headKey], value=csv_dictionary[key][headKey])
                if column['name'] != 'None':
                    dictio_to_save[column['name']] = column['value']
            array_dictionary.append(dictio_to_save)
        print(array_dictionary)
        return array_dictionary
    else:
        raise FileNotFoundError('File to save into database do not exist')


def convert_head_csv_to_column(head_csv, value):
    if head_csv == 'Loc_no':
        return {'name': 'location_number', 'value': int(value)}
    elif head_csv == 'Country':
        return {'name': 'country_location', 'value': str(value)}
    elif head_csv == 'Loc. Description':
        return {'name': 'description', 'value': str(value)}
    elif head_csv == 'Institute Name':
        return {'name': 'institute_name', 'value': str(value)}
    elif head_csv == 'Cooperator':
        return {'name': 'cooperator', 'value': str(value)}
    elif head_csv == 'Latitud':
        return {'name': 'latitude', 'value': str(value)}
    elif head_csv == 'Lat_degress':
        return {'name': 'latitude_degrees', 'value': int(value)}
    elif head_csv == 'Lat_minutes':
        return {'name': 'latitude_minutes', 'value': int(value)}
    elif head_csv == 'Longitude':
        return {'name': 'longitude', 'value': str(value)}
    elif head_csv == 'Long_degress':
        return {'name': 'longitude_degrees', 'value': int(value)}
    elif head_csv == 'Long_minutes':
        return {'name': 'longitude_minutes', 'value': int(value)}
    elif head_csv == 'Altitude':
        return {'name': 'altitude', 'value': int(value)}
    else:
        return {'name': 'None', 'value': 'None'}
