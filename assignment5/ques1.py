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

r = rectangle(3, 5)
print("area of rectangle = ", r.area())
s = square(8)
print("area of square=", s.area())
t = triangle(5, 7)
print("area of triangle = ", t.area())
