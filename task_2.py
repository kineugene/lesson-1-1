if __name__ == '__main__':
    a = 5
    b = 6

    # Умножаем число на 4 (2^2)
    two_left_operation = a << 2
    # Делим число на 4 (2^2), отбрасываем дробную часть
    two_right_operation = a >> 2

    print(f"""
    5 or 6 = {a ^ b}
    5 and 6 = {a & b}
    5 xor 6 = {a | b}
    not 5 = {~ a}
    not 6 = {~ b}
    5 << 2 = {two_left_operation}
    5 >> 2 = {two_right_operation} 
    """)
