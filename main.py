import pygame
from car import *

#start the pygame engine
pygame.init()
pygame.font.init()

FPS = 60
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((1280,720))

player1 = Car(200,200)

def getUserInput():
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_a]:
        player1.rotateLeft()
    elif pressed[pygame.K_d]:
        player1.rotateRight()

while True:
    #loop through and empty the event queue, key presses
    #buttons, clicks, etc.
    for event in pygame.event.get():
        #if the event is a click on the "X" close button
        if event.type == pygame.QUIT:
            quit()
    getUserInput()
    player1.move()

    player1.draw(screen)
    pygame.display.flip()
    fpsClock.tick(FPS)

