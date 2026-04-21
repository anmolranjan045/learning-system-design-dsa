from typing import List
import copy

class ChessPieces:
    def __init__(self, color: str, name: str, position: str) -> None:
        self.__color = color
        self.__name = name
        self.__position = position
    
    def display_piece(self) -> None:
        print(f'{self.__color} {self.__name} is at {self.__position}')
        
    def make_copy(self) -> 'ChessPieces':
        return copy.deepcopy(self)
    
class ChessBoard:
    def __init__(self) -> None:
        self.__board: List[ChessPieces] = []
        
    def add_pieces(self, piece: ChessPieces) -> None:
        self.__board.append(piece)
        
    def display_board(self):
        print("\nBoard State")
        for piece in self.__board:
            piece.display_piece()
    
    def make_copy(self) -> 'ChessBoard':
        return copy.deepcopy(self)
    

board = ChessBoard()
p1 = ChessPieces('Black', 'King', 'A5')
p2 = ChessPieces('Black', 'Queen', 'A6')
p3 = ChessPieces('White', 'King', 'G5')
p4 = ChessPieces('White', 'Queen', 'G6')

board.add_pieces(p1)
board.add_pieces(p2)
board.add_pieces(p3)
board.add_pieces(p4)

board.display_board()

new_board = board.make_copy()

new_board.add_pieces(ChessPieces('Black', 'Knight', 'A2'))

board.display_board()

new_board.display_board()