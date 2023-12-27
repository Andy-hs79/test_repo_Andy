"""
1. Создать класс Human c атрибутами name, surname, birth_year и двумя методами full_name(), который будет  возвращать
полное имя: Name Surname и get_age(), возвращающий возраст, созданного экземпляра.
"""
from datetime import date


class Human:

    def __init__(self, name, surname, birth_year):
        """Constructor"""
        self.name = name.capitalize()
        self.surname = surname.capitalize()
        self.birth_year = birth_year

    def full_name(self) -> str:
        return f'{self.name} {self.surname}'

    def get_age(self) -> int:
        return date.today().year - self.birth_year


man1 = Human('vasya', 'ivanov', 1985)
man2 = Human('petya', 'sidorov', 2001)

print(man1.full_name())
print(man1.get_age())
print(man2.full_name())
print(man2.get_age())

