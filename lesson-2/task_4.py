def function(n):
    total = 1
    total = total + function(n - 1) * -0.5 if n else 0
    return total


if __name__ == '__main__':
    n = int(input("Введите n для вычисления суммы ряда 1 -0.5 0.25 -0.125 ... :\n"))
    print(f"Сумма: {function(n)}")
