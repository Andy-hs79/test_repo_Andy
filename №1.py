# ДЗ на пятницу
# 1. Есть две переменные, поменяйте их значение местами.
# 2. Есть переменная, например a = 5 - длина стороны квадрата. Выведите площадь, периметр и диагональ квадрата со стороной а.
# Вывод должен быть вида:
# Диагональ: 12.5
# Площадь: 24.3
# Периметр: 18.2


# 1.:
print("Задание 1:")
a = 5
b = 7

print("a =", a, "b =", b)
a, b = b, a
print("a =", a, "b =", b)
print() # пропуск строки для красоты

# 2.:
print("Задание 2:")
a = 8

print("Диагональ:", a * 1.41) # точнее а * sqrt(2), но для этого надо подключать math, а мы это еще не проходили)
print("Площадь:", a * a)
print("Периметр:", a * 4)
