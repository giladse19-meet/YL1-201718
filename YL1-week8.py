from turtle import*
import math
import random

class ball(Turtle):
    def __init__(self,raidius,color,speed):
        Turtle. __init__(self)
        self.shape("circle")
        self.shapesize(raidius)
        self.color(color)
        self.speed(speed)

circle1 = ball(5,"green",1)
circle1.goto(50,0)
circle2 = ball(3,"red",1)

def check_dis(circle1,circle2):
    D = math.sqrt(math.pow(circle1.xcor()-circle2.xcor(),2)+math.pow(circle1.ycor()-circle.ycor(),2))

def check_collision(circle1,circle2,D):
    D2 = circle1[raidius]+circle2[raidus]
    if D == D2:
        circle1.color("blue")

check_dis(circle1,circle2)
check_collision(circle1,circle2,D)
