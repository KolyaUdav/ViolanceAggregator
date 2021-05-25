import os
import pandas as pd
import json
import config


column_names = {config.AGE_COLUMN_NAME: 'age',
                config.COLUMN_NAMES[0]: 'Пренебрежение нуждами ребёнка',
                config.COLUMN_NAMES[1]: 'Физическое насилие дома',
                config.COLUMN_NAMES[2]: 'Физическое насилие в школе',
                config.COLUMN_NAMES[3]: 'Психологическое насилие дома',
                config.COLUMN_NAMES[4]: 'Психологическое насилие в школе',
                config.COLUMN_NAMES[5]: 'Сексуальное насилие дома',
                config.COLUMN_NAMES[6]: 'Сексуальное насилие в школе'}


def get_data_from_json():
    json_files = 0

    for _,_,files in os.walk('../json/'):
        json_files = files

    data_arr = []

    for jf in json_files:
        data_dict = {}

        with open('../json/{}'.format(jf), 'r') as data_json:
            data_dict = json.load(data_json)

        data_arr.append(data_dict)

    return data_arr


def create_dataframe(data_arr):
    df = pd.DataFrame(columns=[k for k in column_names.keys()])

    for d in data_arr:
        for value in d.items():
            sv = value[1]['specific']
            cv = value[1]['categories']

            df = df.append({k:sv[v] if k == config.AGE_COLUMN_NAME else len(cv[v]) for (k, v) in column_names.items()}, ignore_index=True)

    return df


def get_dataframe():
    return create_dataframe(get_data_from_json())
