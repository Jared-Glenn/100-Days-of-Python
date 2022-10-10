from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.move_speed = 10
        self.speed("fastest")
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.left(90)
        self.goto(0, -280)

    def go_up(self):
        self.sety(self.ycor() + self.move_speed)

    def back_to_start(self):
        self.goto(0, -280)