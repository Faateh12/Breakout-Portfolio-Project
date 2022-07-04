from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(1, 6)
        self.penup()
        self.goto(position)

    def up(self):
        new_x = self.xcor() + 40
        self.goto(new_x, self.ycor())

    def down(self):
        new_x = self.xcor() - 40
        self.goto(new_x, self.ycor())

