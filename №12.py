from functools import reduce

# 1. Напишите функцию, которая принимает список вида [1, 2, 'aasf', '1', '123', 123, True], и возвращает новый список,
#    состоящий только из чисел [1,2,123]
def get_int_elements(lst: list) -> list[int]:
    return [x for x in lst if type(x) is int]

# 2. Определите является ли число специальным, по определение специальное число - это число, которое состоит только из
#    чисел 0, 1, 2, 3, 4 или 5. Например:
# 12 - специальное
# 5 - специальное
# 62 - нет
# 123450 - специальное
# 1234560 - нет
def is_special(num: int) -> bool:
    num = str(num)
    special_symbols = '012345'
    for char in num:
        if char not in special_symbols:
            return False
    return True

# 3. Напишите функцию operation_range(start, end, step, operator):
#    которая проводит действие, указанное в переменной operator над последовательностью от start до end с шагом step.
#    Например: operation_range(1, 5, 1, "+") -> 15
def operation_range(start: int, end: int, step: int, operator: str): # что здесь поставить в аннотации вывода?
    lst = list(range(start, end + 1, step))
    match operator:
        case '+':
            return reduce((lambda x, y: x + y), lst)
        case '-':
            return reduce((lambda x, y: x - y), lst)
        case '/':
            return reduce((lambda x, y: x / y), lst)
        case '*':
            return reduce((lambda x, y: x * y), lst)
        case '**':
            return reduce((lambda x, y: x ** y), lst)
        case _:
            return 'Wrong operator'
# 4. Функция принимает число и возвращает сумму квадратов чисел этого чиcла.
#    in: 321 out: 14
def get_sum_squares(num: int) -> int:
    num = str(num)
    return sum([int(x)**2 for x in num])

# 5. Функция принимает список чисел и сортирует четные от нечетных: [5, 8, 6, 3, 4]  =>  [5, 3, 8, 6, 4]
def sort_even_odd(lst:list[int]) -> list[int]:
    result = []
    for x in lst:
        if x % 2 != 0:
            result.append(x)
            lst.remove(x)
    result.extend(lst)
    return result

#1
print(get_int_elements([1, 2, 'aasf', '1', '123', 123, True]))
#2
print(is_special(1236))
#3
print(operation_range(1, 5, 1, "+"))
#4
print(get_sum_squares(321))
#5
print(sort_even_odd([5, 8, 6, 3, 4]))
