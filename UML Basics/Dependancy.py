class Document:
    def __init__(self, title: str, content: str, pages: int) -> None:
        self.__title: str = title
        self.__content: str = content
        self.__pages: int = pages
        
    def get_title(self) -> str:
        return self.__title
    
    def get_content(self) -> str:
        return self.__content

    def get_pages(self) -> int:
        return self.__pages
    
    
class Printer:
    def __init__(self, name: str, type: str) -> None:
        self.__printer_type: str = type
        self.__printer_name: str = name
    
    def print_document(self, document: Document) -> None:
        print(f'Printer Name: {self.__printer_name}, Printer Type: {self.__printer_type}')
        print(f'Printing Document: {document.get_title()}, Printing Pages: {document.get_pages()}')
        print(f'Printing: {document.get_content()}')
        print('Printing Complete')
        
    def get_printer_details(self) -> None:
        print(f'{self.__printer_name} {self.__printer_type}')


document: Document = Document(
    title = 'Python Tutorial',
    content = 'This is python tutorial content.',
    pages = 130,
)

office_printer: Printer = Printer(
    "HP LaserJet", "Laser Printer"
)

office_printer.print_document(document)