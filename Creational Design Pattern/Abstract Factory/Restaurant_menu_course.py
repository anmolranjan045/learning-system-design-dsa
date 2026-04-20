from abc import ABC, abstractmethod

class Starter(ABC):
    @abstractmethod
    def prepare(self):
        pass

class MainCourse(ABC):
    @abstractmethod
    def prepare(self):
        pass
    
class Dessert(ABC):
    @abstractmethod
    def prepare(self):
        pass


# ============= NORTH INDIAN DISHES =============


class PaneerTikka(Starter):
    def prepare(self):
        print("Preparing Paneer Tikka (North Indian Starter)")


class ButterChicken(MainCourse):
    def prepare(self):
        print("Preparing Butter Chicken (North Indian Main Course)")


class GulabJamun(Dessert):
    def prepare(self):
        print("Preparing Gulab Jamun (North Indian Dessert)")


# ============= SOUTH INDIAN DISHES =============


class MeduVada(Starter):
    def prepare(self):
        print("Preparing Medu Vada (South Indian Starter)")


class Dosa(MainCourse):
    def prepare(self):
        print("Preparing Dosa (South Indian Main Course)")


class Payasam(Dessert):
    def prepare(self):
        print("Preparing Payasam (South Indian Dessert)")


# ============= CHINESE DISHES =============


class SpringRolls(Starter):
    def prepare(self):
        print("Preparing Spring Rolls (Chinese Starter)")


class FriedRice(MainCourse):
    def prepare(self):
        print("Preparing Fried Rice (Chinese Main Course)")


class FortuneCookie(Dessert):
    def prepare(self):
        print("Preparing Fortune Cookie (Chinese Dessert)")
        
class CuisineFactory(ABC):
    @abstractmethod
    def prepare_starter(self):
        pass
    
    @abstractmethod
    def prepare_main_course(self):
        pass
    
    @abstractmethod
    def prepare_dessert(self):
        pass

class NorthIndianCuisine(CuisineFactory):
    def prepare_starter(self):
        return PaneerTikka()
    
    def prepare_main_course(self):
        return ButterChicken()
    
    def prepare_dessert(self):
        return GulabJamun()
    
class SouthIndianCuisine(CuisineFactory):
    def prepare_starter(self):
        return MeduVada()
    
    def prepare_main_course(self):
        return Dosa()
    
    def prepare_dessert(self):
        return Payasam()
    
class ChineseCuisine(CuisineFactory):
    def prepare_starter(self):
        return SpringRolls()
    
    def prepare_main_course(self):
        return FriedRice()
    
    def prepare_dessert(self):
        return FortuneCookie()
    
class RestaurantService:
    def __init__(self, factory: CuisineFactory):
        self.__factory = factory
    
    def create_meal(self):
        starter = self.__factory.prepare_starter()
        main_course = self.__factory.prepare_main_course()
        dessert = self.__factory.prepare_dessert()
        
        starter.prepare()
        main_course.prepare()
        dessert.prepare()
    
    def change_cuisine(self, new_cuisine: CuisineFactory):
        self.__factory = new_cuisine
                

north_indian = NorthIndianCuisine()
r = RestaurantService(north_indian)
r.create_meal()

south_indian = SouthIndianCuisine()
r.change_cuisine(south_indian)
r.create_meal()