import pygame, sys, time, random 


speed = 15


#windows


frame_size_x = 720
frame_size_y = 488


check_erros = pygame.init()

if(check_erros[1] > 0):
    print("Error " + check_erros[1])
else:
    print("Game Successfully inicialized! ")


#inicio do game


pygame.display.set_caption("Snake Game")
game_window = pygame.display.set_mode()
