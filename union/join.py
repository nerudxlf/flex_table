import pandas as pd

from union.boss import Boss


class JoinObj(Boss):
    def join_outer_is_not(self, left_name: str, right_name: str) -> int:
        """
        объеденяет 2 таблицы по методу outer is not
        :param left_name: название поля левой таблицы для объеденения
        :param right_name: название поля правой таблицы для объеденения
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
        result_inner = pd.merge(left, right, left_on=left_name, right_on=right_name)
        result_outher = pd.merge(left, right, left_on=left_name, right_on=right_name, how='outer')
        result = result_outher[~result_outher.index.isin(result_inner.index)]
        result.to_excel("result_outher.xlsx", index=None)
        return 1

    def join_inner(self, left_name: str, right_name: str) -> int:
        """
        объеденяет 2 таблицы по методу join inner
        :param left_name: название поля левой таблицы для объеденения
        :param right_name: название поля правой таблицы для объеденения
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
        result_inner = pd.merge(left, right, left_on=left_name, right_on=right_name)
        result_inner.to_excel("result_inner.xlsx", index=None)

    def not_unique(self):
        """
        Из исходной таблцы получаем таблицу с неуникальными значениями
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
        df = pd.concat([left, right])
        df = df.loc[df.duplicated(keep=False), :]
        df.to_excel("not_unique.xlsx", index=None)
