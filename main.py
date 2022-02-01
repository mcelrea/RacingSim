import pygame
from car import *
from race_track import *

#start the pygame engine
pygame.init()
pygame.font.init()


myfont = pygame.font.SysFont('Comic Sans MS', 23)

FPS = 60
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((1280,720))

player1 = Car(100,100)
ai1 = AICar(100,80)
track1 = RaceTrack("track 1")

def getUserInput():
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_a]:
        player1.rotateLeft(track1.getWalls())
    elif pressed[pygame.K_d]:
        player1.rotateRight(track1.getWalls())
    if pressed[pygame.K_w]:
        player1.move(track1)
    elif pressed[pygame.K_s]:
        player1.reverse(track1.getWalls())

def drawHUD():
    textsurface = myfont.render("check point 0: " + str(player1.getCheckPoint(0)), False, (0, 0, 0))
    screen.blit(textsurface,(900,0))
    textsurface = myfont.render("check point 1: " + str(player1.getCheckPoint(1)), False, (0, 0, 0))
    screen.blit(textsurface,(900,30))
    textsurface = myfont.render("check point 2: " + str(player1.getCheckPoint(2)), False, (0, 0, 0))
    screen.blit(textsurface,(900,60))
    textsurface = myfont.render("check point 3: " + str(player1.getCheckPoint(3)), False, (0, 0, 0))
    screen.blit(textsurface,(900,90))
    textsurface = myfont.render("check point 4: " + str(player1.getCheckPoint(4)), False, (0, 0, 0))
    screen.blit(textsurface,(900,120))
    textsurface = myfont.render("laps: " + str(player1.getNumLaps()), False, (0, 0, 0))
    screen.blit(textsurface,(900,150))


def clear_screen():
    pygame.draw.rect(screen, (240,224,202), (0, 0, 1280, 720))

def createTrack1():
    track1.addRect(pygame.Rect(0,0,800,25))
    track1.addRect(pygame.Rect(800,0,25,300))
    track1.addRect(pygame.Rect(800,300,300,25))
    track1.addRect(pygame.Rect(1100,300,25,300))
    track1.addRect(pygame.Rect(0,600,1125,25))
    track1.addRect(pygame.Rect(0,0,25,600))
    track1.addRect(pygame.Rect(200,200,400,25))
    track1.addRect(pygame.Rect(200,200,25,250))
    track1.addRect(pygame.Rect(600,200,25,200))
    track1.addRect(pygame.Rect(600,400,150,25))
    track1.addRect(pygame.Rect(750,400,25,100))
    track1.addRect(pygame.Rect(200,400,400,25))

    track1.addCheckPoint(pygame.Rect(500,0,25,200))
    track1.addCheckPoint(pygame.Rect(600,300,200,25))
    track1.addCheckPoint(pygame.Rect(500,425,25,200))
    track1.addCheckPoint(pygame.Rect(0,400,200,25))
    track1.addCheckPoint(pygame.Rect(0,200,200,25))


createTrack1()
while True:
    #loop through and empty the event queue, key presses
    #buttons, clicks, etc.
    for event in pygame.event.get():
        #if the event is a click on the "X" close button
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player1.shiftUp()
            if event.key == pygame.K_DOWN:
                player1.shiftDown()

    getUserInput()
    ai1.move(track1)

    clear_screen()
    track1.drawRaceTrack(screen)
    player1.draw(screen)
    ai1.draw(screen)
    drawHUD()
    pygame.display.flip()
    fpsClock.tick(FPS)

