if __name__ == '__main__':
    symbol_map = {chr(num): num for num in range(32, 128)}

    to_print = dict()
    for symbol, code in symbol_map.items():
        to_print[symbol] = code
        if len(to_print) % 10 == 0:
            print(to_print)
            to_print = dict()
    print(to_print)
