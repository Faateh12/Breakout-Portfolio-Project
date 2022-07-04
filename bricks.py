from turtle import Turtle

class Brick(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("brown")
        self.shapesize(1, 5)
        self.penup()
        self.goto(position)


    def delete_brick(self):
        self.reset()

row1 = []
r1_counter = 6
x1 = -400
y1 = 300

x1 = float(x1)
y1 = float(y1)

while r1_counter > 0:
    r1_counter -= 1
    x1 += 110
    position1 = (x1, y1)
    row1.append(position1)


row2 = []
r2_counter = 6
x2 = -400
y2 = 270

x2 = float(x2)
y2 = float(y2)

while r2_counter > 0:
    r2_counter -= 1
    x2 += 110
    position2 = (x2, y2)
    row2.append(position2)


row3 = []
r3_counter = 6
x3 = -400
y3 = 240

x3 = float(x3)
y3 = float(y3)

while r3_counter > 0:
    r3_counter -= 1
    x3 += 110
    position3 = (x3, y3)
    row3.append(position3)

