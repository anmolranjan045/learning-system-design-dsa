from WeatherStation import WeatherStation
from TV import TVDisplay
from Mobile import MobileDisplay


ws = WeatherStation()
tv = TVDisplay(ws.get_temperature())

print(f'Current Weather Station temperature: {ws.get_temperature()}')
ws.add_observer(tv)
ws.update_temperature(24)

mb = MobileDisplay(ws.get_temperature())
ws.add_observer(mb)
ws.update_temperature(30)