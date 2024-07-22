from turtle import Turtle


class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.position = position
        self.color('white')
        self.shape('square')
        self.speed('fastest')
        self.setheading(90)
        self.turtlesize(1, 5)
        self.setposition(position)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
