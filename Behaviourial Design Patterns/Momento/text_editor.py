from text_memento import TextMemento

class TextEditor:
    def __init__(self) -> None:
        self.__text: str = ""
        
    def write(self, new_text: str):
        self.__text += new_text
    
    def get_text(self) -> str:
        return self.__text

    def save(self) -> TextMemento:
        return TextMemento(self.__text)
    
    def restore(self, tm: TextMemento):
        self.__text = tm.get_saved_text()