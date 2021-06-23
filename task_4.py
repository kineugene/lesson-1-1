import random

if __name__ == '__main__':
    borders = input("Введите границы диапазона целых чисел (через запятую):\n")
    a1, a2 = borders.split(',')
    a1 = int(a1.strip())
    a2 = int(a2.strip())

    print(f"Случайное число в указанном диапазоне: {random.randint(min(a1, a2), max(a1, a2))}")
    print("-------------------------------------------------------")

    borders = input("Введите границы диапазона вещественных чисел (через запятую):\n")
    a1, a2 = borders.split(',')
    a1 = float(a1.strip())
    a2 = float(a2.strip())

    print(f"Случайное число в указанном диапазоне: {random.uniform(min(a1, a2), max(a1, a2))}")
    print("-------------------------------------------------------")

    a1 = ord(input("Введите верхнюю границу диапазона символов:\n"))
    a2 = ord(input("Введите нижнюю границу диапазона символов:\n"))

    print(f"Случайный символ в указанном диапазоне: {chr(random.randint(min(a1, a2), max(a1, a2)))}")
