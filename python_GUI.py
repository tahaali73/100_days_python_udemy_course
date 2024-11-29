from turtle import Turtle, Screen, forward,right
size = 90
sides = 2
turtle1 = Turtle()
for i in range(8):
   sides +=1
   a = 360/sides
   size +=10
   for x in range(0,sides,1):
    forward(100)
    right(a)



screen = Screen()
screen.exitonclick()