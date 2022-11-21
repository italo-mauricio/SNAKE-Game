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
game_window = pygame.display.set_mode(frame_size_x, frame_size_y)


# cores

black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0, 0, 255)

fps_controller = pygame.time.Clock()
# one snake square size
square_size = 20

def init_vars():
    global head_pos, snake_body, food_pos, food_spawn, score, direction
    direction = "RIGHT"
    head_pos = [120,60]
    snake_body = [[120,60]] 




