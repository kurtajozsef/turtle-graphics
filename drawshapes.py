import random
from turtle import Turtle, colormode
from random import uniform


def random_color() -> tuple:
    return uniform(0, 1), uniform(0, 1), uniform(0, 1)


def draw(turtle: Turtle, sides: int, color: tuple):
    turtle.pencolor(color)
    angle = 360 / sides
    for _ in range(sides):
        turtle.forward(100)
        turtle.right(angle)


def draw_shapes(turtle: Turtle):
    for i in range(3, 11):
        draw(turtle, i, random_color())


def random_walk(turtle: Turtle):
    direction = [turtle.right, turtle.left]
    turtle.pensize(5)
    for _ in range(300):
        turtle.pencolor(random_color())
        turtle.forward(20)
        random.choice(direction)(90)


def draw_spirograph(turtle: Turtle, number_of_circles: int):
    angle = 360 / number_of_circles
    for i in range(number_of_circles + 1):
        turtle.pencolor(random_color())
        turtle.circle(100)
        turtle.setheading(angle * i)
        turtle.forward(angle)
