# 1. Напишите программу, которая принимает два числа в качестве аргументов и считает наименьшее общее кратное для этих
#    чисел.
# 2. Напишите программу, которая суммирует все целые числа от значения «start» до величины «end» включительно
#    (start, end - вводятся с клавиатуры). Если пользователь задаст первое число большее чем второе, просто поменяйте их
#    местами.
# 3. Написать проверку на то, является ли введенное число нарциссическим:
#    Пример 153 = 1^3 + 5^3 + 3^3. 153 - число нарцисс (число в степени - длина числа)

# 1-------------
num1 = int(input())
num2 = int(input())
i = min(num1, num2)
while True:
    if i % num1 == 0 and i % num2 == 0:
        break
    i += 1
print(i)

# # 2--------------
# start = int(input())
# end = int(input())
# if start > end:
#     start, end = end, start
# summ = 0
# for i in range(start, end + 1):
#     summ += i
# print(summ)

# # 3 Написать проверку на то, является ли введенное число нарциссическим:
# #  Пример 153 = 1^3 + 5^3 + 3^3. 153 - число нарцисс (число в степени - длина числа)
# num = input()
# summ = 0
# for i in num:
#     summ += int(i) ** len(num)
# if num == summ:
#     print(f"{num} - число нарцисс")
# else:
#     print(f"{num} - число не нарцисс")
