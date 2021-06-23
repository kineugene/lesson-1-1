import string

if __name__ == '__main__':
    alphabet_eng = string.ascii_lowercase

    letter_num = int(input(f"Введите порядковый номер буквы английского алфавита (от 1 до {len(alphabet_eng)}):\n"))

    if 0 < letter_num <= len(alphabet_eng):
        print(f"Буква под номером {letter_num}: {alphabet_eng[letter_num - 1]}")
    else:
        print('Введено некорректное число.')
