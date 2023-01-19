# 1. Move the turtle with keypress

from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle) :
    def __init__(self) :
        super().__init__()
        self.shape("turtle")
        self.penup()
        # self.goto(STARTING_POSITION)
        self.go_to_start()
        self.setheading(90)

    def move(self) :
        # My answer
        # new_y = self.ycor() + 10
        # self.goto(0,new_y)
        self.forward(MOVE_DISTANCE)

    # 4. Detect when turtle reaches the other side
    # 거북이가 화면의 위쪽 가장자리(즉, FINISH_LINE_Y)에 도달했는지 감지하고, 도달했다면 거북이를 시작 위치로 다시 보내고 자동차의 속도를 올리세요. 힌트) MOVE_INCREMENT 속성을 만들어서 자동차 속도를 증가시켜 보세요. 풀다가 막히면, 6단계 풀이 영상을 확인해 보세요.
    def go_to_start(self) :
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self) :
        if self.ycor() > FINISH_LINE_Y :
            return True
        else : 
            return False