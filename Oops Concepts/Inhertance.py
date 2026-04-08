class Animal:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    
    def eat(self) -> None:
        print('I am eating.')
    
    def sleep(self) -> None:
        print('I am sleeping.')
    
class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)
        self.breed = breed
        
    def bark(self):
        print('I am barking.')
        
    def display(self) -> None:
        print(f'Name is {self.name}, age is {self.age} and breed is {self.breed}')
        

dog = Dog("Tommy", 3, "new breed")
dog.eat()
dog.display()
