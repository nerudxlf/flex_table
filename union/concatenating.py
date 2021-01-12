import pandas as pd


class ConObjects:
    def __init__(self, *args):
        self.arr_table_path = list(args)

    def __read_csv(self) -> list:
        print(self.arr_table_path)
        frames = []
        for i in self.arr_table_path:
            df = pd.read_excel(i)
            frames.append(df)
        return frames

    def concat_frames(self) -> int:
        result = pd.concat(self.__read_csv())
        result.to_excel("result_data.xlsx", index=None)
        return 1
