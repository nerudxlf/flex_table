import PySimpleGUI as sg


def get_menu():
    sg.theme('DarkAmber')
    layout_start = [
        [sg.Text('Выберите функцию')],
        [sg.RButton('Объеденить таблицы', key='-UNION-')],
        [sg.RButton('Объеденить 2 таблицы и удалить повторяющиеся', key='-OUTER JOIN-')],
        [sg.RButton('Объеденить 2 таблицы по ключам', key='-INNER KEY-')],
        [sg.RButton('Выбрать только повторяющиеся строки', key='-INNER JOIN-')],
        [sg.RButton('Конвертировать csv в xlsx', key='-TO CSV-')],
        [sg.RButton('Удалить повторяющиеся строки', key='-DELETE-')],
        [sg.RButton('Применить фильтр к таблицы', key='-FILTER-')],
        [sg.RButton('Удалить все символы кроме букв', key='-ONLY LETTERS-')],
        [sg.RButton('Выбрать НЕ уникальные строки из двух таблицы', key='-NOT UNIQUE-')],
        [sg.Text('Выберите файл')],
        [sg.Text('File 1'), sg.InputText(),
         sg.FileBrowse(file_types=(('xlsx', '*.xlsx'), ('xls', '*.xls'), ('csv', '*.csv'))), ],
        [sg.Text('File 2'), sg.InputText(),
         sg.FileBrowse(file_types=(('xlsx', '*.xlsx'), ('xls', '*.xls',), ('csv', '*.csv')))],
        [sg.Button('Add File', key='-ADD FILE-')],
        [sg.Text('Введите аргумент для фильтра или для объединения')],
        [sg.Text('Аргумент для фильтра вводится 1 поле')],
        [sg.Text('Arg 1'), sg.InputText(), sg.Text('Arg 2'), sg.InputText()],
    ]
    return sg.Window('Flex Table', layout_start)
