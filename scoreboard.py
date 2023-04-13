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
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def update_score(self):
        self.clear_score()
        self.score += 1
        self.write_score()

    def clear_score(self):
        self.clear()
        self.penup()
        self.color("black")
        self.goto(-100, 180)

    def game_over(self):
        self.clear_score()
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=FONT)
