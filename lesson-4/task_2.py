#Найдём простые числа до 10 000
import cProfile
import timeit


def get_num_by_sieve_eratosphere(pos):
    numbers = [_ for _ in range(2, 10000)]
    for num in numbers:
        res = 0
        i = 2
        while res < numbers[-1]:
            res = num * i
            if res in numbers:
                numbers.remove(res)
            i += 1
    numbers = [1] + numbers
    return numbers[pos]


def get_num_by_iteration(pos):
    simple_numbers = list()
    numbers = (i for i in range(2, 10000))
    while len(simple_numbers) < pos:
        simple = True
        i = next(numbers)
        for num in simple_numbers:
            if i % num == 0:
                simple = False
        if simple:
            simple_numbers.append(i)

    simple_numbers = [1] + simple_numbers
    return simple_numbers[-1]


if __name__ == '__main__':
    i = int(input("Введите, какое по счёту простое число хотите увидеть: \n"))

    print(f'get_num_by_sieve_eratosphere: {get_num_by_sieve_eratosphere(i)}')
    # print('Время исполнения: ', timeit.timeit(f'get_num_by_sieve_eratosphere({i})',
    #                                           'from task_2 import get_num_by_sieve_eratosphere'))
    cProfile.run(f'get_num_by_sieve_eratosphere({i})')

    print(f'get_num_by_iteration: {get_num_by_iteration(i)}')
    cProfile.run(f'get_num_by_iteration({i})')
    # print('Время исполнения: ', timeit.timeit(f'get_num_by_iteration({i})',
    #                                           'from task_2 import get_num_by_iteration'))


# Введите, какое по счёту простое число хотите увидеть:
# 7
# get_num_by_sieve_eratosphere: 17
#          8774 function calls in 0.705 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.704    0.704 <string>:1(<module>)
#         1    0.461    0.461    0.704    0.704 task_2.py:6(get_num_by_sieve_eratosphere)
#         1    0.000    0.000    0.000    0.000 task_2.py:7(<listcomp>)
#         1    0.000    0.000    0.705    0.705 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      8769    0.243    0.000    0.243    0.000 {method 'remove' of 'list' objects}
#
#
# get_num_by_iteration: 17
#          61 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_2.py:20(get_num_by_iteration)
#        17    0.000    0.000    0.000    0.000 task_2.py:22(<genexpr>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        17    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        16    0.000    0.000    0.000    0.000 {built-in method builtins.next}
#         7    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Очевидно, решето Эратосфера не выгодная стратегия, ибо приходится для получения малых позиций вычислять полный список.
# + для способа перебора можно вычислять хоть до миллиарда, используя генератор. Он не кушает так много ресурсов.