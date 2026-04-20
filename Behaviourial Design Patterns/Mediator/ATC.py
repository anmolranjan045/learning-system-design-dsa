from abc import ABC, abstractmethod

class AirTrafficControl(ABC):
    @abstractmethod
    def register_airplane(self, airplane):
        pass

    @abstractmethod
    def send_message(self, msg: str, sender):
        pass