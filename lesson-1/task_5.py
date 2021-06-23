import string

if __name__ == '__main__':
    alphabet_eng = string.ascii_lowercase

    a = ord('а')
    alphabet_rus = ''.join([chr(i) for i in range(a, a + 6)] + [chr(a + 33)] + [chr(i) for i in range(a + 6, a + 32)])

    letter_one = input("Введите первую букву:\n").lower()
    letter_two = input("Введите вторую букву:\n").lower()

    # TODO проверять из одного ли буквы алфавита
    # TODO проверять буква ли это вообще

    letter_one_pos = alphabet_eng.find(letter_one) if letter_one in alphabet_eng else alphabet_rus.find(letter_one)
    letter_two_pos = alphabet_eng.find(letter_two) if letter_two in alphabet_eng else alphabet_rus.find(letter_two)

    print("Порядковый номер первой буквы:", letter_one_pos + 1)
    print("Порядковый номер второй буквы:", letter_two_pos + 1)
    print("Число букв между ними:", abs(letter_one_pos - letter_two_pos) - 1 if letter_one != letter_two
          else "это та же самая буква")
