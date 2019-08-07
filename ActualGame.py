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
# pygame.font.init()

pygame.init()
screen = pygame.display.set_mode((1000, 800))
white = (255,255,255)
red = (0,255,0)
blue = (0,0,255)

# making Circles 
class Circle(pygame.sprite.Sprite):
    def __init__(self, pos, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((80,80), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, color, (40,40), 40)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.image = self.image.convert_alpha()
    def update(self):
        pass   
def draw(sprites):
    screen.fill(white)
    sprites.draw(screen)
    pygame.display.flip()


### should print text. referecned from https://pythonprogramming.net/displaying-text-pygame-screen/

                                        # TRYIG TO GET TEXT PLEASE HELP ME IM GOING TO EXPLODE!!!!!
##def message_display(text, pos):
##    largetext = pygame.font.Font("freesansbold.ttl",25)
##    TextSurf, TextRect = text_objects(text, largeText)
##    TextRect.center = pos
##    gameDisplay.blit(TextSurf, TextRect)

##def text_objects(text,font):
##   textSurface = font.render(text,True,white)
##   return textSurface, textSurface.get_rect()
##
##smallText = pygame.font.Font("freesansbold.ttf",20)
##textSurf, textRect = text_objects("GO", smallText)
##textRect.center = (150+50,100)
##screen.blit(textSurf, textRect)

# Making Rocket Body options
SaturnV_option = Circle((150+50,100),red)
#message_display("text", (150+50,100))

Falcon_option = Circle((300+50,100),red)
#message_display("text", (300+50,100))

Electron_option = Circle((450+50,100),red)
#message_display("text", (450+50,100))

Atlas_option = Circle((600+50,100),red)
#message_display("text", (600+50,100))

STS_option = Circle((750+50,100),red)
#message_display("text", (750+50,100))

# Making Engine Options

F1_option = Circle((150,600),blue)
Merlin_option = Circle((300,600),blue)
RD_option = Circle((450,600),blue)
Raptor_option = Circle((600,600),blue)
Ruth_option = Circle((750,600),blue)
RS25_option = Circle((900,600),blue)

# making button to go to next screen
next_button = Circle((900,700),red)




list_of_circles = pygame.sprite.Group(SaturnV_option)
list_of_circles.add(Falcon_option,Electron_option,Atlas_option,STS_option,
                    F1_option,Merlin_option,RD_option,Raptor_option,Ruth_option,
                    RS25_option, next_button)


body = ""
engine = ""
counter = 0

running = True

while running:     # start the game!
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
          
    draw(list_of_circles)
    # Writing Names to Engine and Body Options
    # got from https://pygame-zero.readthedocs.io/en/stable/ptext.html
   


    pos = pygame.mouse.get_pos()
    
    if pygame.mouse.get_pressed()[0]: # checking to see which rocket body the user choose
            pos = pygame.mouse.get_pos()
            if SaturnV_option.rect.collidepoint(pos):
                body = SaturnV
                
            elif Falcon_option.rect.collidepoint(pos):
                body = Falcon9
               
            elif Electron_option.rect.collidepoint(pos):
                body = Electron
                
            elif Atlas_option.rect.collidepoint(pos):
                    body = AtlasV
                    
            elif STS_option.rect.collidepoint(pos):
                    body = STS
            
             # checking to see which engine the user choose
            if F1_option.rect.collidepoint(pos):
                engine = F1

            elif Merlin_option.rect.collidepoint(pos):
                engine = Merlin1D
               
            elif Raptor_option.rect.collidepoint(pos):
                engine = Raptor
                
            elif Ruth_option.rect.collidepoint(pos):
                    engine = Rutherford
                    
            elif RS25_option.rect.collidepoint(pos):
                    engine = RS25
                    
            elif RD_option.rect.collidepoint(pos):
                    engine = RD180

                
    if body != "" and engine != "" and counter <1:
        rocket = Rocket(body,engine)
        counter +=1

    if pygame.mouse.get_pressed()[0]: # checking to see if user wants to go to next screen
        pos = pygame.mouse.get_pos()
        if next_button.rect.collidepoint(pos):
           running = False 

running = True 
    
while running:     # window to make the rocket fly 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False

    rect =  pygame.Rect((100,200),(50,50))
    pygame.draw.rect(screen, red, rect)
    
    
    

