class TextMemento:
    def __init__(self, text: str):
        self.__saved_text: str = text
        
    def get_saved_text(self) -> str:
        return self.__saved_text