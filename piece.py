from random import choice

class Piece:
    def __init__(self, game, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.number_moves = 0
        self.game = game
        self.alive = True
        self.valid_moves = self.find_valid_moves(self.game.board)

    def move(self, board):
        valid_moves = self.find_valid_moves(board)
        m = choice(valid_moves)
        self.game.board[self.y, self.x] = 0 # empty current square
        if self.game.board[m] != 0:
            self.game.board[m].alive = False
        self.y, self.x = m
        self.game.board[self.y, self.x] = self # move to next square
        self.number_moves += 1
        return self.game.board
    

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
                if board[self.y+1, self.x+i].color != self.color:
                    valid_moves.append((self.y+1, self.x+i))
            except (IndexError, AttributeError):
                pass
        return valid_moves

    
class Rook(Piece):
    def __init__(self, game, color, x, y):
        self.value = 5
        super().__init__(game, color, x, y)
        
    def find_valid_moves(self, board):
        valid_moves = list()
        directions = [(0,1),(0,-1), (1,0),(-1,0)]
        for direction in directions:
            number_of_squares = 1
            while True:
                y = self.y + number_of_squares*direction[0]
                x = self.x + number_of_squares*direction[1]
                try:
                    if board[y,x] == 0: # Move to Empty Square
                        valid_moves.append((y,x))
                        number_of_squares += 1
                    elif board[y,x].color != self.color: # Take opposing piece
                        valid_moves.append((y,x))
                        break
                    else:
                        break
                except IndexError:
                    pass
        return valid_moves

class Knight(Piece):
    def __init__(self, game, color, x, y):
        self.value = 3
        super().__init__(game, color, x, y)
        
    def find_valid_moves(self, board):
        valid_moves = list()
        options = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
        for option in options:
            y, x = option
            try:
                if board[self.y + y, self.x + x] == 0 or board[self.y + y, self.x + x].color != self.color:
                    valid_moves.append((y,x))
            except IndexError:
                pass
        return valid_moves
    
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