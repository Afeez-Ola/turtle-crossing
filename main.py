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
    car_manager.create_new_car()
    car_manager.car_move()

    print(player.distance(car_manager.all_cars))





screen.exitonclick()