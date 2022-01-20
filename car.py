import math

import pygame

class Car:

    #constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 10
        self.length = 15
        self.angle = 0
        self.speed = 1
        loadImage = pygame.image.load("greenCar.png")
        self.image = pygame.transform.scale(loadImage,(50,25))
        self.myRect = pygame.Rect(self.x, self.y, self.width, self.length)

    def rotateLeft(self):
        self.angle-=1

    def rotateRight(self):
        self.angle+=1

    def move(self):
        self.x += self.speed * math.sin((self.angle+90)/180*math.pi)
        self.y += self.speed * math.cos((self.angle+90)/180*math.pi)

    def draw(self, screen):
        rotatedImage = pygame.transform.rotate(self.image,self.angle)
        new_rect = rotatedImage.get_rect(center = self.image.get_rect(center = (self.x, self.y)).center)
        screen.blit(rotatedImage, new_rect)
