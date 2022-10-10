from turtle import Turtle, Screen
from player import Player
from car import Car
from lanes import Lanes
from level import Level
import time

screen = Screen()
screen.setup(600, 600)
screen.title("Turtle Crossing")
screen.bgcolor("white")
screen.tracer(0)
running = True

player = Player()
player.go_up()

lanes = Lanes()
lanes.setup()
counter = 9

level = Level()
game_speed = 0.09

screen.listen()
screen.onkeypress(player.go_up, "w")
screen.onkeypress(player.go_up, "Up")

while running:
    screen.update()
    if counter >= 9:
        lanes.incoming()
        counter = 0
    counter += 1
    lanes.traffic()
    time.sleep(game_speed)
    for car in lanes.cars:
        if player.distance(car) < 25 and player.ycor() <= (car.ycor() + 10):
            running = False
            level.game_over()
    if player.ycor() >= 300:
        level.level_number += 1
        level.update()
        player.back_to_start()
        game_speed *= 0.5





screen.exitonclick()