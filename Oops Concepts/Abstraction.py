from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    
# Concrete classes
class Rectangle(Shape):
    def __init__(self, length: float, breadth: float):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        print(f'Area is {self.length * self.breadth}')
        
    def perimeter(self):
        print(f'Perimeter is {2 * self.length * self.breadth}')
        
class Circle(Shape):
    __pi : float = 3.14
    def __init__(self, radius: float) -> None:
        self.radius = radius
     
    def area(self) -> None:
        print(f'The area of the circle is {self.__pi * self.radius * self.radius}')
    
    def perimeter(self) -> None:
        print(f'Perimeter of the circle is {2 * self.__pi * self.radius}')

rec = Rectangle(2, 10)
circle = Circle(7)

circle.area()
# shape = Shape()