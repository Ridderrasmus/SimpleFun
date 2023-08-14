# Project Name: 
#   TBD
#
# Project Description: 
#   Let's create Tic Tac Toe in Python!
#
# Project Python Version:
#   3.11.4
# 
# Authors: 
#   Rasmus Tanggaard, Malthe Sørensen, Jonas Søgaard Frederiksen

import pygame
from gameobjects import *
from states import *
from constants import *

class Application:
    
    btn_size = (SCREEN_SIZE - (2*BOARD_PADDING + (BOARD_SIZE-1)*BOARD_PADDING)) / BOARD_SIZE
    
    running = None
    curr_state = None
    game_states = None
    screen = None
    clock = None
    players = None

    def __init__(self):
        
        ## Set running to true ##
        self.running = True
        
        ## Initialize pygame ##
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
        pygame.display.set_caption("Tic Tac Toe")
        pygame.display.set_icon(pygame.image.load("src/assets/window_icon.png"))
        self.clock = pygame.time.Clock()
        self.curr_state = "menu"
        
        ## Create players ##
        self.players = [Player(1, "🙅"), Player(2, "👌")]
        
        
        self.game_states = {
            "menu": Menu(self),
            "board": Board(self, SCREEN_SIZE, self.btn_size),
            "game_over": GameOver(self)
        }
        
        ## Main loop ##
        
        while self.running:
            state = self.game_states[self.curr_state]
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                else:
                    state.event(event)
            
            state.loop()

            ## Update and limit framerate ##
            pygame.display.flip()
            self.clock.tick(60)
            
        ## Quit pygame ##
        pygame.quit()
        
    def change_state(self, state):
        if state not in self.game_states:
            print("Invalid state")
            state = "menu"
            
        self.game_states[self.curr_state].reset()
        self.curr_state = state
        







if __name__ == "__main__":
    app = Application()