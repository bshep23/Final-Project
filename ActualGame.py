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
screen = pygame.display.set_mode((1000, 700))
white = (255,255,255)
blue = (0,0,255)

# making Circles 
class Rects(pygame.sprite.Sprite):
    def __init__(self, left,top,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,40), pygame.SRCALPHA, 32)
        self.rect1 = pygame.Rect((left,top),(width,height))
        pygame.draw.rect(self.image, blue, self.rect1)
        self.rect = self.image.get_rect()
        self.rect.center = ((left+width/2),(top+height/2))
        self.image = self.image.convert_alpha()
    def update(self):
        pass   
def draw(sprites):
    screen.fill(white)
    sprites.draw(screen)
    pygame.display.flip()

# Making Rocket Body options
SaturnV_option = Rects(60,60,40,40)
Falcon_option = Rects(160,60,40,40)
Electron_option = Rects(260,60,40,40)
Atlas_option = Rects(360,60,40,40)
STS_option = Rects(460,60,40,40)

# Making Engine Options

##F1_option = Rects((100,500))
##Merlin_option = Rects((250,500))
##RD_option = Rects((400,500))
##Raptor_option = Rects((550,500))
##Ruth_option = Rects((700,500))
##RS25_option = Rects((850,500))


#


list_of_circles = pygame.sprite.Group(SaturnV_option)
list_of_circles.add(Falcon_option,Electron_option,Atlas_option,STS_option)
                    #F1_option,Merlin_option,RD_option,Raptor_option,Ruth_option,
                    #RS25_option)



running = True

while running:     # start the game!
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
          
    draw(list_of_circles)
    
    if pygame.mouse.get_pressed()[0]: # checking to see which rocket body the user choose
        pos = pygame.mouse.get_pos()
        if SaturnV_option.rect.collidepoint(pos):
            x = SaturnV
            print(x.wet_mass)
        elif Falcon_option.rect.collidepoint(pos):
            x = Falcon9
            print(x.wet_mass)
        elif Electron_option.rect.collidepoint(pos):
            x = Electron
            print(x.wet_mass)
        elif Atlas_option.rect.collidepoint(pos):
                x = AtlasV
                print(x.wet_mass)
        elif STS_option.rect.collidepoint(pos):
                x = STS
                print(x.wet_mass)

        
    if pygame.mouse.get_pressed()[0]: # checking to see which engine the user choose
        pos = pygame.mouse.get_pos()
        if F1_option.rect.collidepoint(pos):
            x = F1
            print(x.mass)
        elif Merlin_option.rect.collidepoint(pos):
            x = Merlin1D
            print(x.mass)
        elif Raptor_option.rect.collidepoint(pos):
            x = Raptor
            print(x.mass)
        elif Ruth_option.rect.collidepoint(pos):
                x = Rutherford
                print(x.mass)
        elif RS25_option.rect.collidepoint(pos):
                x = RS25
                print(x.mass)
        elif RD_option.rect.collidepoint(pos):
                x = RD180
                print(x.mass)

    
    
        
    
    
pygame.quit()      

    
    

