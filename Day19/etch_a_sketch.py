from turtle import Turtle, Screen

alex = Turtle()

def forward() :
    alex.forward(20)

def backward() :
    alex.backward(20)

def right() :
    alex.right(10)
    # new_heading = alex.heaading() + 10
    # alex.setheading(new_heading)

def left() :
    alex.left(10)
    # new_heading = alex.heaading() - 10
    # alex.setheading(new_heading)

def clear_drawing() :
    alex.clear()
    alex.penup()
    alex.home()
    alex.pendown()

screen = Screen()

screen.listen()
screen.onkey(key="w",fun=forward)
screen.onkey(key="s",fun=backward)
screen.onkey(key="a",fun=right)
screen.onkey(key="d",fun=left)
screen.onkey(key="c",fun=clear_drawing)

screen.exitonclick()