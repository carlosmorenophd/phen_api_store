import os.path
import pandas as pd


def get_locations(path):
    csv_location = 'location.csv'
    os.rename(os.path.join(path, '51ST IDYN_Loc_data.xls'), os.path.join(path, csv_location))
    file_name = os.path.join(path, csv_location)
    if os.path.isfile(file_name):
        csv_data = pd.read_csv(file_name, delimiter='\t', engine='python', header=None, )
        csv_dictionary = csv_data.to_dict('index')
        head = csv_dictionary.pop(0)
        array_dictionary = []
        for key in csv_dictionary:
            dictio_to_save = {}
            for headKey in head:
                column = convert_head_csv_to_column_location(head_csv=head[headKey], value=csv_dictionary[key][headKey])
                if column['name'] != 'None':
                    dictio_to_save[column['name']] = column['value']
            array_dictionary.append(dictio_to_save)
        print(array_dictionary)
        return array_dictionary
    else:
        raise FileNotFoundError('Filing to save file or not exist it')


def get_genotypes(path):
    csv_location = 'genotypes.csv'
    os.rename(os.path.join(path, '51ST IDYN_Genotypes_Data.xls'), os.path.join(path, csv_location))
    file_name = os.path.join(path, csv_location)
    if os.path.isfile(file_name):
        csv_data = pd.read_csv(file_name, delimiter='\t', engine='python', header=None, encoding='ISO-8859-1')
        csv_dictionary = csv_data.to_dict('index')
        head = csv_dictionary.pop(0)
        array_dictionary = []
        for key in csv_dictionary:
            dictio_to_save = {}
            for headKey in head:
                column = convert_head_csv_to_column_genotypes(head_csv=head[headKey],
                                                              value=csv_dictionary[key][headKey])
                if column['name'] != 'None':
                    dictio_to_save[column['name']] = column['value']
            array_dictionary.append(dictio_to_save)
        print(array_dictionary)
        return array_dictionary
    else:
        raise FileNotFoundError('Filing to save file or not exist it')


def convert_head_csv_to_column_location(head_csv, value):
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


def convert_head_csv_to_column_genotypes(head_csv, value):
    if head_csv == 'Cid':
        return {'name': 'c_id', 'value': int(value)}
    elif head_csv == 'Sid':
        return {'name': 's_id', 'value': int(value)}
    elif head_csv == 'Cross Name':
        return {'name': 'cross_name', 'value': str(value)}
    elif head_csv == 'Selection History':
        return {'name': 'history', 'value': str(value)}
    else:
        return {'name': 'None', 'value': 'None'}
