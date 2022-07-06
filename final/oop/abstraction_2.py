from abc import ABCMeta, abstractmethod

class Shape(metaclass=ABCMeta):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b
        # pass

r1 = Rectangle(10, 12)
print(r1.area())