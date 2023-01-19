from turtle import Turtle
import random

class Food(Turtle) :

    def __init__(self) :
        
        # Food 클래스가 터틀 클래스를 상속받게 함.(<- Food 클래스는 터틀 클래스가 할 수 있는 모든 일을 할 수 있게 됨.)
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        # food의 기본 크기가 20x20이므로
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self) :
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x, random_y)