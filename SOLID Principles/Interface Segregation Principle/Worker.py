from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass
    
class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass
    
class Robot(Workable):
    def work(self):
        print('Robot is working')
    
class Worker(Workable, Eatable):
    def work(self):
        print('Worker is working')
    
    def eat(self):
        print('Worker is eating')
    
employee = Worker()
employee.eat()
employee.work()

r1 = Robot()
r1.work()