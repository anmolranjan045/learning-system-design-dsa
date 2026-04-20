class Logger:
    __instance = None
    
    def __new__(cls, filename: str):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__filename = filename
            cls.__instance.__log_count = 0
            return cls.__instance
        else:
            return cls.__instance
    
    def get_filename(self) -> str:
        return self.filename
    
    def log(self, msg: str) -> None:
        print(f'Logging: {msg} to {self.__filename}')
        self.__log_count += 1
        
    def get_log_count(self) -> int:
        return self.__log_count
        
logs1 = Logger('app.log')
logs1.log('Saving to Apps logs.')

logs2 = Logger('app.log')
logs2.log('Saving to Apps logs.')
print(logs2)

print(logs2.get_log_count())
print(logs1.get_log_count())