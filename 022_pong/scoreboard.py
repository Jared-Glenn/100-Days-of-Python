from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.penup()
        self.color("white")
        self.p1_score = 0
        self.p2_score = 0

        self.score()


    def score(self):
        self.clear()
        self.goto(-200, 190)
        self.write(f"{self.p1_score}", align="center", font=("Consolas", 50, "bold"))
        self.goto(200, 190)
        self.write(f"{self.p2_score}", align="center", font=("Consolas", 50, "bold"))

