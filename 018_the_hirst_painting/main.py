import colorgram
from turtle import Turtle, Screen, colormode
import random

colormode(255)
tim = Turtle()
tim.hideturtle()
tim.penup()
tim.speed(0)

colors = colorgram.extract("hirst_art.jpg", 35)
color_list = []

for x in range(len(colors)):
    rgb = colors[x].rgb
    tup = (rgb[0], rgb[1], rgb[2])
    color_list.append(tup)

for x in range(5):
    color_list.pop(0)

for x in range(1, 19):
    tim.setpos(-450, ((x*50) - 500))
    for y in range(1, 19):
        tim.dot(20, random.choice(color_list))
        tim.forward(55)


screen = Screen()

screen.exitonclick()