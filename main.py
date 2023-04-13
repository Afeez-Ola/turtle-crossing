import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.onkey(player.up, "Up")
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    new_car = car_manager.create_new_car()
    car_manager.car_move()

    # if player.ycor() > 290:
    #     scoreboard.update_score()

    for car in car_manager.all_cars:
        if player.distance(car) < 25 or player.distance(car) < -25:
            game_is_on = False
screen.exitonclick()
