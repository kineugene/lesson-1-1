if __name__ == '__main__':
    naturals_row_count = int(input("Введите количество вводимых чисел:\n"))
    naturals_row = list()
    print("Вводите числа по одному в строке:")
    for i in range(naturals_row_count):
        naturals_row.append(input())

    search_number = input("Введите число, количество которого нужно определить:\n")

    found = naturals_row.count(search_number)
    print(f'Всего найдено:{found}')
