from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.level = 1
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"Level : {self.level}", align="center", font=FONT)

    def add_point(self):
        self.level += 1
        self.score_update()

    def game_over(self):
        self.goto(0, 0)
        self.hideturtle()
        self.write("GAME OVER", align="center", font=FONT)


