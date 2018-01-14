import turtle
import time
import random
import ball.py

turtle.tracer(0)
hideturtle.()

running = True
sleep = 0.0077
screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_hieght()/2

my_ball = ball(5,5,10,10,5,"red")

number_of_ball = 5
minimum_ball_radius = 10
maximum_ball_radius = 100
minimum_ball_dx = -5
maximum_ball_dx = 5
minimum_ball_dy = -5
maximum_ball_dy = 5

balls = []

for i in range(number_of_balls):
    x = random.randint(screen_width + maximum_ball_radius,screen_height - maximum_ball_radius)
    y = random.randint(screen_height + maximum_ball_radius, screen_width - maximum_ball_radius)
    dx = random.randint(minimum_ball_dx,maximum_ball_dx)
    dy = random.randint(minimum_ball_dy,maximum_ball_dy)
    r = random.randint(minimum_ball_radius,maximum_ball_radius)
    color = (random.random(), random.random(), random.random())
    new_ball = ball(x,y,dx,dy,r,color)
    balls.append(new_ball)

def move_all_balls(balls):
    for current in balls:
            
    
    
        
