"""
2. Создайте функцию, которая генерирует список, состоящий из словарей, с ключами имя и номер телефона
(создать список имен и номеров и по этим данным генерить словарь рандомной длины). Создайте функцию, которая принимает
этот словарь и еще один аргумент, который может быть именем или номером телефона и осуществляет вызов. Если
соответствующего номера или имени нет в переданном словаре, то вызвать ошибку ValueError
"""
import random


def get_phone_book() -> list[dict[str:str]]:
    names_lst = ['Ivanov', 'Petrov', 'Sidorov', 'Vasya', 'Dima', 'Kolya']
    numbers_lst = set()
    # создание набора рандомных номеров, по количеству абонентов
    while len(numbers_lst) < len(names_lst):
        numbers_lst.add(str(random.randint(100_00_00, 999_99_99)))
    numbers_lst = list(numbers_lst)
    # создание заданного списка словарей
    lst = []
    for i in range(len(names_lst)):
        lst.append({'name': names_lst[i],
                    'phone_number': f'{numbers_lst[i][:3]}-{numbers_lst[i][3:5]}-{numbers_lst[i][5:]}'})

    return lst.copy()


def is_phone_number(array: str) -> bool:
    """Проверка является ли аргумент номером телефона"""
    array = array.strip()
    numerics = '0123456789-'
    for i in array:
        if i not in numerics:
            return False
    return True


def call(abon_lst: list, abonent: str) -> None:
    # выбираем действие в зависимости от переданного аргумента
    match is_phone_number(abonent):
        case True:
            for abon in abon_lst:
                if abon['phone_number'] == abonent:
                    print(f'Call subscriber {abon['name']}')
            else:
                raise ValueError('Передано неверное значение')

        case False:
            for abon in abon_lst:
                if abon['name'].lower() == abonent.lower():
                    print(f'Call number {abon['phone_number']}')
            else:
                raise ValueError('Передано неверное значение')



call(get_phone_book(), 'ivanov')
call(get_phone_book(), 'ivan')
call(get_phone_book(), '123-45-67')


