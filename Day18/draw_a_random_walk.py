from turtle import Turtle, Screen
import random

alex = Turtle()
colours = ["forest green","blue violet","navy","gold","dark red","rosy brown","dark slate blue","gray","dark khaki","orange red"]
angle = [0,90,180,270]
alex.pensize(7)
alex.speed("fastest)")

for _ in range(100) :
    alex.color(random.choice(colours))
    alex.forward(20)
    alex.setheading(random.choice(angle))

screen = Screen()
screen.exitonclick()