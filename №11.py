# 1. Написать функцию, которая принимает строку и возвращает центральный элемент(ы) этой строки.
#    Например: "hasbd" -> "s" "bajshd" -> "js"
def middle_el(stroka: str) -> str:
    l = len(stroka)
    if l % 2 != 0:
        return stroka[l // 2]
    else:
        return stroka[(l // 2) - 1: (l // 2) + 1]

# 2. Написать функцию, принимающую число и возвращающую ближайший к этому числу палиндром.
#    11 -> 22
#    188 -> 191
#    191 -> 202
#    2541 -> 2552

def is_palindrom(num: int) -> bool:
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False
def palindrom(num: int) -> int:
    while not is_palindrom(num):
        num += 1
    return num

# 3. Напишите функцию, которая принимает на вход список строк и возвращает наиболее часто встречающуюся строку.
def most_freq_str(lst:list[str]) -> str:
    def get_key(d, value):
        for k, v in d.items():
            if v == value:
                return k
    count = 0
    lst_set = set(lst)
    lst_dict = {}
    for i in lst_set:
        for j in lst:
            if i == j:
                count += 1
        lst_dict[i] = count
        count = 0
    val = max(lst_dict.values())
    return get_key(lst_dict, val)

# 4. Напишите функцию, которая принимает на вход два списка и возвращает новый список, содержащий элементы, которые есть
#    в обоих списках.
def intersect1(lst1: list, lst2: list) -> list:
    return list(set(lst1) & set(lst2))

def intersect2(lst1: list, lst2: list) -> list:
    return list(set(lst1).intersection(lst2))

# 5. Напишите функцию, которая принимает на вход строку и возвращает количество слов в этой строке, в которых есть более
#    3 - х гласных(a, e, i, o, u, y).

# 6. Написать функцию, которая принимает на вход два списка чисел и возвращает новый список, содержащий суммы соответствующих
#    элементов этих списков. Списки мб разной длины.Например: [1, 2, 3, 4][11, 32] -> [12, 34, 3, 4]
def summ(lst1: list, lst2: list) -> list:
    for i in range(len(lst1)):
        lst2[i] += lst1[i]
    return lst2

def sum_el(lst1: list, lst2: list) -> list:
    if len(lst1) < len(lst2):
        return summ(lst1, lst2)
    else:
        return summ(lst2, lst1)


li1 = [1, 2, 3]
li2 = [2, 3, 4, 5]

#1
#print(middle_el('bajshd'))
#2
#print(palindrom(2541))
#3
print(most_freq_str(['a', 'b', 'c', 'a', 'a', 'b', 'c', 'v', 'c', 'a']))

#4
#print('Вариант1:', intersect1(li1, li2))
#print('Вариант2:', intersect2(li1, li2))
#6
#print(sum_el(li2, li1))
