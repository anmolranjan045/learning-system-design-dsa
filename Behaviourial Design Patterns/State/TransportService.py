from Transport_mode import TransportMode

class TransportService:
    def __init__(self, mode: TransportMode):
        self.__mode = mode
        
    def eta(self):
        self.__mode.eta()
        
    def direction(self):
        self.__mode.direction()
        
    def update_mode(self, new_mode: TransportMode):
        self.__mode = new_mode