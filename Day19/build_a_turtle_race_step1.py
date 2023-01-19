from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color : ")
colors = ["red", "black", "hot pink", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0,5) :
    alex = Turtle(shape = "turtle")
    alex.color(colors[turtle_index])
    alex.penup()
    alex.goto(x = -230, y = y_positions[turtle_index])

screen.exitonclick()