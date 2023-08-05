
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        f = open("data.txt")
        self.write(f"score: {self.score} high score:{f.read()}", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            file = open("data.txt", mode="w")
            file.write(str(self.high_score))
            file.close()
        self.score = 0
        self.update()

    def scores(self):
        self.score += 1
        self.update()