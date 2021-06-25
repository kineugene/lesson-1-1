import cProfile
import timeit

def task_2_f():
    number = '123'

    a = int(number[0])
    b = int(number[1])
    c = int(number[2])

    sum = a + b + c
    product = a * b * c

    print("Сумма: ", sum)
    print("Произведение: ", product)


if __name__ == '__main__':
    print("Timeit:", timeit.timeit('task_2_f', 'from task_1 import task_2_f'), '\n')
    cProfile.run('task_2_f()')

