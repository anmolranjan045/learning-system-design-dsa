from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, newTemp: float) -> None:
        pass