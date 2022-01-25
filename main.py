import pygame
from car import *
from race_track import *

#start the pygame engine
pygame.init()
pygame.font.init()

FPS = 60
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((1280,720))

player1 = Car(200,200)
track1 = RaceTrack("track 1")

def getUserInput():
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_a]:
        player1.rotateLeft(track1.getWalls())
    elif pressed[pygame.K_d]:
        player1.rotateRight(track1.getWalls())
    if pressed[pygame.K_w]:
        player1.move(track1.getWalls())
    elif pressed[pygame.K_s]:
        player1.reverse(track1.getWalls())


track1.addRect(pygame.Rect(600,100,50,300))
while True:
    #loop through and empty the event queue, key presses
    #buttons, clicks, etc.
    for event in pygame.event.get():
        #if the event is a click on the "X" close button
        if event.type == pygame.QUIT:
            quit()
    getUserInput()

    track1.drawRaceTrack(screen)
    player1.draw(screen)
    pygame.display.flip()
    fpsClock.tick(FPS)

