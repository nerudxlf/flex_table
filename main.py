from union.concatenating import ConObjects
from union.join import JoinObj
from convert.csv_to_xls import to_xls


def main():
    while True:
        print("1 - объеденить таблицы\n2 - left join\n3 - right join\n4 - csv to xls")
        choice = int(input())
        if choice == 1:
            con = ConObjects("csv", "Scopus/2016.csv", "Scopus/2017-2020.csv")
            con.concat_frames()
        elif choice == 2:
            j = JoinObj()
        elif choice == 3:
            pass
        elif choice == 4:
            print("Введите название путь и название файла")
            name = str(input())
            to_xls(name)
