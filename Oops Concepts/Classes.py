from enum import Enum

class Gender(Enum):
    MALE = "male"
    FEMALE = "female"

class Student:
    def __init__(self, name: str, age: int, address: str, gender: Gender) -> None:
        self.name = name
        self.age = age
        self.address = address
        self.gender = gender
    
    def set_info(self) -> None:
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.address = input("Enter your address: ")
        self.gender = input("Enter your gender: ")
    
    def display(self) -> None:
        print(f"My name is {self.name}, age is {self.age}, gender is {self.gender}")
        
    def get_age(self) -> int:
        return self.age

s1 = Student("Anmol", 24, "Bengaluru", Gender.MALE)
print(s1.get_age())
s1.display()