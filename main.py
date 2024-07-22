import time
from turtle import Screen
from ball import Ball
from players import Player
from score import Score
speed_ball = 0.1
screen = Screen()


screen.bgcolor('black')
screen.title('Pong')
screen.setup(width=800, height=600)
screen.tracer(0)
bounce_ball = Ball()
player_1 = Player((350, 0))
player_2 = Player((-350, 0))
player_1_score = Score((100, 220))
player_2_score = Score((-100, 220))

screen.listen()
screen.onkeypress(player_1.up, "w")
screen.onkeypress(player_1.down, "s")
screen.onkeypress(player_2.up, "o")
screen.onkeypress(player_2.down, "l")

run = True

while run:
    time.sleep(speed_ball)
    screen.update()
    bounce_ball.move()
    if bounce_ball.ycor() > 290 or bounce_ball.ycor() < -290:
        bounce_ball.wall_collision()

    if bounce_ball.distance(player_1) < 50 and bounce_ball.xcor() > 320 or bounce_ball.distance(player_2) < 50 and bounce_ball.xcor() < -320:
        speed_ball -= 0.01
        bounce_ball.player_collision()

    if bounce_ball.xcor() < -400:
        player_1_score.update()
        bounce_ball.reset_button()

    elif bounce_ball.xcor() > 400:
        player_2_score.update()
        bounce_ball.reset_button()

screen.exitonclick()
