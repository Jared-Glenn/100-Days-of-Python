from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
running = False

colors = {
    "red": (1.0, 0.0, 0.0),
    "orange": (1.0, 0.5294117647058824, 0.0),
    "yellow": (1.0, 0.9882352941176471, 0.19215686274509805),
    "green": (0.01568627450980392, 0.5450980392156862, 0.14901960784313725),
    "blue": (0.0, 0.3058823529411765, 0.8),
    "indigo": (0.34509803921568627, 0.0392156862745098, 1.0),
    "violet": (0.7450980392156863, 0.0392156862745098, 1.0),
}

turtle_list = []
y_pos = -110

for color in colors:
    new = Turtle(shape="turtle")
    new.penup()
    new.color(colors[color])
    new.goto(-210, y_pos)
    y_pos += 40
    turtle_list.append(new)

if user_bet:
    running = True

while running:
    for turtle in turtle_list:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            for color in colors:
                if colors[color] == winning_color:
                    winner = color
            running = False
            if colors[user_bet] == winning_color:
                print(f"You've won! {winner.capitalize()} is the winning turtle!")
            else:
                print(f"You've lost. {winner.capitalize()} is the winning turtle.")

screen.exitonclick()