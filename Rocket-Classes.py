# -------------------------------------------------
#        Name: Blake Shepherd
#    Filename: Rocket and Engine Classes.py
#        Date: August 3rd, 2019 
# Description: Rocket and Engine Classes
#               
# -------------------------------------------------


                             # Rocket Body Parent Class

class RocketBody:
    def __init__(self, height, dry_mass, wet_mass, amount_of_fuel, type_fuel, num_eng, cost): # height in ft, Mass in kg
        self.height = height
        self.dry_mass = dry_mass
        self.wet_mass = wet_mass
        self.total_mass = dry_mass + wet_mass
        self.amount_of_fuel = amount_of_fuel
        self.type_fuel = type_fuel
        self.type_oxidizer = "Liquid Oxygen"
        self.num_engine = num_eng
        self.cost = cost

                            # Rocket Body Variables

SaturnV = RocketBody(363,287531,4736117,4730675, "Liquid Hydrogen" , 5, 185000000)  # mass includes mass of engine. INFO: https://history.nasa.gov/SP-4029/Apollo_18-19_Ground_Ignition_Weights.htm, and wikipedia
Falcon9 = RocketBody(230, 31200, 474646, 474646, "RP-1" , 9 , 57000000)             # mass includes mass of engine, INFO: https://www.reddit.com/r/spacex/comments/3lsm0q/f9ft_vs_f9v11_fuel_mass_flow_rate_isp/, and wikipedia
Electron = RocketBody(57, 862 , 8391, 8391, "RP-1", 9 , 6000000)                    # mass includes mass of engine, INFO: http://www.spacelaunchreport.com/electron.html, and wikipedia
AtlasV = RocketBody(191, 20743, 284089, 284089, "RP-1", 1, 110000000)               # mass includes mass of engine, INFO: http://www.braeunig.us/space/specs/atlas.htm, and wikipedia
STS = RocketBody(260, 117254, 654534, 654534, "Liquid Hydrogen", 3,450000000)       # mass includes mass of engine, INFO: https://www.spacelaunchreport.com/sts.html, and wikipedia



                             # Engine Parent Class

class Engine:
    def __init__(self, height, mass, thrust, Isp, burn_rate):
        self.height = height
        self.mass = mass
        self.thrust = thrust
        self.Vex = 9.8*Isp
        self.burn_rate = burn_rate


                            # Engine Variables

F1 = Engine(18.5, 8391, 6748, 304, 2542) # INFO: https://web.archive.org/web/20131109232214/http://www.astronautix.com/engines/f1.htm, and wikipedia

Marlin1D = Engine(height, 490, 716, 282, 235) # INFO: http://www.astronautix.com/m/merlin1d.html, and https://www.reddit.com/r/spacex/comments/3lsm0q/f9ft_vs_f9v11_fuel_mass_flow_rate_isp/

RD-180 = Engine(height, mass, thrust, Isp, burn_rate)

Raptor = Engine(height, mass, thrust,  Isp, burn_rate)

Rutherford = Engine(height, mass, thrust Isp, burn_rate)

RS-25 = Engine(height, mass, thrust Isp, burn_rate)



