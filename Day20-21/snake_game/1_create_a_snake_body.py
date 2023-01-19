from turtle import Screen, Turtle

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Alexnake Game")

# TODO 1 : Create a snake body

# solution 1) My answer
# x_positions = [0,-20,-40]
# for turtle_index in range(0,3) :
#     new_turtle = Turtle("square")
#     new_turtle.color("white")
#     distance = new_turtle.goto(x = x_positions[turtle_index], y = 0)

# solotuion 2) Angela's answer 1
# segment_1 = Turtle("square")
# segment_1.color("white")

# segment_2 = Turtle("square")
# segment_2.color("white")
# segment_2.goto(-20,0)

# segment_3 = Turtle("square")
# segment_3.color("white")
# segment_2.goto(-40,0)

# solution 3) Angela's answer 2
starting_positions = [(0,0),(-20,0),(-40,0)]

for position in starting_positions :
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)
 
screen.exitonclick()