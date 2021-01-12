import pandas as pd

from union.boss import Boss


class JoinObj(Boss):
    def left_join(self, *args) -> int:
        if self.expansion == "xlsx" or self.expansion == "xls":
            left_right = self._read_excel()
        elif self.expansion == "csv":
            left_right = self._read_csv()
        else:
            return 0
        left = left_right[0]
        right = left_right[1]

        result = pd.merge(left, right, how="left", on=list(args))
        result.to_excel("result_data.xlsx", index=None)
        return 1

    def right_join(self, *args) -> int:
        if self.expansion == "xlsx" or self.expansion == "xls":
            left_right = self._read_excel()
        elif self.expansion == "csv":
            left_right = self._read_csv()
        else:
            return 0
        left = left_right[0]
        right = left_right[1]

        result = pd.merge(left, right, how="right", on=list(args))
        result.to_excel("result_data.xlsx", index=None)
        return 1
