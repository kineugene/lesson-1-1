if __name__ == '__main__':
    year = input("Введите год:\n")

    if not year.isdigit():
        print("Введённое значение не является годом.")

    else:
        year = int(year)
        if not year % 100:
            if not year % 400:
                print("Високосный")
            else:
                print("Не високосный")
        elif not year % 4:
            print("Високосный")
        else:
            print("Не високосный")
