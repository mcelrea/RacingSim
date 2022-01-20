import pygame

class Car:

    #constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 10
        self.length = 15
        self.angle = 0
        loadImage = pygame.image.load("greenCar.png")
        self.image = pygame.transform.scale(loadImage,(50,25))
        self.myRect = pygame.Rect(self.x, self.y, self.width, self.length)

    def draw(self, screen):
        screen.blit(self.image, (self.x,self.y))
