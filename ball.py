from turtle import Turtle
import time
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.shapesize(1, 1)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_collision(self):
        self.y_move *= -1

    def player_collision(self):
        time.sleep(0.05)
        self.x_move *= -1

    # def player2_collision(self):
    #     self.y_move *= 1
    #     self.x_move *= -1
    #     self.x_move += random.randint(0, 10)
    #     self.y_move += random.randint(-7, 0)

    def reset_button(self):
        self.speed(5)
        self.goto(0, 0)
        self.x_move *= -1  # Change direction
        self.y_move *= random.choice([-1, 1])

    # else:
    #     new_x = self.xcor() - 10
    #     new_y = self.ycor() - 10
    #     self.goto(new_x, new_y)
