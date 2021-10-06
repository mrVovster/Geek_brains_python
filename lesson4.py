"""
Реализовать скрипт, в котором должна быть предусмотрена
 функция расчета заработной платы сотрудника. В расчете
 необходимо использовать формулу:
 (выработка в часах*ставка в час) + премия.
 Для выполнения расчета для конкретных значений необходимо
 запускать скрипт с параметрами.
"""


def sal():
    try:
        time = float(input('Выработка в часах '))
        salary = int(input('Ставка в у.е. '))
        bonus = int(input('Премия в у.е. '))
        res = time * salary + bonus
        print(f'заработная плата сотрудника  {res}')
    except ValueError:
        return print('Not a number')


sal()
"""
Представлен список чисел. Необходимо вывести 
элементы исходного списка, значения которых 
больше предыдущего элемента.
"""
a = [45, 11, 6, 5, 1, 8, 4, 98, 7, 1, 78, 183, 5]
answer = []

for i in range(len(a) - 1):
    if a[i] < a[i + 1]:
        answer.append(a[i + 1])

print(answer)

"""
Для чисел в пределах от 20 до 240 найти числа,
кратные 20 или 21.
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""
print(f'Числа от 20 до 240 кратные 20 или 21 - {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')

"""
Представлен список чисел. Определить элементы списка,
не имеющие повторений. Сформировать итоговый массив чисел,
соответствующих требованию. Элементы вывести
в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
"""

my_list = [6, 11, 6, 5, 1, 5, 4, 98, 7, 1, 78, 183, 5]
my_new_list = [el for el in my_list if my_list.count(el) == 1]
print(f'Числа не имеющие повторений {my_new_list}')

"""
Реализовать формирование списка, используя
функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000
(включая границы). Необходимо получить результат
вычисления произведения всех элементов списка.
"""

from functools import reduce


def my_func(el_p, el):
    return el_p * el


print(f'Список четных значений {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Результат перемножения всех элементов списка {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')

"""
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа,
начиная с указанного,
б) бесконечный итератор, повторяющий элементы
некоторого списка, определенного заранее.

"""

from itertools import count
from itertools import cycle


def my_count_func(start_number, stop_number):
    for el in count(start_number):
        if el > stop_number:
            break
        else:
            print(el)


def my_cycle_func(my_list, iteration):
    i = 0
    iter = cycle(my_list)
    while i < iteration:
        print(next(iter))
        i += 1


my_count_func(start_number=int(input("enter start number: ")), stop_number=int(input("enter stop number: ")))
my_cycle_func(my_list=[1, 2], iteration=int(input("enter iteration: ")))

"""
Реализовать генератор с помощью функции с ключевым словом yield,
создающим очередное значение. При вызове функции должен создаваться
объект-генератор. Функция должна вызываться следующим образом: for
el in fact(n). Функция отвечает за получение факториала числа, а в
цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
"""

from math import factorial


def fact(n: int):

    for i in range(1, n + 1):
        yield factorial(i)


if __name__ == '__main__':
    input_data = input('Введите количество вычисленных факториалов: ')

    try:
        value = int(input_data)
    except ValueError as e:
        print(e)
        exit(1)

    for el in fact(value):
        print(el)
