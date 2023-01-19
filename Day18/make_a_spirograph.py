import turtle as t
from turtle import Screen
import random

alex = t.Turtle()
t.colormode(255)
alex.speed("fastest")

def random_color() :
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)  
    color = (r,g,b)
    return color

def draw_spirograph(size_of_gap) :
    for _ in range(int(360 / size_of_gap)) :
        alex.color(random_color())
        alex.circle(100)
        alex.setheading(alex.heading() + size_of_gap)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()