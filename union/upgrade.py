import re

from union.boss import Boss
import numpy as np
import pandas as pd


class UpgradeTable(Boss):
    def only_letters(self, name):
        """
        Удаляет из столбцов все симовлы кроме букв
        :param name: название столбца
        :return:
        """
        if self.expansion == "xlsx" or self.expansion == "xls":
            df = self._read_excel()[0]
        elif self.expansion == "csv":
            df = self._read_csv()[0]
        else:
            return 0
        df['new'] = df.apply(lambda x: re.compile('\W').sub('', x.get(name)).upper(), axis=1)
        df.to_excel("only_letters.xlsx", index=False)
