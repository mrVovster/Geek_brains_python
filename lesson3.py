"""
Реализовать функцию, принимающую два числа
(позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""


def div(*args):
    try:
        arg1 = int(input("Input numerator "))
        arg2 = int(input("Input denominator "))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "cannot be divided by zero"

    return res


print(f'result  {div()}')

'''
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных
о пользователе одной строкой.
'''


def my_func(name, surname, year, city, email, phone_number):
    return ' '.join([name, surname, year, city, email, phone_number])


print(my_func(surname='Петров', name='Иван', year='1987', city='Москва', email='test@test.ru',
              phone_number='8-903-300-99-87'))

'''
Реализовать функцию my_func(), которая принимает три позиционных
аргумента, и возвращает сумму наибольших двух аргументов.
'''


def my_func(arg1, arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg2 < arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3


print(
    f'Result - {my_func(int(input("enter first argument ")), int(input("enter second argument ")), int(input("enter third argument ")))}')

'''Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень'''


def my_func(x, y):
    return x ** abs(y)


print(f'square of x and y - {my_func(2, 2)}')

'''
Программа запрашивает у пользователя строку чисел, разделенных
 пробелом. При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и
снова нажать Enter. Сумма вновь введенных чисел будет добавляться
к уже подсчитанной сумме. Но если вместо числа вводится специальный
символ, выполнение программы завершается. Если специальный символ
введен после нескольких чисел, то вначале нужно добавить сумму этих
чисел к полученной ранее сумме и после этого завершить программу.
'''


def my_sum():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Input numbers or x for quit - ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'x' or number[el] == 'x':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Current sum is {sum_res}')
    print(f'Your final sum is {sum_res}')


my_sum()

'''
Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать
строка из слов, разделенных пробелом. Каждое слово состоит
из латинских букв в нижнем регистре. Сделать вывод исходной
строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
'''


def int_func(*args):
    word = input("Input words ")
    print(word.title())
    return


int_func()
