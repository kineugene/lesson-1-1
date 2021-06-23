from utils import is_digit

texts = ['первое', 'второе', 'третье']

if __name__ == '__main__':
    numbers = list()
    print("Введите 3 разных числа.\n")

    while len(numbers) < 3:
        number = input(f"Введите {texts[len(numbers)]} число:\n")
        if not is_digit(number):
            print("Нужно ввести число: целое или с дробной частью.")
        elif float(number) in numbers:
            print("Нужно ввести число, отличное от ранее введённых.")
        else:
            numbers.append(float(number))

    numbers = sorted(numbers)

    print(f"Среднее среди введённых число: {numbers[1]}")
