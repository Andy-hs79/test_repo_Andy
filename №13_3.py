# 3. Напишите функцию, которая принимает два аргумента:
#    количество денег в наличии (str) и корзина покупателя (list[dict]).
#    Далее проверяет хватает ли денег на оплату всех товаров из корзины. В случае, если хватает возвращает ответ вида:
#   {"status": "success",
#   "comment": "Покупки оплачены"}
#
# Если денег не хватает ответ должен быть:
#   {"status": "fail",
#   "comment": "Недостаточно средств. Внесите n сумму денег"}
# n - количество денег, которое не хватает для оплаты всех товаров,
# корзина представляет собой список словарей с ключами: название, количество, стоимость.
def is_money_enough(cash: str, basket: list[dict]) -> dict[str: str]:
    cash = int(cash)
    required_amount: int = 0  # необходимая сумма для покупки
    for goods in basket:
        required_amount += (goods['price'] * goods['count'])

    if required_amount <= cash:
        return {"status": "success", "comment": "Покупки оплачены"}
    else:
        return {"status": "fail", "comment": f"Недостаточно средств. Внесите сумму в размере {required_amount - cash} денег"}


desires: list[dict] = [{'name': 'горошек', 'count': 3, 'price': 78},
                       {'name': 'яйца', 'count': 10, 'price': 95},
                       {'name': 'елка', 'count': 1, 'price': 600}]

print(is_money_enough('205', desires))