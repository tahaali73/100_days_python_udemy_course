from turtle import Turtle

class Slab(Turtle):


    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)

    def go_up(self):
        if self.ycor() < 250:
            y = self.ycor() + 25
            self.goto(self.xcor(), y)

    def go_down(self):
        if self.ycor() > -250:
            y = self.ycor() - 25
            self.goto(self.xcor(), y)