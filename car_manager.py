import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager:
    def __init__(self):

        self.all_cars = []

    def create_new_car(self, ):
        num_of_cars = random.randint(1, 6)
        if num_of_cars == 1:
            car = Turtle("square")

            car.penup()
            car.hideturtle()
            car.setheading(180)
            car.goto(270, 0)
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2, outline=1)
            RANDOM_POSITION = random.randint(-250, 280)
            car.setposition(300, RANDOM_POSITION)
            car.showturtle()
            self.all_cars.append(car)
            return car

    def car_move(self, speed):
        for car in self.all_cars:
            car.forward(speed)

