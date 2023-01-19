import turtle as t
from turtle import Screen
import random

alex = t.Turtle()
color_list = [(199, 157, 97), (198, 138, 167), (149, 94, 53), (146, 66, 92), (134, 163, 190), (183, 145, 47), (207, 216, 235), (20, 62, 29), (179, 96, 127), (68, 105, 133), (230, 167, 193), (234, 197, 216), (65, 108, 80), (126, 36, 53), (29, 85, 44), (133, 170, 152), (202, 96, 70), (236, 199, 86), (228, 210, 194), (176, 185, 220), (58, 50, 24), (111, 121, 162), (101, 145, 122), (202, 222, 214), (78, 78, 25), (124, 40, 31), (74, 37, 55), (86, 144, 158), (141, 211, 228), (230, 173, 163)]
t.colormode(255)
alex.speed("fastest")

alex.penup()
alex.setx(-220)
alex.sety(250)

def color_dot() :
    alex.color((random.choice(color_list)))
    alex.dot(20)

def dots() :
    for _ in range(9) :
        color_dot()
        alex.forward(50)
        color_dot()

def change_direction_right() :
    alex.right(90)
    alex.forward(50)
    alex.right(90)

def change_direction_left() :
    alex.left(90)
    alex.forward(50)
    alex.left(90)

for dot in range(5) :
    dots()
    change_direction_right()
    dots()
    change_direction_left()

screen = Screen()
screen.exitonclick()