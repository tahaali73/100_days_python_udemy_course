import turtle as t
import time
from snake import Snake
import food
import scorecard


screen=t.Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)

snake1 = Snake()
FOOd = food.Food()
score = scorecard.ScoreCard()

screen.listen()
screen.onkey(snake1.up,"Up") 
screen.onkey(snake1.down,"Down") 
screen.onkey(snake1.right,"Right") 
screen.onkey(snake1.left,"Left") 

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake1.move()
    
    
    if snake1.head.distance(FOOd) < 15:
        snake1.extend_snake()
        score.inc_scr()
        FOOd.refresh()

    if snake1.head.xcor() < -290 or snake1.head.xcor() > 290 or snake1.head.ycor() < -290 or snake1.head.ycor() > 290:
        score.gameover()
        game_is_on = False
    
    for segment in snake1.all_turtles[1:]:
        if snake1.head.distance(segment) < 10:
            game_is_on = False
            score.gameover()
   



screen.exitonclick()
