from Transport_mode import TransportMode

class BikeMode(TransportMode):
    def eta(self):
        print('Eta for Bike is: 10min')
    
    def direction(self):
        print('Direct for bike mode')