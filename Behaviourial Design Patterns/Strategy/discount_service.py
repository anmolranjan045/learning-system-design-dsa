from discount_strategy import DiscountStrategy

class DiscountService:
    def __init__(self, discount_strategy: DiscountStrategy):
        self.__discount_strategy = discount_strategy
        
    def update(self, new_discount_strategy: DiscountStrategy):
        self.__discount_strategy = new_discount_strategy
    
    def process(self):
        self.__discount_strategy.calculate_discount()