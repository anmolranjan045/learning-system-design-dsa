from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass
    
class UPIPayment(PaymentMethod):
    def pay(self, amount: float):
        print(f'Payment using UPI amount {amount}')
    
class CreditCard(PaymentMethod):
    def pay(self, amount: float):
        print(f'Payment using Credit Card amount {amount}')
    
class NetBanking(PaymentMethod):
    def pay(self, amount: float):
        print(f'Payment using Net Banking amount {amount}')
    
class ProcessPayment:
    def make_payment(self, amount: float, payment_method: PaymentMethod):
        payment_method.pay(amount)

cc = CreditCard()
nb = NetBanking()
pp = ProcessPayment()
pp.make_payment(1000, cc)
pp.make_payment(5000, nb)
