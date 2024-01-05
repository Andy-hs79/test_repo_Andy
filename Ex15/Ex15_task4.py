# 4.  Напишите функцию, которая будет генерировать случайный пароль. В пароле должно быть от 8 до 15 символов Юникода
#     из диапазонов 48-57 (цифры), 65-90 (буквы латинского алфавита в верхнем регистре) и 97-122 (буквы латинского
#     алфавита в нижнем регистре). Сгенерируйте и выведите на экран три пароля.
import random


def password() -> str:
    # создание списка кодов символов пароля
    symbols_for_generate = list(range(48, 58)) + list(range(65, 91)) + list(range(97, 123))
    numb_symbols = random.randint(8, 15)  # задание количества символов пароля
    result_password = random.sample(symbols_for_generate, numb_symbols)
    result_password = [chr(c) for c in result_password]
    return ''.join(result_password)


for _ in range(3):
    print(password())
