import pandas as pd


def to_xls(path: str) -> int:
    try:
        df = pd.read_csv(path)
        df.to_excel("new_excel.xlsx")
        return 1
    except FileNotFoundError:
        return 0
