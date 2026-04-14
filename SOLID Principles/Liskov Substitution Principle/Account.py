from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, balance: float) -> None:
        self._balance = balance
        
    @abstractmethod
    def deposit(self, amount: float):
        pass