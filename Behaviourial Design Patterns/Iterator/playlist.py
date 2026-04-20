from abc import ABC, abstractmethod
from typing import List

class Song:
    def __init__(self, song_title: str):
        self.__title = song_title
        
    def get_title(self):
        return self.__title
    
class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass
    
    @abstractmethod
    def next(self) -> Song|None:
        pass
        
class PlaylistIterator(Iterator):
    def __init__(self, song_list: List[Song]):
        self.__song_list: List[Song] = song_list
        self.__position = 0
    
    def has_next(self):
        if len(self.__song_list) > self.__position:
            return True
        return False
    
    def next(self) -> Song|None:
        if self.has_next() == True:
            song = self.__song_list[self.__position]
            self.__position += 1
            return song
        return None

class Playlist:
    def __init__(self):
        self.__playlist: List[Song] = []
    
    def add_song(self, song: Song):
        self.__playlist.append(song)
        
    def create_iterator(self):
        return PlaylistIterator(self.__playlist)
    
playlist = Playlist()
playlist.add_song(Song("Song1"))
playlist.add_song(Song("Song2"))
playlist.add_song(Song("Song3"))
playlist.add_song(Song("Song4"))

iterator = playlist.create_iterator()

while iterator.has_next():
    print(iterator.next().get_title())