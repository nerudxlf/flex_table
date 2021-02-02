from setings.menu import get_menu
from union.concatenating import ConObjects
from union.deldup import DelDup
from union.filter import GetTableByFilter
from union.join import JoinObj
from convert.csv_to_xls import to_xls
import PySimpleGUI as sg

from union.upgrade import UpgradeTable


def parse_type(val: list) -> str:
    """
    :param val:
    :return: возвращает расширение в виде строки или 0, если расширение разное
    """
    a = []
    if len(val) == 1:
        sg.popup_quick_message("Добавьте файлы")
        return '0'
    for i in range(0, len(val) - 1):
        a = val[i].split('.')
        b = val[i + 1].split('.')
        if a[1] != b[1]:
            sg.popup_ok("Файлы должны быть с одним расширением")
            return '0'
    return a[1]


def main():
    window = get_menu()
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Add File':
            pass
        if event == '-UNION-' and values[0] and values[1]:
            val = [values[0], values[1]]
            get_type = parse_type(val)
            if get_type == '0':
                pass
            else:
                con = ConObjects(get_type, *val)
                if con == 0:
                    sg.popup_ok("Файл не найден")
                con.concat_frames()
        if event == '-OUTER JOIN-' and values[0] and values[1] and values[2] and values[3]:
            val = [values[0], values[1]]
            get_type = parse_type(val)
            if get_type == '0':
                pass
            else:
                j = JoinObj(get_type, *val)
                if j == 0:
                    sg.popup_ok("Файл не найден")
                j.join_outer_is_not(values[2], values[3])
        if event == '-INNER KEY-' and values[0] and values[1] and values[2] and values[3]:
            val = [values[0], values[1]]
            get_type = parse_type(val)
            if get_type == '0':
                pass
            else:
                j = ConObjects(get_type, *val)
                if j == 0:
                    sg.popup_ok("Файл не найден")
                j.concat_frames_inner(values[2], values[3])
        if event == '-INNER JOIN-' and values[0] and values[1] and values[2] and values[3]:
            val = [values[0], values[1]]
            get_type = parse_type(val)
            if get_type == '0':
                pass
            else:
                j = JoinObj(get_type, *val)
                if not j:
                    sg.popup_ok("Файл не найден")
                j.join_inner(values[2], values[3])
        if event == '-TO CSV-' and values[0]:
            to_xls(values[0])
        if event == '-FIO-' and values[0]:
            get_type = values[0].split('.')[1]
            df = ConObjects(get_type, values[0])
            if not df:
                sg.popup_ok("Файл не найден")
            df.contact_fio()
        if event == '-DELETE-' and values[0]:
            get_type = values[0].split('.')[1]
            delete_string = DelDup(get_type, values[0])
            if not delete_string:
                sg.popup_ok("Файл не найден")
            delete_string.delete()
        if event == '-FILTER-' and values[0] and values[2]:
            get_type = values[0].split('.')[1]
            new_table = GetTableByFilter(get_type, values[0])
            if not new_table:
                sg.popup_ok("Файл не найден")
            new_table.get_new_table(values[2])
        if event == '-ONLY LETTERS-' and values[0] and values[2]:
            get_type = values[0].split('.')[1]
            new_table = UpgradeTable(get_type, values[0])
            if not new_table:
                sg.popup_ok("Файл не найден")
            new_table.only_letters(values[2])
        if event == '-NOT UNIQUE-' and values[0] and values[1]:
            val = [values[0], values[1]]
            get_type = parse_type(val)
            if get_type == '0':
                pass
            else:
                result = JoinObj(get_type, *val)
                if not result:
                    sg.popup_ok("Файл не найден")
                result.not_unique()
