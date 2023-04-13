import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_SPEED = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):

        self.all_cars = []

    def create_new_car(self, car_position):
        num_of_cars = random.randint(1, 6)
        if num_of_cars == 1:
            car = Turtle("square")
            car_position = car.position()
            car.penup()
            car.hideturtle()
            car.setheading(180)
            car.goto(270, 0)
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2, outline=1)
            RANDOM_POSITION = random.randint(-280, 280)
            car.setposition(300, RANDOM_POSITION)
            car.showturtle()
            car.position()
            self.all_cars.append(car)

    def car_move(self):
        for car in self.all_cars:
            car.forward(STARTING_SPEED)


