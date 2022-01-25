import math

import pygame

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
        loadImage = pygame.image.load("greenCar.png")
        self.image = pygame.transform.scale(loadImage,(50,25))
        self.myRect = pygame.Rect(self.x, self.y, self.width, self.length)

    def rotateLeft(self, track):
        oldAngle = self.angle
        self.angle+=3
        for rectangle in track:
            if pygame.Rect.colliderect(rectangle, self.new_rect):
                self.angle = oldAngle

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
        for rectangle in track:
            if pygame.Rect.colliderect(rectangle, self.new_rect):
                self.angle = oldAngle

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
        self.x += self.speed * math.sin((self.angle+90)/180*math.pi)
        self.y += self.speed * math.cos((self.angle+90)/180*math.pi)
        for rectangle in track:
            if pygame.Rect.colliderect(rectangle, self.new_rect):
                self.x = oldx
                self.y = oldy

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
