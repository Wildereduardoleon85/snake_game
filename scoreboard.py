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
        self.color("white")
        self.update()

    def increase(self):
        self.clear()
        self.score += 1
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def print_game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
