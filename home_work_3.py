# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра.

import math

class Calculator:
    def __init__(self):
        pass

    def calc(self):
        
        while True:
            # получаем выбор пользователя
            operation = input("Выберите операцию: +, -, *, /, sin, cos, tan, log (десятичный), sqrt, quit: ").lower()

            if operation == 'quit':
                # выходим из цикла, если пользователь выбрал quit
                break

            if operation in ['sin', 'cos', 'tan', 'log', 'sqrt']:
                # если пользователь выбрал научную функцию
                num = float(input("Введите число: "))
                result = None

                if operation == 'sin':
                    result = math.sin(num)
                elif operation == 'cos':
                    result = math.cos(num)
                elif operation == 'tan':
                    result = math.tan(num)
                elif operation == 'log':
                    result = math.log(num, 10) # указала основание логарифма = 10
                elif operation == 'sqrt':
                    result = math.sqrt(num)

                print('Результат:', result)


            else:
                # если пользователь выбрал арифметическую операцию
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
                result = None

                if operation == '+':
                    result = num1 + num2
                elif operation == '-':
                    result = num1 - num2
                elif operation == '*':
                    result = num1 * num2
                elif operation == '/':
                    if num2 == 0:
                        print("Ошибка: деление на ноль")
                        continue
                    result = num1 / num2

                print('Результат:', result)

my_calc = Calculator()
my_calc.calc()


