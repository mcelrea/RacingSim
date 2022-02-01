import math
import random

import pygame

#changed two things:
    #removed collision detection on changing of angle, the car can ALWAYS rotate now
    #changed collision detection to check which side of car is colliding and allowing it to continue moving
    #    in the opposite axis of the collision

class Car:

    newRect = pygame.Rect(0,0,1,1)
    checkPoints = [False, False, False, False, False]
    numLaps = 0

    #constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 10
        self.length = 15
        self.angle = 0
        self.speed = 1
        self.gear = 1
        loadImage = pygame.image.load("small car.png")
        var = pygame.PixelArray(loadImage)
        var.replace((0,255,30), (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        del var
        self.image = pygame.transform.scale(loadImage,(15,15))
        self.myRect = pygame.Rect(self.x, self.y, self.width, self.length)

    def rotateLeft(self, track):
        oldAngle = self.angle
        self.angle = (self.angle+3) % 360
        #for rectangle in track:
        #    if pygame.Rect.colliderect(rectangle, self.new_rect):
        #        self.angle = oldAngle

    def canRotateLeft(self, track):
        oldAngle = self.angle
        self.angle+=3
        for rectangle in track:
            if pygame.Rect.colliderect(rectangle, self.new_rect):
                self.angle = oldAngle
                return False
        self.angle = oldAngle
        return True

    def getCheckPoint(self, n):
        if(n < len(self.checkPoints)):
            return self.checkPoints[n]
        else:
            return "BAD DATA"

    def rotateRight(self, track):
        oldAngle = self.angle
        self.angle-=3
        if(self.angle < 0):
            self.angle = 359
        #for rectangle in track:
        #    if pygame.Rect.colliderect(rectangle, self.new_rect):
        #        self.angle = oldAngle

    def canRotateRight(self, track):
        oldAngle = self.angle
        self.angle-=3
        for rectangle in track:
            if pygame.Rect.colliderect(rectangle, self.new_rect):
                self.angle = oldAngle
                return False
        self.angle = oldAngle
        return True

    def reverse(self, track):
        if not self.canMove(track) or not self.canRotateRight(track) or not self.canRotateLeft(track):
            self.x -= self.speed * math.sin((self.angle+90)/180*math.pi)
            self.y -= self.speed * math.cos((self.angle+90)/180*math.pi)

    def shiftUp(self):
        self.gear += 1
        if self.gear > 4:
            self.gear = 4

    def shiftDown(self):
        self.gear -= 1
        if self.gear < 1:
            self.gear = 1

    def move(self, track):
        oldx = self.x
        oldy = self.y
        walls = track.getWalls()
        trackCheckPoints = track.getCheckPoints()
        print(self.angle)
        self.x += (self.speed * self.gear) * math.sin((self.angle+90)/180*math.pi)
        self.y += (self.speed * self.gear) * math.cos((self.angle+90)/180*math.pi)
        for rectangle in walls:
            if pygame.Rect.colliderect(rectangle, self.new_rect):
                #hitting top
                if abs(self.new_rect.y - (rectangle.y + rectangle.height)) < 5:
                    self.y = rectangle.y+rectangle.height+10
                #hitting bottom
                elif abs((self.new_rect.y + self.new_rect.height) - rectangle.y) < 5:
                    self.y = rectangle.y-10
                #hitting left
                elif abs(self.new_rect.x - (rectangle.x + rectangle.width)) < 5:
                    self.x = rectangle.x+rectangle.width+10
                #hitting right
                elif abs((self.new_rect.x+self.new_rect.width) - rectangle.x) < 5:
                    self.x = rectangle.x-10
        for i in range(0,len(trackCheckPoints)):
            if pygame.Rect.colliderect(trackCheckPoints[i],self.new_rect):
                #if you hit the first check point
                if i == 0:
                    self.checkPoints[0] = True
                else:
                    #if the previous checkpoint has been hit
                    if self.checkPoints[i-1] == True:
                        self.checkPoints[i] = True
                    #if you hit the last finish line
                    if i == 4:
                        #if car hits finish line correctly, award a lap
                        if self.checkPoints[3]:
                            self.numLaps += 1
                        self.checkPoints[0] = False
                        self.checkPoints[1] = False
                        self.checkPoints[2] = False
                        self.checkPoints[3] = False
                        self.checkPoints[4] = False

    def getNumLaps(self):
        return self.numLaps

    def canMove(self, track):
        oldx = self.x
        oldy = self.y
        self.x += self.speed * math.sin((self.angle+90)/180*math.pi)
        self.y += self.speed * math.cos((self.angle+90)/180*math.pi)
        for rectangle in track:
            if pygame.Rect.colliderect(rectangle, self.new_rect):
                self.x = oldx
                self.y = oldy
                return False
        self.x = oldx
        self.y = oldy
        return True

    def draw(self, screen):
        rotatedImage = pygame.transform.rotate(self.image,self.angle)
        self.new_rect = rotatedImage.get_rect(center = self.image.get_rect(center = (self.x, self.y)).center)
        screen.blit(rotatedImage, self.new_rect)

class AICar(Car):

    '''
    0 = do nothing  20%
    1 = shift up    30%
    2 = shift down  20%
    3 = rotate left 15%
    4 = rotate right 15%
    '''
    dna = []
    movementDelay = 1000 #ms
    nextMove = 0
    currentDNA = 0

    def __init__(self, x, y):
        super(AICar, self).__init__(x, y)
        self.nextMove = pygame.time.get_ticks() + self.movementDelay
        self.createDNA()

    def move(self, track):
        #if it's time for me to have an action
        if self.nextMove < pygame.time.get_ticks():
            if self.dna[self.currentDNA] == 1:
                super().shiftUp()
            elif self.dna[self.currentDNA] == 2:
                super().shiftDown()
            elif self.dna[self.currentDNA] == 3:
                super().rotateLeft(track)
            elif self.dna[self.currentDNA] == 4:
                super().rotateRight(track)
            self.nextMove = pygame.time.get_ticks() + self.movementDelay
            self.currentDNA += 1

        super().move(track)

    def createDNA(self):
        for i in range(100):
            randNum = random.randint(1,100)
            if randNum <= 20:
                self.dna.append(0)
            elif randNum <= 50:
                self.dna.append(1)
            elif randNum <= 70:
                self.dna.append(2)
            elif randNum <= 85:
                self.dna.append(3)
            else:
                self.dna.append(4)