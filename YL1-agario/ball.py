from turtle import *
import random
colormode(255)


class Ball(Turtle):
    def __init__(self,x,y,dx,dy,r,color):
        Turtle. __init__(self)
        self.shape("circle")
        self.shapesize(r/10)
        self.r = r
        self.color(color)
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def move(self,screen_width,screen_height):
        current_x = self.xcor()
        current_y = self.ycor()
        new_x = current_x + self.dx
        new_y = current_y + self.dy
        right_side_ball = new_x + self.r
        top_side_ball = new_y + self.r
        left_side_ball = new_x - self.r
        bottom_side_ball = new_y - self.r
        self.goto(new_x,new_y)
        if right_side_ball >= screen_width / 2:
            self.dx = self.dx * (-1)
        elif left_side_ball <= (screen_width / 2)*(-1):
            self.dx = self.dx * (-1)
        elif top_side_ball >= screen_height / 2:
            self.dy = self.dy * (-1)
        elif bottom_side_ball <= (screen_height / 2)*(-1):
            self.dy = self.dy * (-1)

