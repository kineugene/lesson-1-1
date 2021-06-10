if __name__ == '__main__':
    x1, y1 = (float(i) for i in input("Введите первую точку (x,y):\n").split(','))
    x2, y2 = (float(i) for i in input("Введите вторую точку (x,y):\n").split(','))

    if x1 == x2 or y1 == y2:
        print("Значения x двух точек не должны совпадать.")
    else:
        k = (y1 - y2) / (x1 - x2)
        b = y1 - k * x1
        k = int(k) if k - int(k) == 0 else k
        b = int(b) if b - int(b) == 0 else b

        print(f"Уравнение прямой, проходящей через эти точки: y={k}*x + {b}")


