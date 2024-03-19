from turtle import *

class Progres:
    def __init__(self):
        self.gues = 0
        self.progres_bar()
        self.progres_pen()
        self.progres_write()
    def progres_bar(self):
        bar = Turtle()
        bar.speed('fastest')
        bar.penup()
        bar.goto(-700,-350)
        bar.pendown()
        bar.begin_fill()
        bar.pensize(8)
        bar.forward(810)
        bar.setheading(270)
        bar.forward(24)
        bar.setheading(180)
        bar.forward(810)
        bar.setheading(90)
        bar.forward(24)
        bar.end_fill()


    def progres_pen(self):
        self.pen = Turtle()
        self.pen.hideturtle()
        self.pen.speed('fastest')
        self.pen.penup()
        self.pen.shape('square')
        self.pen.color('green')
        self.pen.goto(-696,-362)
        self.pen.pendown()
        self.pen.pensize(24)

    def pen_move(self):
        self.pen.forward(10)
        self.gues += 1
        self.writer.clear()
        self.writer.write(f"ILERLEME : {self.gues}/81", font=('ariel', 35, 'bold'))

    def progres_write(self):
        self.writer = Turtle()
        self.writer.hideturtle()
        self.writer.speed('fastest')
        self.writer.penup()
        self.writer.goto(-470, -330)
        self.writer.write(f"ILERLEME : {self.gues}/81", font=('ariel', 35, 'bold'))