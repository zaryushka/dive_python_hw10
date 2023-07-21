# Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор. 
# У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор. 
# Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.

# Создайте класс Сотрудник. 
# Воспользуйтесь классом человека из прошлого задания. 
# У сотрудника должен быть:
# шестизначный идентификационный номер
# уровень доступа вычисляемый как остаток от деления суммы цифр id на семь

import random

class Person:
    def __init__(self, first_name, last_name, patronymic, age):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self._age = age

    def get_age(self):
        return self._age
    
    def birthday(self):
        self._age += 1

    def full_name(self):
        return f'{self.first_name} {self.last_name} {self.patronymic} {self._age} лет'

# user = Person('Иванов', 'Иван', 'Иванович', 45)
# print(user.full_name())
# user.birthday()
# print(user.full_name())

class Staff(Person):

    def __init__(self, first_name, last_name, patronymic, age, id):
        super().__init__(first_name, last_name, patronymic, age)
        if len(str(id)) == 6:
            self.id = id
        else:
            self.id = random.randint(100000, 1000000)

    def level(self):
        lev = sum(int(i) for i in str(self.id))
        level = lev % 7
        return level

user_1 = Staff('Харламов', 'Сергей', 'Владимирович', 40, 999999)
print(user_1.level())
print(user_1.full_name())


# решение Саши


# class Person(Human):

#     def __init__(self, first_name, second_name, last_name, age, id_us):
#         super().__init__(first_name, second_name, last_name, age)
#         if len(str(id_us)) == 6:
#             self.id_us = id_us
#         else:
#             self.id_us = rd(100000, 999999)



#     def sec_lev(self):
#         summ = sum(int(i) for i in str(self.id_us))
#         self.secu_level = summ % 7
#         return self.secu_level



# viniamin = Person('Козлов', 'Виньамин', 'Валерьевич', 31, 1111129)
# print(viniamin.full_print())
# print(viniamin.sec_lev())