if __name__ == '__main__':
    x1, y1 = (float(i) for i in input("Введите первую точку (x,y):\n").split(','))
    x2, y2 = (float(i) for i in input("Введите вторую точку (x,y):\n").split(','))

    if x1 == x2:
        print("Значения x двух точек не должны совпадать.")
    else:
        k = (y1 - y2) / (x1 - x2)
        b = y1 - k * x1
        k = int(k) if k.is_integer() else k
        b = int(b) if b.is_integer() else b

        equation = 'y = '
        if k:
            if k == 1:
                equation += 'x '
            elif k == -1:
                equation += '-x '
            else:
                equation += f'{k}x '

        if b:
            if k:
                if b > 0:
                    equation += f'+ {b}'
                else:
                    equation += f'- {abs(b)}'
            else:
                equation += f'{b}'

        print(f"Уравнение прямой, проходящей через эти точки: {equation}")
