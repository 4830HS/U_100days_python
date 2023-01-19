# 4. Create the ball and make it move

# width = 20, height = 20, x_pos = 0, y_pos = 0

from turtle import Turtle

class Ball(Turtle) :
    def __init__(self) :
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    # def move(self) :
    #     new_x = self.xcor() + 10
    #     new_y = self.ycor() + 10
    #     # 볼의 움직임을 둔화시키기 위한 방법 1 : 10 대신 1로 변경
    #     self.goto(new_x, new_y)

    def move(self) :
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self) :
        # 공이 위 아래로 튕겼을 때, 원래의 진행방향과 반대의 방향으로(감소 -> 증가, 증가 -> 감소) y 좌표를 바꿔주어야 함.
        # 위의 방법이 가능하게 하려면 우선 속성을 만들어야 함.(line 14-15)
        # 이후 line 24-25에서 10이라는 숫자 대신, self.x or y_move로 대체
        self.y_move *= -1

    def bounce_x(self) :
        self.x_move *= -1
        self.move_speed += 0.9

    def reset_position(self) :
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()