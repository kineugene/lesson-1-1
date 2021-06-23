def left_side(n):
    return n + left_side(n - 1) if n else 0


if __name__ == '__main__':
    n = int(input("Введите n:\n"))
    print(f"Результат вычисления суммы 1 + 2 +...+n: {left_side(n)}")
    print(f"Результат вычисления n(n+1)/2: {int(n * (n+1)/2)}")
