from turtle import Screen
from ball import Ball
from wall import Wall
from paddle import Paddle
from scoreboard import Scoreboard
import time


screen = Screen()
game_speed = 0.02
running = True

screen.bgcolor("black")
screen.title("Breakout")
screen.setup(width=600, height=800 )
screen.tracer(0)

screen.listen()

ball = Ball()

# CREATE WALL
wall = Wall()
wall.build_wall()

# CREATE PADDLE
paddle = Paddle()
paddle.make_paddle()

screen.onkeypress(paddle.paddle_go_left, "a")
screen.onkeypress(paddle.paddle_go_left, "Left")
screen.onkeypress(paddle.paddle_go_right, "d")
screen.onkeypress(paddle.paddle_go_right, "Right")

# BOUNCE DELAYS
x_updates = 0
y_updates = 0
brick_updates = 0
paddle_updates = 0

# SCOREBOARD
scoreboard = Scoreboard()

while running:
    screen.update()
    if ball.ycor() >= 380 and y_updates == 0:
        ball.top_bounce()
        y_updates = 3
    if (ball.xcor() <= -280 or ball.xcor() >= 280) and x_updates == 0:
        ball.side_bounce()
        x_updates = 3
    if y_updates > 0:
        y_updates -= 1
    if x_updates > 0:
        x_updates -= 1

    if brick_updates == 0:
        for brick in wall.bricks:
            if ball.distance(brick) < 25 and brick.ycor() - 25 <= ball.ycor() <= brick.ycor() + 20:
                ball.top_bounce()
                wall.destroy(brick)
                scoreboard.score += 5
                brick_updates = 1
            elif ball.distance(brick) < 45 and brick.xcor() - 40 <= ball.xcor() <= brick.xcor() + 40 \
                    and brick.ycor() - 20 <= ball.ycor() <= brick.ycor() + 15:
                ball.side_bounce()
                wall.destroy(brick)
                scoreboard.score += 5
                brick_updates = 1
    if brick_updates > 0:
        brick_updates -= 1

    if paddle_updates == 0:
        if ball.distance(paddle.left) < 25:
            ball.left_paddle_bounce()
            paddle_updates = 3
        elif ball.distance(paddle.right) < 25:
            ball.right_paddle_bounce()
            paddle_updates = 3
        elif ball.distance(paddle.middle) < 15 \
                and paddle.middle.ycor() - 20 <= ball.ycor() <= paddle.middle.ycor() + 20\
                and paddle.middle.xcor() - 70 <= ball.xcor() <= paddle.middle.xcor() + 70:
            ball.middle_paddle_bounce()
            paddle_updates = 3
    if paddle_updates > 0:
        paddle_updates -= 1

    if ball.ycor() <= -400:
        ball.destroy()
        scoreboard.lives -= 1
        scoreboard.update_board()
        if scoreboard.lives == 0:
            running = False
        time.sleep(1)
        ball.create()

    if len(wall.bricks) == 0:
        ball.destroy()
        scoreboard.score += 100
        scoreboard.update_board()
        time.sleep(1)
        wall.build_wall()
        game_speed /= 2
        ball.create()



    ball.movement()
    scoreboard.update_board()
    time.sleep(game_speed)

screen.exitonclick()