import categories_dict as cg


def get_categories_cells(file_name):
    if file_name is 'бабичи' or file_name is 'залесье' or \
    file_name is 'коммуна' or file_name is 'мотневичи' or \
    file_name is 'нисимковичи' or file_name is 'полесье' or \
    file_name is 'отор' or file_name is 'ровковичи' or file_name is 'сидоровичи':
        return cg.DICT_1
    else:
        return cg.DICT_2
