if __name__ == '__main__':
    natural_number = input('Введите любое натуральное число:\n')
    even = 0
    odd = 0
    for letter in natural_number:
        if int(letter) % 2 == 0:
            even += 1
        else:
            odd += 1

    print(f"Чётных: {even}, нечётных {odd}")
