from union.concatenating import ConObjects


def main():
    con = ConObjects("WoS/501-1000.xls", "WoS/1001-1500.xls", "WoS/1501-1625.xls")
    con.concat_frames()
