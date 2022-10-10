from turtle import Turtle


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level_number = 1
        self.speed("fastest")
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-280, 260)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.level_number}", align="left", font=("Consolas", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Consolas", 20, "normal"))