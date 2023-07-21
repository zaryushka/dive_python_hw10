# 1) Создайте класс окружность. 
# Класс должен принимать радиус окружности при создании экземпляра. 
# У класса должно быть два метода, возвращающие длину окружности и её площадь

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circle_len(self):
        return 2 * math.pi * self.radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
c1 = Circle(5)

print(c1.circle_len())
print(c1.area())

c2 = Circle(10)

print(c2.circle_len())
print(c2.area())