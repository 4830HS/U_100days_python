# 1. Create the screen
# 5. Detect collision with wall and bounce
# - The screen is 600px tall. Detect collisions with the top and bottom walls. Change the ball's movement direction upon collision.

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
# 볼의 움직임을 둔화시키기 위한 방법 2 : time 모듈 임포트
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Pong")
# turtle 애니메이션을 끄려면 tracer 애니메이션 메소드에 0을 인자로 삽입
# 추후 다시 turtle을 화면에 표시하려면 turtle을 만든 뒤, line 44에서 다시 화면 갱신
screen.tracer(0)

# # 2. Create and move a paddle
# # 3. Create another paddle

# # width = 20 / height = 100 / x_pos = 350 and -350 / y_pos = 0

# # My answer
# # starting_positions = [(350,0)]

# # for position in starting_positions : 
# #     new_segment = Turtle("square")
# #     new_segment.color("white")
# #     new_segment.goto(position)

# paddle = Turtle()
# paddle.shape("square")
# paddle.color("white")
# # 모든 turtle은 20x20로 시작함. 따라서 height는 x5
# paddle.shapesize(stretch_len=1, stretch_wid=5)
# paddle.penup()
# paddle.goto(350,0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
# screen.onkey(go_up, "Up")
# screen.onkey(go_down, "Down")

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on :
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280 :
        # needs to bounce -> ball.py에서 bounce method 만들 것
        ball.bounce_y()
    
    # 6-1. Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()

# 7. Detect when paddle misses
# Detect if the ball goes out of bounds at the edge of the screen. If yes, reset the ball's position to the center of the screen. The ball should then start moving towards the other player.
    # Detect R paddle misses
    # My answer
    # if ball.xcor() > 400 :
    #     ball = Ball()
    #     ball.bounce_x()
    if ball.xcor() > 400 :
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    # My answer
    # if ball.xcor() < -400 :
    #     ball = Ball()
    if ball.xcor() < -400 :
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()