from turtle import Turtle


class Brick(Turtle):
    def __init__(self, xcord, ycord, color):
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.shapesize(.6, 2)
        self.color(color)
        self.penup()
        self.goto(xcord, ycord)