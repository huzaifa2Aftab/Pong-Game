from turtle import Turtle


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.position = position
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(position)
        self.score_update()

    def score_update(self):
        self.write(f' {self.score}', align='center', font=('Arial', 60, 'bold'))

    def update(self):
        self.clear()
        self.score += 1
        self.score_update()

