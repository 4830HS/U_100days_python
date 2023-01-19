from turtle import Turtle, Screen
import random

alex = Turtle()

colours = ["forest green","blue violet","navy","gold","dark red","rosy brown","dark slate blue","gray","dark khaki","orange red"]

def draw_shape(num_sides) :
    angle = 360 / num_sides
    for _ in range(num_sides) :
        alex.forward(100)
        alex.right(angle)

for shape_side_n in range(3,11) :
    alex.color(random.choice(colours))
    draw_shape(shape_side_n)

# alex.pencolor("red")
# alex.forward(100)

# for _ in range(3) :
#     alex.right(120)
#     alex.forward(100)

# alex.pencolor("blue")

# for _ in range(4) :
#     alex.right(90)
#     alex.forward(100)

# alex.pencolor("green")

# for _ in range(5) :
#     alex.right(72)
#     alex.forward(100)

# alex.pencolor("orange")

# for _ in range(6) :
#     alex.right(60)
#     alex.forward(100)

# alex.pencolor("purple")

# for _ in range(7) :
#     alex.right(51.5)
#     alex.forward(100)

# alex.pencolor("hot pink")

# for _ in range(8) :
#     alex.right(45)
#     alex.forward(100) 

# alex.pencolor("black")

# for _ in range(9) :
#     alex.right(40)
#     alex.forward(100)

# alex.pencolor("gold")

# for _ in range(10) :
#     alex.right(36)
#     alex.forward(100)

screen = Screen()
screen.exitonclick()