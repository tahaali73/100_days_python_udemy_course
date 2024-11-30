import random
import turtle as t
"""import colorgram

COLOR = []
colors = colorgram.extract('image.jpg',30)


for color in colors:
    r = color.rgb.r
    b = color.rgb.b
    g = color.rgb.g
    COLOR.append((r,g,b))

print(COLOR)"""

colors =[(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

turlte = t.Turtle()
t.colormode(255)
screen = t.Screen()
screen.reset()
screen.setworldcoordinates(-100,-100,550,370)

t.hideturtle()
forwards = 30
for x in range(7):
   t.home()
   if x>0:
       t.left(90)
       t.forward(forwards)
       t.right(90)
       forwards += 30
   for i in range(12):
      new_color =random.choice(colors)
      t.color(new_color)
      t.dot(15)
      t.up()
      t.forward(30)
      t.down()
      t.dot(15)


screen.exitonclick()
