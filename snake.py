import turtle as t

FORWARD = 20
COLORS=["white","orange","red"]
POSITION = [(0,0),(-20,0),(-40,0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.all_turtles = []
        self.make_snake()
        self.head = self.all_turtles[0]

    def make_snake(self):
        for position in POSITION:
            self.add_snake(position)
            
    def add_snake(self,position):
        new_turtle = t.Turtle()
        new_turtle.up()
        new_turtle.shape("square")
        new_turtle.color(COLORS[0])
        new_turtle.goto(position)
        self.all_turtles.append(new_turtle)
    
    def extend_snake(self):
        self.add_snake(self.all_turtles[-1].position())
    
    def move(self):
        for turttle in range(len(self.all_turtles)-1,0,-1):
            first_turtle_x_cordinates = self.all_turtles[turttle -1].xcor()
            first_turtle_y_cordinates = self.all_turtles[turttle -1].ycor()
            self.all_turtles[turttle].goto(first_turtle_x_cordinates,first_turtle_y_cordinates)
        self.head.forward(FORWARD)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
             self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
           self.head.setheading(RIGHT)