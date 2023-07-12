from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.high_score = self.read_score_from_file()
        self.color("white")
        self.update()

    def increase(self):
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_score_to_file()
        self.score = 0
        self.update()

    def write_score_to_file(self):
        with open("high_score.txt", mode="w") as file:
            file.write(str(self.high_score))

    def read_score_from_file(self):
        with open("high_score.txt") as file:
            content = file.read()
            return int(content)
