# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра.

import csv

class Phonebook:
    def __init__(self):
        self.phonebook = []

    # показать все контакты
    def print_result(self):
        if len(self.phonebook) == 0:
            print('Список контатков пуст')
        else:
            for contact in self.phonebook:
                print(contact)

    # поиск контакта по фамилии
    def search_name(self, last_name):
        result = []
        for contact in self.phonebook:
            if contact[0].lower() == last_name.lower():
                result.append(contact)
        if len(result) == 0:
            print('Контакт с фамилией', last_name.title(), 'не найден')
        else:
            print(*result)


    # поиск контакта по номеру
    def search_number(self, number):
        result = []
        for contact in self.phonebook:
            if number in str(contact[2]):
                result.append(contact)
        if len(result) == 0:
            print('Контакт с номером', number, 'не найден')
        else:
            print(*result)

    # добавить контакт
    def add_contact(self):
        last_name = input('Введите фамилию: ').title()
        name = input('Введите имя: ').title()
        number = input('Введите номер телефона: ')
        self.phonebook.append([last_name, name, number])
        print(*self.phonebook, sep='\n')


    # удалить контакт
    def del_contatct(self):
        last_name = input('Введите фамилию: ')
        for contact in self.phonebook:
            if contact[0].lower() == last_name.lower():
                self.phonebook.remove(contact)
                print('Контакт удален')
                return True
        print('Контакт не найден')
        return False
            

    # сохранить справочник в файл
    def save_file(self):
        file_name = input('Введите имя файла: ')
        with open(file_name, 'a', encoding='utf-8') as file:
            for contact in self.phonebook:
                file.write(contact[0] + ' ' + contact[1] + ' ' + contact[2] + '\n')


    # загрузить справочник из файла
    def load_file(self):
        with open('phonebook.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                self.phonebook.append(row)
                print(row)


    # основное меню, бесконечный цикл
    def main_menu(self):
        while True:
            print('1. Показать все контакты')
            print('2. Поиск контакта по фамилии')
            print('3. Поиск контакта по номеру')
            print('4. Добавить контакт')
            print('5. Удалить контакт')
            print('6. Сохранить справочник в файл')
            print('7. Загрузить справочник из файла')
            print('8. Выход')
            choice = int(input('Выберите пункт меню: '))
            if choice == 1:
                self.print_result()
            elif choice == 2:
                self.search_name(input('Введите фамилию: '))
            elif choice == 3:
                self.search_number(input('Введите номер телефона: '))
            elif choice == 4:
                self.add_contact()
            elif choice == 5:
                self.del_contatct()
            elif choice == 6:
                self.save_file()
            elif choice == 7:
                self.load_file()
            elif choice == 8:
                break
            else:
                print('Некорректный ввод')

my_phonebook = Phonebook()
my_phonebook.main_menu()