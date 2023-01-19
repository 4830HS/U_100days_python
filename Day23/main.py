import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # 3. Detect collision with car
    # 거북이와 자동차의 충돌이 감지되면 게임을 멈추세요. 풀다가 막히면, 5단계 설명 영상을 확인해 보세요.
    for car in car_manager.all_cars :
        if car.distance(player) < 20 :
            game_is_on = False
            scoreboard.game_over()

    # 4. Detect when turtle reaches the other side
    # 거북이가 화면의 위쪽 가장자리(즉, FINISH_LINE_Y)에 도달했는지 감지하고, 도달했다면 거북이를 시작 위치로 다시 보내고 자동차의 속도를 올리세요. 힌트) MOVE_INCREMENT 속성을 만들어서 자동차 속도를 증가시켜 보세요. 풀다가 막히면, 6단계 풀이 영상을 확인해 보세요.
    if player.is_at_finish_line() :
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()