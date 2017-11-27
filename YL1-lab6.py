from turtle import *
import turtle
colormode(255)

class Square(Turtle):
    def __init__(self,size,color):
        Turtle. __init__(self) 
        self.color(color)
        self.shapesize(size)
        self.shape("square")



class Hexagon(Turtle):
    def __init__(self,size,color):
        Turtle.__init__(self)
        self.color(color)
        register_shape("hexagon",((25,0),(50,25),(25,50),(0,50),(-25,25),(0,0)))
        self.shapesize(size)
        self.shape("hexagon")

ah1 = Hexagon(1,"green")
