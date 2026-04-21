from abc import ABC, abstractmethod

class Beverage(ABC):
    @abstractmethod
    def description(self) -> str:
        pass
    
    @abstractmethod
    def get_cost(self) -> float:
        pass
    
class Coffee(Beverage):
    def description(self) -> str:
        return "Plain Coffee"
    
    def get_cost(self) -> float:
        return 20.0
    
class AddOnDecorator(Beverage):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def description(self) -> str:
        pass
    
    def get_cost(self) -> float:
        pass
    
class MilkDecorator(AddOnDecorator):
    def description(self) -> str:
        return self._coffee.description() + ', Milk'
    
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 20.0

class WipCreamDecorator(AddOnDecorator):
    def description(self) -> str:
        return self._coffee.description() + ', Wipped Cream'
    
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 50.0

class SugarDecorator(AddOnDecorator):
    def description(self) -> str:
        return self._coffee.description() + ', Sugar'
    
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 5.0
    

coffee = Coffee()
coffee = MilkDecorator(coffee)
coffee = SugarDecorator(coffee)
print(coffee.description())
print(coffee.get_cost())