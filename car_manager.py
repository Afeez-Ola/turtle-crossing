import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
# RANDOM_POSITION = 0


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        # self.shape("square")
        # self.penup()
        # for i in range(5):
        #     RANDOM_POSITION = random.randint(0, 280)
        #     self.setposition(270, RANDOM_POSITION)
        #     print(RANDOM_POSITION)
        # self.color(random.choice(COLORS))
        # self.shapesize(stretch_wid=2, stretch_len=1, outline=1)
        # self.setheading(90)
        # self.forward(STARTING_MOVE_DISTANCE)
        self.create_new_car()

    def create_new_car(self):
        for i in range(5):
            RANDOM_POSITION = random.randint(0, 280)
            self.setposition(270, RANDOM_POSITION)
            print(RANDOM_POSITION)

        self.shape("square")
        self.penup()
        self.color(random.choice(COLORS))
        self.forward(STARTING_MOVE_DISTANCE)
        self.shapesize(stretch_wid=2, stretch_len=1, outline=1)
        self.setheading(90)

    def car_move(self):
        for _ in range(10):
            self.create_new_car()
            self.forward(STARTING_MOVE_DISTANCE)
            new_x = self.xcor() - 10
            # for i in range(5):
            #     RANDOM_POSITION = random.randint(0, 280)
            #     self.setposition(270, RANDOM_POSITION)
            #     print(RANDOM_POSITION)
            RANDOM_POSITION = random.randint(0, 280)
            self.goto(new_x, RANDOM_POSITION)
