from brick import Brick


class Wall:
    def __init__(self):
        self.bricks = []

    def build_section(self, ycord, color):
        xcords = [-275, -230, -185, -140, -95, -50, -5, 40, 85, 130, 175, 220, 265]
        for xcord in xcords:
            new_brick = Brick(xcord, ycord, color)
            self.bricks.append(new_brick)

    def build_wall(self):
        self.build_section(300, "red")
        self.build_section(283, "red")
        self.build_section(266, "orange")
        self.build_section(249, "orange")
        self.build_section(232, "green")
        self.build_section(215, "green")
        self.build_section(198, "yellow")
        self.build_section(181, "yellow")

    def destroy(self, brick):
        self.bricks.remove(brick)
        brick.reset()