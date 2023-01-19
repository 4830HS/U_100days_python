from turtle import Turtle, Screen

alex = Turtle()

# for _ in range(10) :
#     alex.dot()
#     alex.forward(10)

for _ in range(15) :
    alex.forward(10)
    alex.penup()
    alex.forward(10)
    alex.pendown()

screen = Screen()
screen.exitonclick()