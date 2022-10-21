from turtle import Turtle


class Start(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 80)
        self.count = 5
        self.color("white")
        self.write("Game Starting In ...", align="center", font=("Consolas", 30, "bold"))

    def countdown(self):
        if self.count < 5:
            self.undo()
        self.goto(0, 0)
        self.write(f"{self.count}", align="center", font=("Consolas", 50, "normal"))
        self.count -= 1

    def draw_divider(self):
        y_coord = -300
        self.shape("square")
        self.shapesize(2, 0.75)

        while y_coord < 240:
            self.setpos(0, y_coord)
            self.stamp()
            y_coord += 100

        self.goto(0, 220)
        self.write("SCORE", align="center", font=("Consolas", 50, "bold"))