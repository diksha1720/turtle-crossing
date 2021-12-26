from turtle import Turtle

STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.move_speed = 0.1

    def move(self):
        self.forward(10)

    def restart(self):
        self.move_speed *= 0.6
        self.goto(STARTING_POSITION)
