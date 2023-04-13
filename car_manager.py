import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
# RANDOM_POSITION = 0


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.shape("square")
        self.setheading(90)
        self.goto(270, 0)

        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=2, stretch_len=1, outline=1)

        self.create_new_car()

    def create_new_car(self):
        RANDOM_POSITION = random.randint(0, 280)
        self.setposition(270, RANDOM_POSITION)
        self.showturtle()

    def car_move(self):
        self.forward(STARTING_MOVE_DISTANCE)
