from Control_tower import ControlTower
from Airplane import Airplane

control_tower = ControlTower()
air_india = Airplane("AIR-546", control_tower)
spicejet = Airplane("SPICE-87171", control_tower)
indigo = Airplane("IND-9911", control_tower)

air_india.send_message("I am getting on runway")

express = Airplane("EXP-1122", control_tower)
express.send_message("I am getting on runway")