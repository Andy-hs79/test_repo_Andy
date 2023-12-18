# 1. Создайте простой калькулятор, который считывает из строки ввода(пример: «1 + 13» три подстроки:
#    1-ое число, 2-ое число и операцию, после чего применяет операцию к введённым числам, а затем выводит
#    результат на экран.

str_number1 = input("Введите первое число a: ")
str_number2 = input("Введите второе число b: ")
oper = input("Введите операцию (+, -, *, /, **): ")

if "." in str_number1 or "." in str_number2:
    number1, number2 = float(str_number1), float(str_number2)
else:
    number1, number2 = int(str_number1), int(str_number2)

if oper == "/" and number2 != 0:
    print(number1, '/', number2, '=', number1 / number2)
elif oper == "/" and number2 == 0:
    print("Деление на 0")
if oper == "+":
    print(number1, '+', number2, '=', number1 + number2)
elif oper == "-":
    print(number1, '-', number2, '=', number1 - number2)
elif oper == "*":
    print(number1, '*', number2, '=', number1 * number2)
elif oper == "**":
    print(number1, '**', number2, '=', number1 ** number2)



