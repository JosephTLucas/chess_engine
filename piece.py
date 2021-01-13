from random import choice

class Piece:
    def __init__(self, game, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.number_moves = 0
        self.game = game
        self.valid_moves = self.find_valid_moves(self.game.board)
    

class Pawn(Piece):
    def __init__(self, game, color, x, y):
        self.value = 1
        super().__init__(game, color, x, y)
        
    def find_valid_moves(self, board):
        valid_moves = list()
        # With their first move, a pawn can move forward one or two
        if self.number_moves == 0:
            # Pawns are the only piece with restricted directionality (can only move forward)
            if self.color == "white":
                direction = 1
            else:
                direction = -1
            for i in (1,2):
                # Square must be empty
                if board[self.y + direction*i, self.x] == 0:
                    valid_moves.append((self.y + direction*i, self.x))
        # A pawn can take a piece one square on the forward diagonal
        for i in (-1,1):
            try:
                if board[self.y+1, self.x+i] != 0:
                    valid_moves.append((self.y+1, self.x+i))
            except IndexError:
                pass
        return valid_moves

    def move(self, board):
        valid_moves = self.find_valid_moves(board)
        m = choice(valid_moves)
        self.game.board[self.y, self.x] = 0 # empty current square
        self.y, self.x = m
        self.game.board[self.y, self.x] = self # move to next square
        self.number_moves += 1
        return self.game.board
    
class Rook(Piece):
    def __init__(self, game, color, x, y):
        self.value = 5
        super().__init__(game, color, x, y)
        
    def find_valid_moves(self, board):
        return

class Knight(Piece):
    def __init__(self, game, color, x, y):
        self.value = 3
        super().__init__(game, color, x, y)
        
    def find_valid_moves(self, board):
        return
    
class Bishop(Piece):
    def __init__(self, game, color, x, y):
        self.value = 3
        super().__init__(game, color, x, y)
        
    def find_valid_moves(self, board):
        return
    
class Queen(Piece):
    def __init__(self, game, color, x, y):
        self.value = 9
        super().__init__(game, color, x, y)
        
    def find_valid_moves(self, board):
        return

class King(Piece):
    def __init__(self, game, color, x, y):
        self.value = 100
        super().__init__(game, color, x, y)
        
    def find_valid_moves(self, board):
        return