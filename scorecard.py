from turtle import Turtle

class ScoreCard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score_update()

    def score_update(self):
         self.goto(0,270)
         self.write(f"score is {self.score}", move=False, align='center', font=('Arial', 18, 'normal'))

    def gameover(self):
        self.goto(0,0)
        self.write("Game Over", move=False, align='center', font=('Arial', 18, 'normal'))
    
    def inc_scr(self):
        self.score += 1
        self.clear()
        self.score_update()
