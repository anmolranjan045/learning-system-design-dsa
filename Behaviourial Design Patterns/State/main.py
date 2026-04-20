from Bike_mode import BikeMode
from Walking import WalkingMode

from TransportService import TransportService

bike = BikeMode()
ds = TransportService(bike)
ds.eta()
ds.direction()

walk = WalkingMode()
ds.update_mode(walk)
ds.eta()
ds.direction()
