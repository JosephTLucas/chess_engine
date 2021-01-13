import numpy as np
from piece import Piece, Pawn, Rook, Knight, Bishop, Queen, King

class Game:
    def __init__(self):
        self.board = np.zeros_like([], dtype=Piece, shape=[8,8])
        self.black = list()
        self.white = list()
        self.setup()
        
        
    def setup(self):
        for i in range(8):
            self.white.append(Pawn(self, "white", i, 1))
            self.black.append(Pawn(self, "black", i, 6))
        for i in [0,7]:
            self.white.append(Rook(self, "white", i, 0))
            self.black.append(Rook(self, "black", i, 7))
        for i in [1,6]:
            self.white.append(Knight(self, "white", i, 0))
            self.black.append(Knight(self, "black", i, 7))
        for i in [2,5]:
            self.white.append(Bishop(self, "white", i, 0))
            self.black.append(Bishop(self, "black", i, 7))
        self.white.append(Queen(self, "white", 3, 0))
        self.black.append(Queen(self, "black", 3, 7))
        self.white.append(King(self, "white", 4, 0))
        self.black.append(King(self, "black", 4, 7))
        for i in self.black+self.white:
            self.board[i.y, i.x] = i
    
    def move(self):
        for x in self.white:
            if type(x) is Pawn:
                self.board = x.move(self.board)
        return