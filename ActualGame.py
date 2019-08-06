# -------------------------------------------------
#        Name: Blake Shepherd
#    Filename: ActualGame.py
#        Date: August 5th, 2019 
#
# Description: Actual Game Interface
#               
# -------------------------------------------------
from RocketClasses import *
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
white = (255,255,255)
blue = (0,0,255)

class Circle(pygame.sprite.Sprite):
    def __init__(self, surface_length, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(surface_length, pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, blue, pos, 40)
        self.rect = self.image.get_rect()
        self.rect.center = [320,240]
        self.image = self.image.convert_alpha()
    def update(self):
        pass   
def draw(sprites):
    screen.fill(white)
    sprites.draw(screen)
    pygame.display.flip()


circle1 = Circle((300,300),[200,200])
circle2 = Circle((500,500),[400,400])

list_of_circles = pygame.sprite.Group(circle1)
list_of_circles.add(circle2)



running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
          
    draw(list_of_circles)
    
    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        if circle1.rect.collidepoint(pos):
            x = SaturnV
            print(x)
        elif circle2.rect.collidepoint(pos):
            x = Merlin1D
            print(x)
    
            
        
    
    
pygame.quit()      

    
    

