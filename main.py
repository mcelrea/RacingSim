import pygame
from car import *

#start the pygame engine
pygame.init()
pygame.font.init()

FPS = 60
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((1280,720))

player1 = Car(200,200)

while True:
    #loop through and empty the event queue, key presses
    #buttons, clicks, etc.
    for event in pygame.event.get():
        #if the event is a click on the "X" close button
        if event.type == pygame.QUIT:
            quit()

    player1.draw(screen)
    pygame.display.flip()
    fpsClock.tick(FPS)

