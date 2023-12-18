# 1. Реализуйте декоратор, который проверяет аргументы функции на тип данных. Соответствие аннотациям.
#    Рекомендую использовать метод annotations. В качестве результата возвращаем значение bool.
def annotation_checking(n: int, s: str) -> bool:
    ...


annot = annotation_checking.__annotations__
print(annot)
