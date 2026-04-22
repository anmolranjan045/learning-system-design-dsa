import time
from typing import List

class HighResolutionImage:
    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__image_data = None
        
        self.load_image()
    
    def display(self):
        print(f'{self.__file_name} has image data of {self.__image_data}.')
        
    def load_image(self):
        time.sleep(1)
        self.__image_data = f"[[Loaded image data of {self.__file_name}]]"
        print(f'Loaded {self.__file_name} from disk.')
        
class PhotoGallery:
    def __init__(self):
        self.__images: List[ImageProxy] = []
    
    def add_images(self, file_name: str):
        image_proxy = ImageProxy(file_name)
        self.__images.append(image_proxy)
        
    def display_images(self):
        for image in self.__images:
            image.display()
    
    def show_image(self, index: int):
        self.__images[index].display()
            

class ImageProxy:
    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__real_image = None
    
    def display(self):
        if self.__real_image is None:
            self.__real_image = HighResolutionImage(self.__file_name)
        self.__real_image.display()

gallery = PhotoGallery()
gallery.add_images('ABC.png')
gallery.add_images('QWE.png')
gallery.add_images('HJK.png')
gallery.add_images('UYT.png')

gallery.show_image(2)
gallery.show_image(2)
gallery.show_image(2)

gallery.display_images()