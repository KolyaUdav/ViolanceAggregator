import data_analyze
import config


WRONG_COLUMN_NUM = '!!!Введён неверный номер столбца. Введите верный номер!!!'
CHOOSED = 'Вы выбрали {}'
WRONG_MULTI_COLUMN_NUM = '!!!Введён неверный номер {} столбца. Введите верный номер!!!'
INPUT_COLUMN_NUM = 'Введите номер столбца: '
INPUT_MULTI_COLUMN_NUM = 'Введите номер {} столбца: '
INPUT_AGE = 'Введите возраст: '
WRONG_AGE = '!!!Введён неверный возраст!!!'

options = {
    '1': 'Общий процент',
    '2': 'Общий процент по возрасту',
    '3': 'Отношение интенсивности одной шкалы насилия к другой',
    }


def run():
    print('----- Введите номер опции, которую хотите выбрать -----')
    for key, value in options.items():
        print(key + ' - ' + value)

    input_option_num()


def choose_option(option_num):
    print(CHOOSED.format(options[option_num]))

    print('----- Доступные столбцы -----')

    for column in config.COLUMN_NAMES:
        print(str(config.COLUMN_NAMES.index(column) + 1) + ' - ' + column)

    print('Доступный возраст от ' + str(config.MIN_AGE) + ' до ' + str(config.MAX_AGE) + ' лет.')

    if option_num == '1':
        input_total_percents()
    elif option_num == '2':
        input_age_total_percents()
    elif option_num == '3':
        input_ratio_violance_percents()


def input_option_num():
    option_num = input()

    if check_correct_option(option_num):
        choose_option(option_num)
    else:
        print('!!!Введён неверный номер опции. Введите верный номер!!! ')
        input_option_num()


def input_total_percents():
    column_num = input(INPUT_COLUMN_NUM)

    column_num = normalize_to_index(column_num)

    if check_correct_column(column_num):
        column_name = config.COLUMN_NAMES[column_num]
        print(CHOOSED.format(column_name))
        data_analyze.get_total_percents_analyze(column_name)
    else:
        print(WRONG_COLUMN_NUM)
        input_total_percents()


def input_age_total_percents():
    column_num = input(INPUT_COLUMN_NUM)
    age_str = input(INPUT_AGE)
    column_num = normalize_to_index(column_num)

    if check_correct_column(column_num):
        if check_correct_age(age_str):
            column_name = config.COLUMN_NAMES[column_num]
            print(CHOOSED.format(column_name) + 'по возрасту ' + age_str)
            data_analyze.get_age_total_percents_analyze(column_name, age_str)
        else:
            print(WRONG_AGE)
            input_age_total_percents()
    else:
        print(WRONG_COLUMN_NUM)
        input_age_total_percents()


def input_ratio_violance_percents():
    column_num_1 = input(INPUT_MULTI_COLUMN_NUM.format('первого'))
    column_num_2 = input(INPUT_MULTI_COLUMN_NUM.format('второго'))

    column_num_1 = normalize_to_index(column_num_1)
    column_num_2 = normalize_to_index(column_num_2)

    if check_correct_column(column_num_1):
        if check_correct_column(column_num_2):
            column_name_1 = config.COLUMN_NAMES[column_num_1]
            column_name_2 = config.COLUMN_NAMES[column_num_2]
            print(CHOOSED.format(column_name_1) + ' ' + CHOOSED.format(column_name_2))
            data_analyze.get_ratio_violance_intensity_analyze(column_name_1, column_name_2)
        else:
            print(WRONG_MULTI_COLUMN_NUM.format('ПЕРВОГО'))
            input_ratio_violance_percents()
    else:
        print(WRONG_MULTI_COLUMN_NUM.format('ВТОРОГО'))
        input_ratio_violance_percents()


def input_age_ratio_violance_percents():
    column_num = input(INPUT_COLUMN_NUM)
    age_str = input(INPUT_AGE)
    column_num = normalize_to_index(column_num)

    if check_correct_column(column_num):
        if check_correct_age(age_str):
            column_name = config.COLUMN_NAMES[column_num]
            print(CHOOSED.format(column_name) + 'по возрасту ' + age_str)
            data_analyze.get_ratio_age_to_total_pies(column_name, age_str)
        else:
            print(WRONG_AGE)
            input_age_total_percents()
    else:
        print(WRONG_COLUMN_NUM)
        input_age_total_percents()


def normalize_to_index(num):
    return int(num) - 1


def check_correct_option(num):
    if num in options.keys():
        return True
    else:
        return False


def check_correct_column(column_num):
    if column_num >= 0 and column_num < len(config.COLUMN_NAMES):
        return True
    else:
        return False


def check_correct_age(age_str):
    if int(age_str) >= config.MIN_AGE and int(age_str) <= config.MAX_AGE:
        return True
    else:
        return False


run()
