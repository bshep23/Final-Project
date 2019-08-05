# -------------------------------------------------
#        Name: Blake Shepherd
#    Filename: Rocket and Engine Classes.py
#        Date: August 3rd, 2019 
# Description: Rocket-Classes
#               
# -------------------------------------------------

import time
import math 
# from scipy.integrate import quad

from graphics import *


                                # Rocket Body Parent Class

class RocketBody:
    def __init__(self, height, dry_mass, wet_mass, amount_of_fuel, type_fuel, num_eng, cost): # height in ft, Mass in kg
        self.height = height # feet
        self.dry_mass = dry_mass # kg
        self.wet_mass = wet_mass #kg
        self.amount_of_fuel = amount_of_fuel # kg
        self.type_fuel = type_fuel 
        self.type_oxidizer = "Liquid Oxygen"
        self.num_eng = num_eng
        self.cost = cost 

                            # Rocket Body Variables

SaturnV = RocketBody(363,245576,4736117,4490541, "Liquid Hydrogen" , 5 , 185000000) # mass includes mass of engine. INFO: https://history.nasa.gov/SP-4029/Apollo_18-19_Ground_Ignition_Weights.htm, and wikipedia

Falcon9 = RocketBody(230, 206790, 474646, 267856, "RP-1" , 9 , 57000000)             # mass includes mass of engine, INFO: https://www.reddit.com/r/spacex/comments/3lsm0q/f9ft_vs_f9v11_fuel_mass_flow_rate_isp/, and wikipedia

Electron = RocketBody(57, 520 , 8391, 7871 , "RP-1", 9 , 6000000)                    # mass includes mass of engine, INFO: http://www.spacelaunchreport.com/electron.html, and wikipedia

AtlasV = RocketBody(191, 15198, 284089, 268891, "RP-1", 1, 110000000)               # mass includes mass of engine, INFO: http://www.braeunig.us/space/specs/atlas.htm, and wikipedia

STS = RocketBody(260, 106673, 654534, 547861, "Liquid Hydrogen", 3 ,450000000)       # mass includes mass of engine, INFO: https://www.spacelaunchreport.com/sts.html, and wikipedia



                             # Engine Parent Class

class Engine:
    def __init__(self, height, mass, thrust, Isp, burn_rate, cost): # thrust is in Newtons
        self.height = height # feet
        self.mass = mass #kg
        self.thrust = thrust # kgN
        self.Vex = 9.8*Isp# m/s
        self.burn_rate = burn_rate # kg/s
        self.cost = cost*1000000 # dollars


                            # Engine Variables
                                                                                # Info for all costs: https://space.stackexchange.com/questions/4388/what-are-the-costs-of-the-various-different-engines-in-current-use

F1 = Engine(18.5, 8391, 7770, 304, 2542, 65)                                    # INFO: https://web.archive.org/web/20131109232214/http://www.astronautix.com/engines/f1.htm, and wikipedia
Marlin1D = Engine(7.17, 490, 723, 282, 235, .5)                                 # INFO: http://www.astronautix.com/m/merlin1d.html, and https://www.reddit.com/r/spacex/comments/3lsm0q/f9ft_vs_f9v11_fuel_mass_flow_rate_isp/
RD180 = Engine(12, 5545, 4152, 313, 1250,23)                                   # INFO: http://my.fit.edu/~dkirk/4262/RD180_Presentation.pdf
Raptor = Engine(10, 600, 1700,  356, 931,2)                                     # INFO: https://www.nextbigfuture.com/2019/05/spacex-raptor-engine-will-be-best-on-cost-and-nearly-best-on-isp.html
Rutherford = Engine(17, 38 , 162, 303, .03, .5 )                                    # INFO: http://www.b14643.de/Spacerockets/Specials/Asian_Rocket_engines/engines.htm
RS25 = Engine(14, 3527, 2279, 452, 490, 50)                                    #INFO: https://www.rocket.com/sites/default/files/documents/lr_3-26-19_RS25_data%20sheet.pdf and http://www.b14643.de/Spacerockets_2/United_States_1/Space_Shuttle/Propulsion/engines.htm


            # THIS TOOK TOO MANY HOURS
            

            # Combine Rocket Things

class Rocket:
    def __init__(self, rocket_body, engine):
        self.rocket_body = rocket_body
        self.engine = engine
        self.wet_mass = rocket_body.wet_mass + engine.mass*rocket_body.num_eng
        self.dry_mass = rocket_body.dry_mass + engine.mass*rocket_body.num_eng
        self.payload = eval(input("What payload do you want in kgs?"))*1000
        self.mass = self.wet_mass + self.payload
        self.height = rocket_body.height + engine.height
        self.amount_of_fuel = rocket_body.amount_of_fuel
        self.DeltaV = engine.Vex * math.log((rocket_body.wet_mass/rocket_body.dry_mass))
        self.thrust = engine.thrust*rocket_body.num_eng
        self.TWR = self.thrust/(self.mass*9.8)*1000
        self.num_eng = eval(input("How many Engines do you want?"))
    

    def burn_fuel(self):
        while self.amount_of_fuel > 0:
            print(self.TWR)
            self.amount_of_fuel = self.amount_of_fuel - self.engine.burn_rate*self.num_eng
            self.mass = self.dry_mass + self.amount_of_fuel + self.payload
            self.TWR = self.thrust/(self.mass*9.8)*1000
            



        
        
        
            

My_Rocket = Rocket(AtlasV,RS25)


print(My_Rocket.burn_fuel())

            
            
        
        







