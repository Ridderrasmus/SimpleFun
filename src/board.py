from constants import *
from gameobjects import *

class Board:
    """The game board for tic tac toe.

    Returns:
        Board: A game board for tic tac toe
    """    
    
    players = []
    square_layout = 3
    board_squares = []
    board_width = 0
    board_height = 0
    btn_size = 0
    
    curr_player = None
    
    def __init__(self, players, board_start_pos: tuple|Pos, board_end_pos: tuple|Pos, btn_size: int):
        
        self.players = players
        self.curr_player = players[0]
        
        if type(board_start_pos) == tuple:
            board_start_pos = Pos(board_start_pos[0], board_start_pos[1])
        
        if type(board_end_pos) == tuple:
            board_end_pos = Pos(board_end_pos[0], board_end_pos[1])
            
        self.board_width = board_end_pos.x - board_start_pos.x
        self.board_height = board_end_pos.y - board_start_pos.y
            
        self.btn_size = btn_size
        
        self.create_squares()
        
    
    def __init__(self, players, board_size: tuple|int, btn_size: int):
        
        self.players = players
        self.curr_player = players[0]
        
        if type(board_size) == tuple:
            self.board_width = board_size[0]
            self.board_height = board_size[1]
        else:
            self.board_width = board_size
            self.board_height = board_size
            
        self.btn_size = btn_size
        
        self.create_squares()
        
    def loop(self, screen):
        ### Event loop ###
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.make_move()
                    
            ### Draw BG ###
            screen.fill(BG_COLOUR)
            
            ### Draw screen ###
            gameboard.draw(screen)
    
    def create_squares(self):
        for x in (range(self.square_layout)):
            for y in (range(self.square_layout)):
                this_pos = Pos((x * self.btn_size) + BOARD_PADDING*(1+x), (y * self.btn_size) + BOARD_PADDING*(1+y))
                self.board_squares.append(Button(this_pos, (self.btn_size, self.btn_size), (BG_COLOUR[0], BG_COLOUR[1], BG_COLOUR[2] + 20)))
    
    def check_win(self) -> int:
        square_symbols = [square.symbol for square in self.board_squares]
        
        # Check horizontal
        for i in range(self.square_layout):
            offset = i * self.square_layout
            if square_symbols[offset] == square_symbols[offset+1] == square_symbols[offset+2] != " ":
                return 1
        
        # Check vertical
        for i in range(self.square_layout):
            if square_symbols[i] == square_symbols[i+3] == square_symbols[i+6] != " ":
                return 1
            
        # Check diagonal
        if square_symbols[0] == square_symbols[4] == square_symbols[8] != " ":
            return 1
        elif square_symbols[2] == square_symbols[4] == square_symbols[6] != " ":
            if square_symbols[2] == "":
                return -1
            return 1
        
        # Check draw
        if not " " in square_symbols:
            return 0
        
        return -1
    
    def advance_turn(self) -> bool:
        if self.curr_player == self.players[0]:
            self.curr_player = self.players[1]
        elif self.curr_player == self.players[1]:
            self.curr_player = self.players[0]
        else:
            return False
            
        return True
        
    
    def make_move(self):
        
        if self.board_squares == []:
            self.create_squares()
            return
        
        
        for square in self.board_squares:
            if not square.is_hovered(pygame.mouse.get_pos()):
                continue
                
            if square.symbol != " ":
                return
            
            square.click(self.curr_player)
            
            if self.check_win() < 0:
                self.advance_turn()
            else:
                self.board_squares = []
            
            return
            
            
    
    def draw(self, screen):
        """Draws the board and its squares to the screen.

        Args:
            screen (pygame display): The pygame screen to draw to.
        """        
        for obj in self.board_squares:
            if obj.is_hovered(pygame.mouse.get_pos()):
                obj.curr_colour = obj.hover_colour
            else:
                obj.curr_colour = obj.def_colour
                
            obj.draw(screen)
        