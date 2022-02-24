from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def get(self, name):
        self.name = name
        return name
    
class rectangle(Shape):
   def __init__(self, x,y):
      self.l = x
      self.b=y
   def area(self):
      return self.l*self.b


class square(Shape):
    def __init__(self, x):
        self.x = x

    def area(self):

        return self.x * self.x
    
class triangle(Shape):
    def __init__(self, h, b):
        self.h = h
        self.b = b

    def area(self):
        return 1/2 * self.h * self.b
h = int(input("enter the height of rectangle = "))
w = int(input("enter the width of the rectangle = "))
r = rectangle(h, w)
print("area of rectangle = ", r.area())
side = int(input("enter the side of the square = "))
s = square(side)
print("area of square=", s.area())
base = int(input("enter the base of the triangle = "))
height = int(input("enter the height of the triangle = "))
t = triangle(base, height)
print("area of triangle = ", t.area())
