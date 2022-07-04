from turtle import Turtle

class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(1, 1)
        self.penup()
        self.goto(position)
        self.x_move = 20
        self.y_move = 20


    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)


    def bounce_horizontal(self):
        self.x_move *= -1

    def bounce_vertical(self):
        self.y_move *= -1

    def collision(self):
        self.y_move *= -1

    # def move_up(self):
    #
    #     self.x_move *= -1
