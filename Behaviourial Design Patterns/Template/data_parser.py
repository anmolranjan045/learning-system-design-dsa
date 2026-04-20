from abc import ABC, abstractmethod

class DataParser(ABC):
    def __init__(self, file_name: str):
        self.__file = file_name
        
    def _open(self):
        print(f'Opening the file: {self.__file}')
        
    def _close(self):
        print(f'Closing the file: {self.__file}')
    
    def _parse(self):
        self._open()
        self._data_parser()
        self._close()
        
    @abstractmethod
    def _data_parser(self):
        pass
    
    
class CSVParser(DataParser):
    def _data_parser(self):
        print(f'Parsing CSV file.')
        
csv = CSVParser('Design')
csv._parse()