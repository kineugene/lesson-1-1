if __name__ == '__main__':
    number = str(input("Введите трёхзначное число:\n"))

    a = int(number[0])
    b = int(number[1])
    c = int(number[2])

    sum = a + b + c
    product = a * b * c

    print("Сумма: ", sum)
    print("Произведение: ", product)
