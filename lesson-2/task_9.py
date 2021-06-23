def number_symbols_sum(number: str):
    res = 0
    for symbol in number:
        res += int(symbol)
    return res


if __name__ == '__main__':
    numbers = list(map(str, input("Введите через пробел 3 натуральных числа:\n").split()))
    max_num = ("", 0)
    for number in numbers:
        if number_symbols_sum(number) > max_num[1]:
            max_num = (number, number_symbols_sum(number))

    print(f"Число с максимальной посимвольной суммой: {max_num[0]}\n"
          f"Сумма: {max_num[1]}")
