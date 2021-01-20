import pandas as pd

from union.boss import Boss


class DelDup(Boss):
    def delete(self):
        """
        Удаляем все повторяющиеся значения в таблице
        :return:
        """
        if self.expansion == "xlsx" or self.expansion == "xls":
            df = self._read_excel()[0]
        elif self.expansion == "csv":
            df = self._read_csv()[0]
        else:
            return 0
        df = df.drop_duplicates(keep=False)
        df.to_excel("new_data.xlsx", index=None)
