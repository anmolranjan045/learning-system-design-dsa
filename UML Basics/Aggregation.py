class Student:
    def __init__(self, name: str, roll_no: int):
        self.__name = name
        self.__roll_no = roll_no
    
    def get_name(self):
        return self.__name
    
    def get_roll_no(self):
        return self.__roll_no

# Department class contains students: Aggregation
class Department:
    def __init__(self, name: str):
        self.__dept_name :str = name
        self.__students :List[Student] = []
        
    def add_students(self, student: Student):
        self.__students.append(student)
    
    def show_student(self):
        print(f'Student in {self.__dept_name} are: ')
        for s in self.__students:
            print(f'{s.get_name()} Roll No. {s.get_roll_no()}')

dept: Department = Department('Physics')
student1: Student = Student('Anmol', 12)
student2: Student = Student('Rahul', 23)
student3: Student = Student('Krish', 34)

# dept.show_student()
dept.add_students(student1)
dept.show_student()
dept.add_students(student2)
dept.add_students(student3)
dept.show_student()

# if the container class is deleted the contained class is still there
del dept

print(student1.get_name())