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
import gameobjects as objects


def main():
    
    ## Initialize pygame ##
    pygame.init()
    screen_size = 900
    screen = pygame.display.set_mode((screen_size, screen_size))
    pygame.display.set_caption("Tic Tac Toe")
    pygame.display.set_icon(pygame.image.load("src/assets/window_icon.png"))
    clock = pygame.time.Clock()
    running = True
    game_objects = []
    board_size = 3
    board_padding = 40
    
    bg_colour = (30, 30, 80)
    
    
    
    ## Create game objects ##
    btn_size = (screen_size - (2*board_padding + (board_size-1)*board_padding)) / board_size
    for x in (range(board_size)):
        for y in (range(board_size)):
            this_pos = objects.Pos((x * btn_size) + board_padding*(1+x), (y * btn_size) + board_padding*(1+y))
            game_objects.append(objects.Button(this_pos, (btn_size, btn_size), (bg_colour[0], bg_colour[1], bg_colour[2] + 20)))
            
    ## Create players ##
    players = [objects.Player(1), objects.Player(2)]
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
        screen.fill(bg_colour)
        for obj in game_objects:
            obj.draw(screen)
        
        ## Update  and limit framerate ##
        pygame.display.flip()
        clock.tick(60)
        
    ## Quit pygame ##
    pygame.quit()   
        







if __name__ == "__main__":
    main()