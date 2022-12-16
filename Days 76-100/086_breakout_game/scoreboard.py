from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.penup()
        self.color("white")
        self.score = 0
        self.lives = 3

        self.update_board()

    def update_board(self):
        self.clear()
        self.goto(-150, 350)
        hearts = ""
        for life in range(self.lives):
            hearts += "❤"
        self.write(f"Lives: {hearts}", align="center", font=("Ariel", 30, "bold"))
        self.goto(175, 350)
        display_score = format(self.score, "03d")
        self.write(f"Score: {display_score}", align="center", font=("Ariel", 30, "bold"))