from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.score = 0

    def display(self):
        self.undo()
        self.goto(0, 250)
        self.write(f"Score: {self.score}", align='center', font=('Arial', 15, 'normal'))

    def score_up(self):
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=('Arial', 20, 'normal'))