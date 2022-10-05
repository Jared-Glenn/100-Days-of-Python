from turtle import Turtle, Screen, colormode
from random import randint
import random

tim = Turtle()
tim.shape("turtle")
tim.speed("fastest")
colormode(255)

# tim.penup()
# tim.goto(-500, 0)
# tim.pendown()
#
# for _ in range(50):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# for x in range(3, 11):
#     degrees = 360 / x
#     tim.color(randint(0, 255),
#               randint(0, 255),
#               randint(0, 255))
#     for _ in range(x):
#         tim.forward(100)
#         tim.right(degrees)


# tim.pensize(10)
#
# for _ in range(200):
#     tim.color(randint(0, 255),
#               randint(0, 255),
#               randint(0, 255))
#     direction = random.choice([0, 90, 180, 270])
#     tim.setheading(direction)
#     tim.forward(50)

# tim.pensize(2)

# def random_color():
#     tim.color(randint(0, 255),
#               randint(0, 255),
#               randint(0, 255))
#
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         random_color()
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)

# for _ in range(60):
#
#     tim.circle(100, 180)
#     for _ in range(15):
#         tim.circle(200)
#         tim.setheading(tim.heading() + 10)
#     tim.setheading(tim.heading() + 180)
#     tim.circle(100, 180)
#     tim.setheading(tim.heading() + 10)

draw_spirograph(1)

screen = Screen()















screen.exitonclick()