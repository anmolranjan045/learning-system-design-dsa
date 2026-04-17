from observer import Observer

class MobileDisplay(Observer):
    def __init__(self, temp):
        self.__temp = temp
        
    def update(self, newTemp):
        print(f'Mobile Temperature updated to {newTemp}')
        self.__temp = newTemp
        
    def get_temp(self) -> float:
        return self.__temp