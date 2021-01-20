import random

import pandas as pd

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
