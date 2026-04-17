from discount_strategy import DiscountStrategy

class DiwaliDiscount(DiscountStrategy):
    def calculate_discount(self):
        print(f'Diwali discount is 20%')