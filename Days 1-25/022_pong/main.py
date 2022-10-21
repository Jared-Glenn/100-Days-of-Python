from turtle import Screen
from paddle import *
from ball import *
from scoreboard import *
from start import *
import time

#num_players = int(input("Number of players: (Enter 1 or 2) "))
num_players = 2

screen = Screen()
game_speed = 0.1
player_2 = None
computer = None

screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600 )
screen.tracer(0)

player_1 = Paddle(-350)
if num_players == 1:
    computer = Paddle(350)
else:
    player_2 = Paddle(350)
running = True


screen.listen()
screen.onkeypress(player_1.go_up, "w")
screen.onkeypress(player_1.go_down, "s")
if player_2:
    screen.onkeypress(player_2.go_up, "Up")
    screen.onkeypress(player_2.go_down, "Down")

start = Start()
for _ in range(5):
    screen.update()
    start.countdown()
    time.sleep(1)
start.clear()
start.draw_divider()

ball = Ball()
scoreboard = Scoreboard()

while running:
    screen.update()
    if ball.ycor() <= -280 or ball.ycor() >= 280:
        ball.bounce()
    if ball.xcor() <= -380:
        scoreboard.p2_score += 1
        scoreboard.score()
        ball.color("black")
        ball.destroy()
        ball = Ball()
    if ball.xcor() >= 380:
        scoreboard.p1_score += 1
        scoreboard.score()
        ball.color("black")
        ball.destroy()
        ball = Ball()
    if computer:
        computer.automove()
        if (ball.distance(computer) < 50 and ball.xcor() > 320) or (
                ball.distance(player_1) < 50 and ball.xcor() < -320):
            ball.block()
    else:
        if (ball.distance(player_2) < 100 and ball.xcor() > 320) or (
                ball.distance(player_1) < 100 and ball.xcor() < -320):
            ball.block()
    ball.ball_movement()
    time.sleep(game_speed)


screen.exitonclick()