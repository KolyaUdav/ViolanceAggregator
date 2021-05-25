import config


def get_cells_value(sheet, last_index, categories_dict):
    participants_dict = {}
    i = config.FIRST_INDEX

    while i <= last_index:
        participant_dict = {}

        participant_dict['specific'] = get_specific_cells_value(sheet, i)

        participant_categories_dict = {}

        for key in categories_dict:
            values_category = get_cell_value_category(sheet,
                categories_dict[key], key, i)
            #if len(values_category) > 0:
            participant_categories_dict[key] = values_category
        #if len(participant_categories_dict) > 0:
        participant_dict['categories'] = participant_categories_dict

        participants_dict[i - 2] = participant_dict

        i += 1

    return participants_dict


def get_cell_value_others(sheet, index):
    return get_cell_value(sheet, index, config.OTHERS)


def get_cell_value_family(sheet, index):
    return get_cell_value(sheet, index, config.FAMILY)


def get_cell_value_sex(sheet, index):
    return get_cell_value(sheet, index, config.SEX)


def get_cell_value_age(sheet, index):
    return get_cell_value(sheet, index, config.AGE)


def get_cell_value(sheet, index, letter_index):
    cell_value = sheet[letter_index + str(index)].value

    if cell_value != '' and cell_value != None and cell_value != '-':
        return str(cell_value)
    else:
        return ''


def get_cell_value_category(sheet, category_arr, category_name, index):
    c = 0
    category_value_arr = []

    while c < len(category_arr):
        value = get_cell_value(sheet, index, category_arr[c])
        if value is not '' and value is not None:
            category_value_arr.append(value)
        c += 1

    return category_value_arr


def get_specific_cells_value(sheet, index):
    spec_cells_dict = {}

    spec_cells_dict['sex'] = get_cell_value_sex(sheet, index)
    spec_cells_dict['age'] = get_cell_value_age(sheet, index)
    spec_cells_dict['family'] = get_cell_value_family(sheet, index)
    spec_cells_dict['others'] = get_cell_value_others(sheet, index)

    return spec_cells_dict


def get_cell_data_dict():
    return cell_data_dict


cell_data_dict = {}
