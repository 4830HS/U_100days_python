import turtle as t
from turtle import Screen
import random

alex = t.Turtle()
t.colormode(255)

# def random_color() :
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     return alex.pencolor(r,g,b)

# for _ in range(200) :
#     random_color()
#     alex.forward(20)
#     alex.setheading(random.choice(angle))

# angle = [0,45,90,150,180,240,270]
# alex.pensize(7)
# alex.speed("fastest")

# screen = Screen()
# screen.exitonclick()

def random_color() :
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

angle = [0,45,90,150,180,240,270]
alex.pensize(7)
alex.speed("fastest")

for _ in range(200) :
    alex.color(random_color())
    alex.forward(20)
    alex.setheading(random.choice(angle))

screen = Screen()
screen.exitonclick()