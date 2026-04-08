class Bank:
    def __init__(self, name: str, balance: float):
        self.name: str = name
        self.__balance: float= balance
    
    # getter and setter functions
    # __mentodName for defineing private variables
    def balance_get(self):
        print(f'current balance: {self.__balance}')
    
    def deposit(self, amount: float) -> None:
        self.__balance += amount
        print(f'Amount deposited {amount}, Current balance: {self.__balance}')
        
    def withdraw(self, amount: float) -> None:
        if(self.__balance < amount):
            print(f'Not enough balance, current balance {self.__balance}')
        else:
            self.__balance -= amount
            print(f'Amount withdrawn: {amount}, current balance: {self.__balance}')

account = Bank("Anmol", 1000)
account.withdraw(5000)
account.withdraw(500)
account.deposit(50000)
print(account.name, account.__balance)
    