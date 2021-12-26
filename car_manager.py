from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []

    def create_car(self):
        new_car = Turtle()
        new_car.color(random.choice(COLORS))
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=3)
        new_car.penup()
        y_val = random.randint(-240, 240)
        new_car.goto(280, y_val)
        new_car.setheading(180)
        self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            car.forward(MOVE_INCREMENT)









