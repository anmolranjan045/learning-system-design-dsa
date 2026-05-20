from Device import Devices

class Phone(Devices):
    def __init__(self, temp: float):
        self.__devTemp = temp
        
    def display_temperature(self):
        print(f'Temperature on the Phone is {self.__devTemp}')
    
    def getTemp(self) -> float:
        return self.__devTemp

    def updateTemp(self, newTemp: float):
        self.__devTemp = newTemp