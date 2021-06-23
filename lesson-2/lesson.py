def akkerman_fun(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return akkerman_fun(m - 1, 1)
    elif m > 0 and n > 0:
        return akkerman_fun(m - 1, akkerman_fun(m, n - 1))


def akkerman_lesson():
    print('lesson-2')
    m_n = [[0, 1], [1, 1], [2, 1], [3, 4]]
    for m, n in m_n:
        print(f'Result for akkerman({m}, {n}): {akkerman_fun(m, n)}')


def easy_numbers_lesson():
    n_count = 80
    numbers = set(range(2, n_count + 1))
    easy_numbers = numbers.copy()

    for number in numbers:
        first = True
        for next_number in range(number, n_count + 1, number):
            if first:
                first = False
            else:
                if next_number in easy_numbers:
                    easy_numbers.remove(next_number)

    easy_numbers = sorted(set(easy_numbers))
    print(list(easy_numbers))


def evclidus_lesson():
    a = 3480
    b = 17400
    max_num = max(a, b)
    min_num = min(a, b)

    left = max_num % min_num

    while left != 0:
        max_num = min_num
        min_num = left
        left = max_num % min_num

    print(f"Наибольший общий делитель = {min_num}")


def evclidus_recursion_lesson():

    def evclidus(min, max):
        left = max % min
        if left == 0:
            return min
        else:
            return evclidus(left, min)

    max = 17400
    min = 3480

    print(evclidus(min, max))


if __name__ == '__main__':
    # akkerman_lesson()
    # easy_numbers_lesson()
    # evclidus_lesson()
    evclidus_recursion_lesson()
