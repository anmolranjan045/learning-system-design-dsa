from observer import Observer
from typing import List

class WeatherStation:
    def __init__(self) -> None:
        self.__temperature: float = 0
        self.__observers: List[Observer] = []
    
    def get_temperature(self) -> float:
        return self.__temperature
        
    def update_temperature(self, newTemp: float) -> None:
        self.__temperature = newTemp
        self.__notify_observers()
        
    def add_observer(self, obs: Observer) -> None:
        self.__observers.append(obs)
        
    def remove_observer(self, ob: Observer) -> None:
        self.__observers.remove(ob)
        
    def __notify_observers(self):
        for obs in self.__observers:
            obs.update(self.__temperature)