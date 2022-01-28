import math
import random

import pygame

#changed two things:
    #removed collision detection on changing of angle, the car can ALWAYS rotate now
    #changed collision detection to check which side of car is colliding and allowing it to continue moving
    #    in the opposite axis of the collision

class Car:

    newRect = pygame.Rect(0,0,1,1)

    #constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 10
        self.length = 15
        self.angle = 0
        self.speed = 3
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

    def move(self, track):
        oldx = self.x
        oldy = self.y
        print(self.angle)
        self.x += self.speed * math.sin((self.angle+90)/180*math.pi)
        self.y += self.speed * math.cos((self.angle+90)/180*math.pi)
        for rectangle in track:
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
