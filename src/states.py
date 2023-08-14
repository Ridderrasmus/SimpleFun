from constants import *
from gameobjects import *




###################################
###          Menu state         ###
###################################

class Menu:
    game = None
    
    def __init__(self, game) -> None:
        self.game = game
    
    def loop(self):
        screen = self.game.screen
        ### Draw BG ###
        screen.fill((130, 30, 40))
        
        ## Draw title ##
        title_font = pygame.font.SysFont("segoeuiemoji", 100)
        title_text = title_font.render("Tic Tac Toe", True, (255, 255, 255))
        title_text_rect = title_text.get_rect(center=(SCREEN_SIZE // 2, SCREEN_SIZE // 2 - 100))
        screen.blit(title_text, title_text_rect)
        
    
    def event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.game.curr_state = "board"
    

###################################
###       Game over state       ###
###################################

class GameOver:
    game = None
    
    def __init__(self, game) -> None:
        self.game = game
        
    def event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.game.change_state("menu")
    
    def loop(self):
        screen = self.game.screen
        
    

###################################
###       Main game state       ###
###################################

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
    game = None
    
    curr_player = None
    
    def __init__(self, game, board_start_pos: tuple|Pos, board_end_pos: tuple|Pos, btn_size: int):
        
        self.game = game
        self.players = game.players
        self.curr_player = game.players[0]
        
        if type(board_start_pos) == tuple:
            board_start_pos = Pos(board_start_pos[0], board_start_pos[1])
        
        if type(board_end_pos) == tuple:
            board_end_pos = Pos(board_end_pos[0], board_end_pos[1])
            
        self.board_width = board_end_pos.x - board_start_pos.x
        self.board_height = board_end_pos.y - board_start_pos.y
            
        self.btn_size = btn_size
        
        self.create_squares()
        
    
    def __init__(self, game, board_size: tuple|int, btn_size: int):
        
        self.game = game
        self.players = game.players
        self.curr_player = game.players[0]
        
        if type(board_size) == tuple:
            self.board_width = board_size[0]
            self.board_height = board_size[1]
        else:
            self.board_width = board_size
            self.board_height = board_size
            
        self.btn_size = btn_size
        
        self.create_squares()
        
    def reset(self):
        self.board_squares = []
        self.create_squares()
        
    def loop(self):
        
        screen = self.game.screen

        ### Draw BG ###
        screen.fill(BG_COLOUR)
        
        ### Draw screen ###
        self.draw(screen)
        
    def event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.make_move()
    
    def create_squares(self):
        if self.board_squares != []:
            return
        
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
        
        
        for square in self.board_squares:
            if not square.is_hovered(pygame.mouse.get_pos()):
                continue
                
            if square.symbol != " ":
                return
            
            square.click(self.curr_player)
            
            if self.check_win() < 0:
                self.advance_turn()
            else:
                self.game.change_state("menu")
            
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
        