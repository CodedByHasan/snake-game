from turtle import Turtle
from .constants import ALIGNMENT, FONT, HIGH_SCORE


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        with open(HIGH_SCORE, mode="r", encoding="utf-8") as data:
            self.high_score = int(data.read())

        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.speed("fastest")
        self.hideturtle()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(HIGH_SCORE, mode="w", encoding="utf-8") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()
