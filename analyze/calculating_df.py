import pandas as pd
import config


def create_total_percents_df(df):
    total_percents_dict = {}

    df = df.drop([config.AGE_COLUMN_NAME], axis=1)

    for c in df.columns.values.tolist():
        total_percents_dict[c] = round((len(df[df[c] > 0]) / len(df[c])) * 100)

    df_total_percents = pd.DataFrame(total_percents_dict, index=[config.TOTAL_PERCENTS_VIOLANCED])

    for c in df_total_percents.columns.values.tolist():
        total_percents_dict[c] = round(((len(df[c]) - len(df[df[c] > 0])) / len(df[c]) * 100))

    df_total_percents = df_total_percents.append(pd.DataFrame(total_percents_dict,
        index=[config.TOTAL_PERCENTS_NOT_VIOLANCED]))

    return df_total_percents


def create_age_total_percents_df(df, age):
    age_arr = [str(age) for age in range(config.MIN_AGE, (config.MAX_AGE + 1))]

    if age not in age_arr:
        return 'Неверный возраст'

    age_total_percents_dict = {}

    for c in df.columns.values.tolist():
        if c != config.AGE_COLUMN_NAME:
            age_total_percents_dict[c] = {}
            for a in age_arr:
                age_total_percents_dict[c][a] = round(
                (len(df[(df[c] > 0) & \
                (df[config.AGE_COLUMN_NAME] == age)]) / \
                len(df[df[config.AGE_COLUMN_NAME] == age])) * 100)

    df_age_total_percents = pd.DataFrame(age_total_percents_dict)
    df_age = pd.DataFrame([df_age_total_percents.loc[age]]).rename({age: config.AGE_TOTAL_PERCENTS_VIOLANCED})

    age_free_violance_dict = {}

    for c in df_age_total_percents.columns.values.tolist():
        age_free_violance_dict[c] = 100 - df_age.loc[config.AGE_TOTAL_PERCENTS_VIOLANCED][c]

    df_age = df_age.append(pd.DataFrame(age_free_violance_dict, index=[config.AGE_TOTAL_PERCENTS_NOT_VIOLANCED]))

    return df_age


def get_ratio_age_to_total(df, column, age):
    total_mean = df[df[column] > 0][column].mean()
    age_mean = df[(df[column] > 0) & (df[config.AGE_COLUMN_NAME] == age)][column].mean()

    ratio_index_dict = {'total': total_mean, 'age': age_mean}

    return ratio_index_dict


def get_violance_intensity(df, column):
    if column not in df.columns.values.tolist():
        return 'Указанное имя столбца отсутствует.'

    sum = df[column].sum()

    return sum


def get_ratio_violance_intensity(df, column_1, column_2):
    return get_violance_intensity(df, column_1) / get_violance_intensity(df, column_2)
