import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
car_manager = CarManager()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.onkey(player.up, "Up")
screen.listen()

# car_manager.create_new_car()
# car_manager.create_new_car()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for i in range(10):
        car_manager.create_new_car()
        car_manager.car_move()


screen.exitonclick()