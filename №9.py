# Дополнительные задачи.
# 1. Напишите функцию, которая принимает на вход список чисел и возвращает новый список, содержащий те же числа, но
#    отсортированные по возрастанию.
def sort2(lst:list)->list:
    lst.sort() # подскажи, пожалуйста, почему если я напишу return lst.sort(), то на выходе будет none?
    print("Отсортированный список:")
    return lst


# 2. Напишите функцию, которая принимает на вход список слов и возвращает новый список, содержащий только те слова,
#    которые состоят только из букв (верхнего или нижнего регистра).
def ret_alfa(lst_str:list)->list:
    print('Элементы из букв:')
    return [s for s in lst_str if s.isalpha()]


# 3. Напишите функцию, которая принимает на вход список чисел и возвращает новый список, содержащий только те числа,
#    которые делятся на 3 без остатка.
def div_on_3(lst_int:list)->list:
    print("Делятся на 3:")
    return [x for x in lst_int if x % 3 == 0]


# 4. Напишите функцию, которая принимает на вход список чисел и возвращает новый список, содержащий только те числа,
#    которые являются простыми.
def lst_primes(lst_int:list)->list:
    def is_prime(num:int)->bool:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0: return False
        else: return True

    print('Список простых чисел:')
    return [x for x in lst_int if is_prime(x)]


# 5. Напишите функцию, которая принимает на вход список строк и возвращает новый список, содержащий только те строки,
#    которые длиннее 5 символов.
def str_more_5(lst_str:list)->list:
    print('строки длиннее 5 символов:')
    return [s for s in lst_str if len(s) > 5]


# 6. Напишите функцию, которая принимает на вход список чисел и возвращает новый список, содержащий те же числа, но умноженные на 2.
def dig_x_2(lst_int:list)->list:
    print('Числа умноженные на 2:')
    return [x * 2 for x in lst_int]


# 7. Напишите функцию, которая принимает на вход список строк и возвращает новый список, содержащий только те строки,
#    которые содержат хотя бы одну цифру.
def have_dig(lst_str:list)->list:
    print('Содержат цифры:')
    res = []
    for el in lst_str:
        for d in el:
            if d.isdigit():
                res.append(el)
                break
    return res


# 8. Напишите функцию, которая принимает на вход список строк и возвращает новый список, содержащий те же строки, но в
#    верхнем регистре.
def to_upper(lis_str:list)->list:
    print("Строки в верхнем регистре:")
    return [s.upper() for s in lis_str]


# 1. Напишите функцию, которая принимает строку и возвращает список всех уникальных символов в этой строке.
def unic_simbols(arr_str:str)->list:
    print('Список уникальных символов:')
    return list(set(arr_str.lower()))


# 2. Напишите функцию, которая принимает на вход список строк и возвращает новый список, содержащий только те строки,
#    которые начинаются с буквы 'a' (большой или малой).
def starts_a(lst_str:list)->list:
    print('строки начинающиеся на "а":')
    return [s for s in lst_str if s.startswith('a') or s.startswith('A')]


# 3. Напишите функцию, которая принимает на вход список чисел и возвращает новый список, содержащий только те числа,
#    которые больше среднего значения всех чисел в списке.
def more_aver(lst_int:list)->list:
    print(f"среднее значение списка: {sum(lst_int) // len(lst_int)} \nчисла большие среднего:")
    return [x for x in lst_int if x > sum(lst_int) // len(lst_int)]


# 4. Напишите функцию, которая принимает на вход список строк и возвращает новый список, содержащий те же строки, но с
#    замененным первым символом на символ '*' (например, "hello" станет "*ello").
def first_replace(lst_str:list, simb:str)->list:  # я немного усложнил под любой символ
    print('первый символ заменен на', simb)
    return [simb + s[1:] for s in lst_str]


# 5. Напишите функцию, которая принимает на вход список списков чисел и возвращает новый список, содержащий те же числа,
#    но увеличенные на 1.
def inc_1(lst_lst_int:list)->list:
    res = []
    for el in lst_lst_int:
        res.extend([x + 1 for x in el])
    print('увеличенные числа:')
    return res

test_lst_int = [2, 5, 8, 9, 7, 1, 4, 6, 36, 9, 8, 21, 1, 2, 7]
test_lst_str = ['123456','ahjkj','Jgh','42jmnlj','&*1fgh','AIIOP']
test_str = 'Qwert yuio yuio'
test_lst_lst = [[2, 5, 8], [9, 7], [1, 4, 6, 36], [9, 8, 21, 1, 2, 7]]

print(sort2(test_lst_int.copy())) # ух, западло с пересылкой ссылок, а не значений - вроде меняю в функции, а оно меняется в оригинале
print(ret_alfa(test_lst_str))
print(div_on_3(test_lst_int))
print(lst_primes(test_lst_int))
print(str_more_5(test_lst_str))
print(dig_x_2(test_lst_int))
print(have_dig(test_lst_str))
print(to_upper(test_lst_str))
print(unic_simbols(test_str))
print(starts_a(test_lst_str))
print(more_aver(test_lst_int))
print(first_replace(test_lst_str, '*'))
print(inc_1(test_lst_lst))

