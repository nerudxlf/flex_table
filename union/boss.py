import pandas as pd


class Boss:
    def __init__(self, expansion: str, *args):
        self.arr_table_path = list(args)
        self.expansion = expansion

    def _read_excel(self) -> list:
        frames = []
        for i in self.arr_table_path:
            try:
                df = pd.read_excel(i)
                frames.append(df)
            except FileNotFoundError:
                return []
        return frames

    def _read_csv(self) -> list:
        frames = []
        for i in self.arr_table_path:
            try:
                df = pd.read_csv(i)
                frames.append(df)
            except FileNotFoundError:
                return []
        return frames
