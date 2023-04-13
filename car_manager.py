import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
RANDOM_POSITION = random.randint(0, 280)

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.setposition(270, RANDOM_POSITION)
        self.color(random.choice(COLORS))

        self.shapesize(stretch_wid=2, stretch_len=1, outline=1)
        self.setheading(90)


    def car_move(self):
        self.forward(STARTING_MOVE_DISTANCE)
        new_x = self.xcor() - 10
        self.goto(new_x, RANDOM_POSITION)



