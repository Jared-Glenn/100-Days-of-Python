from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.score = 0
        self.high_score = 0
        self.check_high_score()

    def check_high_score(self):
        with open("data.txt") as data:
            self.high_score = int(data.read())

    def new_high_score(self):
        with open("data.txt", "w") as data:
            data.write(str(self.high_score))

    def display(self):
        self.undo()
        self.goto(0, 250)
        self.write(f"Score: {self.score} --- High Score: {self.high_score}", align='center', font=('Arial', 15, 'normal'))

    def score_up(self):
        self.score += 1

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.new_high_score()
        self.score = 0
        self.display()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align='center', font=('Arial', 20, 'normal'))