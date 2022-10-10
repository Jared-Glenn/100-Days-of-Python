from turtle import Turtle
import random

class Car(Turtle):
    def __init__(self, y):
        super().__init__()
        self.move_speed = 5
        self.speed("fastest")
        self.shape("square")
        self.shapesize(1, 2)
        random_color = random.choice(["red", "orange", "yellow", "green", "blue", "purple"])
        self.color(random_color)
        self.penup()
        self.goto(310, y)

    def drive(self):
        self.setx(self.xcor() - self.move_speed)

