from Device import Devices
from typing import List

class WeatherStation:
    def __init__(self):
        self.__devices: List[Devices] = []
        self.__curTemp: float = 0.0
    
    def getCurTemp(self) -> float:
        return self.__curTemp
    
    def addNewDevice(self, device: Devices) -> None:
        self.__devices.append(device)
        
    def removeDevice(self, device: Devices) -> None:
        try:
            self.__devices.remove(device)
        except:
            print('Device not registered')
    
    def updateTemp(self, newTemp: float) -> None:
        self.__curTemp = newTemp
        self.__notifyDevices()
        
    
    def __notifyDevices(self) -> None:
        for d in self.__devices:
            d.updateTemp(self.__curTemp)