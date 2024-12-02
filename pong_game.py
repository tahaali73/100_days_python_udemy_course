import turtle as t
from slab import Slab
from ball import Ball
import time

screen = t.Screen()

screen.bgcolor("black")
screen.setup(700,600)
screen.title("PONG")
screen.tracer(0)

left_paddle = Slab((-320,0))
right_padlle = Slab((320,0))
Pong_ball = Ball()

game_is_on = True

screen.listen()
screen.onkeypress(right_padlle.go_up,"Up")
screen.onkeypress(right_padlle.go_down,"Down")
screen.onkeypress(left_paddle.go_up,"w")
screen.onkeypress(left_paddle.go_down,"s")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    Pong_ball.move()

    if Pong_ball.ycor() > 280 or Pong_ball.ycor() < -280:
        Pong_ball.bounce()
    
    if Pong_ball.distance(right_padlle) < 50 and Pong_ball.xcor() > 300 or Pong_ball.distance(left_paddle) < 50 and Pong_ball.xcor() < -300:
        Pong_ball.x_bounce()
    
    if Pong_ball.xcor() > 360:
        Pong_ball.reset_ball()
        

    if Pong_ball.xcor() < -360:
        Pong_ball.reset_ball()


screen.exitonclick()