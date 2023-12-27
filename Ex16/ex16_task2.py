"""
2. Создайте функцию, которая генерирует список, состоящий из словарей, с ключами имя и номер телефона.
Создайте функцию которая принимает этот словарь и еще один аргумент, который может быть именем или номером телефона и
осуществляет вызов. Если соответствующего номера или имени нет в переданном словаре, то вызвать ошибку ValueError
"""


def phone_book() -> list[dict[str:str]]:
    lst = [{'name': 'Ivanov', 'phone_number': '123-23-45'},
           {'name': 'Petrov', 'phone_number': '123-45-67'},
           {'name': 'Sidorov', 'phone_number': '123-54-76'}]
    return lst.copy()


def is_phone_number(array: str) -> bool:
    """проверка является ли аргумент номером"""
    array = array.strip()
    numerics = '0123456789-'
    for i in array:
        if i not in numerics:
            return False
    return True


def call(abon_lst: list, abonent: str) -> None:
    # выбираем действие в зависимости от переданого аргумента
    match is_phone_number(abonent):
        case True:
            for abon in abon_lst:
                if abon['phone_number'] == abonent:
                    print(f'Call subscriber {abon['name']}')
        case False:
            for abon in abon_lst:
                if abon['name'].lower() == abonent.lower():
                    print(f'Call number {abon['phone_number']}')
            else:
                raise ValueError('Передано неверное значение')


call(phone_book(), '123-45-67')
call(phone_book(), 'ivanov')
call(phone_book(), 'ivan')


