from ATC import AirTrafficControl

class Airplane:
    def __init__(self, flight_number: str, tower: AirTrafficControl):
        self.__flight_number = flight_number
        self.__tower = tower
        # Register via the interface, not the concrete tower
        self.__tower.register_airplane(self)

    def send_message(self, msg: str):
        self.__tower.send_message(msg, self)

    def get_flight_number(self) -> str:
        return self.__flight_number

    def receive_message(self, msg: str, who_sent: "Airplane"):
        print(f"{self.__flight_number} got '{msg}' from {who_sent.get_flight_number()}")