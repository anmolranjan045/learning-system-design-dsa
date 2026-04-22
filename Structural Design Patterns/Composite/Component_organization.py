from abc import ABC, abstractmethod
from typing import List

class FileSystemComponent(ABC):
    @abstractmethod
    def show_details(self):
        pass
    
class File(FileSystemComponent):
    def __init__(self, name: str):
        self.__name = name
        
    def show_details(self):
        print(f'File details of {self.__name}')
    
class Folder(FileSystemComponent):
    def __init__(self, name: str):
        self.__name = name
        self.__files:List[FileSystemComponent] = []
        
    def add(self, file: FileSystemComponent):
        self.__files.append(file)
    
    def show_details(self):
        print(f'Folder details of {self.__name}')
        for file in self.__files:
            file.show_details()
            
file1 = File('image.png')
file2 = File('newMy.ppt')
file3 = File('FinalPre.doc')

folder = Folder('myDrive')
folder.add(file1)
folder.add(file2)

newFolder = Folder('Document')
newFolder.add(file3)

folder.add(newFolder)

folder.show_details()