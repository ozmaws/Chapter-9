from math import pi
from turtle import *
from random import shuffle
TITLE = 'turtles are evil'
class Shape(object):
    def __init__(self, turtle, color):
        self.turtle = turtle
        self.color = color
    def getcolor(self):
        return self.color
    def setcolor(self, color):
        self.color = color
class Line(Shape):
    def __init__(self, x1, y1, x2, y2, turtle, color):
        Shape.__init__(self, turtle, color)
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
    def draw(self):
        self.turtle.up()
        self.turtle.goto(self._x1, self._y1)
        self.turtle.color(self.color)
        self.turtle.down()
        self.turtle.goto(self._x2, self._y2)
class Circle(Shape):
    def __init__(self, x, y, radius, turtle, color):
        Shape.__init__(self, turtle, color)
        self._x = x
        self._y = y
        self._radius = radius
    def draw(self):
        distance = 5.0 * pi * self._radius / 200.0
        self.turtle.up()
        self.turtle.goto(self._x + self._radius, self._y)
        self.turtle.setheading(90)
        self.turtle.down()
        self.turtle.color(self.color)
        for count in range(200):
            self.turtle.left(3)
            self.turtle.forward(distance)
class Rectangle(Shape):
    def __init__(self, x, y, width, height, turtle, color):
        Shape.__init__(self, turtle, color)
        self._x = x
        self._y = y
        self._width = width
        self._height = height
    def draw(self):
        self.turtle.up()
        self.turtle.goto(self._x, self._y)
        self.turtle.setheading(0)
        self.turtle.down()
        self.turtle.color(self.color)
        self.turtle.forward(self._width)
        self.turtle.left(-80)
        self.turtle.forward(self._height)
        self.turtle.left(-60)
        self.turtle.forward(self._width)
        self.turtle.left(-70)
        self.turtle.forward(self._height)
def change_color():
    colors = ["black", "red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    shuffle(colors)
    return colors[0]
def main():
    playArea = Screen()
    playArea.setup(width=1280, height=720, startx=None, starty=None)
    playArea.bgcolor("white")

    turtle = Turtle()
    turtle.hideturtle()

    head = Circle(80, 0, 10, turtle, change_color())
    body = Line(80, -10, 100, -50, turtle, change_color())
    arms = Line(80, -25, 120, -25, turtle, change_color())
    leftLeg = Line(80, -50, 90, -70, turtle, change_color())
    rightLeg = Line(80, -50, 110, -70, turtle, change_color())
    head.draw()
    body.draw()
    arms.draw()
    leftLeg.draw()
    rightLeg.draw()

    house = Rectangle(-160, 0, 120, 50, turtle, change_color())
    window = Rectangle(-150, -15, 20, 20, turtle,change_color())
    door = Rectangle(-100, -30, 15, 30, turtle, change_color())
    roof1 = Line(-180, 0, -160, 20, turtle, change_color())
    roof2 = Line(-160, 20, -80, 20, turtle, change_color())
    roof3 = Line(-80, 20, -60, 0, turtle, change_color())
    house.draw()
    window.draw()
    door.draw()
    roof1.draw()
    roof2.draw()
    roof3.draw()
main()
