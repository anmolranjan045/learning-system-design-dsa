from discount_strategy import DiscountStrategy

class HoliDiscount(DiscountStrategy):
    def calculate_discount(self):
        print(f'Holi discount is 10%')