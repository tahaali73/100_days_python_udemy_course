from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_cor = random.randint(-270,270)
        y_cor = random.randint(-270,270)
        self.goto(x_cor,y_cor)