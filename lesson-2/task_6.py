import random
import sys
from time import sleep

if __name__ == '__main__':
    print("У вас есть 10 попыток, чтобы угадать число от 0 до 100. "
          "После каждой попытки будет подсказка, больше или меньше указанного загаданное число.")
    number = random.randint(0, 100)
    for i in range(10):
        guess = int(input(f"У вас осталось {10 - i} попыток. Введите число:\n"))
        if guess == number:
            print(f"Верно! Это число {guess}. ")
            break
        elif i == 9:
            print(f"Жаль, но попытки кончились. Загаданное число: {number}. ")
        else:
            print(f"Мимо) Загаданное число {'больше' if guess < number else 'меньше'} указанного.")

    for i in range(6):
        sleep(1)
        sys.stdout.write(f"\rПрограмма завершится через {5 - i} сек.")
        sys.stdout.flush()
