if __name__ == '__main__':
    while True:
        operations = {'*': lambda a, b: a * b,
                      '-': lambda a, b: a - b,
                      '/': lambda a, b: a / b,
                      '+': lambda a, b: a + b}
        operation = input('Введите операцию (+, -, *, /) или 0 для завершения:\n')
        if operation == '0':
            break
        if operation not in operations.keys():
            print('Операция должна быть одной из перечисленных: +, -, *, / или 0 для выхода')
        else:
            a, b = list(map(int, input("Введите через пробел a и b:\n").split()))
            if operation == '/' and b == 0:
                result = '∞'
            else:
                result = operations[operation](a, b)
            print(f'Результат: {result}')
