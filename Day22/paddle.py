# 2. Create and move a paddle
# 3. Create another paddle

# Refactor the code. Create a paddle.py file for the Paddle class
# The Paddle class needs to inherit from Turtle
# Paddle objects need to be initialised with a tuple for the X and Y coordinates.
# The l_paddle needs to move up and down with the "w" and "s" keys

from turtle import Turtle

# 패들 객체가 터틀 객체가 되도록 터틀 클래스 상속받기
class Paddle(Turtle) : 
    def __init__(self, position) :
        super().__init__()
        # paddle = Turtle() <- 삭제(∵ Paddle 클래스 자체가 터틀 클래스이므로)
        # 또한, paddle.shape("square") 등의 paddle을 모두 self로 바꿔줌
        self.shape("square")
        self.color("white")
        # # 모든 turtle은 20x20로 시작함. 따라서 height는 x5
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        # self.goto(350,0) -> position으로 변경
        self.goto(position)

# def go_up() :
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(), new_y)

# def go_down() :
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(), new_y)

    # 메소드의 첫 번째 매개변수는 항상 self
    # paddle 역시 self로 변경
    def go_up(self) :
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self) :
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)