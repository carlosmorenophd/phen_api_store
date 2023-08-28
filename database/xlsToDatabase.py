import os.path
import pandas as pd


def get_locations(path):
    file_name = rename_file_csv(path=path, source='51ST IDYN_Loc_data.xls', destiny='location.csv')
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
    file_name = rename_file_csv(path=path, source='51ST IDYN_Genotypes_Data.xls', destiny='genotypes.csv')
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


def get_raw(path):
    file_name = rename_file_csv(path=path, source='51ST IDYN_RawData.xls', destiny='raw.csv')
    if os.path.isfile(file_name):
        csv_data = pd.read_csv(file_name, delimiter='\t', engine='python', header=None)
        csv_dictionary = csv_data.to_dict('index')
        head = csv_dictionary.pop(0)
        array_dictionary = []
        set_trails(csv_dictionary, head)
        # for key in csv_dictionary:
        #     dictio_to_save = {}
        #     for headKey in head:
        #         column = convert_head_csv_to_column_genotypes(head_csv=head[headKey],
        #                                                       value=csv_dictionary[key][headKey])
        #         if column['name'] != 'None':
        #             dictio_to_save[column['name']] = column['value']
        #     array_dictionary.append(dictio_to_save)
        # print(array_dictionary)
        return array_dictionary
    else:
        raise FileNotFoundError('Filing to save file or not exist it')


def set_trails(csv_dictionary, head):
    unic_trails = []
    array_dictionary = []
    trail_key = None
    for headKey in head:
        if head[headKey] == 'Trial name':
            trail_key = {'name': 'name', 'key': headKey}
    if trail_key:
        for key in csv_dictionary:
            new_trail = csv_dictionary[key][trail_key['key']]
            if not (new_trail in unic_trails):
                unic_trails.append(new_trail)
                array_dictionary.append({'name': trail_key['name'], 'value': new_trail})
    return array_dictionary


def rename_file_csv(path, source, destiny):
    os.rename(os.path.join(path, source), os.path.join(path, destiny))
    return os.path.join(path, destiny)


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
