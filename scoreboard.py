FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-280, 250)
        self.write_scoreboard()

    def write_scoreboard(self):
        self.write(f"Level {self.level}", align="left", font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.level += 1
        self.write_scoreboard()


    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
