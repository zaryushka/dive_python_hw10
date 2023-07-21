# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

# Доработайте задачу 5. Вынесите общие свойства и методы классов в класс Животное. 
# Остальные классы наследуйте от него. Убедитесь, что в созданные ранее классы внесены правки.

class Fish:
    def __init__(self, name, swim, action, sound='unknow'):
        # такая запись обязательно, для того, чтобы параметр, попавший в метод инициализации, переместился в атрибут экземпляра класса
        # слева атрибут экземпляра класса, справа параметр
        self.name = name
        self.action = action
        self.swim = swim
        self.sound = sound

# методы экземпляров класса
    def swim_swim(self):
        return f'рыба {self.name} {self.swim}'

# методы экземпляров класса
    def eat_eat(self):
        return f'рыба {self.name} ест сырое мясо'
    
# методы экземпляров класса
    def action_action(self):
        return f'рыба {self.name} {self.action}'
    
class Animal:
    def __init__(self, name, action):
        self.name = name
        self.action = action
    def any_actions(self):
        return f'животное {self.name} {self.action}'    

class Dog(Animal):
    def __init__(self, name, action, sound):
        super().__init__(name, action)
        self.sound = sound

    def sound_sound(self):
        return f'{self.name} издает звук {self.sound}'
    

nemo = Fish('Немо', 'плавает как дельфин', 'ведет активный образ жизни')
# здесь вызываем конкретный метод данного экземпляра
print(nemo.swim_swim())
print(nemo.action_action())
print(nemo.eat_eat())

# обращение к атибутам данного экземпляра
print(f'{nemo.swim = }')
print(f'{nemo.name = }')
print(f'{nemo.action = }')
print(f'{nemo.sound = }')


bear = Animal('Борис', 'спит')
print(bear.any_actions())

rex = Dog('Рекс', 'виляет хвостом', 'гав-гав')
print(rex.sound_sound())

