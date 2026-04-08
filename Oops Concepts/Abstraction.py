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
        
        
rec = Rectangle(2, 10)
shape = Shape()