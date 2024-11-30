import turtle as t
import random


race_status = False
positions = [-90,-50,-10,30,70,110]
colors=["orange","red","green","blue","yellow","purple"]
all_turtles=[]
user_bet = t.textinput("bet on turtle","write the color of turtle in box you want to bet on")



line = t.Turtle()
line.color('red')
line.shape('turtle')
screen = t.Screen()
screen.screensize(320,300)
line.up()
line.goto(160,150)
line.right(90)
line.down()
line.forward(300)


for turtels in range(6):
    new_tutle = t.Turtle()
    new_tutle.color(colors[turtels])
    new_tutle.shape('turtle')
    new_tutle.up()
    new_tutle.goto(-160,positions[turtels])
    all_turtles.append(new_tutle)

if user_bet:
    race_status=True

while race_status:

    for turtle in all_turtles:
        turtle.forward(random.randint(0,10))
        if turtle.xcor() > 145:
            if turtle.pencolor() == user_bet:
                turtle.write("you lossed,\n better luck next time", move=False, align='left', font=('Arial', 20, 'bold'))
            else: turtle.write("you wint the game", move=False, align='left', font=('Arial', 20, 'bold'))
            race_status=False

screen.exitonclick()