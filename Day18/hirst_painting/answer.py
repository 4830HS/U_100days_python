import turtle as turtle_module
import random

turtle_module.colormode(255)
alex = turtle_module.Turtle()
alex.speed("fastest")
alex.penup()
alex.hideturtle()
color_list = [(199, 157, 97), (198, 138, 167), (149, 94, 53), (146, 66, 92), (134, 163, 190), (183, 145, 47), (207, 216, 235), (20, 62, 29), (179, 96, 127), (68, 105, 133), (230, 167, 193), (234, 197, 216), (65, 108, 80), (126, 36, 53), (29, 85, 44), (133, 170, 152), (202, 96, 70), (236, 199, 86), (228, 210, 194), (176, 185, 220), (58, 50, 24), (111, 121, 162), (101, 145, 122), (202, 222, 214), (78, 78, 25), (124, 40, 31), (74, 37, 55), (86, 144, 158), (141, 211, 228), (230, 173, 163)]

alex.setheading(225)
alex.forward(300)
alex.setheading(0)
number_of_dots = 100

for dot_count in range(1,number_of_dots+1) :
    alex.dot(20,random.choice(color_list))
    alex.forward(50)
    
    if dot_count % 10 == 0 :
        alex.setheading(90)
        alex.forward(50)
        alex.setheading(180)
        alex.forward(500)
        alex.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()