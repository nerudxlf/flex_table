from union.concatenating import ConObjects
from union.deldup import DelDup
from union.join import JoinObj
from convert.csv_to_xls import to_xls


def main():
    while True:
        print("1 - объеденить таблицы\n2 - left join\n3 - right join\n4 - csv to xls\n5 - удалить повторяющиеся строки")
        choice = int(input())
        if choice == 1:
            con = ConObjects("xls", "WoS/501-1000.xls", "WoS/1001-1500.xls", "WoS/1501-1625.xls",)
            con.concat_frames()
        elif choice == 2:
            j = JoinObj("xlsx", "new_excel.xlsx", "result_data30.xlsx")
            j.left_join("Volume")
        elif choice == 3:
            pass
        elif choice == 4:
            print("Введите название путь и название файла")
            name = str(input())
            to_xls(name)
        elif choice == 5:
            delete_string = DelDup("xlsx", "result_data.xlsx")
            delete_string.delete()
