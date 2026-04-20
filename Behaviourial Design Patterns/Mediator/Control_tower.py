from typing import List
from ATC import AirTrafficControl
from Airplane import Airplane

class ControlTower(AirTrafficControl):
    def __init__(self):
        self.__airplanes: List[Airplane] = []

    def register_airplane(self, new_airplane: Airplane):
        if new_airplane not in self.__airplanes:
            self.__airplanes.append(new_airplane)

    def send_message(self, msg: str, sender: Airplane):
        for airplane in self.__airplanes:
            if airplane != sender:
                airplane.receive_message(msg, sender)