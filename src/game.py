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
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Tic Tac Toe")
    pygame.display.set_icon(pygame.image.load("src/assets/window_icon.png"))
    clock = pygame.time.Clock()
    running = True
    game_objects = []
    board_size = 3
    
    ## Create game objects ##
    for x in range(board_size):
        for y in range(board_size):
            game_objects.append(objects.Button(((x * 200) + 10, (y * 200) + 10), (160, 160)))
    
    ## Main loop ##
    
    while running:
        
        ### Event loop ###
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        
        ### Draw here ###
        screen.fill((255, 255, 255))
        for obj in game_objects:
            obj.draw(screen)
        
        ## Update  and limit framerate ##
        pygame.display.flip()
        clock.tick(60)
        
    ## Quit pygame ##
    pygame.quit()   
        







if __name__ == "__main__":
    main()