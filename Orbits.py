# -------------------------------------------------
#        Name: Blake Shepherd and Name
#    Filename: Orbits
#        Date: August 3rd, 2019 
#
# Description: Orbits
#               
# -------------------------------------------------

            # Orbit Parent Class
##import turtle
##
##orbit = turtle.Turtle()
##orbit.color("blue")
##l = turtle.Turtle()
##l.penup()
##orbit.speed(.75)
##orbit.hideturtle()
##
## Tried playing with turtle to get some things done

    
turtle.screensize()
(1000, 1000)
class Orbit:
    def __init__(self, radius, period, deltaV):
        self.radius = radius/2 #kilometers
        self.period = period #hours
        self.deltaV = deltaV

    def displayOrbit(self):
        orbit.circle(self.radius)
        #l.left(90)
        #l.forward(100)
        #l.backward(100)

        



leo = Orbit(200, 1.4, 9.4)
geo = Orbit(358, 24, 13.31)
lun_tran = Orbit(0, 0, 15.8)



