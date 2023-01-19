from turtle import Turtle, Screen

alex_the_turtle = Turtle()

for _ in range(4) :
    alex_the_turtle.forward(100)
    alex_the_turtle.right(90)

screen = Screen()
screen.exitonclick()