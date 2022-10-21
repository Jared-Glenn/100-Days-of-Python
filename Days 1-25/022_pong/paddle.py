from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, xcord):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(5, 1)
        self.color("white")
        self.setpos(xcord, 0)

    def go_up(self):
        if self.ycor() <= 250:
            self.sety(self.ycor() + 30)

    def go_down(self):
        if self.ycor() >= -230:
            self.sety(self.ycor() - 30)

    def automove(self):
        if self.ycor() >= 250:
            self.direction = "Down"
        if self.ycor() <= -230:
            self.direction = "Up"
        if self.direction == "Up":
            self.go_up()
        else:
            self.go_down()