from game import main
from constants import *
from gameobjects import *

class board:
    
    players = []
    square_layout = 0
    board_squares = []
    board_width = 0
    board_height = 0
    btn_width = 0
    btn_height = 0
    
    
    def __init__(self, players, board_size: (), btn_size : ()):
        
        self.players = players
        self.board_width = board_size[0]
        self.board_height = board_size[1]
        self.btn_width = btn_size[0]
        self.btn_height = btn_size[1]
        
        for x in (range(board_size)):
            for y in (range(board_size)):
                this_pos = Pos((x * btn_size) + BOARD_PADDING*(1+x), (y * btn_size) + BOARD_PADDING*(1+y))
                board_squares.append(Button(this_pos, (btn_size, btn_size), (BG_COLOUR[0], BG_COLOUR[1], BG_COLOUR[2] + 20)))
        
        pass
    
    def make_move(self, player, mouse_pos):
        for square in self.board_squares:
            if square.is_hovered(mouse_pos):
                square.click(player)
                return True
            
            

    def draw(self, screen):
        for square in self.board_squares:
            square.draw(screen)
        