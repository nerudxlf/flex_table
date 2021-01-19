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
