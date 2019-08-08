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
pygame.font.init()

# from https://stackoverflow.com/questions/10077644/python-display-text-with-font-color
myfont = pygame.font.SysFont("monospace",15)



pygame.init()
screen = pygame.display.set_mode((1000, 800))
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

# making Circles 
class Circle(pygame.sprite.Sprite):
    def __init__(self, pos, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100,150), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, color, (40,40), 200)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.image = self.image.convert_alpha()
    def update(self):
        pass



# class specifically for next_button
class Circle1(pygame.sprite.Sprite):
    def __init__(self, pos, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((150,25), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, color, (40,40), 200)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.image = self.image.convert_alpha()
    def update(self):
        pass

    
def draw(sprites):
    screen.fill(white)
    sprites.draw(screen)
    pygame.display.flip()


# Making Rocket Body options
SaturnV_option = Circle((150+50,100),red)
Falcon_option = Circle((300+50,100),red)
Electron_option = Circle((450+50,100),red)
Atlas_option = Circle((600+50,100),red)
STS_option = Circle((750+50,100),red)

# Making Engine Options

F1_option = Circle((150,600),blue)
Merlin_option = Circle((300,600),blue)
RD_option = Circle((450,600),blue)
Raptor_option = Circle((600,600),blue)
Ruth_option = Circle((750,600),blue)
RS25_option = Circle((900,600),blue)

# making button to go to next screen
next_button = Circle1((900,750),green)




list_of_circles = pygame.sprite.Group(SaturnV_option)
list_of_circles.add(Falcon_option,Electron_option,Atlas_option,STS_option,
                    F1_option,Merlin_option,RD_option,Raptor_option,Ruth_option,
                    RS25_option,next_button)



# Putting engine imagies on options
RS25_i = pygame.image.load("Rs-25 .jpg")
RS25_i = pygame.transform.scale(RS25_i, (100,150))

F1_i = pygame.image.load("F-1_rocket_engine.jpg")
F1_i = pygame.transform.scale(F1_i, (100,150))

Merlin_i = pygame.image.load("Merlin1D.jpg")
Merlin_i = pygame.transform.scale(Merlin_i, (100,150))

RD_i = pygame.image.load("RD-180.jpg")
RD_i = pygame.transform.scale(RD_i, (100,150))

Raptor_i = pygame.image.load("Raptor.png")
Raptor_i = pygame.transform.scale(Raptor_i, (100,150))

Ruth_i = pygame.image.load("Ruth.png")
Ruth_i = pygame.transform.scale(Ruth_i, (100,150))

Falcon_i = pygame.image.load("falcon9-rocket.jpg")
Falcon_i = pygame.transform.scale(Falcon_i, (100,150))

# Putting Rocket Body Images on options

SaturnV_i = pygame.image.load("SaturnV.jpg")
SaturnV_i = pygame.transform.scale(SaturnV_i, (100,150))

AtlasV_i = pygame.image.load("atlas_V.jpg")
AtlasV_i = pygame.transform.scale(AtlasV_i, (100,150))

Electron_i = pygame.image.load("electron4.jpg")
Electron_i = pygame.transform.scale(Electron_i, (100,150))

STS_i = pygame.image.load("Space Shuttle.jpg")
STS_i = pygame.transform.scale(STS_i, (100,150))

bg_i = pygame.image.load("BackGround1.jpg")



# Writing Text for Objects

Sat_message = "Mass:" + "  " + str(SaturnV.wet_mass)
Sat_message2 = "Amount of Fuel:" + " " + str(SaturnV.amount_of_fuel)
Sat_message3 = "Name:" + " " + "SaturnV"
Sat_message4 = "Cost:" + " " + str(SaturnV.cost)
SaturnText = myfont.render(Sat_message, 10,(0,0,0))
SaturnText2 = myfont.render(Sat_message2, 10,(0,0,0))
SaturnText3 = myfont.render(Sat_message3, 10,(0,0,0))
SaturnText4 = myfont.render(Sat_message4, 10, (0,0,0))

# Functions To Write Stats

def writeStatsB():
    file = open("Stats.txt" , "r")
    stats = file.readlines()
    deltax = 150
    counter = 0
    for s in stats[0:5]:
        s = s.split(",")
        name = "Name: " + str(s[0]) 
        height = "Height: " + str(s[1]) + "ft"
        dry_mass = "Dry Mass: " + str(s[2]) + "Kg"
        wet_mass = "Wet Mass: " + str(s[3]) + "Kg"
        amount_of_fuel = "Amount of Fuel: " + str(s[4]) + "Kg"
        cost = "Cost: " + "$" + str( int(s[7])/1000000) + " million"
        nameText = myfont.render(name,10,(0,0,0))
        heightText = myfont.render(height,10,(0,0,0))
        dry_massText = myfont.render(dry_mass,10,(0,0,0))
        amount_of_fuelText = myfont.render(amount_of_fuel,10,(0,0,0))
        costText = myfont.render(cost,10,(0,0,0))
        screen.blit(nameText,(150 + deltax*counter,100+80))
        screen.blit(heightText,(150 + deltax*counter,100+90))
        screen.blit(dry_massText,(150 + deltax*counter,100+100))
        screen.blit(amount_of_fuelText,(150 + deltax*counter,100+110))
        screen.blit(costText,(150 + deltax*counter,100+120))
        counter +=1 
        
def writeStatsE():
    file = open("Stats.txt" , "r")
    stats = file.readlines()
    deltax = 150
    counter = 0
    for s in stats[5:]:
        s = s.split(",")
        name = "Name: " + str(s[0]) 
        height = "Height: " + str(s[1]) + "ft"
        mass =  "Mass: " + str(s[2]) + "Kg"
        Thrust = "Thrust: " + str(s[3]) + "KN"
        ISP = "ISP: " + str(s[4]) + "secs"
        burn_rate = "Burn Rate: " + str(s[5]) + "Kg/sec"
        cost = "Cost: " + "$" + str( s[6])  + " million"
        nameText = myfont.render(name,10,(0,0,0))
        heightText = myfont.render(height,10,(0,0,0))
        massText = myfont.render(mass,10,(0,0,0))
        ThrustText = myfont.render(Thrust,10,(0,0,0))
        ISPText = myfont.render(ISP,10,(0,0,0))
        burn_rateText = myfont.render(burn_rate,10,(0,0,0))
        costText = myfont.render(cost,10,(0,0,0))
        screen.blit(nameText,(150-50 + deltax*counter,600-75+150))
        screen.blit(heightText,(150-50 + deltax*counter,600-75+10+150))
        screen.blit(massText,(150-50 + deltax*counter,600-75+20+150))
        screen.blit(ThrustText,(150-50 + deltax*counter,600-75+30+150))
        screen.blit(ISPText,(150-50 + deltax*counter,600-75+40+150))
        screen.blit(costText,(150-50 + deltax*counter,600-75+50+150))
        counter +=1 
        
        
def RocketStats(rocket):
    mass = "Mass: " + str(rocket.mass) + " That's " + str(rocket.mass//5896) + " " + "elephants!"
    height = "Height: " + str(rocket.height) + " That's " + str(rocket.height//2.6) +" " + "Shaqs!"
    TWR = "Thrust to Weight on the Pad is " + str(rocket.TWR) 
    Thrust = "Thrust: "  + str(rocket.thrust) + " That's " + str(rocket.TWR/745) + " " + "horses"
    cost = "Cost: " + str(rocket.cost) + " That's a lot of money!"
    br = "Burn Rate: " + str(rocket.burn_rate) + "kg/sec" + " That's " + str(rocket.burn_rate/.5) + " water bottles per second"
    massText = myfont.render(mass,10,(0,0,0))
    heightText = myfont.render(height,10,(0,0,0))
    TWRText = myfont.render(TWR,10,(0,0,0))
    thrustText = myfont.render(Thrust,10,(0,0,0))
    costText = myfont.render(cost,10,(0,0,0))
    brText = myfont.render(br,10,(0,0,0))
    screen.blit(massText, (110,260))
    
    

pygame.display.flip()
body = ""
engine = ""
counter = 0

running = True

while running:     # start the game!
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False

    
    draw(list_of_circles)
    writeStatsB()
    writeStatsE()
    # putting images
    screen.blit(RS25_i, (900-50,600-75))
    screen.blit(F1_i, (150-50,600-75))
    screen.blit(Merlin_i, (300-50,600-75))
    screen.blit(RD_i, (450-50,600-75))
    screen.blit(Raptor_i, (600-50,600-75))
    screen.blit(Ruth_i, (750-50,600-75))
    screen.blit(SaturnV_i, (150+50-50,100-75))
    screen.blit(AtlasV_i, (600+50-50,100-75))
    screen.blit(Electron_i, (450+50-50,100-75))
    screen.blit(STS_i, (750+50-50,100-75))
    screen.blit(Falcon_i, (300+50-50,100-75))
    
    # drawing rectangle to middle of the screen for the stats

##    box = pygame.Rect(100,250, 800,200)
##    pygame.draw.rect(screen, blue, box)
    pygame.display.flip()

    # getting text to put on the rectangle


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
        RocketStats(rocket)
        counter +=1
        


    

    

    if pygame.mouse.get_pressed()[0]: # checking to see if user wants to refresh the screen
        pos = pygame.mouse.get_pos()
        if next_button.rect.collidepoint(pos):
           pygame.display.flip()
    

