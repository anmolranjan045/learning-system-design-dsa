from abc import ABC, abstractmethod

class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass

class Pizza(Food):
    def prepare(self):
        print('Preparing Pizza.')

class Pasta(Food):
    def prepare(self):
        print('Preparing Pasta.')

class FoodFactory:
    @staticmethod
    def create_food(food_type: str) -> Food|None:
        if food_type == "Pizza":
            return Pizza()
        elif food_type == "Pasta":
            return Pasta()
        else:
            print(f'Cannot prepare {food_type}')
            return None

class RestaurantService:
    def take_order(self, food_type: str):
        f = FoodFactory.create_food(food_type)
        f.prepare()
        return f
        
restaurant_service = RestaurantService()
print(restaurant_service.take_order('Pizza'))
print(restaurant_service.take_order('Pizza'))