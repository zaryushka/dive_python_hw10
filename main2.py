# Создайте класс прямоугольник. 
# Класс должен принимать длину и ширину при создании экземпляра. 
# У класса должно быть два метода, возвращающие периметр и площадь. 
# Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.

class Rectangle:
    def __init__(self, length, width=None):
        if not width:
            self.width = length
        else:
            self.width = width
        self.length = length

    def get_perimetr(self):
        return 2 * self.length + 2 * self.width

    def get_area(self):
        return self.length * self.width


rectagle = Rectangle(2)
print(rectagle.get_area())
print(rectagle.get_perimetr())