import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(random.choice(COLORS))
        self.setposition(0, random.randint(0, 280))
        self.shapesize(stretch_wid=2, stretch_len=1, outline=1)
        self.setheading(90)
        self.forward(STARTING_MOVE_DISTANCE)


