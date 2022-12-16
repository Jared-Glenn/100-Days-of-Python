from turtle import Turtle
from random import choice


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_speed = 15
        self.y_speed = 15
        self.x_move = self.x_speed * choice([1, -1])
        self.y_move = self.y_speed * (-1)
        self.create()

    def create(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 100)

    def movement(self):
        self.setx(self.xcor() + self.x_move)
        self.sety(self.ycor() + self.y_move)

    def side_bounce(self):
        self.x_move *= -1

    def top_bounce(self):
        self.y_move *= -1

    def middle_paddle_bounce(self):
        self.y_move *= -1

    def left_paddle_bounce(self):
        self.y_move *= -1
        self.x_move = abs(self.x_move)

    def right_paddle_bounce(self):
        self.y_move *= -1
        self.x_move = abs(self.x_move) * -1

    def destroy(self):
        self.reset()