import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# speed = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.speed = 5

    def create_new_car(self):
        self.penup()
        self.hideturtle()
        self.shape("square")
        self.setheading(180)
        self.goto(270, 0)
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2, outline=1)
        RANDOM_POSITION = random.randint(0, 280)
        self.setposition(270, RANDOM_POSITION)
        self.showturtle()
        # self.car_move()

    def car_move(self, speed):
        self.forward(speed)
