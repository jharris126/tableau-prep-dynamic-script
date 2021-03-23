import requests
import pandas as pd

#gets data as json from api and returns dataframe, converts all columns to strings (schema only grabs first page)
def get_data(reason):
    url = 'https://swapi.dev/api/people'
    response = requests.get(url).json()
    next_page = response['next']
    data = response['results']

    if reason == 'data':
        while next_page is not None:
            response = requests.get(next_page).json()
            data.extend(response['results'])
            next_page = response['next']

    return pd.DataFrame(data).astype(str)


#converts pandas data types to prep data types (leaves dates as string to convert in prep)
def convert_types(type):
    if type == 'object':
        new_type = prep_string()
    elif type == 'int64':
        new_type = prep_int()
    elif type == 'float64':
        new_type = prep_decimal()
    else:
        new_type = prep_string()

    return new_type


#make get dataframe from api call and return to prep
def get_swapi_data(df):
    return get_data('data')


#get dataframe from api call and return schema to prep
def get_output_schema():
    cols_dict = get_data('schema').dtypes.to_dict()
    cols_dict = {item: convert_types(value) for (item, value) in cols_dict.items()}
    return pd.DataFrame(cols_dict)
