class Student:
    def __init__(self, name: str, roll_no: int, cgpa: int) -> None:
        self.__name :str = name
        self.__roll_no :int = roll_no
        self.__cgpa :int = cgpa
    
    def get_name(self) -> str:
        return self.__name
    
class Teacher:
    def __init__(self, name: str) -> None:
        self.__name :str = name
    
    def get_name(self) -> str:
        return self.__name
    
    def teach(self, stu: Student) -> None:
        print(f'{self.__name} is teaching {stu.get_name()}')
        
student = Student("Anmol", 11, 8.4)
teacher = Teacher("Prabhat")

teacher.teach(student)