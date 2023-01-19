# TODO 2-3 : Detect collision with food

from turtle import Screen
# 더이상 Turtle은 사용하지 않으니 'Turtle'은 import 항목에서 지워주기
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Alexnake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on :
    screen.update()
    time.sleep(0.1)
    snake.move()
   
    # Detect collision with food.
    if snake.head.distance(food) < 13 :
        # food의 크기가 10x10이므로
        food.refresh()

screen.exitonclick()