from abc import ABC, abstractmethod

class Devices(ABC):
    @abstractmethod
    def updateTemp(self, curTemp: float):
        pass