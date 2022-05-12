# Snake Game!
import pygame, random, sys, time

# Errors
check_errors = pygame.init()
if check_errors[1] > 0:
    print("(!) Had {0} errors, exiting...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) PyGame successfully initialized")

# Interface
playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption("Snake Game!")
red = pygame.Color(255, 0, 0) #game over
green = pygame.Color(12, 108, 7 ) #snake
blue = pygame.Color(0, 0, 255) 
black = pygame.Color(0, 0, 0)#score
cream = pygame.Color(225, 221, 146 ) #bg
brown = pygame.Color(81, 20, 7) #food

# Snake
fpsController = pygame.time.Clock()

snakePos = [110, 50]
snakeBody = [[100, 50], [90, 50], [80, 50]]

# Food
