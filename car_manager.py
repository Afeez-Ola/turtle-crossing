import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_POSITION = (270, 0)
MOVE_DISTANCE = 10
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_DISTANCE
        self.key = 6

    def create_new_car(self):
        num_of_cars = random.randint(3, self.key)
        if num_of_cars == 3:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2, outline=1)
            car.color(random.choice(COLORS))
            RANDOM_POSITION = random.randint(-250, 280)
            car.goto(300, RANDOM_POSITION)
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        self.key += -1
