from observer import Observer

class TVDisplay(Observer):
    def __init__(self, temp):
        self.__temp = temp
        
    def update(self, newTemp):
        print(f'TV Temperature updated to {newTemp}')
        self.__temp = newTemp
        
    def get_temp(self) -> float:
        return self.__temp