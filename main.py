import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
player = Player()
score = Scoreboard()

cars = []
car = CarManager((280, 0))
cars.append(car)

screen.listen()
screen.onkey(player.move, "Up")


counter = 0
game_is_on = True
while game_is_on:
    counter += 1
    if counter % 6 == 0:
        y_val = random.randint(-240, 240)
        car = CarManager((280, y_val))
        cars.append(car)
    time.sleep(player.move_speed)
    screen.update()
    for c in cars:
        if player.distance(c) < 25:
            score.game_over()
            game_is_on = False
        c.move_car()
    if player.ycor() > 250:
        print("Level Up")
        score.add_point()
        player.restart()

screen.exitonclick()
