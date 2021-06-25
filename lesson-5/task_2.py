from collections import *

hex_dec = {'0': 0,
           '1': 1,
           '2': 2,
           '3': 3,
           '4': 4,
           '5': 5,
           '6': 6,
           '7': 7,
           '8': 8,
           '9': 9,
           'a': 10,
           'b': 11,
           'c': 12,
           'd': 13,
           'e': 14,
           'f': 15}

dec_hex = {0: '0',
           1: '1',
           2: '2',
           3: '3',
           4: '4',
           5: '5',
           6: '6',
           7: '7',
           8: '8',
           9: '9',
           10: 'a',
           11: 'b',
           12: 'c',
           13: 'd',
           14: 'e',
           15: 'f'}


def sum16(a, b):
    res = list()
    left = 0
    for i in range(max(len(a), len(b))):
        pre_res = 0
        if i < len(a):
            pre_res += hex_dec[a[-i-1]]
        if i < len(b):
            pre_res += hex_dec[b[-i-1]]
        pre_res += left
        left = pre_res // 16
        res.append(dec_hex[pre_res % 16])

    if left:
        res.append(dec_hex[left])

    res.reverse()
    return res


def mul16(a, b):
    res = ['0']

    count_zero = 0

    for b_next in b[::-1]:
        to_sum = list()
        left = 0
        for a_next in a[::-1]:
            mul_res = hex_dec[a_next] * hex_dec[b_next]
            pre_res = mul_res + left
            left = pre_res // 16
            to_sum.append(dec_hex[pre_res % 16])

        if left:
            to_sum.append(dec_hex[left])
        to_sum.reverse()

        for i in range(count_zero):
            to_sum.append('0')
        count_zero += 1

        res = sum16(res, to_sum)
    return res


if __name__ == '__main__':
    a_val = list(input('Введите первое шестнадцитиричное число: \n'))
    b_val = list(input('Введите второе шестнадцитиричное число: \n'))

    print(f'Сумма: {sum16(a_val, b_val)}')
    print(f'Произведение: {mul16(a_val, b_val)}')

    # А ещё можно перевести оба числа в 10чную систему, вычислить и перевести обратно в 16чную.
    # Но тогда почти не будут использоваться коллекции
