from Transport_mode import TransportMode

class WalkingMode(TransportMode):
    def eta(self):
        print('Eta for Walking is: 25min')
    
    def direction(self):
        print('Direct for Walking mode')