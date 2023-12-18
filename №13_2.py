# 2. Создайте декоратор, который ограничивает доступ к функции определенным типам пользователей. Предполагается, что тип
#    пользователя будет передаваться в качестве аргумента user_type(str) в декорируемую функцию.
#    Типы пользователей: "admin", "user", "auth_user".
#    Результат должен быть вида: "access", если разрешен "denied", если нет.
def access_validation(func) -> str:
    ...
    greeting()


@access_validation
def greeting(user_type: str) -> None:
    print('Hello world')
    ...


