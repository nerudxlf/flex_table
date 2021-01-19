import random

import pandas as pd

from union.boss import Boss


class GetTableByFilter(Boss):
    def get_new_table(self, name: str):
        """
        :param name:
        :return:
        """
        if self.expansion == "xlsx" or self.expansion == "xls":
            df = self._read_excel()[0]
        elif self.expansion == "csv":
            df = self._read_csv()[0]
        else:
            return 0
        df = df.filter(items=[name])
        df.to_excel(f"new_table_{name}.xlsx", index=None)
