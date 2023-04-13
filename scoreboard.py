from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.color("black")
        self.goto(-100, 180)
        self.write(self.score, align="center", font=FONT)

    # def update_score(self):
    #