from order import Order
from chef import Chef

class PastaOrder(Order):
    def __init__(self, chef: Chef):
        self.__chef = chef
        
    def execute(self):
        print('Pasta Order')
        self.__chef.cook_pasta()