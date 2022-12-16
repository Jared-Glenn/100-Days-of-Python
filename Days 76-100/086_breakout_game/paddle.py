from turtle import Turtle


class Paddle:
    def __init__(self):
        self.speed = 50
        self.left = None
        self.middle = None
        self.right = None

    def make_paddle(self):
        self.left = LeftPaddle()
        self.middle = MiddlePaddle()
        self.right = RightPaddle()

    def paddle_go_left(self):
        if self.left.xcor() > -280:
            self.left.setx(self.left.xcor() - self.speed)
            self.middle.setx(self.middle.xcor() - self.speed)
            self.right.setx(self.right.xcor() - self.speed)

    def paddle_go_right(self):
        if self.right.xcor() < 280:
            self.left.setx(self.left.xcor() + self.speed)
            self.middle.setx(self.middle.xcor() + self.speed)
            self.right.setx(self.right.xcor() + self.speed)


class LeftPaddle(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.shapesize(0.4, 1.5)
        self.color("white")
        self.right(44)
        self.penup()
        self.goto(-40, -310)


class MiddlePaddle(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.shapesize(0.4, 3)
        self.color("white")
        self.penup()
        self.goto(0, -320)


class RightPaddle(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.shapesize(0.3, 1.5)
        self.color("white")
        self.right(-44)
        self.penup()
        self.goto(40, -310)