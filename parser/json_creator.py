import json


def dict_to_json(file_name, dict):
    try:
        with open('../json/{}.json'.format(file_name), 'w') as outfile:
            json.dump(dict, outfile, sort_keys=False,indent=4,ensure_ascii=False)
            print('Данные {} записаны в json'.format(file_name))
    except EnvironmentError:
        print('Невозможно сохранить json файл ', file_name)
