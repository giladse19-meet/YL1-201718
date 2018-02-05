import turtle
import time
import random
import ball
import math
from ball import Ball
turtle.tracer(delay=0)
turtle.hideturtle()

running = True
sleep = 0.0077
screen_width = int(turtle.getcanvas().winfo_width()/2)
screen_height = int(turtle.getcanvas().winfo_height()/2)

my_ball = Ball(5,5,10,10,5,"red")

number_of_balls = 5
minimum_ball_radius = 10
maximum_ball_radius = 100
minimum_ball_dx = -5
maximum_ball_dx = 5
minimum_ball_dy = -5
maximum_ball_dy = 5

balls = []

for i in range(number_of_balls):
    x = random.randint(-screen_width + maximum_ball_radius,screen_width - maximum_ball_radius)
    y = random.randint(-screen_height + maximum_ball_radius, screen_height - maximum_ball_radius)
    dx = random.randint(minimum_ball_dx,maximum_ball_dx)
    while dx == 0:
        dx = random.randint(minimum_ball_dx,maximum_ball_dx)
    dy = random.randint(minimum_ball_dy,maximum_ball_dy)
    while dy == 0:
        dy = random.randint(minimum_ball_dy,maximum_ball_dy)
    r = random.randint(minimum_ball_radius,maximum_ball_radius)
    color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    new_ball = Ball(x,y,dx,dy,r,color)
    balls.append(new_ball)

def move_all_balls(balls,screen_width,screen_height):
    for current in balls:
        current.move(screen_width,screen_height)

def collide(ball_a,ball_b):
    if ball_a == ball_b:
        return(False)

    D = math.sqrt(math.pow(ball_a.xcor()- ball_b.xcor(),2)+math.pow(ball_a.ycor()-ball_b.ycor(),2))
    if D + 10 == ball_a.r + ball_b.r:
        return(True)
    else:
        return(False)

for i in range(20):
    move_all_balls(balls,screen_width,screen_height)
def check_all_balls_collision():
    for ball_a in balls:
        for ball_b in balls:
            if collide(ball_a,ball_b):
                a_r = ball_a.r
                b_r = ball_b.r
                if a_r < b_r:
                    random_x = random.randint(-int(screen_width) + maximum_ball_radius, int(screen_height) - maximum_ball_radius)
                    random_y = random.randint(-int(screen_height) + maximum_ball_radius, int(screen_width) - maximum_ball_radius)
                    ball_a.goto(random_x,random_y)
                    ball_a.dx = random.randint(minimum_ball_dx,maximum_ball_dx)
                    while ball_a.dx == 0:
                        ball_a.dx = random.randint(minimum_ball_dx,maximum_ball_dx)
                    while ball_a.dy == 0:
                        ball_a.dy = random.randint(minimum_ball_dy,maximum_ball_dy)
                    ball_a.r = random.randint(minimum_ball_radius,maximum_ball_radius)
                    ball_a.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
                    ball_b.shapesize(ball_b.r/10)
                    ball_b.r = ball_b.r + 1
                    ball_b.shapesize(ball_b.r/10)
                else:
                    random_x = random.randint(-int(screen_width) + maximum_ball_radius, int(screen_height) - maximum_ball_radius)
                    random_y = random.randint(-int(screen_height) + maximum_ball_radius, int(screen_width) - maximum_ball_radius)
                    ball_b.goto(random_x,random_y)
                    ball_b.dx = random.randint(minimum_ball_dx,maximum_ball_dx)
                    while ball_b.dx == 0:
                        ball_b.dx = random.randint(minimum_ball_dx,maximum_ball_dx)
                    while ball_b.dy == 0:
                        ball_b.dy = random.randint(minimum_ball_dy,maximum_ball_dy)
                    ball_b.r = random.randint(minimum_ball_radius,maximum_ball_radius)
                    ball_b.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
                    ball_a.shapesize(ball_a.r/10)
                    ball_a.r = ball_a.r + 1
                    ball_a.shapesize(ball_a.r/10)
                    

def check_myball_collision():
    for m in balls:
        if collide(my_ball,m):
            my_r = my_ball.r
            c_r = m.r
            if my_r < c_r:
                return(False)
            else:
                m.goto(random.randint(screen_width + maximum_ball_radius,screen_height - maximum_ball_radius),random.randint(screen_height + maximum_ball_radius, screen_width - maximum_ball_radius))
                m.dx = random.randint(minimum_ball_dx,maximum_ball_dx)
                while m.dx == 0:
                    m.dx = random.randint(minimum_ball_dx,maximum_ball_dy)
                while m.dy == 0:
                    m.dy = random.randint(minimum_ball_dy,maximum_ball_dy)
                m.r = random.randint(minimum_ball_radius,maximum_ball_radius)
                m.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
                my_ball.shapesize(my_ball.r/10)
                my_ball.r = my_ball.r + 1
                my_ball.shapesize(my_ball.r/10)
                return(True)

def movearound(event):
    my_ball.goto(event.x - screen_width,screen_height - event.y)
turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()

while running == True:
    if screen_width != int(turtle.getcanvas().winfo_width()/2):
        screen_width = turtle.canvwidth/2
        screen_height = turtle.canvheight/2
    if screen_height != int(turtle.getcanvas().winfo_height()/2):
        screen_width = turtle.canvwidth/2
        screen_height = turtle.canvheight/2
    move_all_balls(balls,screen_width,screen_height)
    check_all_balls_collision()
    running = check_myball_collision()
    turtle.update()
    time.sleep(sleep)
