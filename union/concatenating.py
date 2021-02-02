import random

import pandas as pd
import numpy as np

from union.boss import Boss


class ConObjects(Boss):
    def concat_frames(self) -> int:
        """
        Объеденяет 2 и более таблицы
        :return: возвращает 1 в случае успеха 0 в случае неудачи
        """
        if self.expansion == "xlsx" or self.expansion == "xls":
            result = pd.concat(self._read_excel())
        elif self.expansion == "csv":
            result = pd.concat(self._read_csv())
        else:
            return 0
        result.to_excel(f"result_data{int(random.random() * 100)}.xlsx", index=None)
        return 1

    def concat_frames_inner(self, left_name, right_name):
        """
        Объединяет 2 таблицы по 2 столбацм
        :param left_name: название первого столбца
        :param right_name: название второго столбца
        :return:
        """
        if self.expansion == "xlsx" or self.expansion == "xls":
            left_right = self._read_excel()
        elif self.expansion == "csv":
            left_right = self._read_csv()
        else:
            return 0
        left = left_right[0]
        right = left_right[1]
        result = pd.merge(left=left, right=right, left_on=left_name, right_on=right_name)
        result.to_excel("result_con_data.xlsx", index=None)

    def contact_fio(self):
        """
        Функция объединяет столбцы Имя Фамилия Отчество в один столбец
        :return:
        """
        if self.expansion == "xlsx" or self.expansion == "xls":
            df = self._read_excel()
        elif self.expansion == "csv":
            df = self._read_csv()
        else:
            return 0
        frame = pd.DataFrame(np.concatenate(df))
        fio = frame.filter(items=[0, 1, 2, 4, 5, 12])
        fio['new_name'] = fio.apply(lambda x: x[0]+" ", axis=1)
        fio['new_surname'] = fio.apply(lambda x: x[1][0] + ".", axis=1)
        fio['new_patronymic'] = fio.apply(lambda x: x[2][0] + ".", axis=1)
        fio['FIO'] = fio['new_name'] + fio['new_surname'] + fio['new_patronymic']
        new_frame = fio.filter(items=['FIO', 4, 5, 12])
        new_frame.to_excel("fio.xlsx", index=False)
