import pandas as pd


class Boss:
    """Класс родитель для остальных классов связанных с взаимодействием с таблицами"""
    def __init__(self, expansion: str, *args):
        self.arr_table_path = list(args)
        self.expansion = expansion

    def _read_excel(self) -> list:
        """
        Функция читает файлы с раширением xls, xlsx
        :return: возвращаем массив из объектов типа DataFrame
        """
        frames = []
        for i in self.arr_table_path:
            try:
                df = pd.read_excel(i)
                frames.append(df)
            except FileNotFoundError:
                return []
        return frames

    def _read_csv(self) -> list:
        """
        Функция читает файлы с расширением cvs
        :return: возвращает массив из объектов типа DataFrame
        """
        frames = []
        for i in self.arr_table_path:
            try:
                df = pd.read_csv(i)
                frames.append(df)
            except FileNotFoundError:
                return []
        return frames
