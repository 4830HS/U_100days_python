# 5. Create a scroeboard
# 현재 게임 레벨을 보여주는 점수판을 만드세요. 거북이가 성공적으로 길을 건널 때마다 레벨이 올라갑니다. 거북이와 자동차가 부딪히면 화면 중앙에 ‘게임 종료’가 표시되어야 합니다. 풀다가 막히면, 7단계 설명 영상을 확인해 보세요.

from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle) :

    def __init__(self) :
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.update_scoreboard()

    def update_scoreboard(self) :
        # 원래 점수를 지워주기 위해 clear 사용
        self.clear()
        self.write(f"Level : {self.level}", align = "left", font = FONT)

    def increase_level(self) :
        self.level += 1
        self.update_scoreboard()

    def game_over(self) :
        self.goto(0,0)
        self.write(f"GAME OVER", align = "center", font = FONT)