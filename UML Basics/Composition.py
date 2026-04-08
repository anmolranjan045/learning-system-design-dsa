class Engine:
    def __init__(self, engine_type: str, horse_power: int) -> None:
        self.__engine_type = engine_type
        self.__horse_power = horse_power
    
    def get_details(self) -> str:
        return f'Engine: {self.__engine_type} & Horse Power: {self.__horse_power}'
    
    def start(self) -> None:
        print(f'{self.__engine_type} has started.')

class Car:
    def __init__(self, brand: str, model: str, engine_type: str, horse_power: int):
        self.__brand: str = brand
        self.__model: str = model
        
        # COMPOSITION: Engine is created inside the Car constructor
        self.__engine = Engine(engine_type, horse_power)
    
    def get_car_details(self) -> None:
        print(f'Car: {self.__brand}, {self.__model}')
        print(f'Engine: {self.__engine.get_details()}')
    
    def start_car(self) -> None:
        print(f'Starting car {self.__brand} {self.__model}')
        self.__engine.start()
        print('Car is ready to drive.')
        
myCar = Car('Toyota', 'Fortuner', 'Desiel', 204)
myCar.get_car_details()
myCar.start_car()

del myCar