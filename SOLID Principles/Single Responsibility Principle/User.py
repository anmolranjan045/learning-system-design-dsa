class User:
    def __init__(self, name: str, age: int, email: str) -> None:
        self.__name = name
        self.__age = age
        self.__email = email
        
    def get_user_details(self) -> str:
        return f'User Name: {self.__name}, User Age: {self.__age}'
        
    def isAdult(self) -> bool:
        return self.__age > 18
