from scoreboard import Score
from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Brick, row1, row2, row3
from game_over import GameOver
import time



screen = Screen()
screen.bgcolor('black')
screen.setup(width=700, height=700)
screen.title('Breakout')
screen.tracer(0)

row1_bricks = []
row2_bricks = []
row3_bricks = []

breakout_paddle = Paddle((0, -190))
breakout_paddle.speed(0)
ball = Ball((0, -100))
for i in row1:
    r1_brick = Brick(i)
    row1_bricks.append(r1_brick)
for i in row2:
    r2_brick = Brick(i)
    row2_bricks.append(r2_brick)
for i in row3:
    r3_brick = Brick(i)
    row3_bricks.append(r3_brick)

game_score = 0
score = Score()
score.write(f"Score: {game_score}", font=("Verdana", 18, "normal"))


def update_score():
    global game_score
    game_score += 1
    score.clear()
    score.write(f"Score: {game_score}", font=("Verdana", 18, "normal"))



screen.listen()
screen.onkey(breakout_paddle.up, "Right")
screen.onkey(breakout_paddle.down, "Left")

ball_location = (ball.xcor(), ball.ycor())
paddle_location = (breakout_paddle.xcor(), breakout_paddle.ycor())




game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() <= -340:
        game = GameOver()
        game.write("GAME OVER!!", font=("Times", 25, "bold"))
        break
    elif ball.ycor() >= 340:
        ball.bounce_vertical()
    elif ball.pos() == (-330, 330) or ball.pos() == (330, 330):
        ball.bounce_vertical()
    elif ball.xcor() >= 320 or ball.xcor() <= -320:
        ball.bounce_horizontal()
    elif ball.distance(breakout_paddle) < 70 and ball.ycor() == -160:
        ball.collision()
    elif game_score == 18:
        game = GameOver()
        game.write("CONGRATS!!", font=("Times", 25, "bold"))
        break
    for i in row1_bricks:
        if ball.ycor() >= 280 and ball.distance(i) <= 50:
            ball.collision()
            i.delete_brick()
            update_score()
    for i in row2_bricks:
        if ball.ycor() >= 250 and ball.distance(i) <= 50:
            ball.collision()
            i.delete_brick()
            update_score()
    for i in row3_bricks:
        if ball.ycor() >= 220 and ball.distance(i) <= 50:
            ball.collision()
            i.delete_brick()
            update_score()


screen.exitonclick()