# 1. напишите сортировку "пузырьком"
# 2. Пользователь вводит число от 0 до 100, узнайте, что за число пользователь ввел, максимум за 7 попыток
#    (рекомендую использовать алгоритм бинарного поиска) на каждую из попыток программа должна отвечать True/False

# 1.---------------------
def booble(lst = []):
    flag = True
    i = 0
    n = len(lst)
    flag = False # чтобы если не сделано ни одного обмена, то завершить
    for i in range (n - 1):
        flag = True
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                flag = False
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        if flag:
            break
    return lst

def bin_search(n):
    min_el = 0
    max_el = 100



lst = [1,4,2,3,4,6,8,9,7,0,1]

print(lst)
print(booble(lst))


