def is_digit(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
