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
screen.onkey(player.down, "Down")
screen.onkey(player.left, "Left")
screen.onkey(player.right, "Right")

screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    new_car = car_manager.create_new_car()
    car_manager.move_cars()

    if player.ycor() > 280:
        scoreboard.update_score()
        player.reset_player()
        car_manager.level_up()

    for car in car_manager.all_cars:
        if player.distance(car) < 20 or player.distance(car) < -10:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()
