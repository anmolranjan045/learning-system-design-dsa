from Account import Account

class FixedDeposit(Account):
    def __init__(self, balance: float):
        return super().__init__(balance)
    
    def deposit(self, amount: float) -> None:
        self._balance += amount
        print(f'Amount Deposited in FD {amount}, current balance {self._balance}')
    