from WeatherStation import WeatherStation
from Phone import Phone

ws = WeatherStation()
phone = Phone(ws.getCurTemp())
ws.addNewDevice(phone)

phone.display_temperature()

ws.updateTemp(98.0)

phone.display_temperature()