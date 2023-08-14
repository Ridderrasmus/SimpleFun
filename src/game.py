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
from constants import *

def main():
    
    ## Initialize pygame ##
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    screen.lock(False)
    pygame.display.set_caption("Tic Tac Toe")
    pygame.display.set_icon(pygame.image.load("src/assets/window_icon.png"))
    clock = pygame.time.Clock()
    running = True
    game_objects = []
    
    
    
    
    ## Create game objects ##
    btn_size = (SCREEN_SIZE - (2*BOARD_PADDING + (BOARD_SIZE-1)*BOARD_PADDING)) / BOARD_SIZE
    for x in (range(BOARD_SIZE)):
        for y in (range(BOARD_SIZE)):
            this_pos = Pos((x * btn_size) + BOARD_PADDING*(1+x), (y * btn_size) + BOARD_PADDING*(1+y))
            game_objects.append(Button(this_pos, (btn_size, btn_size), (BG_COLOUR[0], BG_COLOUR[1], BG_COLOUR[2] + 20)))
            
    ## Create players ##
    players = [Player(1), Player(2)]
    curr_round = 1
    
    ## Main loop ##
    
    while running:
        
        
        ### Event loop ###
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for obj in game_objects:
                    if obj.is_hovered(pygame.mouse.get_pos()):
                        if ((curr_round % 2) == 0):
                            obj.click(players[1])
                            curr_round += 1
                        else:
                            obj.click(players[0])
                            curr_round += 1
                
        for obj in game_objects:
            if obj.is_hovered(pygame.mouse.get_pos()):
                obj.curr_colour = obj.hover_colour
            else:
                obj.curr_colour = obj.def_colour
        
        
        ### Draw here ###
        screen.fill(BG_COLOUR)
        for obj in game_objects:
            obj.draw(screen)
        
        ## Update  and limit framerate ##
        pygame.display.flip()
        clock.tick(60)
        
    ## Quit pygame ##
    pygame.quit()   
        







if __name__ == "__main__":
    main()