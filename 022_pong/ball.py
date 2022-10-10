from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_speed = 15
        self.y_speed = 15
        self.x_move = self.x_speed * random.choice([-1, 1])
        self.y_move = self.y_speed * random.choice([-1, 1])
        self.create()

    def create(self):
        self.shape("circle")
        self.color("white")
        self.penup()

    def ball_movement(self):
        self.setx(self.xcor() + self.x_move)
        self.sety(self.ycor() + self.y_move)

    def bounce(self):
        self.y_move *= -1

    def block(self):
        self.x_move *= -1
        if self.x_move > 0:
            self.x_move += 2
        else:
            self.x_move -= 2

    def destroy(self):
        self.reset()
