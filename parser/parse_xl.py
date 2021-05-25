import openpyxl as opxl
import config
import cell_info, cells_categories
import json_creator


def load_xl_file(file_name):
    workbook = opxl.load_workbook('../anketi/{}.xlsx'.format(file_name))
    return workbook


def get_sheet(wb):
    return wb.active


file_name = input('Имя файла: ')
last_cell_number = int(input('Номер последней ячейки: '))
sheet = get_sheet(load_xl_file(file_name))
сtg = cells_categories.get_categories_cells(file_name)
table_data = cell_info.get_cells_value(sheet, last_cell_number, сtg)

json_creator.dict_to_json(file_name, table_data)


# ночинаем с ячейки 3
# A - sex, B - age, C - family, D - others
