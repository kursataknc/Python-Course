import turtle as turtle
from turtle import *  # different import methods are instanced here
from turtle import Turtle
import random

amk = turtle.Turtle()
amk.shape("turtle")
amk.color("black")
amk.shapesize(2)
amk.speed("fastest")
amk.pensize(15)
turtle.colormode(255)

turnings = ["left(90)", "right(90)", "left(180)", "right(180)", "left(270)", "right(270)"]
degrees = [0, 90, 180, 270]


def random_color():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	random_color = (r, g, b)
	return random_color


for _ in range(200):
	amk.forward(30)
	amk.right(degrees[random.randint(0, 3)])
	amk.color(random_color())

screen = Screen()
screen.exitonclick()
