# import turtle

# timmy = turtle.Turtle()



# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.fillcolor("yellow")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)

# my_screen.exitonclick()



from turtle import *

color('red', 'yellow')
begin_fill()
while True :
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()