import os

import json_to_df
import build_graph
import calculating_df


def get_total_percents_analyze(column_name_1):
    df = calculating_df.create_total_percents_df(json_to_df.get_dataframe())
    build_graph.get_total_percents_pie(df, column_name_1,
        'Общий процент по шкале {}'.format(column_name_1))


def get_ratio_violance_intensity_analyze(column_name_1, column_name_2):
    df = json_to_df.get_dataframe()
    build_graph.get_ratio_violance_intensity_pie(
        calculating_df.get_violance_intensity(df, column_name_1),
        calculating_df.get_violance_intensity(df, column_name_2),
        column_name_1, column_name_2,
        'Отношение интенсивности насилия между {} и {}'.format(column_name_1,
        column_name_2))


def get_age_total_percents_analyze(column_name_1, age_str):
    age_total_df = calculating_df.create_age_total_percents_df(
        json_to_df.get_dataframe(), age_str)
    build_graph.get_age_total_percents_pie(age_total_df,
        column_name_1, age_str,
        'Общий процент по возрасту {} лет и по шкале {}'.format(age_str,
        column_name_1))


def get_ratio_age_to_total_text(column_name_1, age_str):
    rat_dict = calculating_df.get_ratio_age_to_total(json_to_df.get_dataframe(),
        column_name_1, age_str)
    return rat_dict


def get_ratio_age_to_total_pies(column_name_1, age_str):
    age_total_df = calculating_df.create_age_total_percents_df(
        json_to_df.get_dataframe(), age_str)
    total_df = df = calculating_df.create_total_percents_df(json_to_df.get_dataframe())
    age_total_pie = build_graph.get_age_total_percents_pie(age_total_df,
        column_name_1, age_str, '')
    total_pie = build_graph.get_total_percents_pie(df, column_name_1, '')
