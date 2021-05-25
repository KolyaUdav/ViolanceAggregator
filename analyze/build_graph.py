import sys
import matplotlib
import matplotlib.pyplot as plt
import config


TOTAL_PERCENTS_L1 = 'Имелись эпизоды насилия'
TOTAL_PERCENTS_L2 = 'Эпизоды насилия отсутствуют'

TOTAL_PERCENTS_C1 = 'mediumvioletred'
TOTAL_PERCENTS_C2 = 'dodgerblue'


def create_pie(v1, v2, l1, l2, c1, c2, title):
    pie_data = [v1, v2]
    pie_labels = [l1, l2]
    pie_colors = [c1, c2]

    plt.pie(pie_data, labels=pie_labels, autopct='%1.1f%%', colors=pie_colors)
    plt.title(label=title.replace('_', ' '))
    plt.legend()
    plt.show()
    plt.clf()


def get_total_percents_pie(df, column, title):
    create_pie(v1=df[column][config.TOTAL_PERCENTS_VIOLANCED],
        v2=df[column][config.TOTAL_PERCENTS_NOT_VIOLANCED],
        l1=TOTAL_PERCENTS_L1, l2=TOTAL_PERCENTS_L2,
        c1=TOTAL_PERCENTS_C1, c2=TOTAL_PERCENTS_C2, title=title)


def get_age_total_percents_pie(df, column, age, title):
    create_pie(v1=df[column][config.AGE_TOTAL_PERCENTS_VIOLANCED],
        v2=df[column][config.AGE_TOTAL_PERCENTS_NOT_VIOLANCED],
        l1=TOTAL_PERCENTS_L1, l2=TOTAL_PERCENTS_L2,
        c1=TOTAL_PERCENTS_C1, c2=TOTAL_PERCENTS_C2, title=title)


def get_ratio_violance_intensity_pie(intensity_1, intensity_2, column_1, column_2, title):
    create_pie(v1=intensity_1, v2=intensity_2,
    l1=column_1, l2=column_2, c1=TOTAL_PERCENTS_C1, c2=TOTAL_PERCENTS_C2, title=title)



    #save_pie(total_percents_pie, f_name)
