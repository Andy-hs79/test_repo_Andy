# 1. На входе программа получает список целых чисел s. Ваша задача - вывести следующие списки по одному в строке:
# 2. Напишите декоратор, который замеряет время выполнения функции и кол-во памяти, которое занимает ответ.
# 3. Напишите декоратор, который будет корректировать результат функции, а именно помещать их в словарь.
#    {"status": "success", "result": ...}
# ----------------------------------------------------------------------------------------------------------------------
import time, sys


def res_to_dict(func):
    def wrapper(*args):
        res = func(*args)
        res_dict = {"status": "success"}
        res_dict["result"] = res
        print(res_dict)
        return res

    return wrapper


def func_measuring(func):
    def wrapper(*args):
        start = time.perf_counter_ns()
        res = func(*args)
        print(res)
        print(f'результат занимает {sys.getsizeof(func)} байт')
        print(f'время выполнения {time.perf_counter_ns() - start} ns')
        return res

    return wrapper


#    Список, состоящий из квадратов s.
@res_to_dict
@func_measuring
def squares(lst: list[int]) -> list:
    return [x ** 2 for x in lst]


#    Список, состоящий из остатков деления на 11 элементов s.
@res_to_dict
@func_measuring
def remainder_division_11(lst: list[int]) -> list:
    return [x % 11 for x in lst]


#    Список, состоящий только из чётных элементов s.
@res_to_dict
@func_measuring
def even_numbers(lst: list[int]) -> list:
    return [x for x in lst if x % 2 == 0]


#    Список, состоящий только из элементов s с нечётным количеством цифр.
@res_to_dict
@func_measuring
def odd_quantity_dig(lst: list[int]) -> list:
    return [x for x in lst if len(str(x)) % 2 != 0]


#    Список, состоящий только из двухзначных элементов s, записанных 2 раза подряд.
@res_to_dict
@func_measuring
def double_dig(lst: list[int]) -> list:
    return [s[i] for i in range(len(lst)) if len(str(lst[i])) == 2 and lst[i] == lst[i - 1]]


#    Список, состоящий из элементов s, стоящих на позициях, не кратных 3.
@res_to_dict
@func_measuring
def position_not_div_3(lst: list[int]) -> list:
    return [s[i] for i in range(len(lst)) if i % 3 != 0]


s = [1, 2, 3, 4, 5, 11, 12, 12, 12, 555, 20]

squares(s)
remainder_division_11(s)
even_numbers(s)
odd_quantity_dig(s)
double_dig(s)
position_not_div_3(s)
