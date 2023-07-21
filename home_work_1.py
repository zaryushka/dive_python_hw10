# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.

class Factory:
    def _init__(self):
        pass

    def animal_types(self, animal_type, *args, **kwargs):
        if animal_type == 'fish':
            return Fish(*args, **kwargs)
        elif animal_type == 'dog':
            return Dog(*args, **kwargs)
        elif animal_type == 'animal':
            return Animal(*args, **kwargs)
        else:
            return 'Такого животного нет'


class Fish:
    def __init__(self, name, swim, action):
        self.name = name
        self.action = action
        self.swim = swim

    def swim_swim(self):
        return f'рыба {self.name} {self.swim}'

    def eat_eat(self):
        return f'рыба {self.name} ест сырое мясо'
    
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
    
# class Factory(Fish):
#     def __init__(self, name, swim, action):
#         super().__init__(name, swim, action)
        

# factory_1 = Factory('Флаундер', 'плавает как ракета', 'самый позитивный персонаж')
# print(factory_1.swim_swim())
# print(factory_1.eat_eat())
# print(factory_1.action_action())


factory = Factory()
fish = factory.animal_types('fish', 'Немо', 'плавает как дельфин', 'ведет активный образ жизни')
print(fish.swim_swim())
print(fish.eat_eat())
print(fish.action_action())

dog = factory.animal_types('dog', 'Рекс', 'виляет хвостом', 'гав-гав')
print(dog.sound_sound())