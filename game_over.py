from turtle import Turtle

class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto((-100, 0))
        self.hideturtle()