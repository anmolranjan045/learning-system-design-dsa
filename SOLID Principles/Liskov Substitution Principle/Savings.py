from WithdrawableAccount import WithdrawableAccount

class Savings(WithdrawableAccount):
    def __init__(self, balance):
        super().__init__(balance)
        
    def withdraw(self, amount: float):
        if self._balance < amount:
            print(f'Insufficient balance, cannot withdraw {amount}')
        else:
            self._balance -= amount
            print(f'Successfully withdrawn amount {amount}, Remaining balance {self._balance}')
    
    def deposit(self, amount: float):
        self._balance += amount
        print(f'Successful deposited {amount}, current balance {self._balance}')