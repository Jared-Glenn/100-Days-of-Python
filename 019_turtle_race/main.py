from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_back():
    tim.back(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def clear_screen():
    screen.resetscreen()

screen.listen()
screen.onkeypress(move_forwards, "w")
screen.onkeypress(move_back, "s")
screen.onkeypress(turn_left, "a")
screen.onkeypress(turn_right, "d")
screen.onkey(clear_screen, "c")

screen.exitonclick()