import datetime
from collections import *
from dataclasses import dataclass

if __name__ == '__main__':
    c = Counter()
    some_list = [1, 2, 3, 1, 1, 3, 1]
    for i in some_list:
        c[i] += 1

    print(c)
    print(list(c))
    print(sum(c.values()))
    print(len(some_list))
    print(c.most_common())
    print(c.most_common()[:-3:-1])

    or_dict = OrderedDict({'a': 1, 'b': 11, 'c': 233})
    print(or_dict)

    point = namedtuple('point', 'x, y')
    A = point(1, 2)
    B = point(2, 3)
    print(A, B)

    ComplexNumber = namedtuple('ComplexNumber', 're, im')
    c_num1 = ComplexNumber(1, 2)
    c_num2 = ComplexNumber(2, 3)

    c_num3 = ComplexNumber(c_num1.re * c_num2.re - c_num1.im * c_num2.im,
                           c_num1.im * c_num2.im + c_num1.re * c_num2.re)
    print(c_num3)

    students = {'St1': 1, 'St2': 5, 'St3': 4.5}
    avg_rate = (sum(students.values()))/len(students)
    avg_students = {st: rate for st, rate in students.items() if rate > avg_rate}

    print(f'Студенты с баллом выше среднего: {avg_students}. Средний балл: {avg_rate}')

    #
    @dataclass
    class Item:
        id: int
        name: str
        count: int

        def buy_item(self, count):
            self.count -= count

    items_in_shells = [Item(1, "Вафля", 14), Item(2, "Молоко", 4)]
    buy_item = namedtuple('buy_item', 'id, count')
    items_to_buy = [buy_item(1, 3), buy_item(2, 1)]
    for item_to_buy in items_to_buy:
        for item_in_shell in items_in_shells:
            if item_to_buy.id == item_in_shell.id:
                item_in_shell.buy_item(item_to_buy.count)

    print(items_in_shells)

    #
    dates = list()
    for i in range(3):
        imput_date = list(map(int, input(f'Введите дату {i} (напр. 11.06.1989) : \n').split('.')))
        dates.append(datetime.date(year=imput_date[2], month=imput_date[1], day=imput_date[0]))

    if dates[0] < dates[2] < dates[1]:
        print('Последняя дата в пределах впервых двух')
    else:
        print('Последняя дата не в пределах впервых двух')


